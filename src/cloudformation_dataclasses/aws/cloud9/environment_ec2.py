"""PropertyTypes for AWS::Cloud9::EnvironmentEC2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ConnectionType:
    """ConnectionType enum values."""

    CONNECT_SSH = "CONNECT_SSH"
    CONNECT_SSM = "CONNECT_SSM"


class EnvironmentLifecycleStatus:
    """EnvironmentLifecycleStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class EnvironmentStatus:
    """EnvironmentStatus enum values."""

    ERROR = "error"
    CREATING = "creating"
    CONNECTING = "connecting"
    READY = "ready"
    STOPPING = "stopping"
    STOPPED = "stopped"
    DELETING = "deleting"


class EnvironmentType:
    """EnvironmentType enum values."""

    SSH = "ssh"
    EC2 = "ec2"


class ManagedCredentialsAction:
    """ManagedCredentialsAction enum values."""

    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class ManagedCredentialsStatus:
    """ManagedCredentialsStatus enum values."""

    ENABLED_ON_CREATE = "ENABLED_ON_CREATE"
    ENABLED_BY_OWNER = "ENABLED_BY_OWNER"
    DISABLED_BY_DEFAULT = "DISABLED_BY_DEFAULT"
    DISABLED_BY_OWNER = "DISABLED_BY_OWNER"
    DISABLED_BY_COLLABORATOR = "DISABLED_BY_COLLABORATOR"
    PENDING_REMOVAL_BY_COLLABORATOR = "PENDING_REMOVAL_BY_COLLABORATOR"
    PENDING_START_REMOVAL_BY_COLLABORATOR = "PENDING_START_REMOVAL_BY_COLLABORATOR"
    PENDING_REMOVAL_BY_OWNER = "PENDING_REMOVAL_BY_OWNER"
    PENDING_START_REMOVAL_BY_OWNER = "PENDING_START_REMOVAL_BY_OWNER"
    FAILED_REMOVAL_BY_COLLABORATOR = "FAILED_REMOVAL_BY_COLLABORATOR"
    FAILED_REMOVAL_BY_OWNER = "FAILED_REMOVAL_BY_OWNER"


class MemberPermissions:
    """MemberPermissions enum values."""

    READ_WRITE = "read-write"
    READ_ONLY = "read-only"


class Permissions:
    """Permissions enum values."""

    OWNER = "owner"
    READ_WRITE = "read-write"
    READ_ONLY = "read-only"


@dataclass
class Repository(PropertyType):
    PATH_COMPONENT = "PathComponent"
    REPOSITORY_URL = "RepositoryUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_component": "PathComponent",
        "repository_url": "RepositoryUrl",
    }

    path_component: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

