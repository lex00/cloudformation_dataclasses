"""File organization utilities for splitting resources into category files.

This module provides shared logic for organizing CloudFormation resources
into category-based files (network.py, compute.py, etc.).

Used by:
- Importer: when generating new packages from CloudFormation templates
- Linter: when splitting existing resource files

The algorithm:
1. Parse resources and determine their AWS service type
2. Group by category (network, compute, storage, etc.)
3. Detect and break import cycles
4. Output resources organized into files
"""

from dataclasses import dataclass
from typing import Optional


# =============================================================================
# Service Category Mapping
# =============================================================================

# Map AWS service names to category files
SERVICE_CATEGORIES: dict[str, str] = {
    # Compute
    "EC2": "compute",
    "Lambda": "compute",
    "ECS": "compute",
    "EKS": "compute",
    "Batch": "compute",
    "AutoScaling": "compute",
    "ElasticBeanstalk": "compute",
    "Lightsail": "compute",
    # Storage
    "S3": "storage",
    "EFS": "storage",
    "FSx": "storage",
    "Backup": "storage",
    # Database
    "RDS": "database",
    "DynamoDB": "database",
    "ElastiCache": "database",
    "Neptune": "database",
    "DocumentDB": "database",
    "Redshift": "database",
    "MemoryDB": "database",
    # Networking
    "ElasticLoadBalancing": "network",
    "ElasticLoadBalancingV2": "network",
    "Route53": "network",
    "CloudFront": "network",
    "APIGateway": "network",
    "ApiGatewayV2": "network",
    "GlobalAccelerator": "network",
    # Security/IAM
    "IAM": "security",
    "Cognito": "security",
    "SecretsManager": "security",
    "KMS": "security",
    "WAF": "security",
    "WAFv2": "security",
    "ACM": "security",
    "CertificateManager": "security",
    "SSM": "security",
    # Messaging/Integration
    "SNS": "messaging",
    "SQS": "messaging",
    "EventBridge": "messaging",
    "Events": "messaging",
    "StepFunctions": "messaging",
    "AppSync": "messaging",
    # Monitoring/Logging
    "CloudWatch": "monitoring",
    "Logs": "monitoring",
    "CloudTrail": "monitoring",
    "XRay": "monitoring",
    # CI/CD
    "CodeBuild": "cicd",
    "CodePipeline": "cicd",
    "CodeCommit": "cicd",
    "CodeDeploy": "cicd",
    # Infrastructure
    "CloudFormation": "infra",
    "Config": "infra",
    "ServiceCatalog": "infra",
}

# EC2 resource types that should go to network.py instead of compute.py
EC2_NETWORK_TYPES: set[str] = {
    "VPC",
    "Subnet",
    "InternetGateway",
    "NatGateway",
    "RouteTable",
    "Route",
    "SecurityGroup",
    "NetworkAcl",
    "VPCEndpoint",
    "EIP",
    "VPCGatewayAttachment",
    "SubnetRouteTableAssociation",
    "NetworkInterface",
    "VPNGateway",
    "VPNConnection",
    "CustomerGateway",
    "TransitGateway",
    "TransitGatewayAttachment",
    # PropertyTypes for SecurityGroup
    "Ingress",
    "Egress",
}


@dataclass
class ResourceInfo:
    """Information about a resource class extracted from source."""

    class_name: str
    service: str  # e.g., "EC2", "ElasticLoadBalancingV2"
    type_name: str  # e.g., "SecurityGroup", "LoadBalancer"
    source_lines: tuple[int, int]  # (start_line, end_line) 1-indexed
    dependencies: set[str]  # class names this resource references


def get_category(service: str, type_name: str) -> str:
    """Get the category file for a resource based on its AWS service.

    Args:
        service: AWS service name (e.g., "EC2", "ElasticLoadBalancingV2")
        type_name: Resource type within the service (e.g., "SecurityGroup")

    Returns:
        Category name like 'compute', 'network', 'security', or 'main'
    """
    # Special case: EC2 VPC-related resources go to network
    if service == "EC2" and type_name in EC2_NETWORK_TYPES:
        return "network"

    return SERVICE_CATEGORIES.get(service, "main")


def organize_resources(
    resources: dict[str, ResourceInfo],
    *,
    min_resources_to_split: int = 3,
) -> dict[str, list[str]]:
    """Organize resources into category files.

    Args:
        resources: Map of class_name -> ResourceInfo
        min_resources_to_split: Minimum resources needed before splitting

    Returns:
        Map of filename -> list of class names in order
    """
    if len(resources) < min_resources_to_split:
        # Not enough resources to bother splitting
        return {"main": list(resources.keys())}

    # Group by category
    categories: dict[str, list[str]] = {}
    for class_name, info in resources.items():
        category = get_category(info.service, info.type_name)
        if category not in categories:
            categories[category] = []
        categories[category].append(class_name)

    # Build resource -> file mapping
    resource_to_file: dict[str, str] = {}
    for category, class_names in categories.items():
        for class_name in class_names:
            resource_to_file[class_name] = category

    # Build file-level dependency graph and break cycles
    file_deps = _build_file_dependencies(resources, resource_to_file)

    # Iteratively move resources to break file-level cycles
    max_iterations = len(resources) + 1
    for _ in range(max_iterations):
        cycle = _find_cycle(file_deps)
        if not cycle:
            break

        # Find a resource in the cycle to move to main
        # Pick from the file with fewest resources (least disruptive)
        cycle_files = [f for f in cycle if f != "main"]
        if not cycle_files:
            break

        # Find file with most dependencies to others (hub node)
        hub_file = max(cycle_files, key=lambda f: len(file_deps.get(f, set())))

        # Move one resource from hub_file to main
        for class_name, file in resource_to_file.items():
            if file == hub_file:
                resource_to_file[class_name] = "main"
                if "main" not in categories:
                    categories["main"] = []
                categories["main"].append(class_name)
                categories[hub_file].remove(class_name)
                break

        # Rebuild file dependencies
        file_deps = _build_file_dependencies(resources, resource_to_file)

    # Clean up empty categories
    categories = {cat: names for cat, names in categories.items() if names}

    return categories


def _build_file_dependencies(
    resources: dict[str, ResourceInfo],
    resource_to_file: dict[str, str],
) -> dict[str, set[str]]:
    """Build file-level dependency graph."""
    file_deps: dict[str, set[str]] = {}

    for class_name, info in resources.items():
        src_file = resource_to_file.get(class_name, "main")
        if src_file not in file_deps:
            file_deps[src_file] = set()

        for dep_class in info.dependencies:
            if dep_class in resource_to_file:
                dep_file = resource_to_file[dep_class]
                if dep_file != src_file:
                    file_deps[src_file].add(dep_file)

    return file_deps


def _find_cycle(file_deps: dict[str, set[str]]) -> Optional[list[str]]:
    """Detect cycles using DFS. Returns cycle path or None."""
    visited: set[str] = set()
    rec_stack: set[str] = set()
    path: list[str] = []

    def dfs(node: str) -> Optional[list[str]]:
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        for neighbor in file_deps.get(node, set()):
            if neighbor not in visited:
                result = dfs(neighbor)
                if result:
                    return result
            elif neighbor in rec_stack:
                # Found cycle
                cycle_start = path.index(neighbor)
                return path[cycle_start:]

        path.pop()
        rec_stack.remove(node)
        return None

    for node in file_deps:
        if node not in visited:
            result = dfs(node)
            if result:
                return result
    return None
