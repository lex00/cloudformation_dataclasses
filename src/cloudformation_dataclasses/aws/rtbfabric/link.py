"""PropertyTypes for AWS::RTBFabric::Link."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid": "NoBid",
        "header_tag": "HeaderTag",
    }

    no_bid: Optional[NoBidAction] = None
    header_tag: Optional[HeaderTagAction] = None


@dataclass
class ApplicationLogs(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "link_application_log_sampling": "LinkApplicationLogSampling",
    }

    link_application_log_sampling: Optional[LinkApplicationLogSampling] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "criteria": "Criteria",
    }

    criteria: Optional[list[FilterCriterion]] = None


@dataclass
class FilterCriterion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "values": "Values",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class HeaderTagAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class ModuleConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid": "NoBid",
        "open_rtb_attribute": "OpenRtbAttribute",
    }

    no_bid: Optional[NoBidModuleParameters] = None
    open_rtb_attribute: Optional[OpenRtbAttributeModuleParameters] = None


@dataclass
class NoBidAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "no_bid_reason_code": "NoBidReasonCode",
    }

    no_bid_reason_code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NoBidModuleParameters(PropertyType):
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

