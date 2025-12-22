"""PropertyTypes for AWS::WAFv2::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionValue:
    """ActionValue enum values."""

    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    COUNT = "COUNT"
    CAPTCHA = "CAPTCHA"
    CHALLENGE = "CHALLENGE"
    EXCLUDED_AS_COUNT = "EXCLUDED_AS_COUNT"


class AssociatedResourceType:
    """AssociatedResourceType enum values."""

    CLOUDFRONT = "CLOUDFRONT"
    API_GATEWAY = "API_GATEWAY"
    COGNITO_USER_POOL = "COGNITO_USER_POOL"
    APP_RUNNER_SERVICE = "APP_RUNNER_SERVICE"
    VERIFIED_ACCESS_INSTANCE = "VERIFIED_ACCESS_INSTANCE"


class BodyParsingFallbackBehavior:
    """BodyParsingFallbackBehavior enum values."""

    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"
    EVALUATE_AS_STRING = "EVALUATE_AS_STRING"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


class CountryCode:
    """CountryCode enum values."""

    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    SS = "SS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"
    XK = "XK"


class DataProtectionAction:
    """DataProtectionAction enum values."""

    SUBSTITUTION = "SUBSTITUTION"
    HASH = "HASH"


class FailureReason:
    """FailureReason enum values."""

    TOKEN_MISSING = "TOKEN_MISSING"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    TOKEN_INVALID = "TOKEN_INVALID"
    TOKEN_DOMAIN_MISMATCH = "TOKEN_DOMAIN_MISMATCH"


class FallbackBehavior:
    """FallbackBehavior enum values."""

    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class FieldToProtectType:
    """FieldToProtectType enum values."""

    SINGLE_HEADER = "SINGLE_HEADER"
    SINGLE_COOKIE = "SINGLE_COOKIE"
    SINGLE_QUERY_ARGUMENT = "SINGLE_QUERY_ARGUMENT"
    QUERY_STRING = "QUERY_STRING"
    BODY = "BODY"


class FilterBehavior:
    """FilterBehavior enum values."""

    KEEP = "KEEP"
    DROP = "DROP"


class FilterRequirement:
    """FilterRequirement enum values."""

    MEETS_ALL = "MEETS_ALL"
    MEETS_ANY = "MEETS_ANY"


class ForwardedIPPosition:
    """ForwardedIPPosition enum values."""

    FIRST = "FIRST"
    LAST = "LAST"
    ANY = "ANY"


class IPAddressVersion:
    """IPAddressVersion enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"


class InspectionLevel:
    """InspectionLevel enum values."""

    COMMON = "COMMON"
    TARGETED = "TARGETED"


class JsonMatchScope:
    """JsonMatchScope enum values."""

    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class LabelMatchScope:
    """LabelMatchScope enum values."""

    LABEL = "LABEL"
    NAMESPACE = "NAMESPACE"


class LogScope:
    """LogScope enum values."""

    CUSTOMER = "CUSTOMER"
    SECURITY_LAKE = "SECURITY_LAKE"
    CLOUDWATCH_TELEMETRY_RULE_MANAGED = "CLOUDWATCH_TELEMETRY_RULE_MANAGED"


class LogType:
    """LogType enum values."""

    WAF_LOGS = "WAF_LOGS"


class LowReputationMode:
    """LowReputationMode enum values."""

    ACTIVE_UNDER_DDOS = "ACTIVE_UNDER_DDOS"
    ALWAYS_ON = "ALWAYS_ON"


