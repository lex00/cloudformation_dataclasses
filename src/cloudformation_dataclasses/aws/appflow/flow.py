"""PropertyTypes for AWS::AppFlow::Flow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AggregationType:
    """AggregationType enum values."""

    NONE = "None"
    SINGLEFILE = "SingleFile"


class AmplitudeConnectorOperator:
    """AmplitudeConnectorOperator enum values."""

    BETWEEN = "BETWEEN"


class AuthenticationType:
    """AuthenticationType enum values."""

    OAUTH2 = "OAUTH2"
    APIKEY = "APIKEY"
    BASIC = "BASIC"
    CUSTOM = "CUSTOM"


class CatalogType:
    """CatalogType enum values."""

    GLUE = "GLUE"


class ConnectionMode:
    """ConnectionMode enum values."""

    PUBLIC = "Public"
    PRIVATE = "Private"


class ConnectorProvisioningType:
    """ConnectorProvisioningType enum values."""

    LAMBDA = "LAMBDA"


class ConnectorType:
    """ConnectorType enum values."""

    SALESFORCE = "Salesforce"
    SINGULAR = "Singular"
    SLACK = "Slack"
    REDSHIFT = "Redshift"
    S3 = "S3"
    MARKETO = "Marketo"
    GOOGLEANALYTICS = "Googleanalytics"
    ZENDESK = "Zendesk"
    SERVICENOW = "Servicenow"
    DATADOG = "Datadog"
    TRENDMICRO = "Trendmicro"
    SNOWFLAKE = "Snowflake"
    DYNATRACE = "Dynatrace"
    INFORNEXUS = "Infornexus"
    AMPLITUDE = "Amplitude"
    VEEVA = "Veeva"
    EVENTBRIDGE = "EventBridge"
    LOOKOUTMETRICS = "LookoutMetrics"
    UPSOLVER = "Upsolver"
    HONEYCODE = "Honeycode"
    CUSTOMERPROFILES = "CustomerProfiles"
    SAPODATA = "SAPOData"
    CUSTOMCONNECTOR = "CustomConnector"
    PARDOT = "Pardot"


class DataPullMode:
    """DataPullMode enum values."""

    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"


class DataTransferApiType:
    """DataTransferApiType enum values."""

    SYNC = "SYNC"
    ASYNC = "ASYNC"
    AUTOMATIC = "AUTOMATIC"


class DatadogConnectorOperator:
    """DatadogConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    BETWEEN = "BETWEEN"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class DynatraceConnectorOperator:
    """DynatraceConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    BETWEEN = "BETWEEN"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    INPROGRESS = "InProgress"
    SUCCESSFUL = "Successful"
    ERROR = "Error"
    CANCELSTARTED = "CancelStarted"
    CANCELED = "Canceled"


class FileType:
    """FileType enum values."""

    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"


class FlowStatus:
    """FlowStatus enum values."""

    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DELETED = "Deleted"
    DRAFT = "Draft"
    ERRORED = "Errored"
    SUSPENDED = "Suspended"


class GoogleAnalyticsConnectorOperator:
    """GoogleAnalyticsConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    BETWEEN = "BETWEEN"


class InforNexusConnectorOperator:
    """InforNexusConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    BETWEEN = "BETWEEN"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class MarketoConnectorOperator:
    """MarketoConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class OAuth2CustomPropType:
    """OAuth2CustomPropType enum values."""

    TOKEN_URL = "TOKEN_URL"
    AUTH_URL = "AUTH_URL"


class OAuth2GrantType:
    """OAuth2GrantType enum values."""

    CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"
    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    JWT_BEARER = "JWT_BEARER"


