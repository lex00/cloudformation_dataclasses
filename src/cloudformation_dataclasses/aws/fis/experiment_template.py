"""PropertyTypes for AWS::FIS::ExperimentTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountTargeting:
    """AccountTargeting enum values."""

    SINGLE_ACCOUNT = "single-account"
    MULTI_ACCOUNT = "multi-account"


class ActionsMode:
    """ActionsMode enum values."""

    SKIP_ALL = "skip-all"
    RUN_ALL = "run-all"


class EmptyTargetResolutionMode:
    """EmptyTargetResolutionMode enum values."""

    FAIL = "fail"
    SKIP = "skip"


class ExperimentActionStatus:
    """ExperimentActionStatus enum values."""

    PENDING = "pending"
    INITIATING = "initiating"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"
    SKIPPED = "skipped"


class ExperimentReportStatus:
    """ExperimentReportStatus enum values."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class ExperimentStatus:
    """ExperimentStatus enum values."""

    PENDING = "pending"
    INITIATING = "initiating"
    RUNNING = "running"
    COMPLETED = "completed"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"
    CANCELLED = "cancelled"


class SafetyLeverStatus:
    """SafetyLeverStatus enum values."""

    DISENGAGED = "disengaged"
    ENGAGED = "engaged"
    ENGAGING = "engaging"


class SafetyLeverStatusInput:
    """SafetyLeverStatusInput enum values."""

    DISENGAGED = "disengaged"
    ENGAGED = "engaged"


@dataclass
class CloudWatchDashboard(PropertyType):
    DASHBOARD_IDENTIFIER = "DashboardIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dashboard_identifier": "DashboardIdentifier",
    }

    dashboard_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    LOG_GROUP_ARN = "LogGroupArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSources(PropertyType):
    CLOUD_WATCH_DASHBOARDS = "CloudWatchDashboards"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_dashboards": "CloudWatchDashboards",
    }

    cloud_watch_dashboards: Optional[list[CloudWatchDashboard]] = None


@dataclass
class ExperimentReportS3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateAction(PropertyType):
    ACTION_ID = "ActionId"
    DESCRIPTION = "Description"
    PARAMETERS = "Parameters"
    TARGETS = "Targets"
    START_AFTER = "StartAfter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action_id": "ActionId",
        "description": "Description",
        "parameters": "Parameters",
        "targets": "Targets",
        "start_after": "StartAfter",
    }

    action_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[dict[str, str]] = None
    targets: Optional[dict[str, str]] = None
    start_after: Optional[Union[list[str], Ref]] = None


@dataclass
class ExperimentTemplateExperimentOptions(PropertyType):
    EMPTY_TARGET_RESOLUTION_MODE = "EmptyTargetResolutionMode"
    ACCOUNT_TARGETING = "AccountTargeting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "empty_target_resolution_mode": "EmptyTargetResolutionMode",
        "account_targeting": "AccountTargeting",
    }

    empty_target_resolution_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_targeting: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateExperimentReportConfiguration(PropertyType):
    DATA_SOURCES = "DataSources"
    POST_EXPERIMENT_DURATION = "PostExperimentDuration"
    OUTPUTS = "Outputs"
    PRE_EXPERIMENT_DURATION = "PreExperimentDuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_sources": "DataSources",
        "post_experiment_duration": "PostExperimentDuration",
        "outputs": "Outputs",
        "pre_experiment_duration": "PreExperimentDuration",
    }

    data_sources: Optional[DataSources] = None
    post_experiment_duration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    outputs: Optional[Outputs] = None
    pre_experiment_duration: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateLogConfiguration(PropertyType):
    S3_CONFIGURATION = "S3Configuration"
    LOG_SCHEMA_VERSION = "LogSchemaVersion"
    CLOUD_WATCH_LOGS_CONFIGURATION = "CloudWatchLogsConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_configuration": "S3Configuration",
        "log_schema_version": "LogSchemaVersion",
        "cloud_watch_logs_configuration": "CloudWatchLogsConfiguration",
    }

    s3_configuration: Optional[S3Configuration] = None
    log_schema_version: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cloud_watch_logs_configuration: Optional[CloudWatchLogsConfiguration] = None


@dataclass
class ExperimentTemplateStopCondition(PropertyType):
    VALUE = "Value"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "source": "Source",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateTarget(PropertyType):
    FILTERS = "Filters"
    PARAMETERS = "Parameters"
    RESOURCE_TAGS = "ResourceTags"
    RESOURCE_TYPE = "ResourceType"
    RESOURCE_ARNS = "ResourceArns"
    SELECTION_MODE = "SelectionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "parameters": "Parameters",
        "resource_tags": "ResourceTags",
        "resource_type": "ResourceType",
        "resource_arns": "ResourceArns",
        "selection_mode": "SelectionMode",
    }

    filters: Optional[list[ExperimentTemplateTargetFilter]] = None
    parameters: Optional[dict[str, str]] = None
    resource_tags: Optional[dict[str, str]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_arns: Optional[Union[list[str], Ref]] = None
    selection_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateTargetFilter(PropertyType):
    PATH = "Path"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "values": "Values",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Outputs(PropertyType):
    EXPERIMENT_REPORT_S3_CONFIGURATION = "ExperimentReportS3Configuration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "experiment_report_s3_configuration": "ExperimentReportS3Configuration",
    }

    experiment_report_s3_configuration: Optional[ExperimentReportS3Configuration] = None


@dataclass
class S3Configuration(PropertyType):
    BUCKET_NAME = "BucketName"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

