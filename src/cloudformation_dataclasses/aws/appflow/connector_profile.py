"""PropertyTypes for AWS::AppFlow::ConnectorProfile."""

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
class AmplitudeConnectorProfileCredentials(PropertyType):
    SECRET_KEY = "SecretKey"
    API_KEY = "ApiKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_key": "SecretKey",
        "api_key": "ApiKey",
    }

    secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApiKeyCredentials(PropertyType):
    API_SECRET_KEY = "ApiSecretKey"
    API_KEY = "ApiKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_secret_key": "ApiSecretKey",
        "api_key": "ApiKey",
    }

    api_secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthCredentials(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorOAuthRequest(PropertyType):
    AUTH_CODE = "AuthCode"
    REDIRECT_URI = "RedirectUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code": "AuthCode",
        "redirect_uri": "RedirectUri",
    }

    auth_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorProfileConfig(PropertyType):
    CONNECTOR_PROFILE_CREDENTIALS = "ConnectorProfileCredentials"
    CONNECTOR_PROFILE_PROPERTIES = "ConnectorProfileProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_profile_credentials": "ConnectorProfileCredentials",
        "connector_profile_properties": "ConnectorProfileProperties",
    }

    connector_profile_credentials: Optional[ConnectorProfileCredentials] = None
    connector_profile_properties: Optional[ConnectorProfileProperties] = None


@dataclass
class ConnectorProfileCredentials(PropertyType):
    AMPLITUDE = "Amplitude"
    GOOGLE_ANALYTICS = "GoogleAnalytics"
    SERVICE_NOW = "ServiceNow"
    CUSTOM_CONNECTOR = "CustomConnector"
    SAPO_DATA = "SAPOData"
    PARDOT = "Pardot"
    VEEVA = "Veeva"
    TRENDMICRO = "Trendmicro"
    DATADOG = "Datadog"
    MARKETO = "Marketo"
    REDSHIFT = "Redshift"
    SINGULAR = "Singular"
    SLACK = "Slack"
    SNOWFLAKE = "Snowflake"
    DYNATRACE = "Dynatrace"
    ZENDESK = "Zendesk"
    INFOR_NEXUS = "InforNexus"
    SALESFORCE = "Salesforce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amplitude": "Amplitude",
        "google_analytics": "GoogleAnalytics",
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "trendmicro": "Trendmicro",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "redshift": "Redshift",
        "singular": "Singular",
        "slack": "Slack",
        "snowflake": "Snowflake",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    amplitude: Optional[AmplitudeConnectorProfileCredentials] = None
    google_analytics: Optional[GoogleAnalyticsConnectorProfileCredentials] = None
    service_now: Optional[ServiceNowConnectorProfileCredentials] = None
    custom_connector: Optional[CustomConnectorProfileCredentials] = None
    sapo_data: Optional[SAPODataConnectorProfileCredentials] = None
    pardot: Optional[PardotConnectorProfileCredentials] = None
    veeva: Optional[VeevaConnectorProfileCredentials] = None
    trendmicro: Optional[TrendmicroConnectorProfileCredentials] = None
    datadog: Optional[DatadogConnectorProfileCredentials] = None
    marketo: Optional[MarketoConnectorProfileCredentials] = None
    redshift: Optional[RedshiftConnectorProfileCredentials] = None
    singular: Optional[SingularConnectorProfileCredentials] = None
    slack: Optional[SlackConnectorProfileCredentials] = None
    snowflake: Optional[SnowflakeConnectorProfileCredentials] = None
    dynatrace: Optional[DynatraceConnectorProfileCredentials] = None
    zendesk: Optional[ZendeskConnectorProfileCredentials] = None
    infor_nexus: Optional[InforNexusConnectorProfileCredentials] = None
    salesforce: Optional[SalesforceConnectorProfileCredentials] = None


