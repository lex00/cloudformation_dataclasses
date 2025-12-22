"""PropertyTypes for AWS::Logs::Transformer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionStatus:
    """ActionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CLIENT_ERROR = "CLIENT_ERROR"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


class AnomalyDetectorStatus:
    """AnomalyDetectorStatus enum values."""

    INITIALIZING = "INITIALIZING"
    TRAINING = "TRAINING"
    ANALYZING = "ANALYZING"
    FAILED = "FAILED"
    DELETED = "DELETED"
    PAUSED = "PAUSED"


class DataProtectionStatus:
    """DataProtectionStatus enum values."""

    ACTIVATED = "ACTIVATED"
    DELETED = "DELETED"
    ARCHIVED = "ARCHIVED"
    DISABLED = "DISABLED"


class DeliveryDestinationType:
    """DeliveryDestinationType enum values."""

    S3 = "S3"
    CWL = "CWL"
    FH = "FH"
    XRAY = "XRAY"


class Distribution:
    """Distribution enum values."""

    RANDOM = "Random"
    BYLOGSTREAM = "ByLogStream"


class EntityRejectionErrorType:
    """EntityRejectionErrorType enum values."""

    INVALIDENTITY = "InvalidEntity"
    INVALIDTYPEVALUE = "InvalidTypeValue"
    INVALIDKEYATTRIBUTES = "InvalidKeyAttributes"
    INVALIDATTRIBUTES = "InvalidAttributes"
    ENTITYSIZETOOLARGE = "EntitySizeTooLarge"
    UNSUPPORTEDLOGGROUPTYPE = "UnsupportedLogGroupType"
    MISSINGREQUIREDFIELDS = "MissingRequiredFields"


class EvaluationFrequency:
    """EvaluationFrequency enum values."""

    ONE_MIN = "ONE_MIN"
    FIVE_MIN = "FIVE_MIN"
    TEN_MIN = "TEN_MIN"
    FIFTEEN_MIN = "FIFTEEN_MIN"
    THIRTY_MIN = "THIRTY_MIN"
    ONE_HOUR = "ONE_HOUR"


class EventSource:
    """EventSource enum values."""

    CLOUDTRAIL = "CloudTrail"
    ROUTE53RESOLVER = "Route53Resolver"
    VPCFLOW = "VPCFlow"
    EKSAUDIT = "EKSAudit"
    AWSWAF = "AWSWAF"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    RUNNING = "Running"
    INVALIDQUERY = "InvalidQuery"
    COMPLETE = "Complete"
    FAILED = "Failed"
    TIMEOUT = "Timeout"


class ExportTaskStatusCode:
    """ExportTaskStatusCode enum values."""

    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PENDING_CANCEL = "PENDING_CANCEL"
    RUNNING = "RUNNING"


class FlattenedElement:
    """FlattenedElement enum values."""

    FIRST = "first"
    LAST = "last"


