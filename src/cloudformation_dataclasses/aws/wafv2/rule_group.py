"""PropertyTypes for AWS::WAFv2::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

