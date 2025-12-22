"""PropertyTypes for AWS::WAFv2::RuleGroup."""

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
class AllowAction(PropertyType):
    CUSTOM_REQUEST_HANDLING = "CustomRequestHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_request_handling": "CustomRequestHandling",
    }

    custom_request_handling: Optional[CustomRequestHandling] = None


@dataclass
class AndStatement(PropertyType):
    STATEMENTS = "Statements"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statements": "Statements",
    }

    statements: Optional[list[Statement]] = None


@dataclass
class AsnMatchStatement(PropertyType):
    FORWARDED_IP_CONFIG = "ForwardedIPConfig"
    ASN_LIST = "AsnList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
        "asn_list": "AsnList",
    }

    forwarded_ip_config: Optional[ForwardedIPConfiguration] = None
    asn_list: Optional[Union[list[int], Ref]] = None


@dataclass
class BlockAction(PropertyType):
    CUSTOM_RESPONSE = "CustomResponse"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_response": "CustomResponse",
    }

    custom_response: Optional[CustomResponse] = None


@dataclass
class Body(PropertyType):
    OVERSIZE_HANDLING = "OversizeHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "oversize_handling": "OversizeHandling",
    }

    oversize_handling: Optional[Union[str, OversizeHandling, Ref, GetAtt, Sub]] = None


@dataclass
class ByteMatchStatement(PropertyType):
    SEARCH_STRING_BASE64 = "SearchStringBase64"
    TEXT_TRANSFORMATIONS = "TextTransformations"
    POSITIONAL_CONSTRAINT = "PositionalConstraint"
    SEARCH_STRING = "SearchString"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "search_string_base64": "SearchStringBase64",
        "text_transformations": "TextTransformations",
        "positional_constraint": "PositionalConstraint",
        "search_string": "SearchString",
        "field_to_match": "FieldToMatch",
    }

    search_string_base64: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_transformations: Optional[list[TextTransformation]] = None
    positional_constraint: Optional[Union[str, PositionalConstraint, Ref, GetAtt, Sub]] = None
    search_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class CaptchaAction(PropertyType):
    CUSTOM_REQUEST_HANDLING = "CustomRequestHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_request_handling": "CustomRequestHandling",
    }

    custom_request_handling: Optional[CustomRequestHandling] = None


@dataclass
class CaptchaConfig(PropertyType):
    IMMUNITY_TIME_PROPERTY = "ImmunityTimeProperty"

    _property_mappings: ClassVar[dict[str, str]] = {
        "immunity_time_property": "ImmunityTimeProperty",
    }

    immunity_time_property: Optional[ImmunityTimeProperty] = None


@dataclass
class ChallengeAction(PropertyType):
    CUSTOM_REQUEST_HANDLING = "CustomRequestHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_request_handling": "CustomRequestHandling",
    }

    custom_request_handling: Optional[CustomRequestHandling] = None


@dataclass
class ChallengeConfig(PropertyType):
    IMMUNITY_TIME_PROPERTY = "ImmunityTimeProperty"

    _property_mappings: ClassVar[dict[str, str]] = {
        "immunity_time_property": "ImmunityTimeProperty",
    }

    immunity_time_property: Optional[ImmunityTimeProperty] = None


@dataclass
class CookieMatchPattern(PropertyType):
    ALL = "All"
    INCLUDED_COOKIES = "IncludedCookies"
    EXCLUDED_COOKIES = "ExcludedCookies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all": "All",
        "included_cookies": "IncludedCookies",
        "excluded_cookies": "ExcludedCookies",
    }

    all: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    included_cookies: Optional[Union[list[str], Ref]] = None
    excluded_cookies: Optional[Union[list[str], Ref]] = None


@dataclass
class Cookies(PropertyType):
    MATCH_SCOPE = "MatchScope"
    MATCH_PATTERN = "MatchPattern"
    OVERSIZE_HANDLING = "OversizeHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "match_scope": "MatchScope",
        "match_pattern": "MatchPattern",
        "oversize_handling": "OversizeHandling",
    }

    match_scope: Optional[Union[str, MapMatchScope, Ref, GetAtt, Sub]] = None
    match_pattern: Optional[CookieMatchPattern] = None
    oversize_handling: Optional[Union[str, OversizeHandling, Ref, GetAtt, Sub]] = None


@dataclass
class CountAction(PropertyType):
    CUSTOM_REQUEST_HANDLING = "CustomRequestHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_request_handling": "CustomRequestHandling",
    }

    custom_request_handling: Optional[CustomRequestHandling] = None


