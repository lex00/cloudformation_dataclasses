"""Topological sort and cycle detection for resource dependencies."""

from __future__ import annotations

import re
from typing import Any

from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRIntrinsic,
    IRTemplate,
)

from .context import build_arn_pattern_map, build_name_pattern_map


# =============================================================================
# Strongly Connected Components (Tarjan's Algorithm)
# =============================================================================


def find_strongly_connected_components(template: IRTemplate) -> list[list[str]]:
    """Find strongly connected components using Tarjan's algorithm.

    Returns a list of SCCs, where each SCC is a list of resource IDs.
    Resources in the same SCC form a cycle and should be in the same file.
    SCCs are returned in reverse topological order (dependencies first).
    """
    # Only consider resources (not parameters, etc.)
    resources = set(template.resources.keys())

    # Build pattern maps for implicit ref/get_att detection
    # These are needed to find dependencies created during code generation
    name_pattern_map = build_name_pattern_map(template)
    arn_pattern_map = build_arn_pattern_map(template)

    # Build adjacency list for resources only, including implicit dependencies
    graph: dict[str, list[str]] = {}
    for resource_id in resources:
        deps = find_resource_dependencies(
            template, resource_id, name_pattern_map, arn_pattern_map
        )
        graph[resource_id] = [d for d in deps if d in resources]

    # Tarjan's algorithm
    index_counter = [0]
    stack: list[str] = []
    lowlinks: dict[str, int] = {}
    index: dict[str, int] = {}
    on_stack: set[str] = set()
    sccs: list[list[str]] = []

    def strongconnect(node: str) -> None:
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack.add(node)

        for successor in graph.get(node, []):
            if successor not in index:
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node], lowlinks[successor])
            elif successor in on_stack:
                lowlinks[node] = min(lowlinks[node], index[successor])

        # If node is a root node, pop the stack and generate an SCC
        if lowlinks[node] == index[node]:
            scc: list[str] = []
            while True:
                successor = stack.pop()
                on_stack.remove(successor)
                scc.append(successor)
                if successor == node:
                    break
            sccs.append(scc)

    for node in resources:
        if node not in index:
            strongconnect(node)

    return sccs


# =============================================================================
# Topological Sort
# =============================================================================


def topological_sort(template: IRTemplate) -> list[str]:
    """Sort resources so dependencies come first."""
    visited: set[str] = set()
    result: list[str] = []

    def visit(resource_id: str) -> None:
        if resource_id in visited:
            return
        visited.add(resource_id)

        # Visit dependencies first
        for dep_id in template.reference_graph.get(resource_id, []):
            if dep_id in template.resources:
                visit(dep_id)

        result.append(resource_id)

    for resource_id in template.resources:
        visit(resource_id)

    return result


# =============================================================================
# Resource Dependency Detection
# =============================================================================


def find_resource_dependencies(
    template: IRTemplate,
    resource_id: str,
    name_pattern_map: dict[str, str] | None = None,
    arn_pattern_map: dict[str, tuple[str, str]] | None = None,
) -> set[str]:
    """Find other resources that this resource depends on (for imports).

    Args:
        template: The IR template
        resource_id: The resource we're finding dependencies for
        name_pattern_map: Map of Sub patterns to resource IDs for implicit ref detection
        arn_pattern_map: Map of ARN Sub patterns to (resource_id, suffix) for get_att detection
    """
    deps = set()

    # Explicit references from reference graph
    for ref_target in template.reference_graph.get(resource_id, []):
        if ref_target in template.resources and ref_target != resource_id:
            deps.add(ref_target)

    # Implicit references from Sub patterns that match resource names or ARNs
    resource = template.resources.get(resource_id)
    if resource:
        _find_sub_pattern_refs(
            resource.properties, name_pattern_map, arn_pattern_map, resource_id, deps, template
        )

        # DependsOn references (for class-based depends_on)
        for dep in resource.depends_on:
            if dep in template.resources and dep != resource_id:
                deps.add(dep)

    return deps


