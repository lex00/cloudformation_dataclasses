"""PropertyTypes for AWS::Route53::HostedZone."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HostedZoneConfig(PropertyType):
    COMMENT = "Comment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HostedZoneFeatures(PropertyType):
    ENABLE_ACCELERATED_RECOVERY = "EnableAcceleratedRecovery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_accelerated_recovery": "EnableAcceleratedRecovery",
    }

    enable_accelerated_recovery: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HostedZoneTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryLoggingConfig(PropertyType):
    CLOUD_WATCH_LOGS_LOG_GROUP_ARN = "CloudWatchLogsLogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group_arn": "CloudWatchLogsLogGroupArn",
    }

    cloud_watch_logs_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VPC(PropertyType):
    VPC_REGION = "VPCRegion"
    VPC_ID = "VPCId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_region": "VPCRegion",
        "vpc_id": "VPCId",
    }

    vpc_region: Optional[Union[str, VPCRegion, Ref, GetAtt, Sub]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