@dataclass
class CustomHTTPHeader(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomRequestHandling(PropertyType):
    INSERT_HEADERS = "InsertHeaders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "insert_headers": "InsertHeaders",
    }

    insert_headers: Optional[list[CustomHTTPHeader]] = None


@dataclass
class CustomResponse(PropertyType):
    RESPONSE_CODE = "ResponseCode"
    CUSTOM_RESPONSE_BODY_KEY = "CustomResponseBodyKey"
    RESPONSE_HEADERS = "ResponseHeaders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "response_code": "ResponseCode",
        "custom_response_body_key": "CustomResponseBodyKey",
        "response_headers": "ResponseHeaders",
    }

    response_code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    custom_response_body_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_headers: Optional[list[CustomHTTPHeader]] = None


@dataclass
class CustomResponseBody(PropertyType):
    CONTENT_TYPE = "ContentType"
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "content": "Content",
    }

    content_type: Optional[Union[str, ResponseContentType, Ref, GetAtt, Sub]] = None
    content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FieldToMatch(PropertyType):
    ALL_QUERY_ARGUMENTS = "AllQueryArguments"
    JA3_FINGERPRINT = "JA3Fingerprint"
    SINGLE_QUERY_ARGUMENT = "SingleQueryArgument"
    QUERY_STRING = "QueryString"
    HEADERS = "Headers"
    METHOD = "Method"
    URI_FRAGMENT = "UriFragment"
    JSON_BODY = "JsonBody"
    URI_PATH = "UriPath"
    COOKIES = "Cookies"
    JA4_FINGERPRINT = "JA4Fingerprint"
    BODY = "Body"
    SINGLE_HEADER = "SingleHeader"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_query_arguments": "AllQueryArguments",
        "ja3_fingerprint": "JA3Fingerprint",
        "single_query_argument": "SingleQueryArgument",
        "query_string": "QueryString",
        "headers": "Headers",
        "method": "Method",
        "uri_fragment": "UriFragment",
        "json_body": "JsonBody",
        "uri_path": "UriPath",
        "cookies": "Cookies",
        "ja4_fingerprint": "JA4Fingerprint",
        "body": "Body",
        "single_header": "SingleHeader",
    }

    all_query_arguments: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    ja3_fingerprint: Optional[JA3Fingerprint] = None
    single_query_argument: Optional[SingleQueryArgument] = None
    query_string: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    headers: Optional[Headers] = None
    method: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    uri_fragment: Optional[UriFragment] = None
    json_body: Optional[JsonBody] = None
    uri_path: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    cookies: Optional[Cookies] = None
    ja4_fingerprint: Optional[JA4Fingerprint] = None
    body: Optional[Body] = None
    single_header: Optional[SingleHeader] = None


@dataclass
class ForwardedIPConfiguration(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"
    HEADER_NAME = "HeaderName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
        "header_name": "HeaderName",
    }

    fallback_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeoMatchStatement(PropertyType):
    FORWARDED_IP_CONFIG = "ForwardedIPConfig"
    COUNTRY_CODES = "CountryCodes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
        "country_codes": "CountryCodes",
    }

    forwarded_ip_config: Optional[ForwardedIPConfiguration] = None
    country_codes: Optional[Union[list[str], Ref]] = None


@dataclass
class HeaderMatchPattern(PropertyType):
    ALL = "All"
    INCLUDED_HEADERS = "IncludedHeaders"
    EXCLUDED_HEADERS = "ExcludedHeaders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all": "All",
        "included_headers": "IncludedHeaders",
        "excluded_headers": "ExcludedHeaders",
    }

    all: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    included_headers: Optional[Union[list[str], Ref]] = None
    excluded_headers: Optional[Union[list[str], Ref]] = None


@dataclass
class Headers(PropertyType):
    MATCH_SCOPE = "MatchScope"
    MATCH_PATTERN = "MatchPattern"
    OVERSIZE_HANDLING = "OversizeHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "match_scope": "MatchScope",
        "match_pattern": "MatchPattern",
        "oversize_handling": "OversizeHandling",
    }

    match_scope: Optional[Union[str, MapMatchScope, Ref, GetAtt, Sub]] = None
    match_pattern: Optional[HeaderMatchPattern] = None
    oversize_handling: Optional[Union[str, OversizeHandling, Ref, GetAtt, Sub]] = None


