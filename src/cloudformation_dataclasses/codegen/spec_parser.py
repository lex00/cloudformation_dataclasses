"""
CloudFormation spec parser and downloader.

This module handles downloading and parsing AWS CloudFormation Resource Specifications.
The spec is a JSON file that describes all AWS resources, their properties, and types.

The spec file is committed to the repository for reproducibility. Use the 'update' command
to download a new version from AWS.

Spec URL: https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json
"""

from __future__ import annotations

import gzip
import json
from dataclasses import dataclass, field
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    requests = None  # type: ignore

from .config import (
    CLOUDFORMATION_SPEC_DATE,
    GENERATOR_VERSION,
    COMBINED_VERSION,
    SPEC_URL,
    SPEC_FILE,
)

# Keep legacy alias for compatibility
CLOUDFORMATION_SPEC_VERSION = CLOUDFORMATION_SPEC_DATE


class SpecVersionMismatchError(Exception):
    """Raised when downloaded spec version doesn't match pinned version."""

    pass


@dataclass
class PropertySpec:
    """Specification for a CloudFormation property."""

    name: str
    documentation: str = ""
    primitive_type: str | None = None  # String, Integer, Boolean, etc.
    type: str | None = None  # List, Map, or PropertyType name
    item_type: str | None = None  # For List types
    primitive_item_type: str | None = None  # For List of primitives
    required: bool = False
    update_type: str | None = None  # Mutable, Immutable, Conditional

    @classmethod
    def from_dict(cls, name: str, data: dict[str, Any]) -> PropertySpec:
        """Create PropertySpec from CloudFormation spec dictionary."""
        return cls(
            name=name,
            documentation=data.get("Documentation", ""),
            primitive_type=data.get("PrimitiveType"),
            type=data.get("Type"),
            item_type=data.get("ItemType"),
            primitive_item_type=data.get("PrimitiveItemType"),
            required=data.get("Required", False),
            update_type=data.get("UpdateType"),
        )


@dataclass
class ResourceSpec:
    """Specification for a CloudFormation resource type."""

    resource_type: str  # e.g., "AWS::S3::Bucket"
    documentation: str = ""
    properties: dict[str, PropertySpec] = field(default_factory=dict)
    attributes: dict[str, dict[str, Any]] = field(default_factory=dict)
    additional_properties: bool = False

    @property
    def service_name(self) -> str:
        """Extract service name from resource type (e.g., 'S3' from 'AWS::S3::Bucket')."""
        parts = self.resource_type.split("::")
        return parts[1] if len(parts) >= 2 else "Unknown"

    @property
    def class_name(self) -> str:
        """Extract class name from resource type (e.g., 'Bucket' from 'AWS::S3::Bucket')."""
        parts = self.resource_type.split("::")
        return parts[2] if len(parts) >= 3 else "Unknown"

    @classmethod
    def from_dict(cls, resource_type: str, data: dict[str, Any]) -> ResourceSpec:
        """Create ResourceSpec from CloudFormation spec dictionary."""
        properties = {}
        for prop_name, prop_data in data.get("Properties", {}).items():
            properties[prop_name] = PropertySpec.from_dict(prop_name, prop_data)

        return cls(
            resource_type=resource_type,
            documentation=data.get("Documentation", ""),
            properties=properties,
            attributes=data.get("Attributes", {}),
            additional_properties=data.get("AdditionalProperties", False),
        )


@dataclass
class PropertyTypeSpec:
    """Specification for a CloudFormation property type (nested structures)."""

    type_name: str  # e.g., "AWS::S3::Bucket.VersioningConfiguration"
    documentation: str = ""
    properties: dict[str, PropertySpec] = field(default_factory=dict)

    @property
    def simple_name(self) -> str:
        """Extract simple name from property type (e.g., 'VersioningConfiguration')."""
        return self.type_name.split(".")[-1]

    @property
    def resource_type(self) -> str:
        """Extract resource type this property belongs to."""
        parts = self.type_name.split(".")
        return parts[0] if len(parts) >= 1 else ""

    @classmethod
    def from_dict(cls, type_name: str, data: dict[str, Any]) -> PropertyTypeSpec:
        """Create PropertyTypeSpec from CloudFormation spec dictionary."""
        properties = {}
        for prop_name, prop_data in data.get("Properties", {}).items():
            properties[prop_name] = PropertySpec.from_dict(prop_name, prop_data)

        return cls(
            type_name=type_name,
            documentation=data.get("Documentation", ""),
            properties=properties,
        )


