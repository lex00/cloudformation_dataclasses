"""PropertyTypes for AWS::RTBFabric::OutboundExternalLink."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationLogs(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "link_application_log_sampling": "LinkApplicationLogSampling",
    }

    link_application_log_sampling: Optional[LinkApplicationLogSampling] = None


@dataclass
class LinkApplicationLogSampling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_log": "FilterLog",
        "error_log": "ErrorLog",
    }

    filter_log: Optional[Union[float, Ref, GetAtt, Sub]] = None
    error_log: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LinkAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "responder_error_masking": "ResponderErrorMasking",
        "customer_provided_id": "CustomerProvidedId",
    }

    responder_error_masking: Optional[list[ResponderErrorMaskingForHttpCode]] = None
    customer_provided_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LinkLogSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_logs": "ApplicationLogs",
    }

    application_logs: Optional[ApplicationLogs] = None


@dataclass
class ResponderErrorMaskingForHttpCode(PropertyType):
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