@dataclass
class ConnectorProfileProperties(PropertyType):
    SERVICE_NOW = "ServiceNow"
    CUSTOM_CONNECTOR = "CustomConnector"
    SAPO_DATA = "SAPOData"
    PARDOT = "Pardot"
    VEEVA = "Veeva"
    DATADOG = "Datadog"
    MARKETO = "Marketo"
    REDSHIFT = "Redshift"
    SLACK = "Slack"
    SNOWFLAKE = "Snowflake"
    DYNATRACE = "Dynatrace"
    ZENDESK = "Zendesk"
    INFOR_NEXUS = "InforNexus"
    SALESFORCE = "Salesforce"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_now": "ServiceNow",
        "custom_connector": "CustomConnector",
        "sapo_data": "SAPOData",
        "pardot": "Pardot",
        "veeva": "Veeva",
        "datadog": "Datadog",
        "marketo": "Marketo",
        "redshift": "Redshift",
        "slack": "Slack",
        "snowflake": "Snowflake",
        "dynatrace": "Dynatrace",
        "zendesk": "Zendesk",
        "infor_nexus": "InforNexus",
        "salesforce": "Salesforce",
    }

    service_now: Optional[ServiceNowConnectorProfileProperties] = None
    custom_connector: Optional[CustomConnectorProfileProperties] = None
    sapo_data: Optional[SAPODataConnectorProfileProperties] = None
    pardot: Optional[PardotConnectorProfileProperties] = None
    veeva: Optional[VeevaConnectorProfileProperties] = None
    datadog: Optional[DatadogConnectorProfileProperties] = None
    marketo: Optional[MarketoConnectorProfileProperties] = None
    redshift: Optional[RedshiftConnectorProfileProperties] = None
    slack: Optional[SlackConnectorProfileProperties] = None
    snowflake: Optional[SnowflakeConnectorProfileProperties] = None
    dynatrace: Optional[DynatraceConnectorProfileProperties] = None
    zendesk: Optional[ZendeskConnectorProfileProperties] = None
    infor_nexus: Optional[InforNexusConnectorProfileProperties] = None
    salesforce: Optional[SalesforceConnectorProfileProperties] = None


@dataclass
class CustomAuthCredentials(PropertyType):
    CREDENTIALS_MAP = "CredentialsMap"
    CUSTOM_AUTHENTICATION_TYPE = "CustomAuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credentials_map": "CredentialsMap",
        "custom_authentication_type": "CustomAuthenticationType",
    }

    credentials_map: Optional[dict[str, str]] = None
    custom_authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomConnectorProfileCredentials(PropertyType):
    BASIC = "Basic"
    API_KEY = "ApiKey"
    OAUTH2 = "Oauth2"
    CUSTOM = "Custom"
    AUTHENTICATION_TYPE = "AuthenticationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "basic": "Basic",
        "api_key": "ApiKey",
        "oauth2": "Oauth2",
        "custom": "Custom",
        "authentication_type": "AuthenticationType",
    }

    basic: Optional[BasicAuthCredentials] = None
    api_key: Optional[ApiKeyCredentials] = None
    oauth2: Optional[OAuth2Credentials] = None
    custom: Optional[CustomAuthCredentials] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomConnectorProfileProperties(PropertyType):
    O_AUTH2_PROPERTIES = "OAuth2Properties"
    PROFILE_PROPERTIES = "ProfileProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "o_auth2_properties": "OAuth2Properties",
        "profile_properties": "ProfileProperties",
    }

    o_auth2_properties: Optional[OAuth2Properties] = None
    profile_properties: Optional[dict[str, str]] = None


