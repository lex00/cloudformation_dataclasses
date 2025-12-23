"""PropertyTypes for AWS::NetworkFirewall::FirewallPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "publish_metric_action": "PublishMetricAction",
    }

    publish_metric_action: Optional[PublishMetricAction] = None


@dataclass
class CustomAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_name": "ActionName",
        "action_definition": "ActionDefinition",
    }

    action_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_definition: Optional[ActionDefinition] = None


@dataclass
class Dimension(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FirewallPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stateless_rule_group_references": "StatelessRuleGroupReferences",
        "stateful_rule_group_references": "StatefulRuleGroupReferences",
        "enable_tls_session_holding": "EnableTLSSessionHolding",
        "stateless_default_actions": "StatelessDefaultActions",
        "stateful_engine_options": "StatefulEngineOptions",
        "stateless_custom_actions": "StatelessCustomActions",
        "stateless_fragment_default_actions": "StatelessFragmentDefaultActions",
        "policy_variables": "PolicyVariables",
        "stateful_default_actions": "StatefulDefaultActions",
        "tls_inspection_configuration_arn": "TLSInspectionConfigurationArn",
    }

    stateless_rule_group_references: Optional[list[StatelessRuleGroupReference]] = None
    stateful_rule_group_references: Optional[list[StatefulRuleGroupReference]] = None
    enable_tls_session_holding: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    stateless_default_actions: Optional[Union[list[str], Ref]] = None
    stateful_engine_options: Optional[StatefulEngineOptions] = None
    stateless_custom_actions: Optional[list[CustomAction]] = None
    stateless_fragment_default_actions: Optional[Union[list[str], Ref]] = None
    policy_variables: Optional[PolicyVariables] = None
    stateful_default_actions: Optional[Union[list[str], Ref]] = None
    tls_inspection_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowTimeouts(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tcp_idle_timeout_seconds": "TcpIdleTimeoutSeconds",
    }

    tcp_idle_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IPSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
    }

    definition: Optional[Union[list[str], Ref]] = None


@dataclass
class PolicyVariables(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_variables": "RuleVariables",
    }

    rule_variables: Optional[dict[str, Any]] = None


@dataclass
class PublishMetricAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dimensions": "Dimensions",
    }

    dimensions: Optional[list[Dimension]] = None


@dataclass
class StatefulEngineOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_exception_policy": "StreamExceptionPolicy",
        "flow_timeouts": "FlowTimeouts",
        "rule_order": "RuleOrder",
    }

    stream_exception_policy: Optional[Union[str, StreamExceptionPolicy, Ref, GetAtt, Sub]] = None
    flow_timeouts: Optional[FlowTimeouts] = None
    rule_order: Optional[Union[str, RuleOrder, Ref, GetAtt, Sub]] = None


@dataclass
class StatefulRuleGroupOverride(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, OverrideAction, Ref, GetAtt, Sub]] = None


@dataclass
class StatefulRuleGroupReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "priority": "Priority",
        "override": "Override",
        "deep_threat_inspection": "DeepThreatInspection",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    override: Optional[StatefulRuleGroupOverride] = None
    deep_threat_inspection: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class StatelessRuleGroupReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "priority": "Priority",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None

