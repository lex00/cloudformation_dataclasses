"""PropertyTypes for AWS::SSM::MaintenanceWindowTask."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchOutputConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_output_enabled": "CloudWatchOutputEnabled",
        "cloud_watch_log_group_name": "CloudWatchLogGroupName",
    }

    cloud_watch_output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "region": "Region",
        "s3_prefix": "S3Prefix",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowAutomationParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "document_version": "DocumentVersion",
    }

    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowLambdaParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_context": "ClientContext",
        "qualifier": "Qualifier",
        "payload": "Payload",
    }

    client_context: Optional[Union[str, Ref, GetAtt, Sub]] = None
    qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowRunCommandParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_seconds": "TimeoutSeconds",
        "comment": "Comment",
        "output_s3_key_prefix": "OutputS3KeyPrefix",
        "parameters": "Parameters",
        "cloud_watch_output_config": "CloudWatchOutputConfig",
        "document_hash_type": "DocumentHashType",
        "service_role_arn": "ServiceRoleArn",
        "notification_config": "NotificationConfig",
        "document_version": "DocumentVersion",
        "output_s3_bucket_name": "OutputS3BucketName",
        "document_hash": "DocumentHash",
    }

    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    cloud_watch_output_config: Optional[CloudWatchOutputConfig] = None
    document_hash_type: Optional[Union[str, DocumentHashType, Ref, GetAtt, Sub]] = None
    service_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_config: Optional[NotificationConfig] = None
    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_hash: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowStepFunctionsParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input": "Input",
        "name": "Name",
    }

    input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_arn": "NotificationArn",
        "notification_type": "NotificationType",
        "notification_events": "NotificationEvents",
    }

    notification_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_type: Optional[Union[str, NotificationType, Ref, GetAtt, Sub]] = None
    notification_events: Optional[Union[list[str], Ref]] = None


@dataclass
class Target(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskInvocationParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_window_run_command_parameters": "MaintenanceWindowRunCommandParameters",
        "maintenance_window_automation_parameters": "MaintenanceWindowAutomationParameters",
        "maintenance_window_step_functions_parameters": "MaintenanceWindowStepFunctionsParameters",
        "maintenance_window_lambda_parameters": "MaintenanceWindowLambdaParameters",
    }

    maintenance_window_run_command_parameters: Optional[MaintenanceWindowRunCommandParameters] = None
    maintenance_window_automation_parameters: Optional[MaintenanceWindowAutomationParameters] = None
    maintenance_window_step_functions_parameters: Optional[MaintenanceWindowStepFunctionsParameters] = None
    maintenance_window_lambda_parameters: Optional[MaintenanceWindowLambdaParameters] = None