class Operator:
    """Operator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    CONTAINS = "CONTAINS"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class OperatorPropertiesKeys:
    """OperatorPropertiesKeys enum values."""

    VALUE = "VALUE"
    VALUES = "VALUES"
    DATA_TYPE = "DATA_TYPE"
    UPPER_BOUND = "UPPER_BOUND"
    LOWER_BOUND = "LOWER_BOUND"
    SOURCE_DATA_TYPE = "SOURCE_DATA_TYPE"
    DESTINATION_DATA_TYPE = "DESTINATION_DATA_TYPE"
    VALIDATION_ACTION = "VALIDATION_ACTION"
    MASK_VALUE = "MASK_VALUE"
    MASK_LENGTH = "MASK_LENGTH"
    TRUNCATE_LENGTH = "TRUNCATE_LENGTH"
    MATH_OPERATION_FIELDS_ORDER = "MATH_OPERATION_FIELDS_ORDER"
    CONCAT_FORMAT = "CONCAT_FORMAT"
    SUBFIELD_CATEGORY_MAP = "SUBFIELD_CATEGORY_MAP"
    EXCLUDE_SOURCE_FIELDS_LIST = "EXCLUDE_SOURCE_FIELDS_LIST"
    INCLUDE_NEW_FIELDS = "INCLUDE_NEW_FIELDS"
    ORDERED_PARTITION_KEYS_LIST = "ORDERED_PARTITION_KEYS_LIST"


class Operators:
    """Operators enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    CONTAINS = "CONTAINS"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class PardotConnectorOperator:
    """PardotConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    EQUAL_TO = "EQUAL_TO"
    NO_OP = "NO_OP"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"


class PathPrefix:
    """PathPrefix enum values."""

    EXECUTION_ID = "EXECUTION_ID"
    SCHEMA_VERSION = "SCHEMA_VERSION"


class PrefixFormat:
    """PrefixFormat enum values."""

    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"


class PrefixType:
    """PrefixType enum values."""

    FILENAME = "FILENAME"
    PATH = "PATH"
    PATH_AND_FILENAME = "PATH_AND_FILENAME"


class PrivateConnectionProvisioningFailureCause:
    """PrivateConnectionProvisioningFailureCause enum values."""

    CONNECTOR_AUTHENTICATION = "CONNECTOR_AUTHENTICATION"
    CONNECTOR_SERVER = "CONNECTOR_SERVER"
    INTERNAL_SERVER = "INTERNAL_SERVER"
    ACCESS_DENIED = "ACCESS_DENIED"
    VALIDATION = "VALIDATION"


class PrivateConnectionProvisioningStatus:
    """PrivateConnectionProvisioningStatus enum values."""

    FAILED = "FAILED"
    PENDING = "PENDING"
    CREATED = "CREATED"


class S3ConnectorOperator:
    """S3ConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class S3InputFileType:
    """S3InputFileType enum values."""

    CSV = "CSV"
    JSON = "JSON"


class SAPODataConnectorOperator:
    """SAPODataConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    CONTAINS = "CONTAINS"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class SalesforceConnectorOperator:
    """SalesforceConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    CONTAINS = "CONTAINS"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class SalesforceDataTransferApi:
    """SalesforceDataTransferApi enum values."""

    AUTOMATIC = "AUTOMATIC"
    BULKV2 = "BULKV2"
    REST_SYNC = "REST_SYNC"


class ScheduleFrequencyType:
    """ScheduleFrequencyType enum values."""

    BYMINUTE = "BYMINUTE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    ONCE = "ONCE"


class ServiceNowConnectorOperator:
    """ServiceNowConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    CONTAINS = "CONTAINS"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class SingularConnectorOperator:
    """SingularConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class SlackConnectorOperator:
    """SlackConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class SupportedDataTransferType:
    """SupportedDataTransferType enum values."""

    RECORD = "RECORD"
    FILE = "FILE"


class TaskType:
    """TaskType enum values."""

    ARITHMETIC = "Arithmetic"
    FILTER = "Filter"
    MAP = "Map"
    MAP_ALL = "Map_all"
    MASK = "Mask"
    MERGE = "Merge"
    PASSTHROUGH = "Passthrough"
    TRUNCATE = "Truncate"
    VALIDATE = "Validate"
    PARTITION = "Partition"


class TrendmicroConnectorOperator:
    """TrendmicroConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    EQUAL_TO = "EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class TriggerType:
    """TriggerType enum values."""

    SCHEDULED = "Scheduled"
    EVENT = "Event"
    ONDEMAND = "OnDemand"


