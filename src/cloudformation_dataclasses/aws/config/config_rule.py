"""PropertyTypes for AWS::Config::ConfigRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Compliance(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPolicyDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_debug_log_delivery": "EnableDebugLogDelivery",
        "policy_text": "PolicyText",
        "policy_runtime": "PolicyRuntime",
    }

    enable_debug_log_delivery: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    policy_text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EvaluationModeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, EvaluationMode, Ref, GetAtt, Sub]] = None


@dataclass
class Scope(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compliance_resource_id": "ComplianceResourceId",
        "tag_key": "TagKey",
        "compliance_resource_types": "ComplianceResourceTypes",
        "tag_value": "TagValue",
    }

    compliance_resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    compliance_resource_types: Optional[Union[list[str], Ref]] = None
    tag_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
        "custom_policy_details": "CustomPolicyDetails",
        "source_identifier": "SourceIdentifier",
        "source_details": "SourceDetails",
    }

    owner: Optional[Union[str, Owner, Ref, GetAtt, Sub]] = None
    custom_policy_details: Optional[CustomPolicyDetails] = None
    source_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_details: Optional[list[SourceDetail]] = None


@dataclass
class SourceDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_source": "EventSource",
        "maximum_execution_frequency": "MaximumExecutionFrequency",
        "message_type": "MessageType",
    }

    event_source: Optional[Union[str, EventSource, Ref, GetAtt, Sub]] = None
    maximum_execution_frequency: Optional[Union[str, MaximumExecutionFrequency, Ref, GetAtt, Sub]] = None
    message_type: Optional[Union[str, MessageType, Ref, GetAtt, Sub]] = None

