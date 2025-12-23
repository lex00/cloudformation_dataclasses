"""PropertyTypes for AWS::IoTAnalytics::Dataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_name": "ActionName",
        "container_action": "ContainerAction",
        "query_action": "QueryAction",
    }

    action_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_action: Optional[ContainerAction] = None
    query_action: Optional[QueryAction] = None


@dataclass
class ContainerAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "variables": "Variables",
        "execution_role_arn": "ExecutionRoleArn",
        "image": "Image",
        "resource_configuration": "ResourceConfiguration",
    }

    variables: Optional[list[Variable]] = None
    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_configuration: Optional[ResourceConfiguration] = None


@dataclass
class DatasetContentDeliveryRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "entry_name": "EntryName",
    }

    destination: Optional[DatasetContentDeliveryRuleDestination] = None
    entry_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatasetContentDeliveryRuleDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iot_events_destination_configuration": "IotEventsDestinationConfiguration",
        "s3_destination_configuration": "S3DestinationConfiguration",
    }

    iot_events_destination_configuration: Optional[IotEventsDestinationConfiguration] = None
    s3_destination_configuration: Optional[S3DestinationConfiguration] = None


@dataclass
class DatasetContentVersionValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_name": "DatasetName",
    }

    dataset_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeltaTime(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time_expression": "TimeExpression",
        "offset_seconds": "OffsetSeconds",
    }

    time_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    offset_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeltaTimeSessionWindowConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_in_minutes": "TimeoutInMinutes",
    }

    timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delta_time": "DeltaTime",
    }

    delta_time: Optional[DeltaTime] = None


@dataclass
class GlueConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IotEventsDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_name": "InputName",
        "role_arn": "RoleArn",
    }

    input_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LateDataRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_configuration": "RuleConfiguration",
        "rule_name": "RuleName",
    }

    rule_configuration: Optional[LateDataRuleConfiguration] = None
    rule_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LateDataRuleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delta_time_session_window_configuration": "DeltaTimeSessionWindowConfiguration",
    }

    delta_time_session_window_configuration: Optional[DeltaTimeSessionWindowConfiguration] = None


@dataclass
class OutputFileUriValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_name": "FileName",
    }

    file_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "sql_query": "SqlQuery",
    }

    filters: Optional[list[Filter]] = None
    sql_query: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
        "compute_type": "ComputeType",
    }

    volume_size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    compute_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_days": "NumberOfDays",
        "unlimited": "Unlimited",
    }

    number_of_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_configuration": "GlueConfiguration",
        "bucket": "Bucket",
        "key": "Key",
        "role_arn": "RoleArn",
    }

    glue_configuration: Optional[GlueConfiguration] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Trigger(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule": "Schedule",
        "triggering_dataset": "TriggeringDataset",
    }

    schedule: Optional[Schedule] = None
    triggering_dataset: Optional[TriggeringDataset] = None


@dataclass
class TriggeringDataset(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_name": "DatasetName",
    }

    dataset_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Variable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dataset_content_version_value": "DatasetContentVersionValue",
        "double_value": "DoubleValue",
        "output_file_uri_value": "OutputFileUriValue",
        "variable_name": "VariableName",
        "string_value": "StringValue",
    }

    dataset_content_version_value: Optional[DatasetContentVersionValue] = None
    double_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    output_file_uri_value: Optional[OutputFileUriValue] = None
    variable_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    string_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VersioningConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_versions": "MaxVersions",
        "unlimited": "Unlimited",
    }

    max_versions: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unlimited: Optional[Union[bool, Ref, GetAtt, Sub]] = None

