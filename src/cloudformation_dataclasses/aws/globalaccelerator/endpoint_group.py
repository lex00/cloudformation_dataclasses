"""PropertyTypes for AWS::GlobalAccelerator::EndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorStatus:
    """AcceleratorStatus enum values."""

    DEPLOYED = "DEPLOYED"
    IN_PROGRESS = "IN_PROGRESS"


class ByoipCidrState:
    """ByoipCidrState enum values."""

    PENDING_PROVISIONING = "PENDING_PROVISIONING"
    READY = "READY"
    PENDING_ADVERTISING = "PENDING_ADVERTISING"
    ADVERTISING = "ADVERTISING"
    PENDING_WITHDRAWING = "PENDING_WITHDRAWING"
    PENDING_DEPROVISIONING = "PENDING_DEPROVISIONING"
    DEPROVISIONED = "DEPROVISIONED"
    FAILED_PROVISION = "FAILED_PROVISION"
    FAILED_ADVERTISING = "FAILED_ADVERTISING"
    FAILED_WITHDRAW = "FAILED_WITHDRAW"
    FAILED_DEPROVISION = "FAILED_DEPROVISION"


class ClientAffinity:
    """ClientAffinity enum values."""

    NONE = "NONE"
    SOURCE_IP = "SOURCE_IP"


class CustomRoutingAcceleratorStatus:
    """CustomRoutingAcceleratorStatus enum values."""

    DEPLOYED = "DEPLOYED"
    IN_PROGRESS = "IN_PROGRESS"


class CustomRoutingDestinationTrafficState:
    """CustomRoutingDestinationTrafficState enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class CustomRoutingProtocol:
    """CustomRoutingProtocol enum values."""

    TCP = "TCP"
    UDP = "UDP"


class HealthCheckProtocol:
    """HealthCheckProtocol enum values."""

    TCP = "TCP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class HealthState:
    """HealthState enum values."""

    INITIAL = "INITIAL"
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class IpAddressFamily:
    """IpAddressFamily enum values."""

    IPV4 = "IPv4"
    IPV6 = "IPv6"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "IPV4"
    DUAL_STACK = "DUAL_STACK"


class Protocol:
    """Protocol enum values."""

    TCP = "TCP"
    UDP = "UDP"


@dataclass
class EndpointConfiguration(PropertyType):
    ATTACHMENT_ARN = "AttachmentArn"
    ENDPOINT_ID = "EndpointId"
    WEIGHT = "Weight"
    CLIENT_IP_PRESERVATION_ENABLED = "ClientIPPreservationEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attachment_arn": "AttachmentArn",
        "endpoint_id": "EndpointId",
        "weight": "Weight",
        "client_ip_preservation_enabled": "ClientIPPreservationEnabled",
    }

    attachment_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    client_ip_preservation_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PortOverride(PropertyType):
    LISTENER_PORT = "ListenerPort"
    ENDPOINT_PORT = "EndpointPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "listener_port": "ListenerPort",
        "endpoint_port": "EndpointPort",
    }

    listener_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    endpoint_port: Optional[Union[int, Ref, GetAtt, Sub]] = None