class MapMatchScope:
    """MapMatchScope enum values."""

    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class OversizeHandling:
    """OversizeHandling enum values."""

    CONTINUE = "CONTINUE"
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class ParameterExceptionField:
    """ParameterExceptionField enum values."""

    WEB_ACL = "WEB_ACL"
    RULE_GROUP = "RULE_GROUP"
    REGEX_PATTERN_SET = "REGEX_PATTERN_SET"
    IP_SET = "IP_SET"
    MANAGED_RULE_SET = "MANAGED_RULE_SET"
    RULE = "RULE"
    EXCLUDED_RULE = "EXCLUDED_RULE"
    STATEMENT = "STATEMENT"
    BYTE_MATCH_STATEMENT = "BYTE_MATCH_STATEMENT"
    SQLI_MATCH_STATEMENT = "SQLI_MATCH_STATEMENT"
    XSS_MATCH_STATEMENT = "XSS_MATCH_STATEMENT"
    SIZE_CONSTRAINT_STATEMENT = "SIZE_CONSTRAINT_STATEMENT"
    GEO_MATCH_STATEMENT = "GEO_MATCH_STATEMENT"
    RATE_BASED_STATEMENT = "RATE_BASED_STATEMENT"
    RULE_GROUP_REFERENCE_STATEMENT = "RULE_GROUP_REFERENCE_STATEMENT"
    REGEX_PATTERN_REFERENCE_STATEMENT = "REGEX_PATTERN_REFERENCE_STATEMENT"
    IP_SET_REFERENCE_STATEMENT = "IP_SET_REFERENCE_STATEMENT"
    MANAGED_RULE_SET_STATEMENT = "MANAGED_RULE_SET_STATEMENT"
    LABEL_MATCH_STATEMENT = "LABEL_MATCH_STATEMENT"
    AND_STATEMENT = "AND_STATEMENT"
    OR_STATEMENT = "OR_STATEMENT"
    NOT_STATEMENT = "NOT_STATEMENT"
    IP_ADDRESS = "IP_ADDRESS"
    IP_ADDRESS_VERSION = "IP_ADDRESS_VERSION"
    FIELD_TO_MATCH = "FIELD_TO_MATCH"
    TEXT_TRANSFORMATION = "TEXT_TRANSFORMATION"
    SINGLE_QUERY_ARGUMENT = "SINGLE_QUERY_ARGUMENT"
    SINGLE_HEADER = "SINGLE_HEADER"
    DEFAULT_ACTION = "DEFAULT_ACTION"
    RULE_ACTION = "RULE_ACTION"
    ENTITY_LIMIT = "ENTITY_LIMIT"
    OVERRIDE_ACTION = "OVERRIDE_ACTION"
    SCOPE_VALUE = "SCOPE_VALUE"
    RESOURCE_ARN = "RESOURCE_ARN"
    RESOURCE_TYPE = "RESOURCE_TYPE"
    TAGS = "TAGS"
    TAG_KEYS = "TAG_KEYS"
    METRIC_NAME = "METRIC_NAME"
    FIREWALL_MANAGER_STATEMENT = "FIREWALL_MANAGER_STATEMENT"
    FALLBACK_BEHAVIOR = "FALLBACK_BEHAVIOR"
    POSITION = "POSITION"
    FORWARDED_IP_CONFIG = "FORWARDED_IP_CONFIG"
    IP_SET_FORWARDED_IP_CONFIG = "IP_SET_FORWARDED_IP_CONFIG"
    HEADER_NAME = "HEADER_NAME"
    CUSTOM_REQUEST_HANDLING = "CUSTOM_REQUEST_HANDLING"
    RESPONSE_CONTENT_TYPE = "RESPONSE_CONTENT_TYPE"
    CUSTOM_RESPONSE = "CUSTOM_RESPONSE"
    CUSTOM_RESPONSE_BODY = "CUSTOM_RESPONSE_BODY"
    JSON_MATCH_PATTERN = "JSON_MATCH_PATTERN"
    JSON_MATCH_SCOPE = "JSON_MATCH_SCOPE"
    BODY_PARSING_FALLBACK_BEHAVIOR = "BODY_PARSING_FALLBACK_BEHAVIOR"
    LOGGING_FILTER = "LOGGING_FILTER"
    FILTER_CONDITION = "FILTER_CONDITION"
    EXPIRE_TIMESTAMP = "EXPIRE_TIMESTAMP"
    CHANGE_PROPAGATION_STATUS = "CHANGE_PROPAGATION_STATUS"
    ASSOCIABLE_RESOURCE = "ASSOCIABLE_RESOURCE"
    LOG_DESTINATION = "LOG_DESTINATION"
    MANAGED_RULE_GROUP_CONFIG = "MANAGED_RULE_GROUP_CONFIG"
    PAYLOAD_TYPE = "PAYLOAD_TYPE"
    HEADER_MATCH_PATTERN = "HEADER_MATCH_PATTERN"
    COOKIE_MATCH_PATTERN = "COOKIE_MATCH_PATTERN"
    MAP_MATCH_SCOPE = "MAP_MATCH_SCOPE"
    OVERSIZE_HANDLING = "OVERSIZE_HANDLING"
    CHALLENGE_CONFIG = "CHALLENGE_CONFIG"
    TOKEN_DOMAIN = "TOKEN_DOMAIN"
    ATP_RULE_SET_RESPONSE_INSPECTION = "ATP_RULE_SET_RESPONSE_INSPECTION"
    ASSOCIATED_RESOURCE_TYPE = "ASSOCIATED_RESOURCE_TYPE"
    SCOPE_DOWN = "SCOPE_DOWN"
    CUSTOM_KEYS = "CUSTOM_KEYS"
    ACP_RULE_SET_RESPONSE_INSPECTION = "ACP_RULE_SET_RESPONSE_INSPECTION"
    DATA_PROTECTION_CONFIG = "DATA_PROTECTION_CONFIG"
    LOW_REPUTATION_MODE = "LOW_REPUTATION_MODE"


