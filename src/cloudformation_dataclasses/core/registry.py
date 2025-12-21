"""
Global registry for @cloudformation_dataclass wrapper classes.

This module provides auto-registration for CloudFormation resources,
enabling multi-file template organization and type-based queries.

Example:
    # tables/users.py
    @cloudformation_dataclass
    class UsersTable:
        resource: Table
        table_name = "users"
        # Automatically registered!

    # main.py
    from cloudformation_dataclasses import registry

    # Get all registered resources
    all_resources = registry.get_all()

    # Query by type
    tables = registry.get_by_type(Table)  # [UsersTable, OrdersTable]
    tables = registry.get_by_type("AWS::DynamoDB::Table")  # same
"""

from __future__ import annotations

from threading import Lock
from typing import TYPE_CHECKING, Any, Type

if TYPE_CHECKING:
    pass


class ResourceRegistry:
    """
    Global registry for @cloudformation_dataclass wrapper classes.

    Resources auto-register when decorated, enabling:
    - Multi-file template organization
    - Type-based queries (e.g., all DynamoDB tables)
    - Automatic template building
    """

    def __init__(self) -> None:
        self._resources: dict[str, Type[Any]] = {}  # class_name -> class
        self._by_type: dict[str, list[Type[Any]]] = {}  # cf_type -> [classes]
        self._lock = Lock()

    def register(self, wrapper_cls: Type[Any], resource_type: str) -> None:
        """
        Register a wrapper class.

        Args:
            wrapper_cls: The @cloudformation_dataclass decorated class
            resource_type: The CloudFormation resource type (e.g., "AWS::S3::Bucket")
        """
        with self._lock:
            name = wrapper_cls.__name__
            self._resources[name] = wrapper_cls

            if resource_type not in self._by_type:
                self._by_type[resource_type] = []
            self._by_type[resource_type].append(wrapper_cls)

    def get_all(self, scope_package: str | None = None) -> list[Type[Any]]:
        """Get all registered wrapper classes, optionally filtered by package.

        Args:
            scope_package: If provided, only return resources from modules
                that start with this package name.

        Returns:
            List of registered wrapper classes.
        """
        resources = list(self._resources.values())
        if scope_package:
            resources = [r for r in resources if r.__module__.startswith(scope_package)]
        return resources

    def get_by_type(self, resource_type: Type[Any] | str) -> list[Type[Any]]:
        """
        Get wrapper classes by resource type.

        Args:
            resource_type: Either a class (Table) or CF type string ("AWS::DynamoDB::Table")

        Returns:
            List of wrapper classes that wrap the specified resource type

        Example:
            >>> from cloudformation_dataclasses.aws.dynamodb import Table
            >>> tables = registry.get_by_type(Table)
            >>> # or
            >>> tables = registry.get_by_type("AWS::DynamoDB::Table")
        """
        if isinstance(resource_type, type):
            # Get CF type from class
            cf_type = getattr(resource_type, "resource_type", None)
            if cf_type is None:
                return []
        else:
            cf_type = resource_type

        return list(self._by_type.get(cf_type, []))

    def get_by_name(self, name: str) -> Type[Any] | None:
        """
        Get a wrapper class by its class name.

        Args:
            name: The class name (e.g., "UsersTable")

        Returns:
            The wrapper class, or None if not found
        """
        return self._resources.get(name)

    def clear(self) -> None:
        """
        Clear the registry.

        Useful for testing to ensure isolation between tests.
        """
        with self._lock:
            self._resources.clear()
            self._by_type.clear()

    def __len__(self) -> int:
        """Return the number of registered resources."""
        return len(self._resources)

    def __contains__(self, name: str) -> bool:
        """Check if a resource with the given name is registered."""
        return name in self._resources


# Global registry instance
registry = ResourceRegistry()
