"""PropertyTypes for AWS::ApiGateway::DocumentationPart."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessAssociationSourceType:
    """AccessAssociationSourceType enum values."""

    VPCE = "VPCE"


class ApiKeySourceType:
    """ApiKeySourceType enum values."""

    HEADER = "HEADER"
    AUTHORIZER = "AUTHORIZER"


class ApiKeysFormat:
    """ApiKeysFormat enum values."""

    CSV = "csv"


class ApiStatus:
    """ApiStatus enum values."""

    UPDATING = "UPDATING"
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    FAILED = "FAILED"


class AuthorizerType:
    """AuthorizerType enum values."""

    TOKEN = "TOKEN"
    REQUEST = "REQUEST"
    COGNITO_USER_POOLS = "COGNITO_USER_POOLS"


class CacheClusterSize:
    """CacheClusterSize enum values."""

    _0_5 = "0.5"
    _1_6 = "1.6"
    _6_1 = "6.1"
    _13_5 = "13.5"
    _28_4 = "28.4"
    _58_2 = "58.2"
    _118 = "118"
    _237 = "237"


class CacheClusterStatus:
    """CacheClusterStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    AVAILABLE = "AVAILABLE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    FLUSH_IN_PROGRESS = "FLUSH_IN_PROGRESS"


class ConnectionType:
    """ConnectionType enum values."""

    INTERNET = "INTERNET"
    VPC_LINK = "VPC_LINK"


class ContentHandlingStrategy:
    """ContentHandlingStrategy enum values."""

    CONVERT_TO_BINARY = "CONVERT_TO_BINARY"
    CONVERT_TO_TEXT = "CONVERT_TO_TEXT"


class DocumentationPartType:
    """DocumentationPartType enum values."""

    API = "API"
    AUTHORIZER = "AUTHORIZER"
    MODEL = "MODEL"
    RESOURCE = "RESOURCE"
    METHOD = "METHOD"
    PATH_PARAMETER = "PATH_PARAMETER"
    QUERY_PARAMETER = "QUERY_PARAMETER"
    REQUEST_HEADER = "REQUEST_HEADER"
    REQUEST_BODY = "REQUEST_BODY"
    RESPONSE = "RESPONSE"
    RESPONSE_HEADER = "RESPONSE_HEADER"
    RESPONSE_BODY = "RESPONSE_BODY"