def _find_sub_pattern_refs(
    properties: dict[str, Any],
    name_pattern_map: dict[str, str] | None,
    arn_pattern_map: dict[str, tuple[str, str]] | None,
    current_resource_id: str,
    deps: set[str],
    template: IRTemplate,
) -> None:
    """Recursively find Sub patterns that reference other resources."""
    for prop in properties.values():
        if hasattr(prop, 'value'):
            _find_sub_in_value(
                prop.value, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )


def _find_sub_in_value(
    value: Any,
    name_pattern_map: dict[str, str] | None,
    arn_pattern_map: dict[str, tuple[str, str]] | None,
    current_resource_id: str,
    deps: set[str],
    template: IRTemplate,
) -> None:
    """Recursively find Sub patterns in a value."""
    if isinstance(value, IRIntrinsic):
        if value.type == IntrinsicType.SUB:
            # Extract template string
            if isinstance(value.args, str):
                template_str = value.args
            elif isinstance(value.args, (list, tuple)) and len(value.args) >= 1:
                template_str = value.args[0]
            else:
                template_str = None

            if template_str:
                # Extract variable references from the template string
                var_refs = re.findall(r"\$\{([^}]+)\}", template_str)
                # Filter out pseudo-parameters (AWS::*)
                non_pseudo_vars = [v for v in var_refs if not v.startswith("AWS::")]
                # Check if all non-pseudo vars are parameters
                all_params = all(v in template.parameters for v in non_pseudo_vars)

                # Check if it matches a resource name pattern (ref dependency)
                # This creates a dependency because the generated code uses ref(ResourceName)
                if name_pattern_map and template_str in name_pattern_map:
                    ref_target = name_pattern_map[template_str]
                    if ref_target != current_resource_id:
                        deps.add(ref_target)
                # Check if it matches an ARN pattern (get_att dependency)
                # Only add dependency if we would actually convert to get_att()
                # Skip if all non-pseudo vars are parameters (we keep Sub in that case)
                elif arn_pattern_map and template_str in arn_pattern_map:
                    if not all_params:
                        ref_target, _ = arn_pattern_map[template_str]
                        if ref_target != current_resource_id:
                            deps.add(ref_target)

        # Also check nested intrinsics
        if isinstance(value.args, (list, tuple)):
            for arg in value.args:
                _find_sub_in_value(
                    arg, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
                )
        elif isinstance(value.args, dict):
            for v in value.args.values():
                _find_sub_in_value(
                    v, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
                )
    elif isinstance(value, dict):
        for v in value.values():
            _find_sub_in_value(
                v, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )
    elif isinstance(value, list):
        for item in value:
            _find_sub_in_value(
                item, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )


# =============================================================================
# SCC Resource Ordering
# =============================================================================


def order_scc_resources(
    scc: list[str],
    template: IRTemplate,
    name_pattern_map: dict[str, str] | None = None,
    arn_pattern_map: dict[str, tuple[str, str]] | None = None,
) -> list[str]:
    """Order resources within an SCC to minimize forward references.

    Uses a heuristic: resources with fewer dependencies on other SCC members
    come first.
    """
    scc_set = set(scc)

    # Build pattern maps if not provided
    if name_pattern_map is None:
        name_pattern_map = build_name_pattern_map(template)
    if arn_pattern_map is None:
        arn_pattern_map = build_arn_pattern_map(template)

    # Count how many SCC members each resource depends on
    # Use full dependency detection (including implicit refs from code generation)
    dep_counts: dict[str, int] = {}
    for resource_id in scc:
        deps = find_resource_dependencies(
            template, resource_id, name_pattern_map, arn_pattern_map
        )
        scc_deps = [d for d in deps if d in scc_set]
        dep_counts[resource_id] = len(scc_deps)

    # Sort by dependency count (ascending), then alphabetically for stability
    return sorted(scc, key=lambda r: (dep_counts[r], r))