class ImportStatus:
    """ImportStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class IndexSource:
    """IndexSource enum values."""

    ACCOUNT = "ACCOUNT"
    LOG_GROUP = "LOG_GROUP"


class IndexType:
    """IndexType enum values."""

    FACET = "FACET"
    FIELD_INDEX = "FIELD_INDEX"


class InheritedProperty:
    """InheritedProperty enum values."""

    ACCOUNT_DATA_PROTECTION = "ACCOUNT_DATA_PROTECTION"


class IntegrationStatus:
    """IntegrationStatus enum values."""

    PROVISIONING = "PROVISIONING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class IntegrationType:
    """IntegrationType enum values."""

    OPENSEARCH = "OPENSEARCH"


class ListAggregateLogGroupSummariesGroupBy:
    """ListAggregateLogGroupSummariesGroupBy enum values."""

    DATA_SOURCE_NAME_TYPE_AND_FORMAT = "DATA_SOURCE_NAME_TYPE_AND_FORMAT"
    DATA_SOURCE_NAME_AND_TYPE = "DATA_SOURCE_NAME_AND_TYPE"


class LogGroupClass:
    """LogGroupClass enum values."""

    STANDARD = "STANDARD"
    INFREQUENT_ACCESS = "INFREQUENT_ACCESS"
    DELIVERY = "DELIVERY"


class OCSFVersion:
    """OCSFVersion enum values."""

    V1_1 = "V1.1"
    V1_5 = "V1.5"


class OpenSearchResourceStatusType:
    """OpenSearchResourceStatusType enum values."""

    ACTIVE = "ACTIVE"
    NOT_FOUND = "NOT_FOUND"
    ERROR = "ERROR"


class OrderBy:
    """OrderBy enum values."""

    LOGSTREAMNAME = "LogStreamName"
    LASTEVENTTIME = "LastEventTime"


class OutputFormat:
    """OutputFormat enum values."""

    JSON = "json"
    PLAIN = "plain"
    W3C = "w3c"
    RAW = "raw"
    PARQUET = "parquet"


class PolicyScope:
    """PolicyScope enum values."""

    ACCOUNT = "ACCOUNT"
    RESOURCE = "RESOURCE"


class PolicyType:
    """PolicyType enum values."""

    DATA_PROTECTION_POLICY = "DATA_PROTECTION_POLICY"
    SUBSCRIPTION_FILTER_POLICY = "SUBSCRIPTION_FILTER_POLICY"
    FIELD_INDEX_POLICY = "FIELD_INDEX_POLICY"
    TRANSFORMER_POLICY = "TRANSFORMER_POLICY"
    METRIC_EXTRACTION_POLICY = "METRIC_EXTRACTION_POLICY"


class QueryLanguage:
    """QueryLanguage enum values."""

    CWLI = "CWLI"
    SQL = "SQL"
    PPL = "PPL"


class QueryStatus:
    """QueryStatus enum values."""

    SCHEDULED = "Scheduled"
    RUNNING = "Running"
    COMPLETE = "Complete"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    TIMEOUT = "Timeout"
    UNKNOWN = "Unknown"


class S3TableIntegrationSourceStatus:
    """S3TableIntegrationSourceStatus enum values."""

    ACTIVE = "ACTIVE"
    UNHEALTHY = "UNHEALTHY"
    FAILED = "FAILED"
    DATA_SOURCE_DELETE_IN_PROGRESS = "DATA_SOURCE_DELETE_IN_PROGRESS"


class ScheduledQueryDestinationType:
    """ScheduledQueryDestinationType enum values."""

    S3 = "S3"


class ScheduledQueryState:
    """ScheduledQueryState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Scope:
    """Scope enum values."""

    ALL = "ALL"


class StandardUnit:
    """StandardUnit enum values."""

    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


class State:
    """State enum values."""

    ACTIVE = "Active"
    SUPPRESSED = "Suppressed"
    BASELINE = "Baseline"


class SuppressionState:
    """SuppressionState enum values."""

    SUPPRESSED = "SUPPRESSED"
    UNSUPPRESSED = "UNSUPPRESSED"


class SuppressionType:
    """SuppressionType enum values."""

    LIMITED = "LIMITED"
    INFINITE = "INFINITE"


class SuppressionUnit:
    """SuppressionUnit enum values."""

    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"


class Type:
    """Type enum values."""

    BOOLEAN = "boolean"
    INTEGER = "integer"
    DOUBLE = "double"
    STRING = "string"


@dataclass
class AddKeyEntry(PropertyType):
    OVERWRITE_IF_EXISTS = "OverwriteIfExists"
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overwrite_if_exists": "OverwriteIfExists",
        "value": "Value",
        "key": "Key",
    }

    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AddKeys(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[AddKeyEntry]] = None


@dataclass
class CopyValue(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[CopyValueEntry]] = None


