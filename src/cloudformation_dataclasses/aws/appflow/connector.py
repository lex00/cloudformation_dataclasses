"""PropertyTypes for AWS::AppFlow::Connector."""

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
class ConnectorProvisioningConfig(PropertyType):
    LAMBDA = "Lambda"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_": "Lambda",
    }

    lambda_: Optional[LambdaConnectorProvisioningConfig] = None


@dataclass
class LambdaConnectorProvisioningConfig(PropertyType):
    LAMBDA_ARN = "LambdaArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