class DomainNameStatus:
    """DomainNameStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"
    PENDING = "PENDING"
    PENDING_CERTIFICATE_REIMPORT = "PENDING_CERTIFICATE_REIMPORT"
    PENDING_OWNERSHIP_VERIFICATION = "PENDING_OWNERSHIP_VERIFICATION"
    FAILED = "FAILED"


class EndpointAccessMode:
    """EndpointAccessMode enum values."""

    BASIC = "BASIC"
    STRICT = "STRICT"


class EndpointType:
    """EndpointType enum values."""

    REGIONAL = "REGIONAL"
    EDGE = "EDGE"
    PRIVATE = "PRIVATE"


class GatewayResponseType:
    """GatewayResponseType enum values."""

    DEFAULT_4XX = "DEFAULT_4XX"
    DEFAULT_5XX = "DEFAULT_5XX"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    INVALID_API_KEY = "INVALID_API_KEY"
    ACCESS_DENIED = "ACCESS_DENIED"
    AUTHORIZER_FAILURE = "AUTHORIZER_FAILURE"
    AUTHORIZER_CONFIGURATION_ERROR = "AUTHORIZER_CONFIGURATION_ERROR"
    INVALID_SIGNATURE = "INVALID_SIGNATURE"
    EXPIRED_TOKEN = "EXPIRED_TOKEN"
    MISSING_AUTHENTICATION_TOKEN = "MISSING_AUTHENTICATION_TOKEN"
    INTEGRATION_FAILURE = "INTEGRATION_FAILURE"
    INTEGRATION_TIMEOUT = "INTEGRATION_TIMEOUT"
    API_CONFIGURATION_ERROR = "API_CONFIGURATION_ERROR"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    BAD_REQUEST_PARAMETERS = "BAD_REQUEST_PARAMETERS"
    BAD_REQUEST_BODY = "BAD_REQUEST_BODY"
    REQUEST_TOO_LARGE = "REQUEST_TOO_LARGE"
    THROTTLED = "THROTTLED"
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"
    WAF_FILTERED = "WAF_FILTERED"


class IntegrationType:
    """IntegrationType enum values."""

    HTTP = "HTTP"
    AWS = "AWS"
    MOCK = "MOCK"
    HTTP_PROXY = "HTTP_PROXY"
    AWS_PROXY = "AWS_PROXY"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"


class LocationStatusType:
    """LocationStatusType enum values."""

    DOCUMENTED = "DOCUMENTED"
    UNDOCUMENTED = "UNDOCUMENTED"


class Op:
    """Op enum values."""

    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
    MOVE = "move"
    COPY = "copy"
    TEST = "test"


class PutMode:
    """PutMode enum values."""

    MERGE = "merge"
    OVERWRITE = "overwrite"


class QuotaPeriodType:
    """QuotaPeriodType enum values."""

    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class ResourceOwner:
    """ResourceOwner enum values."""

    SELF = "SELF"
    OTHER_ACCOUNTS = "OTHER_ACCOUNTS"


class ResponseTransferMode:
    """ResponseTransferMode enum values."""

    BUFFERED = "BUFFERED"
    STREAM = "STREAM"


class RoutingMode:
    """RoutingMode enum values."""

    BASE_PATH_MAPPING_ONLY = "BASE_PATH_MAPPING_ONLY"
    ROUTING_RULE_ONLY = "ROUTING_RULE_ONLY"
    ROUTING_RULE_THEN_BASE_PATH_MAPPING = "ROUTING_RULE_THEN_BASE_PATH_MAPPING"


class SecurityPolicy:
    """SecurityPolicy enum values."""

    TLS_1_0 = "TLS_1_0"
    TLS_1_2 = "TLS_1_2"
    SECURITYPOLICY_TLS13_1_3_2025_09 = "SecurityPolicy_TLS13_1_3_2025_09"
    SECURITYPOLICY_TLS13_1_3_FIPS_2025_09 = "SecurityPolicy_TLS13_1_3_FIPS_2025_09"
    SECURITYPOLICY_TLS13_1_2_PFS_PQ_2025_09 = "SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09"
    SECURITYPOLICY_TLS13_1_2_FIPS_PQ_2025_09 = "SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09"
    SECURITYPOLICY_TLS13_1_2_PQ_2025_09 = "SecurityPolicy_TLS13_1_2_PQ_2025_09"
    SECURITYPOLICY_TLS13_1_2_2021_06 = "SecurityPolicy_TLS13_1_2_2021_06"
    SECURITYPOLICY_TLS13_2025_EDGE = "SecurityPolicy_TLS13_2025_EDGE"
    SECURITYPOLICY_TLS12_PFS_2025_EDGE = "SecurityPolicy_TLS12_PFS_2025_EDGE"
    SECURITYPOLICY_TLS12_2018_EDGE = "SecurityPolicy_TLS12_2018_EDGE"


class UnauthorizedCacheControlHeaderStrategy:
    """UnauthorizedCacheControlHeaderStrategy enum values."""

    FAIL_WITH_403 = "FAIL_WITH_403"
    SUCCEED_WITH_RESPONSE_HEADER = "SUCCEED_WITH_RESPONSE_HEADER"
    SUCCEED_WITHOUT_RESPONSE_HEADER = "SUCCEED_WITHOUT_RESPONSE_HEADER"


class VpcLinkStatus:
    """VpcLinkStatus enum values."""

    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    DELETING = "DELETING"
    FAILED = "FAILED"


@dataclass
class Location(PropertyType):
    PATH = "Path"
    TYPE = "Type"
    METHOD = "Method"
    STATUS_CODE = "StatusCode"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "type_": "Type",
        "method": "Method",
        "status_code": "StatusCode",
        "name": "Name",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

