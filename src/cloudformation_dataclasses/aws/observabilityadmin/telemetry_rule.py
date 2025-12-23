"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionCondition(PropertyType):
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedEventSelector(PropertyType):
    FIELD_SELECTORS = "FieldSelectors"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_selectors": "FieldSelectors",
        "name": "Name",
    }

    field_selectors: Optional[list[AdvancedFieldSelector]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    FIELD = "Field"
    EQUALS = "Equals"
    NOT_STARTS_WITH = "NotStartsWith"
    NOT_ENDS_WITH = "NotEndsWith"
    STARTS_WITH = "StartsWith"
    ENDS_WITH = "EndsWith"
    NOT_EQUALS = "NotEquals"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field": "Field",
        "equals": "Equals",
        "not_starts_with": "NotStartsWith",
        "not_ends_with": "NotEndsWith",
        "starts_with": "StartsWith",
        "ends_with": "EndsWith",
        "not_equals": "NotEquals",
    }

    field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    equals: Optional[Union[list[str], Ref]] = None
    not_starts_with: Optional[Union[list[str], Ref]] = None
    not_ends_with: Optional[Union[list[str], Ref]] = None
    starts_with: Optional[Union[list[str], Ref]] = None
    ends_with: Optional[Union[list[str], Ref]] = None
    not_equals: Optional[Union[list[str], Ref]] = None


@dataclass
class CloudtrailParameters(PropertyType):
    ADVANCED_EVENT_SELECTORS = "AdvancedEventSelectors"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_event_selectors": "AdvancedEventSelectors",
    }

    advanced_event_selectors: Optional[list[AdvancedEventSelector]] = None


@dataclass
class Condition(PropertyType):
    LABEL_NAME_CONDITION = "LabelNameCondition"
    ACTION_CONDITION = "ActionCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "label_name_condition": "LabelNameCondition",
        "action_condition": "ActionCondition",
    }

    label_name_condition: Optional[LabelNameCondition] = None
    action_condition: Optional[ActionCondition] = None


@dataclass
class ELBLoadBalancerLoggingParameters(PropertyType):
    FIELD_DELIMITER = "FieldDelimiter"
    OUTPUT_FORMAT = "OutputFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_delimiter": "FieldDelimiter",
        "output_format": "OutputFormat",
    }

    field_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_format: Optional[Union[str, OutputFormat, Ref, GetAtt, Sub]] = None


@dataclass
class FieldToMatch(PropertyType):
    URI_PATH = "UriPath"
    QUERY_STRING = "QueryString"
    METHOD = "Method"
    SINGLE_HEADER = "SingleHeader"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uri_path": "UriPath",
        "query_string": "QueryString",
        "method": "Method",
        "single_header": "SingleHeader",
    }

    uri_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    single_header: Optional[SingleHeader] = None


@dataclass
class Filter(PropertyType):
    REQUIREMENT = "Requirement"
    BEHAVIOR = "Behavior"
    CONDITIONS = "Conditions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "requirement": "Requirement",
        "behavior": "Behavior",
        "conditions": "Conditions",
    }

    requirement: Optional[Union[str, FilterRequirement, Ref, GetAtt, Sub]] = None
    behavior: Optional[Union[str, FilterBehavior, Ref, GetAtt, Sub]] = None
    conditions: Optional[list[Condition]] = None


@dataclass
class LabelNameCondition(PropertyType):
    LABEL_NAME = "LabelName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "label_name": "LabelName",
    }

    label_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogDeliveryParameters(PropertyType):
    LOG_TYPES = "LogTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_types": "LogTypes",
    }

    log_types: Optional[Union[list[str], Ref]] = None


@dataclass
class LoggingFilter(PropertyType):
    FILTERS = "Filters"
    DEFAULT_BEHAVIOR = "DefaultBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "default_behavior": "DefaultBehavior",
    }

    filters: Optional[list[Filter]] = None
    default_behavior: Optional[Union[str, FilterBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class SingleHeader(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TelemetryDestinationConfiguration(PropertyType):
    RETENTION_IN_DAYS = "RetentionInDays"
    DESTINATION_PATTERN = "DestinationPattern"
    ELB_LOAD_BALANCER_LOGGING_PARAMETERS = "ELBLoadBalancerLoggingParameters"
    VPC_FLOW_LOG_PARAMETERS = "VPCFlowLogParameters"
    CLOUDTRAIL_PARAMETERS = "CloudtrailParameters"
    WAF_LOGGING_PARAMETERS = "WAFLoggingParameters"
    LOG_DELIVERY_PARAMETERS = "LogDeliveryParameters"
    DESTINATION_TYPE = "DestinationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_in_days": "RetentionInDays",
        "destination_pattern": "DestinationPattern",
        "elb_load_balancer_logging_parameters": "ELBLoadBalancerLoggingParameters",
        "vpc_flow_log_parameters": "VPCFlowLogParameters",
        "cloudtrail_parameters": "CloudtrailParameters",
        "waf_logging_parameters": "WAFLoggingParameters",
        "log_delivery_parameters": "LogDeliveryParameters",
        "destination_type": "DestinationType",
    }

    retention_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    elb_load_balancer_logging_parameters: Optional[ELBLoadBalancerLoggingParameters] = None
    vpc_flow_log_parameters: Optional[VPCFlowLogParameters] = None
    cloudtrail_parameters: Optional[CloudtrailParameters] = None
    waf_logging_parameters: Optional[WAFLoggingParameters] = None
    log_delivery_parameters: Optional[LogDeliveryParameters] = None
    destination_type: Optional[Union[str, DestinationType, Ref, GetAtt, Sub]] = None


@dataclass
class TelemetryRule(PropertyType):
    TELEMETRY_SOURCE_TYPES = "TelemetrySourceTypes"
    DESTINATION_CONFIGURATION = "DestinationConfiguration"
    SELECTION_CRITERIA = "SelectionCriteria"
    RESOURCE_TYPE = "ResourceType"
    TELEMETRY_TYPE = "TelemetryType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "telemetry_source_types": "TelemetrySourceTypes",
        "destination_configuration": "DestinationConfiguration",
        "selection_criteria": "SelectionCriteria",
        "resource_type": "ResourceType",
        "telemetry_type": "TelemetryType",
    }

    telemetry_source_types: Optional[Union[list[str], Ref]] = None
    destination_configuration: Optional[TelemetryDestinationConfiguration] = None
    selection_criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    telemetry_type: Optional[Union[str, TelemetryType, Ref, GetAtt, Sub]] = None


@dataclass
class VPCFlowLogParameters(PropertyType):
    LOG_FORMAT = "LogFormat"
    MAX_AGGREGATION_INTERVAL = "MaxAggregationInterval"
    TRAFFIC_TYPE = "TrafficType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_format": "LogFormat",
        "max_aggregation_interval": "MaxAggregationInterval",
        "traffic_type": "TrafficType",
    }

    log_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_aggregation_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    traffic_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WAFLoggingParameters(PropertyType):
    REDACTED_FIELDS = "RedactedFields"
    LOGGING_FILTER = "LoggingFilter"
    LOG_TYPE = "LogType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "redacted_fields": "RedactedFields",
        "logging_filter": "LoggingFilter",
        "log_type": "LogType",
    }

    redacted_fields: Optional[list[FieldToMatch]] = None
    logging_filter: Optional[LoggingFilter] = None
    log_type: Optional[Union[str, WAFLogType, Ref, GetAtt, Sub]] = None