@dataclass
class DatadogConnectorProfileCredentials(PropertyType):
    APPLICATION_KEY = "ApplicationKey"
    API_KEY = "ApiKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_key": "ApplicationKey",
        "api_key": "ApiKey",
    }

    application_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatadogConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynatraceConnectorProfileCredentials(PropertyType):
    API_TOKEN = "ApiToken"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_token": "ApiToken",
    }

    api_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynatraceConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GoogleAnalyticsConnectorProfileCredentials(PropertyType):
    REFRESH_TOKEN = "RefreshToken"
    CLIENT_SECRET = "ClientSecret"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_ID = "ClientId"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class InforNexusConnectorProfileCredentials(PropertyType):
    ACCESS_KEY_ID = "AccessKeyId"
    USER_ID = "UserId"
    SECRET_ACCESS_KEY = "SecretAccessKey"
    DATAKEY = "Datakey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_key_id": "AccessKeyId",
        "user_id": "UserId",
        "secret_access_key": "SecretAccessKey",
        "datakey": "Datakey",
    }

    access_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_access_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    datakey: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InforNexusConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MarketoConnectorProfileCredentials(PropertyType):
    CLIENT_SECRET = "ClientSecret"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_ID = "ClientId"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class MarketoConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Credentials(PropertyType):
    O_AUTH_REQUEST = "OAuthRequest"
    REFRESH_TOKEN = "RefreshToken"
    CLIENT_SECRET = "ClientSecret"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_ID = "ClientId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "o_auth_request": "OAuthRequest",
        "refresh_token": "RefreshToken",
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
    }

    o_auth_request: Optional[ConnectorOAuthRequest] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2Properties(PropertyType):
    TOKEN_URL_CUSTOM_PROPERTIES = "TokenUrlCustomProperties"
    TOKEN_URL = "TokenUrl"
    O_AUTH2_GRANT_TYPE = "OAuth2GrantType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "token_url_custom_properties": "TokenUrlCustomProperties",
        "token_url": "TokenUrl",
        "o_auth2_grant_type": "OAuth2GrantType",
    }

    token_url_custom_properties: Optional[dict[str, str]] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuthCredentials(PropertyType):
    REFRESH_TOKEN = "RefreshToken"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_SECRET = "ClientSecret"
    CLIENT_ID = "ClientId"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_secret": "ClientSecret",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class OAuthProperties(PropertyType):
    AUTH_CODE_URL = "AuthCodeUrl"
    TOKEN_URL = "TokenUrl"
    O_AUTH_SCOPES = "OAuthScopes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code_url": "AuthCodeUrl",
        "token_url": "TokenUrl",
        "o_auth_scopes": "OAuthScopes",
    }

    auth_code_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_scopes: Optional[Union[list[str], Ref]] = None


@dataclass
class PardotConnectorProfileCredentials(PropertyType):
    REFRESH_TOKEN = "RefreshToken"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_CREDENTIALS_ARN = "ClientCredentialsArn"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_credentials_arn": "ClientCredentialsArn",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_credentials_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class PardotConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"
    IS_SANDBOX_ENVIRONMENT = "IsSandboxEnvironment"
    BUSINESS_UNIT_ID = "BusinessUnitId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
        "is_sandbox_environment": "IsSandboxEnvironment",
        "business_unit_id": "BusinessUnitId",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_sandbox_environment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    business_unit_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConnectorProfileCredentials(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedshiftConnectorProfileProperties(PropertyType):
    DATABASE_URL = "DatabaseUrl"
    BUCKET_NAME = "BucketName"
    IS_REDSHIFT_SERVERLESS = "IsRedshiftServerless"
    DATA_API_ROLE_ARN = "DataApiRoleArn"
    DATABASE_NAME = "DatabaseName"
    WORKGROUP_NAME = "WorkgroupName"
    BUCKET_PREFIX = "BucketPrefix"
    CLUSTER_IDENTIFIER = "ClusterIdentifier"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_url": "DatabaseUrl",
        "bucket_name": "BucketName",
        "is_redshift_serverless": "IsRedshiftServerless",
        "data_api_role_arn": "DataApiRoleArn",
        "database_name": "DatabaseName",
        "workgroup_name": "WorkgroupName",
        "bucket_prefix": "BucketPrefix",
        "cluster_identifier": "ClusterIdentifier",
        "role_arn": "RoleArn",
    }

    database_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_redshift_serverless: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_api_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SAPODataConnectorProfileCredentials(PropertyType):
    BASIC_AUTH_CREDENTIALS = "BasicAuthCredentials"
    O_AUTH_CREDENTIALS = "OAuthCredentials"

    _property_mappings: ClassVar[dict[str, str]] = {
        "basic_auth_credentials": "BasicAuthCredentials",
        "o_auth_credentials": "OAuthCredentials",
    }

    basic_auth_credentials: Optional[BasicAuthCredentials] = None
    o_auth_credentials: Optional[OAuthCredentials] = None


