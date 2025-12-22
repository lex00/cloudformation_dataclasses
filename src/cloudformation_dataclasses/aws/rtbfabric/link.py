"""PropertyTypes for AWS::RTBFabric::Link."""

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
class Action(PropertyType):
    NO_BID = "NoBid"
    HEADER_TAG = "HeaderTag"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid": "NoBid",
        "header_tag": "HeaderTag",
    }

    no_bid: Optional[NoBidAction] = None
    header_tag: Optional[HeaderTagAction] = None


@dataclass
class ApplicationLogs(PropertyType):
    LINK_APPLICATION_LOG_SAMPLING = "LinkApplicationLogSampling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "link_application_log_sampling": "LinkApplicationLogSampling",
    }

    link_application_log_sampling: Optional[LinkApplicationLogSampling] = None


@dataclass
class Filter(PropertyType):
    CRITERIA = "Criteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "criteria": "Criteria",
    }

    criteria: Optional[list[FilterCriterion]] = None


@dataclass
class FilterCriterion(PropertyType):
    PATH = "Path"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "values": "Values",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class HeaderTagAction(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class ModuleConfiguration(PropertyType):
    DEPENDS_ON = "DependsOn"
    VERSION = "Version"
    MODULE_PARAMETERS = "ModuleParameters"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "depends_on": "DependsOn",
        "version": "Version",
        "module_parameters": "ModuleParameters",
        "name": "Name",
    }

    depends_on: Optional[Union[list[str], Ref]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    module_parameters: Optional[ModuleParameters] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ModuleParameters(PropertyType):
    NO_BID = "NoBid"
    OPEN_RTB_ATTRIBUTE = "OpenRtbAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid": "NoBid",
        "open_rtb_attribute": "OpenRtbAttribute",
    }

    no_bid: Optional[NoBidModuleParameters] = None
    open_rtb_attribute: Optional[OpenRtbAttributeModuleParameters] = None


@dataclass
class NoBidAction(PropertyType):
    NO_BID_REASON_CODE = "NoBidReasonCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid_reason_code": "NoBidReasonCode",
    }

    no_bid_reason_code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NoBidModuleParameters(PropertyType):
    PASS_THROUGH_PERCENTAGE = "PassThroughPercentage"
    REASON_CODE = "ReasonCode"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pass_through_percentage": "PassThroughPercentage",
        "reason_code": "ReasonCode",
        "reason": "Reason",
    }

    pass_through_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    reason_code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenRtbAttributeModuleParameters(PropertyType):
    FILTER_TYPE = "FilterType"
    ACTION = "Action"
    HOLDBACK_PERCENTAGE = "HoldbackPercentage"
    FILTER_CONFIGURATION = "FilterConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_type": "FilterType",
        "action": "Action",
        "holdback_percentage": "HoldbackPercentage",
        "filter_configuration": "FilterConfiguration",
    }

    filter_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Action] = None
    holdback_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    filter_configuration: Optional[list[Filter]] = None


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