@dataclass
class CloudFormationSpec:
    """
    Complete CloudFormation specification.

    Contains all resource types and property types from AWS CloudFormation spec.
    """

    resource_types: dict[str, ResourceSpec] = field(default_factory=dict)
    property_types: dict[str, PropertyTypeSpec] = field(default_factory=dict)
    spec_version: str = "Unknown"
    downloaded_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CloudFormationSpec:
        """Parse CloudFormation spec from JSON dictionary."""
        resource_types = {}
        for resource_type, resource_data in data.get("ResourceTypes", {}).items():
            resource_types[resource_type] = ResourceSpec.from_dict(resource_type, resource_data)

        property_types = {}
        for type_name, type_data in data.get("PropertyTypes", {}).items():
            property_types[type_name] = PropertyTypeSpec.from_dict(type_name, type_data)

        return cls(
            resource_types=resource_types,
            property_types=property_types,
            spec_version=data.get("ResourceSpecificationVersion", "Unknown"),
            downloaded_at=datetime.now(),
        )

    def get_property_types_for_resource(self, resource_type: str) -> dict[str, PropertyTypeSpec]:
        """
        Get all property types that belong to a specific resource.

        Args:
            resource_type: Resource type like "AWS::S3::Bucket"

        Returns:
            Dictionary of property type specs for this resource
        """
        result = {}
        prefix = f"{resource_type}."
        for type_name, prop_type in self.property_types.items():
            if type_name.startswith(prefix):
                result[type_name] = prop_type
        return result

    def get_resources_by_service(self, service: str) -> dict[str, ResourceSpec]:
        """
        Get all resources for a specific AWS service.

        Args:
            service: Service name like "S3", "EC2", "Lambda"

        Returns:
            Dictionary of resource specs for this service
        """
        result = {}
        prefix = f"AWS::{service}::"
        for resource_type, resource_spec in self.resource_types.items():
            if resource_type.startswith(prefix):
                result[resource_type] = resource_spec
        return result

    def list_services(self) -> list[str]:
        """
        Get list of all AWS services in the spec.

        Returns:
            Sorted list of service names
        """
        services = set()
        for resource_type in self.resource_types.keys():
            parts = resource_type.split("::")
            if len(parts) >= 2:
                services.add(parts[1])
        return sorted(services)


def download_spec(url: str = SPEC_URL, cache_path: Path | None = None) -> dict[str, Any]:
    """
    Download CloudFormation spec from AWS.

    Args:
        url: URL to CloudFormation spec (default: AWS's latest spec)
        cache_path: Optional path to cache the downloaded spec

    Returns:
        Parsed JSON specification as dictionary

    Raises:
        ImportError: If requests library is not installed
        requests.RequestException: If download fails

    Example:
        >>> spec_data = download_spec()
        >>> print(f"Spec version: {spec_data['ResourceSpecificationVersion']}")
    """
    if requests is None:
        raise ImportError(
            "requests library is required for downloading specs. "
            "Install it with: pip install cloudformation_dataclasses[dev]"
        )

    # Check cache first
    if cache_path and cache_path.exists():
        print(f"Loading spec from cache: {cache_path}")
        with open(cache_path, "r") as f:
            return json.load(f)

    # Download from AWS
    print(f"Downloading CloudFormation spec from {url}...")
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    # Try to decompress if gzipped, otherwise use raw content
    try:
        content = gzip.decompress(response.content)
        spec_data = json.loads(content)
    except gzip.BadGzipFile:
        # Content is not gzipped (despite URL), parse directly
        spec_data = response.json()

    # Cache if path provided
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with open(cache_path, "w") as f:
            json.dump(spec_data, f, indent=2)
        print(f"Cached spec to: {cache_path}")

    return spec_data


def load_spec(spec_path: Path) -> CloudFormationSpec:
    """
    Load CloudFormation spec from a local JSON file.

    Args:
        spec_path: Path to CloudFormation spec JSON file

    Returns:
        Parsed CloudFormation specification

    Example:
        >>> spec = load_spec(Path("cloudformation_spec.json"))
        >>> print(f"Found {len(spec.resource_types)} resource types")
    """
    with open(spec_path, "r") as f:
        data = json.load(f)
    return CloudFormationSpec.from_dict(data)


def get_spec(
    spec_file: Path | None = None,
    force_download: bool = False,
) -> CloudFormationSpec:
    """
    Get CloudFormation spec from the committed spec file.

    The spec file is committed to the repository for reproducibility.
    Use the 'update' command to download a new version from AWS.

    Args:
        spec_file: Path to spec file (default: specs/CloudFormationResourceSpecification.json)
        force_download: Force re-download to cache (for checking updates)

    Returns:
        Parsed CloudFormation specification

    Example:
        >>> spec = get_spec()
        >>> print(f"Spec version: {spec.spec_version}")
        >>> print(f"Services: {', '.join(spec.list_services()[:5])}...")
    """
    if spec_file is None:
        spec_file = SPEC_FILE

    if not spec_file.exists():
        raise FileNotFoundError(
            f"CloudFormation spec file not found: {spec_file}\n"
            f"The spec file should be committed to the repository.\n"
            f"Run: uv run python -m cloudformation_dataclasses.codegen.spec_parser update"
        )

    print(f"Loading spec from: {spec_file}")
    with open(spec_file, "r") as f:
        spec_data = json.load(f)

    spec = CloudFormationSpec.from_dict(spec_data)
    return spec


