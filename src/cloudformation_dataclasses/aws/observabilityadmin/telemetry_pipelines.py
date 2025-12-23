"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryPipelines."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class TelemetryPipeline(PropertyType):
    STATUS = "Status"
    LAST_UPDATE_TIME_STAMP = "LastUpdateTimeStamp"
    CREATED_TIME_STAMP = "CreatedTimeStamp"
    CONFIGURATION = "Configuration"
    STATUS_REASON = "StatusReason"
    ARN = "Arn"
    TAGS = "Tags"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "last_update_time_stamp": "LastUpdateTimeStamp",
        "created_time_stamp": "CreatedTimeStamp",
        "configuration": "Configuration",
        "status_reason": "StatusReason",
        "arn": "Arn",
        "tags": "Tags",
        "name": "Name",
    }

    status: Optional[Union[str, TelemetryPipelineStatus, Ref, GetAtt, Sub]] = None
    last_update_time_stamp: Optional[Union[float, Ref, GetAtt, Sub]] = None
    created_time_stamp: Optional[Union[float, Ref, GetAtt, Sub]] = None
    configuration: Optional[TelemetryPipelineConfiguration] = None
    status_reason: Optional[TelemetryPipelineStatusReason] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TelemetryPipelineConfiguration(PropertyType):
    BODY = "Body"

    _property_mappings: ClassVar[dict[str, str]] = {
        "body": "Body",
    }

    body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TelemetryPipelineStatusReason(PropertyType):
    DESCRIPTION = "Description"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None