@dataclass
class CopyValueEntry(PropertyType):
    TARGET = "Target"
    OVERWRITE_IF_EXISTS = "OverwriteIfExists"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "overwrite_if_exists": "OverwriteIfExists",
        "source": "Source",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Csv(PropertyType):
    QUOTE_CHARACTER = "QuoteCharacter"
    DELIMITER = "Delimiter"
    COLUMNS = "Columns"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "quote_character": "QuoteCharacter",
        "delimiter": "Delimiter",
        "columns": "Columns",
        "source": "Source",
    }

    quote_character: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    columns: Optional[Union[list[str], Ref]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateTimeConverter(PropertyType):
    LOCALE = "Locale"
    TARGET = "Target"
    MATCH_PATTERNS = "MatchPatterns"
    SOURCE_TIMEZONE = "SourceTimezone"
    TARGET_FORMAT = "TargetFormat"
    TARGET_TIMEZONE = "TargetTimezone"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "locale": "Locale",
        "target": "Target",
        "match_patterns": "MatchPatterns",
        "source_timezone": "SourceTimezone",
        "target_format": "TargetFormat",
        "target_timezone": "TargetTimezone",
        "source": "Source",
    }

    locale: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match_patterns: Optional[Union[list[str], Ref]] = None
    source_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_timezone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteKeys(PropertyType):
    WITH_KEYS = "WithKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class Grok(PropertyType):
    SOURCE = "Source"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
        "match": "Match",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListToMap(PropertyType):
    VALUE_KEY = "ValueKey"
    TARGET = "Target"
    FLATTEN = "Flatten"
    FLATTENED_ELEMENT = "FlattenedElement"
    SOURCE = "Source"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value_key": "ValueKey",
        "target": "Target",
        "flatten": "Flatten",
        "flattened_element": "FlattenedElement",
        "source": "Source",
        "key": "Key",
    }

    value_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    flatten: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    flattened_element: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LowerCaseString(PropertyType):
    WITH_KEYS = "WithKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class MoveKeyEntry(PropertyType):
    TARGET = "Target"
    OVERWRITE_IF_EXISTS = "OverwriteIfExists"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "overwrite_if_exists": "OverwriteIfExists",
        "source": "Source",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MoveKeys(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[MoveKeyEntry]] = None