def check_for_updates() -> tuple[bool, str, str]:
    """
    Check if a newer CloudFormation spec is available from AWS.

    Returns:
        Tuple of (has_update, current_date, remote_date)
    """
    if requests is None:
        raise ImportError(
            "requests library is required for checking updates. "
            "Install it with: pip install cloudformation_dataclasses[dev]"
        )

    # Get Last-Modified header from AWS
    response = requests.head(SPEC_URL, timeout=10)
    response.raise_for_status()

    last_modified = response.headers.get("Last-Modified")
    if not last_modified:
        raise ValueError("No Last-Modified header in response")

    # Parse HTTP date format: "Thu, 11 Dec 2025 22:11:08 GMT"
    remote_dt = parsedate_to_datetime(last_modified)
    remote_date = remote_dt.strftime("%Y.%m.%d")

    has_update = remote_date > CLOUDFORMATION_SPEC_DATE
    return has_update, CLOUDFORMATION_SPEC_DATE, remote_date


def update_spec() -> tuple[str, str]:
    """
    Download and save the latest CloudFormation spec from AWS.

    Returns:
        Tuple of (new_date, aws_version)
    """
    if requests is None:
        raise ImportError(
            "requests library is required for downloading specs. "
            "Install it with: pip install cloudformation_dataclasses[dev]"
        )

    # Get headers first to get the date
    head_response = requests.head(SPEC_URL, timeout=10)
    head_response.raise_for_status()

    last_modified = head_response.headers.get("Last-Modified")
    if not last_modified:
        raise ValueError("No Last-Modified header in response")

    remote_dt = parsedate_to_datetime(last_modified)
    new_date = remote_dt.strftime("%Y.%m.%d")

    # Download the spec
    print(f"Downloading CloudFormation spec from {SPEC_URL}...")
    response = requests.get(SPEC_URL, timeout=60)
    response.raise_for_status()

    # Decompress
    try:
        content = gzip.decompress(response.content)
        spec_data = json.loads(content)
    except gzip.BadGzipFile:
        spec_data = response.json()

    aws_version = spec_data.get("ResourceSpecificationVersion", "Unknown")

    # Save to committed spec file
    SPEC_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SPEC_FILE, "w") as f:
        json.dump(spec_data, f, indent=2)

    print(f"Saved spec to: {SPEC_FILE}")

    return new_date, aws_version


if __name__ == "__main__":
    """CLI for downloading and inspecting CloudFormation specs."""
    import argparse

    parser = argparse.ArgumentParser(
        description=f"CloudFormation spec parser and downloader (current: {CLOUDFORMATION_SPEC_DATE})",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Check command
    check_parser = subparsers.add_parser(
        "check",
        help="Check if a newer CloudFormation spec is available from AWS",
    )

    # Update command
    update_parser = subparsers.add_parser(
        "update",
        help="Download and save the latest CloudFormation spec from AWS",
    )

    # Version command
    version_parser = subparsers.add_parser(
        "version",
        help="Show CloudFormation spec version information",
    )

    # List services command
    list_parser = subparsers.add_parser(
        "list-services",
        help="List all available AWS services",
    )

    args = parser.parse_args()

    if args.command == "check":
        print("Checking for CloudFormation spec updates...")
        print(f"Current spec date: {CLOUDFORMATION_SPEC_DATE}")
        try:
            has_update, current, remote = check_for_updates()
            print(f"Remote spec date:  {remote}")
            if has_update:
                print("\n🔄 Update available!")
                print(
                    "   Run: uv run python -m cloudformation_dataclasses.codegen.spec_parser update"
                )
            else:
                print("\n✅ Spec is up to date")
        except Exception as e:
            print(f"\n❌ Error checking for updates: {e}")

    elif args.command == "update":
        print("Updating CloudFormation spec...")
        print(f"Current spec date: {CLOUDFORMATION_SPEC_DATE}")
        try:
            new_date, aws_version = update_spec()
            print("\n✅ Downloaded CloudFormation spec")
            print(f"   New date: {new_date}")
            if new_date != CLOUDFORMATION_SPEC_DATE:
                print("\n⚠️  Don't forget to update config.py:")
                print(f'   CLOUDFORMATION_SPEC_DATE = "{new_date}"')
                print("\n   Then regenerate services and run tests.")
        except Exception as e:
            print(f"\n❌ Error updating spec: {e}")

    elif args.command == "version":
        spec = get_spec()
        print("CloudFormation Code Generator Version Information:")
        print("\nSpec Version:")
        print(f"  Date (pinned): {CLOUDFORMATION_SPEC_DATE}")
        print(f"  File version:  {spec.spec_version}")
        print("\nGenerator Version:")
        print(f"  Current: {GENERATOR_VERSION}")
        print(f"\nCombined Version: {COMBINED_VERSION}")
        print("\nSpec Contents:")
        print(f"  Resource types: {len(spec.resource_types)}")
        print(f"  Property types: {len(spec.property_types)}")
        print(f"  Services: {len(spec.list_services())}")
        print(f"\nSpec File: {SPEC_FILE}")

    elif args.command == "list-services":
        spec = get_spec()
        print(f"AWS Services ({len(spec.list_services())}):")
        for service in spec.list_services():
            resources = spec.get_resources_by_service(service)
            print(f"  {service}: {len(resources)} resources")

    else:
        parser.print_help()
