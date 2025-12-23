"""PropertyTypes for AWS::QuickSight::VPCConnection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NetworkInterface(PropertyType):
    STATUS = "Status"
    AVAILABILITY_ZONE = "AvailabilityZone"
    SUBNET_ID = "SubnetId"
    ERROR_MESSAGE = "ErrorMessage"
    NETWORK_INTERFACE_ID = "NetworkInterfaceId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "availability_zone": "AvailabilityZone",
        "subnet_id": "SubnetId",
        "error_message": "ErrorMessage",
        "network_interface_id": "NetworkInterfaceId",
    }

    status: Optional[Union[str, NetworkInterfaceStatus, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

