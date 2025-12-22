"""PropertyTypes for AWS::RTBFabric::InboundExternalLink."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class FilterType:
    """FilterType enum values."""

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class LinkDirection:
    """LinkDirection enum values."""

    RESPONSE = "RESPONSE"
    REQUEST = "REQUEST"


class LinkStatus:
    """LinkStatus enum values."""

    PENDING_CREATION = "PENDING_CREATION"
    PENDING_REQUEST = "PENDING_REQUEST"
    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"
    FAILED = "FAILED"
    PENDING_DELETION = "PENDING_DELETION"
    DELETED = "DELETED"
    PENDING_UPDATE = "PENDING_UPDATE"
    PENDING_ISOLATION = "PENDING_ISOLATION"
    ISOLATED = "ISOLATED"
    PENDING_RESTORATION = "PENDING_RESTORATION"


class Protocol:
    """Protocol enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"


class RequesterGatewayStatus:
    """RequesterGatewayStatus enum values."""

    PENDING_CREATION = "PENDING_CREATION"
    ACTIVE = "ACTIVE"
    PENDING_DELETION = "PENDING_DELETION"
    DELETED = "DELETED"
    ERROR = "ERROR"
    PENDING_UPDATE = "PENDING_UPDATE"
    ISOLATED = "ISOLATED"
    PENDING_ISOLATION = "PENDING_ISOLATION"
    PENDING_RESTORATION = "PENDING_RESTORATION"


class ResponderErrorMaskingAction:
    """ResponderErrorMaskingAction enum values."""

    NO_BID = "NO_BID"
    PASSTHROUGH = "PASSTHROUGH"


class ResponderErrorMaskingLoggingType:
    """ResponderErrorMaskingLoggingType enum values."""

    NONE = "NONE"
    METRIC = "METRIC"
    RESPONSE = "RESPONSE"


class ResponderGatewayStatus:
    """ResponderGatewayStatus enum values."""

    PENDING_CREATION = "PENDING_CREATION"
    ACTIVE = "ACTIVE"
    PENDING_DELETION = "PENDING_DELETION"
    DELETED = "DELETED"
    ERROR = "ERROR"
    PENDING_UPDATE = "PENDING_UPDATE"
    ISOLATED = "ISOLATED"
    PENDING_ISOLATION = "PENDING_ISOLATION"
    PENDING_RESTORATION = "PENDING_RESTORATION"


@dataclass
class ApplicationLogs(PropertyType):
    LINK_APPLICATION_LOG_SAMPLING = "LinkApplicationLogSampling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "link_application_log_sampling": "LinkApplicationLogSampling",
    }

    link_application_log_sampling: Optional[LinkApplicationLogSampling] = None


@dataclass
class LinkApplicationLogSampling(PropertyType):
    FILTER_LOG = "FilterLog"
    ERROR_LOG = "ErrorLog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_log": "FilterLog",
        "error_log": "ErrorLog",
    }

    filter_log: Optional[Union[float, Ref, GetAtt, Sub]] = None
    error_log: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LinkAttributes(PropertyType):
    RESPONDER_ERROR_MASKING = "ResponderErrorMasking"
    CUSTOMER_PROVIDED_ID = "CustomerProvidedId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "responder_error_masking": "ResponderErrorMasking",
        "customer_provided_id": "CustomerProvidedId",
    }

    responder_error_masking: Optional[list[ResponderErrorMaskingForHttpCode]] = None
    customer_provided_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LinkLogSettings(PropertyType):
    APPLICATION_LOGS = "ApplicationLogs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_logs": "ApplicationLogs",
    }

    application_logs: Optional[ApplicationLogs] = None


@dataclass
class ResponderErrorMaskingForHttpCode(PropertyType):
    HTTP_CODE = "HttpCode"
    ACTION = "Action"
    RESPONSE_LOGGING_PERCENTAGE = "ResponseLoggingPercentage"
    LOGGING_TYPES = "LoggingTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_code": "HttpCode",
        "action": "Action",
        "response_logging_percentage": "ResponseLoggingPercentage",
        "logging_types": "LoggingTypes",
    }

    http_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_logging_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    logging_types: Optional[Union[list[str], Ref]] = None

