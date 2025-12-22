"""PropertyTypes for AWS::DAX::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChangeType:
    """ChangeType enum values."""

    IMMEDIATE = "IMMEDIATE"
    REQUIRES_REBOOT = "REQUIRES_REBOOT"


class ClusterEndpointEncryptionType:
    """ClusterEndpointEncryptionType enum values."""

    NONE = "NONE"
    TLS = "TLS"


class IsModifiable:
    """IsModifiable enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"
    CONDITIONAL = "CONDITIONAL"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUAL_STACK = "dual_stack"


class ParameterType:
    """ParameterType enum values."""

    DEFAULT = "DEFAULT"
    NODE_TYPE_SPECIFIC = "NODE_TYPE_SPECIFIC"


class SSEStatus:
    """SSEStatus enum values."""

    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class SourceType:
    """SourceType enum values."""

    CLUSTER = "CLUSTER"
    PARAMETER_GROUP = "PARAMETER_GROUP"
    SUBNET_GROUP = "SUBNET_GROUP"


@dataclass
class SSESpecification(PropertyType):
    SSE_ENABLED = "SSEEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
    }

    sse_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

