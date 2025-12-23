"""PropertyTypes for AWS::StepFunctions::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogsLogGroup(PropertyType):
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    TYPE = "Type"
    KMS_KEY_ID = "KmsKeyId"
    KMS_DATA_KEY_REUSE_PERIOD_SECONDS = "KmsDataKeyReusePeriodSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "kms_key_id": "KmsKeyId",
        "kms_data_key_reuse_period_seconds": "KmsDataKeyReusePeriodSeconds",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_data_key_reuse_period_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LogDestination(PropertyType):
    CLOUD_WATCH_LOGS_LOG_GROUP = "CloudWatchLogsLogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_log_group": "CloudWatchLogsLogGroup",
    }

    cloud_watch_logs_log_group: Optional[CloudWatchLogsLogGroup] = None


@dataclass
class LoggingConfiguration(PropertyType):
    INCLUDE_EXECUTION_DATA = "IncludeExecutionData"
    DESTINATIONS = "Destinations"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_execution_data": "IncludeExecutionData",
        "destinations": "Destinations",
        "level": "Level",
    }

    include_execution_data: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    destinations: Optional[list[LogDestination]] = None
    level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    VERSION = "Version"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagsEntry(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TracingConfiguration(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