@dataclass
class SAPODataConnectorProfileProperties(PropertyType):
    APPLICATION_SERVICE_PATH = "ApplicationServicePath"
    APPLICATION_HOST_URL = "ApplicationHostUrl"
    O_AUTH_PROPERTIES = "OAuthProperties"
    DISABLE_SSO = "DisableSSO"
    LOGON_LANGUAGE = "LogonLanguage"
    PRIVATE_LINK_SERVICE_NAME = "PrivateLinkServiceName"
    PORT_NUMBER = "PortNumber"
    CLIENT_NUMBER = "ClientNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_service_path": "ApplicationServicePath",
        "application_host_url": "ApplicationHostUrl",
        "o_auth_properties": "OAuthProperties",
        "disable_sso": "DisableSSO",
        "logon_language": "LogonLanguage",
        "private_link_service_name": "PrivateLinkServiceName",
        "port_number": "PortNumber",
        "client_number": "ClientNumber",
    }

    application_service_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_host_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth_properties: Optional[OAuthProperties] = None
    disable_sso: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    logon_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_link_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    client_number: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceConnectorProfileCredentials(PropertyType):
    JWT_TOKEN = "JwtToken"
    REFRESH_TOKEN = "RefreshToken"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_CREDENTIALS_ARN = "ClientCredentialsArn"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"
    O_AUTH2_GRANT_TYPE = "OAuth2GrantType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jwt_token": "JwtToken",
        "refresh_token": "RefreshToken",
        "access_token": "AccessToken",
        "client_credentials_arn": "ClientCredentialsArn",
        "connector_o_auth_request": "ConnectorOAuthRequest",
        "o_auth2_grant_type": "OAuth2GrantType",
    }

    jwt_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_credentials_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None
    o_auth2_grant_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SalesforceConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"
    IS_SANDBOX_ENVIRONMENT = "isSandboxEnvironment"
    USE_PRIVATE_LINK_FOR_METADATA_AND_AUTHORIZATION = "usePrivateLinkForMetadataAndAuthorization"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
        "is_sandbox_environment": "isSandboxEnvironment",
        "use_private_link_for_metadata_and_authorization": "usePrivateLinkForMetadataAndAuthorization",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_sandbox_environment: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    use_private_link_for_metadata_and_authorization: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowConnectorProfileCredentials(PropertyType):
    USERNAME = "Username"
    O_AUTH2_CREDENTIALS = "OAuth2Credentials"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "o_auth2_credentials": "OAuth2Credentials",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    o_auth2_credentials: Optional[OAuth2Credentials] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNowConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingularConnectorProfileCredentials(PropertyType):
    API_KEY = "ApiKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_key": "ApiKey",
    }

    api_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlackConnectorProfileCredentials(PropertyType):
    CLIENT_SECRET = "ClientSecret"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_ID = "ClientId"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class SlackConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeConnectorProfileCredentials(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnowflakeConnectorProfileProperties(PropertyType):
    WAREHOUSE = "Warehouse"
    BUCKET_NAME = "BucketName"
    PRIVATE_LINK_SERVICE_NAME = "PrivateLinkServiceName"
    STAGE = "Stage"
    REGION = "Region"
    BUCKET_PREFIX = "BucketPrefix"
    ACCOUNT_NAME = "AccountName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "warehouse": "Warehouse",
        "bucket_name": "BucketName",
        "private_link_service_name": "PrivateLinkServiceName",
        "stage": "Stage",
        "region": "Region",
        "bucket_prefix": "BucketPrefix",
        "account_name": "AccountName",
    }

    warehouse: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_link_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrendmicroConnectorProfileCredentials(PropertyType):
    API_SECRET_KEY = "ApiSecretKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "api_secret_key": "ApiSecretKey",
    }

    api_secret_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VeevaConnectorProfileCredentials(PropertyType):
    USERNAME = "Username"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VeevaConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZendeskConnectorProfileCredentials(PropertyType):
    CLIENT_SECRET = "ClientSecret"
    ACCESS_TOKEN = "AccessToken"
    CLIENT_ID = "ClientId"
    CONNECTOR_O_AUTH_REQUEST = "ConnectorOAuthRequest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_secret": "ClientSecret",
        "access_token": "AccessToken",
        "client_id": "ClientId",
        "connector_o_auth_request": "ConnectorOAuthRequest",
    }

    client_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connector_o_auth_request: Optional[ConnectorOAuthRequest] = None


@dataclass
class ZendeskConnectorProfileProperties(PropertyType):
    INSTANCE_URL = "InstanceUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_url": "InstanceUrl",
    }

    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

