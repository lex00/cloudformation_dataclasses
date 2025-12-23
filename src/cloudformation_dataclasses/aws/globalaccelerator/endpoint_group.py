"""PropertyTypes for AWS::GlobalAccelerator::EndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

