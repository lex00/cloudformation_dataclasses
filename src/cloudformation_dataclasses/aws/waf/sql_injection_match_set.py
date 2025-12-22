"""PropertyTypes for AWS::WAF::SqlInjectionMatchSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChangeAction:
    """ChangeAction enum values."""

    INSERT = "INSERT"
    DELETE = "DELETE"


class ChangeTokenStatus:
    """ChangeTokenStatus enum values."""

    PROVISIONED = "PROVISIONED"
    PENDING = "PENDING"
    INSYNC = "INSYNC"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


class GeoMatchConstraintType:
    """GeoMatchConstraintType enum values."""

    COUNTRY = "Country"


class GeoMatchConstraintValue:
    """GeoMatchConstraintValue enum values."""

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


class IPSetDescriptorType:
    """IPSetDescriptorType enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"


class MatchFieldType:
    """MatchFieldType enum values."""

    URI = "URI"
    QUERY_STRING = "QUERY_STRING"
    HEADER = "HEADER"
    METHOD = "METHOD"
    BODY = "BODY"
    SINGLE_QUERY_ARG = "SINGLE_QUERY_ARG"
    ALL_QUERY_ARGS = "ALL_QUERY_ARGS"


class MigrationErrorType:
    """MigrationErrorType enum values."""

    ENTITY_NOT_SUPPORTED = "ENTITY_NOT_SUPPORTED"
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"
    S3_BUCKET_NO_PERMISSION = "S3_BUCKET_NO_PERMISSION"
    S3_BUCKET_NOT_ACCESSIBLE = "S3_BUCKET_NOT_ACCESSIBLE"
    S3_BUCKET_NOT_FOUND = "S3_BUCKET_NOT_FOUND"
    S3_BUCKET_INVALID_REGION = "S3_BUCKET_INVALID_REGION"
    S3_INTERNAL_ERROR = "S3_INTERNAL_ERROR"


class ParameterExceptionField:
    """ParameterExceptionField enum values."""

    CHANGE_ACTION = "CHANGE_ACTION"
    WAF_ACTION = "WAF_ACTION"
    WAF_OVERRIDE_ACTION = "WAF_OVERRIDE_ACTION"
    PREDICATE_TYPE = "PREDICATE_TYPE"
    IPSET_TYPE = "IPSET_TYPE"
    BYTE_MATCH_FIELD_TYPE = "BYTE_MATCH_FIELD_TYPE"
    SQL_INJECTION_MATCH_FIELD_TYPE = "SQL_INJECTION_MATCH_FIELD_TYPE"
    BYTE_MATCH_TEXT_TRANSFORMATION = "BYTE_MATCH_TEXT_TRANSFORMATION"
    BYTE_MATCH_POSITIONAL_CONSTRAINT = "BYTE_MATCH_POSITIONAL_CONSTRAINT"
    SIZE_CONSTRAINT_COMPARISON_OPERATOR = "SIZE_CONSTRAINT_COMPARISON_OPERATOR"
    GEO_MATCH_LOCATION_TYPE = "GEO_MATCH_LOCATION_TYPE"
    GEO_MATCH_LOCATION_VALUE = "GEO_MATCH_LOCATION_VALUE"
    RATE_KEY = "RATE_KEY"
    RULE_TYPE = "RULE_TYPE"
    NEXT_MARKER = "NEXT_MARKER"
    RESOURCE_ARN = "RESOURCE_ARN"
    TAGS = "TAGS"
    TAG_KEYS = "TAG_KEYS"


class ParameterExceptionReason:
    """ParameterExceptionReason enum values."""

    INVALID_OPTION = "INVALID_OPTION"
    ILLEGAL_COMBINATION = "ILLEGAL_COMBINATION"
    ILLEGAL_ARGUMENT = "ILLEGAL_ARGUMENT"
    INVALID_TAG_KEY = "INVALID_TAG_KEY"


class PositionalConstraint:
    """PositionalConstraint enum values."""

    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class PredicateType:
    """PredicateType enum values."""

    IPMATCH = "IPMatch"
    BYTEMATCH = "ByteMatch"
    SQLINJECTIONMATCH = "SqlInjectionMatch"
    GEOMATCH = "GeoMatch"
    SIZECONSTRAINT = "SizeConstraint"
    XSSMATCH = "XssMatch"
    REGEXMATCH = "RegexMatch"


class RateKey:
    """RateKey enum values."""

    IP = "IP"


class TextTransformation:
    """TextTransformation enum values."""

    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"


class WafActionType:
    """WafActionType enum values."""

    BLOCK = "BLOCK"
    ALLOW = "ALLOW"
    COUNT = "COUNT"


class WafOverrideActionType:
    """WafOverrideActionType enum values."""

    NONE = "NONE"
    COUNT = "COUNT"


class WafRuleType:
    """WafRuleType enum values."""

    REGULAR = "REGULAR"
    RATE_BASED = "RATE_BASED"
    GROUP = "GROUP"


@dataclass
class FieldToMatch(PropertyType):
    DATA = "Data"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data": "Data",
        "type_": "Type",
    }

    data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, MatchFieldType, Ref, GetAtt, Sub]] = None


@dataclass
class SqlInjectionMatchTuple(PropertyType):
    FIELD_TO_MATCH = "FieldToMatch"
    TEXT_TRANSFORMATION = "TextTransformation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "field_to_match": "FieldToMatch",
        "text_transformation": "TextTransformation",
    }

    field_to_match: Optional[FieldToMatch] = None
    text_transformation: Optional[Union[str, TextTransformation, Ref, GetAtt, Sub]] = None

