"""PropertyTypes for AWS::Route53::HostedZone."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HostedZoneConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HostedZoneFeatures(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_accelerated_recovery": "EnableAcceleratedRecovery",
    }

    enable_accelerated_recovery: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HostedZoneTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryLoggingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group_arn": "CloudWatchLogsLogGroupArn",
    }

    cloud_watch_logs_log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VPC(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_region": "VPCRegion",
        "vpc_id": "VPCId",
    }

    vpc_region: Optional[Union[str, VPCRegion, Ref, GetAtt, Sub]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

