"""PropertyTypes for AWS::CustomerProfiles::Integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectorOperator(PropertyType):
    S3 = "S3"
    SERVICE_NOW = "ServiceNow"
    ZENDESK = "Zendesk"
    MARKETO = "Marketo"
    SALESFORCE = "Salesforce"

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
    DESCRIPTION = "Description"
    TASKS = "Tasks"
    FLOW_NAME = "FlowName"
    TRIGGER_CONFIG = "TriggerConfig"
    SOURCE_FLOW_CONFIG = "SourceFlowConfig"
    KMS_ARN = "KmsArn"

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
    DATETIME_TYPE_FIELD_NAME = "DatetimeTypeFieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "datetime_type_field_name": "DatetimeTypeFieldName",
    }

    datetime_type_field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MarketoSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ObjectTypeMapping(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3SourceProperties(PropertyType):
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    INCLUDE_DELETED_RECORDS = "IncludeDeletedRecords"
    OBJECT = "Object"
    ENABLE_DYNAMIC_FIELD_UPDATE = "EnableDynamicFieldUpdate"

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
    SCHEDULE_END_TIME = "ScheduleEndTime"
    TIMEZONE = "Timezone"
    SCHEDULE_EXPRESSION = "ScheduleExpression"
    FIRST_EXECUTION_FROM = "FirstExecutionFrom"
    SCHEDULE_START_TIME = "ScheduleStartTime"
    DATA_PULL_MODE = "DataPullMode"
    SCHEDULE_OFFSET = "ScheduleOffset"

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
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConnectorProperties(PropertyType):
    S3 = "S3"
    SERVICE_NOW = "ServiceNow"
    ZENDESK = "Zendesk"
    MARKETO = "Marketo"
    SALESFORCE = "Salesforce"

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
    CONNECTOR_PROFILE_NAME = "ConnectorProfileName"
    SOURCE_CONNECTOR_PROPERTIES = "SourceConnectorProperties"
    CONNECTOR_TYPE = "ConnectorType"
    INCREMENTAL_PULL_CONFIG = "IncrementalPullConfig"

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
    SOURCE_FIELDS = "SourceFields"
    DESTINATION_FIELD = "DestinationField"
    CONNECTOR_OPERATOR = "ConnectorOperator"
    TASK_TYPE = "TaskType"
    TASK_PROPERTIES = "TaskProperties"

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
    OPERATOR_PROPERTY_KEY = "OperatorPropertyKey"
    PROPERTY = "Property"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator_property_key": "OperatorPropertyKey",
        "property": "Property",
    }

    operator_property_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    property: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TriggerConfig(PropertyType):
    TRIGGER_TYPE = "TriggerType"
    TRIGGER_PROPERTIES = "TriggerProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trigger_type": "TriggerType",
        "trigger_properties": "TriggerProperties",
    }

    trigger_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_properties: Optional[TriggerProperties] = None


@dataclass
class TriggerProperties(PropertyType):
    SCHEDULED = "Scheduled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scheduled": "Scheduled",
    }

    scheduled: Optional[ScheduledTriggerProperties] = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None

