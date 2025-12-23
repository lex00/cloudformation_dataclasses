"""PropertyTypes for AWS::Glue::IntegrationResourceProperty."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SourceProcessingProperties(PropertyType):
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleArn",
    }

    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetProcessingProperties(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    KMS_ARN = "KmsArn"
    ROLE_ARN = "RoleArn"
    EVENT_BUS_ARN = "EventBusArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "kms_arn": "KmsArn",
        "role_arn": "RoleArn",
        "event_bus_arn": "EventBusArn",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_bus_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