class VeevaConnectorOperator:
    """VeevaConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    CONTAINS = "CONTAINS"
    BETWEEN = "BETWEEN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


class WriteOperationType:
    """WriteOperationType enum values."""

    INSERT = "INSERT"
    UPSERT = "UPSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class ZendeskConnectorOperator:
    """ZendeskConnectorOperator enum values."""

    PROJECTION = "PROJECTION"
    GREATER_THAN = "GREATER_THAN"
    ADDITION = "ADDITION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SUBTRACTION = "SUBTRACTION"
    MASK_ALL = "MASK_ALL"
    MASK_FIRST_N = "MASK_FIRST_N"
    MASK_LAST_N = "MASK_LAST_N"
    VALIDATE_NON_NULL = "VALIDATE_NON_NULL"
    VALIDATE_NON_ZERO = "VALIDATE_NON_ZERO"
    VALIDATE_NON_NEGATIVE = "VALIDATE_NON_NEGATIVE"
    VALIDATE_NUMERIC = "VALIDATE_NUMERIC"
    NO_OP = "NO_OP"


@dataclass
class AggregationConfig(PropertyType):
    TARGET_FILE_SIZE = "TargetFileSize"
    AGGREGATION_TYPE = "AggregationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_file_size": "TargetFileSize",
        "aggregation_type": "AggregationType",
    }

    target_file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    aggregation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AmplitudeSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorOperator(PropertyType):
    AMPLITUDE = "Amplitude"
    S3 = "S3"
    GOOGLE_ANALYTICS = "GoogleAnalytics"
    SERVICE_NOW = "ServiceNow"
    CUSTOM_CONNECTOR = "CustomConnector"
    SAPO_DATA = "SAPOData"
    PARDOT = "Pardot"
    VEEVA = "Veeva"
    TRENDMICRO = "Trendmicro"
    DATADOG = "Datadog"
    MARKETO = "Marketo"
    SINGULAR = "Singular"
    SLACK = "Slack"
    DYNATRACE = "Dynatrace"
    ZENDESK = "Zendesk"
    INFOR_NEXUS = "InforNexus"
    SALESFORCE = "Salesforce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amplitude": "Amplitude",
        "s3": "S3",
        "google_analytics": "GoogleAnalytics",
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "trendmicro": "Trendmicro",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "singular": "Singular",
        "slack": "Slack",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    amplitude: Optional[Union[str, AmplitudeConnectorOperator, Ref, GetAtt, Sub]] = None
    s3: Optional[Union[str, S3ConnectorOperator, Ref, GetAtt, Sub]] = None
    google_analytics: Optional[Union[str, GoogleAnalyticsConnectorOperator, Ref, GetAtt, Sub]] = None
    service_now: Optional[Union[str, ServiceNowConnectorOperator, Ref, GetAtt, Sub]] = None
    custom_connector: Optional[Union[str, Operator, Ref, GetAtt, Sub]] = None
    sapo_data: Optional[Union[str, SAPODataConnectorOperator, Ref, GetAtt, Sub]] = None
    pardot: Optional[Union[str, PardotConnectorOperator, Ref, GetAtt, Sub]] = None
    veeva: Optional[Union[str, VeevaConnectorOperator, Ref, GetAtt, Sub]] = None
    trendmicro: Optional[Union[str, TrendmicroConnectorOperator, Ref, GetAtt, Sub]] = None
    datadog: Optional[Union[str, DatadogConnectorOperator, Ref, GetAtt, Sub]] = None
    marketo: Optional[Union[str, MarketoConnectorOperator, Ref, GetAtt, Sub]] = None
    singular: Optional[Union[str, SingularConnectorOperator, Ref, GetAtt, Sub]] = None
    slack: Optional[Union[str, SlackConnectorOperator, Ref, GetAtt, Sub]] = None
    dynatrace: Optional[Union[str, DynatraceConnectorOperator, Ref, GetAtt, Sub]] = None
    zendesk: Optional[Union[str, ZendeskConnectorOperator, Ref, GetAtt, Sub]] = None
    infor_nexus: Optional[Union[str, InforNexusConnectorOperator, Ref, GetAtt, Sub]] = None
    salesforce: Optional[Union[str, SalesforceConnectorOperator, Ref, GetAtt, Sub]] = None


@dataclass
class CustomConnectorDestinationProperties(PropertyType):
    ID_FIELD_NAMES = "IdFieldNames"
    ENTITY_NAME = "EntityName"
    WRITE_OPERATION_TYPE = "WriteOperationType"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"
    CUSTOM_PROPERTIES = "CustomProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_field_names": "IdFieldNames",
        "entity_name": "EntityName",
        "write_operation_type": "WriteOperationType",
        "error_handling_config": "ErrorHandlingConfig",
        "custom_properties": "CustomProperties",
    }

    id_field_names: Optional[Union[list[str], Ref]] = None
    entity_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    write_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None
    custom_properties: Optional[dict[str, str]] = None


@dataclass
class CustomConnectorSourceProperties(PropertyType):
    ENTITY_NAME = "EntityName"
    DATA_TRANSFER_API = "DataTransferApi"
    CUSTOM_PROPERTIES = "CustomProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_name": "EntityName",
        "data_transfer_api": "DataTransferApi",
        "custom_properties": "CustomProperties",
    }

    entity_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_transfer_api: Optional[DataTransferApi] = None
    custom_properties: Optional[dict[str, str]] = None


@dataclass
class DataTransferApi(PropertyType):
    TYPE = "Type"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "name": "Name",
    }

    type_: Optional[Union[str, DataTransferApiType, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatadogSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DestinationConnectorProperties(PropertyType):
    S3 = "S3"
    CUSTOM_CONNECTOR = "CustomConnector"
    UPSOLVER = "Upsolver"
    SAPO_DATA = "SAPOData"
    SNOWFLAKE = "Snowflake"
    LOOKOUT_METRICS = "LookoutMetrics"
    EVENT_BRIDGE = "EventBridge"
    ZENDESK = "Zendesk"
    MARKETO = "Marketo"
    REDSHIFT = "Redshift"
    SALESFORCE = "Salesforce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "custom_connector": "CustomConnector",
        "upsolver": "Upsolver",
        "sapo_data": "SAPOData",
        "snowflake": "Snowflake",
        "lookout_metrics": "LookoutMetrics",
        "event_bridge": "EventBridge",
        "zendesk": "Zendesk",
        "marketo": "Marketo",
        "redshift": "Redshift",
        "salesforce": "Salesforce",
    }

    s3: Optional[S3DestinationProperties] = None
    custom_connector: Optional[CustomConnectorDestinationProperties] = None
    upsolver: Optional[UpsolverDestinationProperties] = None
    sapo_data: Optional[SAPODataDestinationProperties] = None
    snowflake: Optional[SnowflakeDestinationProperties] = None
    lookout_metrics: Optional[LookoutMetricsDestinationProperties] = None
    event_bridge: Optional[EventBridgeDestinationProperties] = None
    zendesk: Optional[ZendeskDestinationProperties] = None
    marketo: Optional[MarketoDestinationProperties] = None
    redshift: Optional[RedshiftDestinationProperties] = None
    salesforce: Optional[SalesforceDestinationProperties] = None


@dataclass
class DestinationFlowConfig(PropertyType):
    CONNECTOR_PROFILE_NAME = "ConnectorProfileName"
    API_VERSION = "ApiVersion"
    CONNECTOR_TYPE = "ConnectorType"
    DESTINATION_CONNECTOR_PROPERTIES = "DestinationConnectorProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_profile_name": "ConnectorProfileName",
        "api_version": "ApiVersion",
        "connector_type": "ConnectorType",
        "destination_connector_properties": "DestinationConnectorProperties",
    }

    connector_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_connector_properties: Optional[DestinationConnectorProperties] = None


@dataclass
class DynatraceSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorHandlingConfig(PropertyType):
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"
    FAIL_ON_FIRST_ERROR = "FailOnFirstError"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
        "fail_on_first_error": "FailOnFirstError",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fail_on_first_error: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeDestinationProperties(PropertyType):
    OBJECT = "Object"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
        "error_handling_config": "ErrorHandlingConfig",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class GlueDataCatalog(PropertyType):
    DATABASE_NAME = "DatabaseName"
    ROLE_ARN = "RoleArn"
    TABLE_PREFIX = "TablePrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
        "role_arn": "RoleArn",
        "table_prefix": "TablePrefix",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GoogleAnalyticsSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IncrementalPullConfig(PropertyType):
    DATETIME_TYPE_FIELD_NAME = "DatetimeTypeFieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "datetime_type_field_name": "DatetimeTypeFieldName",
    }

    datetime_type_field_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InforNexusSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LookoutMetricsDestinationProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MarketoDestinationProperties(PropertyType):
    OBJECT = "Object"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
        "error_handling_config": "ErrorHandlingConfig",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class MarketoSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataCatalogConfig(PropertyType):
    GLUE_DATA_CATALOG = "GlueDataCatalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_data_catalog": "GlueDataCatalog",
    }

    glue_data_catalog: Optional[GlueDataCatalog] = None


@dataclass
class PardotSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PrefixConfig(PropertyType):
    PREFIX_TYPE = "PrefixType"
    PATH_PREFIX_HIERARCHY = "PathPrefixHierarchy"
    PREFIX_FORMAT = "PrefixFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix_type": "PrefixType",
        "path_prefix_hierarchy": "PathPrefixHierarchy",
        "prefix_format": "PrefixFormat",
    }

    prefix_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    path_prefix_hierarchy: Optional[Union[list[str], Ref]] = None
    prefix_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftDestinationProperties(PropertyType):
    OBJECT = "Object"
    BUCKET_PREFIX = "BucketPrefix"
    INTERMEDIATE_BUCKET_NAME = "IntermediateBucketName"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
        "bucket_prefix": "BucketPrefix",
        "intermediate_bucket_name": "IntermediateBucketName",
        "error_handling_config": "ErrorHandlingConfig",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    intermediate_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class S3DestinationProperties(PropertyType):
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"
    S3_OUTPUT_FORMAT_CONFIG = "S3OutputFormatConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
        "s3_output_format_config": "S3OutputFormatConfig",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_format_config: Optional[S3OutputFormatConfig] = None


@dataclass
class S3InputFormatConfig(PropertyType):
    S3_INPUT_FILE_TYPE = "S3InputFileType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_input_file_type": "S3InputFileType",
    }

    s3_input_file_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3OutputFormatConfig(PropertyType):
    PREFIX_CONFIG = "PrefixConfig"
    FILE_TYPE = "FileType"
    AGGREGATION_CONFIG = "AggregationConfig"
    PRESERVE_SOURCE_DATA_TYPING = "PreserveSourceDataTyping"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix_config": "PrefixConfig",
        "file_type": "FileType",
        "aggregation_config": "AggregationConfig",
        "preserve_source_data_typing": "PreserveSourceDataTyping",
    }

    prefix_config: Optional[PrefixConfig] = None
    file_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregation_config: Optional[AggregationConfig] = None
    preserve_source_data_typing: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3SourceProperties(PropertyType):
    S3_INPUT_FORMAT_CONFIG = "S3InputFormatConfig"
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_input_format_config": "S3InputFormatConfig",
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
    }

    s3_input_format_config: Optional[S3InputFormatConfig] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SAPODataDestinationProperties(PropertyType):
    ID_FIELD_NAMES = "IdFieldNames"
    OBJECT_PATH = "ObjectPath"
    WRITE_OPERATION_TYPE = "WriteOperationType"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"
    SUCCESS_RESPONSE_HANDLING_CONFIG = "SuccessResponseHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_field_names": "IdFieldNames",
        "object_path": "ObjectPath",
        "write_operation_type": "WriteOperationType",
        "error_handling_config": "ErrorHandlingConfig",
        "success_response_handling_config": "SuccessResponseHandlingConfig",
    }

    id_field_names: Optional[Union[list[str], Ref]] = None
    object_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    write_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None
    success_response_handling_config: Optional[SuccessResponseHandlingConfig] = None


@dataclass
class SAPODataPaginationConfig(PropertyType):
    MAX_PAGE_SIZE = "maxPageSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_page_size": "maxPageSize",
    }

    max_page_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SAPODataParallelismConfig(PropertyType):
    MAX_PARALLELISM = "maxParallelism"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_parallelism": "maxParallelism",
    }

    max_parallelism: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SAPODataSourceProperties(PropertyType):
    OBJECT_PATH = "ObjectPath"
    PAGINATION_CONFIG = "paginationConfig"
    PARALLELISM_CONFIG = "parallelismConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_path": "ObjectPath",
        "pagination_config": "paginationConfig",
        "parallelism_config": "parallelismConfig",
    }

    object_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pagination_config: Optional[SAPODataPaginationConfig] = None
    parallelism_config: Optional[SAPODataParallelismConfig] = None


@dataclass
class SalesforceDestinationProperties(PropertyType):
    ID_FIELD_NAMES = "IdFieldNames"
    WRITE_OPERATION_TYPE = "WriteOperationType"
    DATA_TRANSFER_API = "DataTransferApi"
    OBJECT = "Object"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_field_names": "IdFieldNames",
        "write_operation_type": "WriteOperationType",
        "data_transfer_api": "DataTransferApi",
        "object": "Object",
        "error_handling_config": "ErrorHandlingConfig",
    }

    id_field_names: Optional[Union[list[str], Ref]] = None
    write_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_transfer_api: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    INCLUDE_DELETED_RECORDS = "IncludeDeletedRecords"
    DATA_TRANSFER_API = "DataTransferApi"
    OBJECT = "Object"
    ENABLE_DYNAMIC_FIELD_UPDATE = "EnableDynamicFieldUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_deleted_records": "IncludeDeletedRecords",
        "data_transfer_api": "DataTransferApi",
        "object": "Object",
        "enable_dynamic_field_update": "EnableDynamicFieldUpdate",
    }

    include_deleted_records: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_transfer_api: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_dynamic_field_update: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    SCHEDULE_END_TIME = "ScheduleEndTime"
    SCHEDULE_EXPRESSION = "ScheduleExpression"
    FIRST_EXECUTION_FROM = "FirstExecutionFrom"
    TIME_ZONE = "TimeZone"
    SCHEDULE_START_TIME = "ScheduleStartTime"
    DATA_PULL_MODE = "DataPullMode"
    SCHEDULE_OFFSET = "ScheduleOffset"
    FLOW_ERROR_DEACTIVATION_THRESHOLD = "FlowErrorDeactivationThreshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_end_time": "ScheduleEndTime",
        "schedule_expression": "ScheduleExpression",
        "first_execution_from": "FirstExecutionFrom",
        "time_zone": "TimeZone",
        "schedule_start_time": "ScheduleStartTime",
        "data_pull_mode": "DataPullMode",
        "schedule_offset": "ScheduleOffset",
        "flow_error_deactivation_threshold": "FlowErrorDeactivationThreshold",
    }

    schedule_end_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_execution_from: Optional[Union[float, Ref, GetAtt, Sub]] = None
    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_start_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    data_pull_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_offset: Optional[Union[float, Ref, GetAtt, Sub]] = None
    flow_error_deactivation_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingularSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlackSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeDestinationProperties(PropertyType):
    OBJECT = "Object"
    BUCKET_PREFIX = "BucketPrefix"
    INTERMEDIATE_BUCKET_NAME = "IntermediateBucketName"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
        "bucket_prefix": "BucketPrefix",
        "intermediate_bucket_name": "IntermediateBucketName",
        "error_handling_config": "ErrorHandlingConfig",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    intermediate_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class SourceConnectorProperties(PropertyType):
    AMPLITUDE = "Amplitude"
    S3 = "S3"
    GOOGLE_ANALYTICS = "GoogleAnalytics"
    SERVICE_NOW = "ServiceNow"
    CUSTOM_CONNECTOR = "CustomConnector"
    SAPO_DATA = "SAPOData"
    PARDOT = "Pardot"
    VEEVA = "Veeva"
    TRENDMICRO = "Trendmicro"
    DATADOG = "Datadog"
    MARKETO = "Marketo"
    SINGULAR = "Singular"
    SLACK = "Slack"
    DYNATRACE = "Dynatrace"
    ZENDESK = "Zendesk"
    INFOR_NEXUS = "InforNexus"
    SALESFORCE = "Salesforce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amplitude": "Amplitude",
        "s3": "S3",
        "google_analytics": "GoogleAnalytics",
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "trendmicro": "Trendmicro",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "singular": "Singular",
        "slack": "Slack",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    amplitude: Optional[AmplitudeSourceProperties] = None
    s3: Optional[S3SourceProperties] = None
    google_analytics: Optional[GoogleAnalyticsSourceProperties] = None
    service_now: Optional[ServiceNowSourceProperties] = None
    custom_connector: Optional[CustomConnectorSourceProperties] = None
    sapo_data: Optional[SAPODataSourceProperties] = None
    pardot: Optional[PardotSourceProperties] = None
    veeva: Optional[VeevaSourceProperties] = None
    trendmicro: Optional[TrendmicroSourceProperties] = None
    datadog: Optional[DatadogSourceProperties] = None
    marketo: Optional[MarketoSourceProperties] = None
    singular: Optional[SingularSourceProperties] = None
    slack: Optional[SlackSourceProperties] = None
    dynatrace: Optional[DynatraceSourceProperties] = None
    zendesk: Optional[ZendeskSourceProperties] = None
    infor_nexus: Optional[InforNexusSourceProperties] = None
    salesforce: Optional[SalesforceSourceProperties] = None


@dataclass
class SourceFlowConfig(PropertyType):
    CONNECTOR_PROFILE_NAME = "ConnectorProfileName"
    API_VERSION = "ApiVersion"
    SOURCE_CONNECTOR_PROPERTIES = "SourceConnectorProperties"
    CONNECTOR_TYPE = "ConnectorType"
    INCREMENTAL_PULL_CONFIG = "IncrementalPullConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_profile_name": "ConnectorProfileName",
        "api_version": "ApiVersion",
        "source_connector_properties": "SourceConnectorProperties",
        "connector_type": "ConnectorType",
        "incremental_pull_config": "IncrementalPullConfig",
    }

    connector_profile_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_connector_properties: Optional[SourceConnectorProperties] = None
    connector_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    incremental_pull_config: Optional[IncrementalPullConfig] = None


@dataclass
class SuccessResponseHandlingConfig(PropertyType):
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
    task_properties: Optional[list[TaskPropertiesObject]] = None


@dataclass
class TaskPropertiesObject(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrendmicroSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TriggerConfig(PropertyType):
    TRIGGER_TYPE = "TriggerType"
    TRIGGER_PROPERTIES = "TriggerProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trigger_type": "TriggerType",
        "trigger_properties": "TriggerProperties",
    }

    trigger_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_properties: Optional[ScheduledTriggerProperties] = None


@dataclass
class UpsolverDestinationProperties(PropertyType):
    BUCKET_NAME = "BucketName"
    BUCKET_PREFIX = "BucketPrefix"
    S3_OUTPUT_FORMAT_CONFIG = "S3OutputFormatConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "bucket_prefix": "BucketPrefix",
        "s3_output_format_config": "S3OutputFormatConfig",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_output_format_config: Optional[UpsolverS3OutputFormatConfig] = None


@dataclass
class UpsolverS3OutputFormatConfig(PropertyType):
    PREFIX_CONFIG = "PrefixConfig"
    FILE_TYPE = "FileType"
    AGGREGATION_CONFIG = "AggregationConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix_config": "PrefixConfig",
        "file_type": "FileType",
        "aggregation_config": "AggregationConfig",
    }

    prefix_config: Optional[PrefixConfig] = None
    file_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aggregation_config: Optional[AggregationConfig] = None


@dataclass
class VeevaSourceProperties(PropertyType):
    INCLUDE_ALL_VERSIONS = "IncludeAllVersions"
    INCLUDE_RENDITIONS = "IncludeRenditions"
    DOCUMENT_TYPE = "DocumentType"
    OBJECT = "Object"
    INCLUDE_SOURCE_FILES = "IncludeSourceFiles"

    _property_mappings: ClassVar[dict[str, str]] = {
        "include_all_versions": "IncludeAllVersions",
        "include_renditions": "IncludeRenditions",
        "document_type": "DocumentType",
        "object": "Object",
        "include_source_files": "IncludeSourceFiles",
    }

    include_all_versions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_renditions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    document_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_source_files: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ZendeskDestinationProperties(PropertyType):
    ID_FIELD_NAMES = "IdFieldNames"
    WRITE_OPERATION_TYPE = "WriteOperationType"
    OBJECT = "Object"
    ERROR_HANDLING_CONFIG = "ErrorHandlingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_field_names": "IdFieldNames",
        "write_operation_type": "WriteOperationType",
        "object": "Object",
        "error_handling_config": "ErrorHandlingConfig",
    }

    id_field_names: Optional[Union[list[str], Ref]] = None
    write_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    error_handling_config: Optional[ErrorHandlingConfig] = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object": "Object",
    }

    object: Optional[Union[str, Ref, GetAtt, Sub]] = None