@dataclass
class IPSetForwardedIPConfiguration(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"
    HEADER_NAME = "HeaderName"
    POSITION = "Position"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
        "header_name": "HeaderName",
        "position": "Position",
    }

    fallback_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    position: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IPSetReferenceStatement(PropertyType):
    IP_SET_FORWARDED_IP_CONFIG = "IPSetForwardedIPConfig"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_forwarded_ip_config": "IPSetForwardedIPConfig",
        "arn": "Arn",
    }

    ip_set_forwarded_ip_config: Optional[IPSetForwardedIPConfiguration] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImmunityTimeProperty(PropertyType):
    IMMUNITY_TIME = "ImmunityTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "immunity_time": "ImmunityTime",
    }

    immunity_time: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JA3Fingerprint(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
    }

    fallback_behavior: Optional[Union[str, FallbackBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class JA4Fingerprint(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
    }

    fallback_behavior: Optional[Union[str, FallbackBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class JsonBody(PropertyType):
    MATCH_SCOPE = "MatchScope"
    MATCH_PATTERN = "MatchPattern"
    INVALID_FALLBACK_BEHAVIOR = "InvalidFallbackBehavior"
    OVERSIZE_HANDLING = "OversizeHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "match_scope": "MatchScope",
        "match_pattern": "MatchPattern",
        "invalid_fallback_behavior": "InvalidFallbackBehavior",
        "oversize_handling": "OversizeHandling",
    }

    match_scope: Optional[Union[str, JsonMatchScope, Ref, GetAtt, Sub]] = None
    match_pattern: Optional[JsonMatchPattern] = None
    invalid_fallback_behavior: Optional[Union[str, BodyParsingFallbackBehavior, Ref, GetAtt, Sub]] = None
    oversize_handling: Optional[Union[str, OversizeHandling, Ref, GetAtt, Sub]] = None


@dataclass
class JsonMatchPattern(PropertyType):
    ALL = "All"
    INCLUDED_PATHS = "IncludedPaths"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all": "All",
        "included_paths": "IncludedPaths",
    }

    all: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    included_paths: Optional[Union[list[str], Ref]] = None


@dataclass
class Label(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LabelMatchStatement(PropertyType):
    SCOPE = "Scope"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
        "key": "Key",
    }

    scope: Optional[Union[str, LabelMatchScope, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LabelSummary(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotStatement(PropertyType):
    STATEMENT = "Statement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statement": "Statement",
    }

    statement: Optional[Statement] = None


@dataclass
class OrStatement(PropertyType):
    STATEMENTS = "Statements"

    _property_mappings: ClassVar[dict[str, str]] = {
        "statements": "Statements",
    }

    statements: Optional[list[Statement]] = None


@dataclass
class RateBasedStatement(PropertyType):
    AGGREGATE_KEY_TYPE = "AggregateKeyType"
    CUSTOM_KEYS = "CustomKeys"
    FORWARDED_IP_CONFIG = "ForwardedIPConfig"
    LIMIT = "Limit"
    EVALUATION_WINDOW_SEC = "EvaluationWindowSec"
    SCOPE_DOWN_STATEMENT = "ScopeDownStatement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregate_key_type": "AggregateKeyType",
        "custom_keys": "CustomKeys",
        "forwarded_ip_config": "ForwardedIPConfig",
        "limit": "Limit",
        "evaluation_window_sec": "EvaluationWindowSec",
        "scope_down_statement": "ScopeDownStatement",
    }

    aggregate_key_type: Optional[Union[str, RateBasedStatementAggregateKeyType, Ref, GetAtt, Sub]] = None
    custom_keys: Optional[list[RateBasedStatementCustomKey]] = None
    forwarded_ip_config: Optional[ForwardedIPConfiguration] = None
    limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    evaluation_window_sec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    scope_down_statement: Optional[Statement] = None


@dataclass
class RateBasedStatementCustomKey(PropertyType):
    COOKIE = "Cookie"
    FORWARDED_IP = "ForwardedIP"
    QUERY_ARGUMENT = "QueryArgument"
    JA3_FINGERPRINT = "JA3Fingerprint"
    HEADER = "Header"
    HTTP_METHOD = "HTTPMethod"
    QUERY_STRING = "QueryString"
    URI_PATH = "UriPath"
    IP = "IP"
    JA4_FINGERPRINT = "JA4Fingerprint"
    ASN = "ASN"
    LABEL_NAMESPACE = "LabelNamespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cookie": "Cookie",
        "forwarded_ip": "ForwardedIP",
        "query_argument": "QueryArgument",
        "ja3_fingerprint": "JA3Fingerprint",
        "header": "Header",
        "http_method": "HTTPMethod",
        "query_string": "QueryString",
        "uri_path": "UriPath",
        "ip": "IP",
        "ja4_fingerprint": "JA4Fingerprint",
        "asn": "ASN",
        "label_namespace": "LabelNamespace",
    }

    cookie: Optional[RateLimitCookie] = None
    forwarded_ip: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    query_argument: Optional[RateLimitQueryArgument] = None
    ja3_fingerprint: Optional[RateLimitJA3Fingerprint] = None
    header: Optional[RateLimitHeader] = None
    http_method: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    query_string: Optional[RateLimitQueryString] = None
    uri_path: Optional[RateLimitUriPath] = None
    ip: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    ja4_fingerprint: Optional[RateLimitJA4Fingerprint] = None
    asn: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    label_namespace: Optional[RateLimitLabelNamespace] = None


@dataclass
class RateLimitCookie(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "name": "Name",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitHeader(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "name": "Name",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitJA3Fingerprint(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
    }

    fallback_behavior: Optional[Union[str, FallbackBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitJA4Fingerprint(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
    }

    fallback_behavior: Optional[Union[str, FallbackBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitLabelNamespace(PropertyType):
    NAMESPACE = "Namespace"

    _property_mappings: ClassVar[dict[str, str]] = {
        "namespace": "Namespace",
    }

    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitQueryArgument(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "name": "Name",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RateLimitQueryString(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
    }

    text_transformations: Optional[list[TextTransformation]] = None


@dataclass
class RateLimitUriPath(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
    }

    text_transformations: Optional[list[TextTransformation]] = None


@dataclass
class RegexMatchStatement(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    REGEX_STRING = "RegexString"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "regex_string": "RegexString",
        "field_to_match": "FieldToMatch",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    regex_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class RegexPatternSetReferenceStatement(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    ARN = "Arn"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "arn": "Arn",
        "field_to_match": "FieldToMatch",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class Rule(PropertyType):
    ACTION = "Action"
    PRIORITY = "Priority"
    STATEMENT = "Statement"
    CHALLENGE_CONFIG = "ChallengeConfig"
    RULE_LABELS = "RuleLabels"
    VISIBILITY_CONFIG = "VisibilityConfig"
    CAPTCHA_CONFIG = "CaptchaConfig"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "priority": "Priority",
        "statement": "Statement",
        "challenge_config": "ChallengeConfig",
        "rule_labels": "RuleLabels",
        "visibility_config": "VisibilityConfig",
        "captcha_config": "CaptchaConfig",
        "name": "Name",
    }

    action: Optional[RuleAction] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    statement: Optional[Statement] = None
    challenge_config: Optional[ChallengeConfig] = None
    rule_labels: Optional[list[Label]] = None
    visibility_config: Optional[VisibilityConfig] = None
    captcha_config: Optional[CaptchaConfig] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleAction(PropertyType):
    CAPTCHA = "Captcha"
    BLOCK = "Block"
    COUNT = "Count"
    ALLOW = "Allow"
    CHALLENGE = "Challenge"

    _property_mappings: ClassVar[dict[str, str]] = {
        "captcha": "Captcha",
        "block": "Block",
        "count": "Count",
        "allow": "Allow",
        "challenge": "Challenge",
    }

    captcha: Optional[CaptchaAction] = None
    block: Optional[BlockAction] = None
    count: Optional[CountAction] = None
    allow: Optional[AllowAction] = None
    challenge: Optional[ChallengeAction] = None


@dataclass
class SingleHeader(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleQueryArgument(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SizeConstraintStatement(PropertyType):
    COMPARISON_OPERATOR = "ComparisonOperator"
    TEXT_TRANSFORMATIONS = "TextTransformations"
    SIZE = "Size"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison_operator": "ComparisonOperator",
        "text_transformations": "TextTransformations",
        "size": "Size",
        "field_to_match": "FieldToMatch",
    }

    comparison_operator: Optional[Union[str, ComparisonOperator, Ref, GetAtt, Sub]] = None
    text_transformations: Optional[list[TextTransformation]] = None
    size: Optional[Union[float, Ref, GetAtt, Sub]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class SqliMatchStatement(PropertyType):
    SENSITIVITY_LEVEL = "SensitivityLevel"
    TEXT_TRANSFORMATIONS = "TextTransformations"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sensitivity_level": "SensitivityLevel",
        "text_transformations": "TextTransformations",
        "field_to_match": "FieldToMatch",
    }

    sensitivity_level: Optional[Union[str, SensitivityLevel, Ref, GetAtt, Sub]] = None
    text_transformations: Optional[list[TextTransformation]] = None
    field_to_match: Optional[FieldToMatch] = None


@dataclass
class Statement(PropertyType):
    SIZE_CONSTRAINT_STATEMENT = "SizeConstraintStatement"
    AND_STATEMENT = "AndStatement"
    XSS_MATCH_STATEMENT = "XssMatchStatement"
    NOT_STATEMENT = "NotStatement"
    BYTE_MATCH_STATEMENT = "ByteMatchStatement"
    RATE_BASED_STATEMENT = "RateBasedStatement"
    GEO_MATCH_STATEMENT = "GeoMatchStatement"
    LABEL_MATCH_STATEMENT = "LabelMatchStatement"
    REGEX_MATCH_STATEMENT = "RegexMatchStatement"
    SQLI_MATCH_STATEMENT = "SqliMatchStatement"
    REGEX_PATTERN_SET_REFERENCE_STATEMENT = "RegexPatternSetReferenceStatement"
    OR_STATEMENT = "OrStatement"
    ASN_MATCH_STATEMENT = "AsnMatchStatement"
    IP_SET_REFERENCE_STATEMENT = "IPSetReferenceStatement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "size_constraint_statement": "SizeConstraintStatement",
        "and_statement": "AndStatement",
        "xss_match_statement": "XssMatchStatement",
        "not_statement": "NotStatement",
        "byte_match_statement": "ByteMatchStatement",
        "rate_based_statement": "RateBasedStatement",
        "geo_match_statement": "GeoMatchStatement",
        "label_match_statement": "LabelMatchStatement",
        "regex_match_statement": "RegexMatchStatement",
        "sqli_match_statement": "SqliMatchStatement",
        "regex_pattern_set_reference_statement": "RegexPatternSetReferenceStatement",
        "or_statement": "OrStatement",
        "asn_match_statement": "AsnMatchStatement",
        "ip_set_reference_statement": "IPSetReferenceStatement",
    }

    size_constraint_statement: Optional[SizeConstraintStatement] = None
    and_statement: Optional[AndStatement] = None
    xss_match_statement: Optional[XssMatchStatement] = None
    not_statement: Optional[NotStatement] = None
    byte_match_statement: Optional[ByteMatchStatement] = None
    rate_based_statement: Optional[RateBasedStatement] = None
    geo_match_statement: Optional[GeoMatchStatement] = None
    label_match_statement: Optional[LabelMatchStatement] = None
    regex_match_statement: Optional[RegexMatchStatement] = None
    sqli_match_statement: Optional[SqliMatchStatement] = None
    regex_pattern_set_reference_statement: Optional[RegexPatternSetReferenceStatement] = None
    or_statement: Optional[OrStatement] = None
    asn_match_statement: Optional[AsnMatchStatement] = None
    ip_set_reference_statement: Optional[IPSetReferenceStatement] = None


@dataclass
class TextTransformation(PropertyType):
    TYPE = "Type"
    PRIORITY = "Priority"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "priority": "Priority",
    }

    type_: Optional[Union[str, TextTransformationType, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class UriFragment(PropertyType):
    FALLBACK_BEHAVIOR = "FallbackBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_behavior": "FallbackBehavior",
    }

    fallback_behavior: Optional[Union[str, FallbackBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class VisibilityConfig(PropertyType):
    METRIC_NAME = "MetricName"
    SAMPLED_REQUESTS_ENABLED = "SampledRequestsEnabled"
    CLOUD_WATCH_METRICS_ENABLED = "CloudWatchMetricsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "sampled_requests_enabled": "SampledRequestsEnabled",
        "cloud_watch_metrics_enabled": "CloudWatchMetricsEnabled",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sampled_requests_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class XssMatchStatement(PropertyType):
    TEXT_TRANSFORMATIONS = "TextTransformations"
    FIELD_TO_MATCH = "FieldToMatch"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_transformations": "TextTransformations",
        "field_to_match": "FieldToMatch",
    }

    text_transformations: Optional[list[TextTransformation]] = None
    field_to_match: Optional[FieldToMatch] = None

