"""PropertyTypes for AWS::S3Outposts::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FailedReason(PropertyType):
    MESSAGE = "Message"
    ERROR_CODE = "ErrorCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "error_code": "ErrorCode",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterface(PropertyType):
    NETWORK_INTERFACE_ID = "NetworkInterfaceId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_interface_id": "NetworkInterfaceId",
    }

    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

