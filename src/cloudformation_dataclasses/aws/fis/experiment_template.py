"""PropertyTypes for AWS::FIS::ExperimentTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchDashboard(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dashboard_identifier": "DashboardIdentifier",
    }

    dashboard_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataSources(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_dashboards": "CloudWatchDashboards",
    }

    cloud_watch_dashboards: Optional[list[CloudWatchDashboard]] = None


@dataclass
class ExperimentReportS3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateAction(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "empty_target_resolution_mode": "EmptyTargetResolutionMode",
        "account_targeting": "AccountTargeting",
    }

    empty_target_resolution_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_targeting: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateExperimentReportConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "source": "Source",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ExperimentTemplateTarget(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "values": "Values",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Outputs(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "experiment_report_s3_configuration": "ExperimentReportS3Configuration",
    }

    experiment_report_s3_configuration: Optional[ExperimentReportS3Configuration] = None


@dataclass
class S3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "prefix": "Prefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

