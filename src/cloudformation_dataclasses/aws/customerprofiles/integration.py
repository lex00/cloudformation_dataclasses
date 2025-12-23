"""PropertyTypes for AWS::CustomerProfiles::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectorOperator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "service_now": "ServiceNow",
        "zendesk": "Zendesk",
        "marketo": "Marketo",
        "salesforce": "Salesforce",
    }

    s3: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_now: Optional[Union[str, Ref, GetAtt, Sub]] = None
    zendesk: Optional[Union[str, Ref, GetAtt, Sub]] = None
    marketo: Optional[Union[str, Ref, GetAtt, Sub]] = None
    salesforce: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "tasks": "Tasks",
        "flow_name": "FlowName",
        "trigger_config": "TriggerConfig",
        "source_flow_config": "SourceFlowConfig",
        "kms_arn": "KmsArn",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tasks: Optional[list[Task]] = None
    flow_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_config: Optional[TriggerConfig] = None
    source_flow_config: Optional[SourceFlowConfig] = None
    kms_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IncrementalPullConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "datetime_type_field_name": "DatetimeTypeFieldName",
    }

    datetime_type_field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MarketoSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectTypeMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3SourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_deleted_records": "IncludeDeletedRecords",
        "object": "Object",
        "enable_dynamic_field_update": "EnableDynamicFieldUpdate",
    }

    include_deleted_records: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_dynamic_field_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_end_time": "ScheduleEndTime",
        "timezone": "Timezone",
        "schedule_expression": "ScheduleExpression",
        "first_execution_from": "FirstExecutionFrom",
        "schedule_start_time": "ScheduleStartTime",
        "data_pull_mode": "DataPullMode",
        "schedule_offset": "ScheduleOffset",
    }

    schedule_end_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_execution_from: Optional[Union[float, Ref, GetAtt, Sub]] = None
    schedule_start_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    data_pull_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_offset: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConnectorProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "service_now": "ServiceNow",
        "zendesk": "Zendesk",
        "marketo": "Marketo",
        "salesforce": "Salesforce",
    }

    s3: Optional[S3SourceProperties] = None
    service_now: Optional[ServiceNowSourceProperties] = None
    zendesk: Optional[ZendeskSourceProperties] = None
    marketo: Optional[MarketoSourceProperties] = None
    salesforce: Optional[SalesforceSourceProperties] = None


@dataclass
class SourceFlowConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_profile_name": "ConnectorProfileName",
        "source_connector_properties": "SourceConnectorProperties",
        "connector_type": "ConnectorType",
        "incremental_pull_config": "IncrementalPullConfig",
    }

    connector_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_connector_properties: Optional[SourceConnectorProperties] = None
    connector_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    incremental_pull_config: Optional[IncrementalPullConfig] = None


@dataclass
class Task(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_fields": "SourceFields",
        "destination_field": "DestinationField",
        "connector_operator": "ConnectorOperator",
        "task_type": "TaskType",
        "task_properties": "TaskProperties",
    }

    source_fields: Optional[Union[list[str], Ref]] = None
    destination_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_operator: Optional[ConnectorOperator] = None
    task_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    task_properties: Optional[list[TaskPropertiesMap]] = None


@dataclass
class TaskPropertiesMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operator_property_key": "OperatorPropertyKey",
        "property": "Property",
    }

    operator_property_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TriggerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "trigger_type": "TriggerType",
        "trigger_properties": "TriggerProperties",
    }

    trigger_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_properties: Optional[TriggerProperties] = None


@dataclass
class TriggerProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scheduled": "Scheduled",
    }

    scheduled: Optional[ScheduledTriggerProperties] = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None

