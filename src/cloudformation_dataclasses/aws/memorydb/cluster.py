"""PropertyTypes for AWS::MemoryDB::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AZStatus:
    """AZStatus enum values."""

    SINGLEAZ = "singleaz"
    MULTIAZ = "multiaz"


class AuthenticationType:
    """AuthenticationType enum values."""

    PASSWORD = "password"
    NO_PASSWORD = "no-password"
    IAM = "iam"


class DataTieringStatus:
    """DataTieringStatus enum values."""

    TRUE = "true"
    FALSE = "false"


class InputAuthenticationType:
    """InputAuthenticationType enum values."""

    PASSWORD = "password"
    IAM = "iam"


class IpDiscovery:
    """IpDiscovery enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUAL_STACK = "dual_stack"


class ServiceUpdateStatus:
    """ServiceUpdateStatus enum values."""

    AVAILABLE = "available"
    IN_PROGRESS = "in-progress"
    COMPLETE = "complete"
    SCHEDULED = "scheduled"


class ServiceUpdateType:
    """ServiceUpdateType enum values."""

    SECURITY_UPDATE = "security-update"


class SourceType:
    """SourceType enum values."""

    NODE = "node"
    PARAMETER_GROUP = "parameter-group"
    SUBNET_GROUP = "subnet-group"
    CLUSTER = "cluster"
    USER = "user"
    ACL = "acl"


class UpdateStrategy:
    """UpdateStrategy enum values."""

    COORDINATED = "coordinated"
    UNCOORDINATED = "uncoordinated"


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None