class PayloadType:
    """PayloadType enum values."""

    JSON = "JSON"
    FORM_ENCODED = "FORM_ENCODED"


class Platform:
    """Platform enum values."""

    IOS = "IOS"
    ANDROID = "ANDROID"


class PositionalConstraint:
    """PositionalConstraint enum values."""

    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class RateBasedStatementAggregateKeyType:
    """RateBasedStatementAggregateKeyType enum values."""

    IP = "IP"
    FORWARDED_IP = "FORWARDED_IP"
    CUSTOM_KEYS = "CUSTOM_KEYS"
    CONSTANT = "CONSTANT"


class ResourceType:
    """ResourceType enum values."""

    APPLICATION_LOAD_BALANCER = "APPLICATION_LOAD_BALANCER"
    API_GATEWAY = "API_GATEWAY"
    APPSYNC = "APPSYNC"
    COGNITO_USER_POOL = "COGNITO_USER_POOL"
    APP_RUNNER_SERVICE = "APP_RUNNER_SERVICE"
    VERIFIED_ACCESS_INSTANCE = "VERIFIED_ACCESS_INSTANCE"
    AMPLIFY = "AMPLIFY"


class ResponseContentType:
    """ResponseContentType enum values."""

    TEXT_PLAIN = "TEXT_PLAIN"
    TEXT_HTML = "TEXT_HTML"
    APPLICATION_JSON = "APPLICATION_JSON"


class Scope:
    """Scope enum values."""

    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class SensitivityLevel:
    """SensitivityLevel enum values."""

    LOW = "LOW"
    HIGH = "HIGH"


class SensitivityToAct:
    """SensitivityToAct enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class SizeInspectionLimit:
    """SizeInspectionLimit enum values."""

    KB_16 = "KB_16"
    KB_32 = "KB_32"
    KB_48 = "KB_48"
    KB_64 = "KB_64"


class TextTransformationType:
    """TextTransformationType enum values."""

    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"
    BASE64_DECODE = "BASE64_DECODE"
    HEX_DECODE = "HEX_DECODE"
    MD5 = "MD5"
    REPLACE_COMMENTS = "REPLACE_COMMENTS"
    ESCAPE_SEQ_DECODE = "ESCAPE_SEQ_DECODE"
    SQL_HEX_DECODE = "SQL_HEX_DECODE"
    CSS_DECODE = "CSS_DECODE"
    JS_DECODE = "JS_DECODE"
    NORMALIZE_PATH = "NORMALIZE_PATH"
    NORMALIZE_PATH_WIN = "NORMALIZE_PATH_WIN"
    REMOVE_NULLS = "REMOVE_NULLS"
    REPLACE_NULLS = "REPLACE_NULLS"
    BASE64_DECODE_EXT = "BASE64_DECODE_EXT"
    URL_DECODE_UNI = "URL_DECODE_UNI"
    UTF8_TO_UNICODE = "UTF8_TO_UNICODE"


class UsageOfAction:
    """UsageOfAction enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class ActionCondition(PropertyType):
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, ActionValue, Ref, GetAtt, Sub]] = None


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
class FieldToMatch(PropertyType):
    QUERY_STRING = "QueryString"
    URI_PATH = "UriPath"
    METHOD = "Method"
    SINGLE_HEADER = "SingleHeader"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_string": "QueryString",
        "uri_path": "UriPath",
        "method": "Method",
        "single_header": "SingleHeader",
    }

    query_string: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    uri_path: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    method: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
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