@dataclass
class ParseCloudfront(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseJSON(PropertyType):
    DESTINATION = "Destination"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseKeyValue(PropertyType):
    DESTINATION = "Destination"
    KEY_VALUE_DELIMITER = "KeyValueDelimiter"
    OVERWRITE_IF_EXISTS = "OverwriteIfExists"
    FIELD_DELIMITER = "FieldDelimiter"
    NON_MATCH_VALUE = "NonMatchValue"
    SOURCE = "Source"
    KEY_PREFIX = "KeyPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "key_value_delimiter": "KeyValueDelimiter",
        "overwrite_if_exists": "OverwriteIfExists",
        "field_delimiter": "FieldDelimiter",
        "non_match_value": "NonMatchValue",
        "source": "Source",
        "key_prefix": "KeyPrefix",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_value_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    field_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    non_match_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParsePostgres(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseRoute53(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseToOCSF(PropertyType):
    EVENT_SOURCE = "EventSource"
    OCSF_VERSION = "OcsfVersion"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_source": "EventSource",
        "ocsf_version": "OcsfVersion",
        "source": "Source",
    }

    event_source: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ocsf_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseVPC(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParseWAF(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Processor(PropertyType):
    PARSE_CLOUDFRONT = "ParseCloudfront"
    LOWER_CASE_STRING = "LowerCaseString"
    UPPER_CASE_STRING = "UpperCaseString"
    DELETE_KEYS = "DeleteKeys"
    RENAME_KEYS = "RenameKeys"
    GROK = "Grok"
    SPLIT_STRING = "SplitString"
    CSV = "Csv"
    ADD_KEYS = "AddKeys"
    PARSE_TO_OCSF = "ParseToOCSF"
    SUBSTITUTE_STRING = "SubstituteString"
    PARSE_KEY_VALUE = "ParseKeyValue"
    PARSE_WAF = "ParseWAF"
    PARSE_VPC = "ParseVPC"
    PARSE_ROUTE53 = "ParseRoute53"
    TYPE_CONVERTER = "TypeConverter"
    PARSE_JSON = "ParseJSON"
    PARSE_POSTGRES = "ParsePostgres"
    COPY_VALUE = "CopyValue"
    MOVE_KEYS = "MoveKeys"
    DATE_TIME_CONVERTER = "DateTimeConverter"
    TRIM_STRING = "TrimString"
    LIST_TO_MAP = "ListToMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parse_cloudfront": "ParseCloudfront",
        "lower_case_string": "LowerCaseString",
        "upper_case_string": "UpperCaseString",
        "delete_keys": "DeleteKeys",
        "rename_keys": "RenameKeys",
        "grok": "Grok",
        "split_string": "SplitString",
        "csv": "Csv",
        "add_keys": "AddKeys",
        "parse_to_ocsf": "ParseToOCSF",
        "substitute_string": "SubstituteString",
        "parse_key_value": "ParseKeyValue",
        "parse_waf": "ParseWAF",
        "parse_vpc": "ParseVPC",
        "parse_route53": "ParseRoute53",
        "type_converter": "TypeConverter",
        "parse_json": "ParseJSON",
        "parse_postgres": "ParsePostgres",
        "copy_value": "CopyValue",
        "move_keys": "MoveKeys",
        "date_time_converter": "DateTimeConverter",
        "trim_string": "TrimString",
        "list_to_map": "ListToMap",
    }

    parse_cloudfront: Optional[ParseCloudfront] = None
    lower_case_string: Optional[LowerCaseString] = None
    upper_case_string: Optional[UpperCaseString] = None
    delete_keys: Optional[DeleteKeys] = None
    rename_keys: Optional[RenameKeys] = None
    grok: Optional[Grok] = None
    split_string: Optional[SplitString] = None
    csv: Optional[Csv] = None
    add_keys: Optional[AddKeys] = None
    parse_to_ocsf: Optional[ParseToOCSF] = None
    substitute_string: Optional[SubstituteString] = None
    parse_key_value: Optional[ParseKeyValue] = None
    parse_waf: Optional[ParseWAF] = None
    parse_vpc: Optional[ParseVPC] = None
    parse_route53: Optional[ParseRoute53] = None
    type_converter: Optional[TypeConverter] = None
    parse_json: Optional[ParseJSON] = None
    parse_postgres: Optional[ParsePostgres] = None
    copy_value: Optional[CopyValue] = None
    move_keys: Optional[MoveKeys] = None
    date_time_converter: Optional[DateTimeConverter] = None
    trim_string: Optional[TrimString] = None
    list_to_map: Optional[ListToMap] = None


@dataclass
class RenameKeyEntry(PropertyType):
    OVERWRITE_IF_EXISTS = "OverwriteIfExists"
    RENAME_TO = "RenameTo"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "overwrite_if_exists": "OverwriteIfExists",
        "rename_to": "RenameTo",
        "key": "Key",
    }

    overwrite_if_exists: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rename_to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RenameKeys(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[RenameKeyEntry]] = None


@dataclass
class SplitString(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[SplitStringEntry]] = None


@dataclass
class SplitStringEntry(PropertyType):
    DELIMITER = "Delimiter"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "source": "Source",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SubstituteString(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[SubstituteStringEntry]] = None


@dataclass
class SubstituteStringEntry(PropertyType):
    FROM = "From"
    TO = "To"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "source": "Source",
    }

    from_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    to: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TrimString(PropertyType):
    WITH_KEYS = "WithKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class TypeConverter(PropertyType):
    ENTRIES = "Entries"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entries": "Entries",
    }

    entries: Optional[list[TypeConverterEntry]] = None


@dataclass
class TypeConverterEntry(PropertyType):
    TYPE = "Type"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "key": "Key",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpperCaseString(PropertyType):
    WITH_KEYS = "WithKeys"

    _property_mappings: ClassVar[dict[str, str]] = {
        "with_keys": "WithKeys",
    }

    with_keys: Optional[Union[list[str], Ref]] = None

