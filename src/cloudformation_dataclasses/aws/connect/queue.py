"""PropertyTypes for AWS::Connect::Queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OutboundCallerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_caller_id_number_arn": "OutboundCallerIdNumberArn",
        "outbound_flow_arn": "OutboundFlowArn",
        "outbound_caller_id_name": "OutboundCallerIdName",
    }

    outbound_caller_id_number_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    outbound_flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    outbound_caller_id_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutboundEmailConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "outbound_email_address_id": "OutboundEmailAddressId",
    }

    outbound_email_address_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

