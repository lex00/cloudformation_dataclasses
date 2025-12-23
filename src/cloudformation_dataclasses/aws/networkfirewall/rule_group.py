"""PropertyTypes for AWS::NetworkFirewall::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionDefinition(PropertyType):
    PUBLISH_METRIC_ACTION = "PublishMetricAction"

    _property_mappings: ClassVar[dict[str, str]] = {
        "publish_metric_action": "PublishMetricAction",
    }

    publish_metric_action: Optional[PublishMetricAction] = None


@dataclass
class Address(PropertyType):
    ADDRESS_DEFINITION = "AddressDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address_definition": "AddressDefinition",
    }

    address_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomAction(PropertyType):
    ACTION_NAME = "ActionName"
    ACTION_DEFINITION = "ActionDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action_name": "ActionName",
        "action_definition": "ActionDefinition",
    }

    action_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action_definition: Optional[ActionDefinition] = None


@dataclass
class Dimension(PropertyType):
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Header(PropertyType):
    DESTINATION = "Destination"
    PROTOCOL = "Protocol"
    SOURCE_PORT = "SourcePort"
    DIRECTION = "Direction"
    DESTINATION_PORT = "DestinationPort"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "protocol": "Protocol",
        "source_port": "SourcePort",
        "direction": "Direction",
        "destination_port": "DestinationPort",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, StatefulRuleProtocol, Ref, GetAtt, Sub]] = None
    source_port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direction: Optional[Union[str, StatefulRuleDirection, Ref, GetAtt, Sub]] = None
    destination_port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IPSet(PropertyType):
    DEFINITION = "Definition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
    }

    definition: Optional[Union[list[str], Ref]] = None


@dataclass
class IPSetReference(PropertyType):
    REFERENCE_ARN = "ReferenceArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "reference_arn": "ReferenceArn",
    }

    reference_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MatchAttributes(PropertyType):
    PROTOCOLS = "Protocols"
    TCP_FLAGS = "TCPFlags"
    DESTINATION_PORTS = "DestinationPorts"
    DESTINATIONS = "Destinations"
    SOURCES = "Sources"
    SOURCE_PORTS = "SourcePorts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "protocols": "Protocols",
        "tcp_flags": "TCPFlags",
        "destination_ports": "DestinationPorts",
        "destinations": "Destinations",
        "sources": "Sources",
        "source_ports": "SourcePorts",
    }

    protocols: Optional[Union[list[int], Ref]] = None
    tcp_flags: Optional[list[TCPFlagField]] = None
    destination_ports: Optional[list[PortRange]] = None
    destinations: Optional[list[Address]] = None
    sources: Optional[list[Address]] = None
    source_ports: Optional[list[PortRange]] = None


@dataclass
class PortRange(PropertyType):
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PortSet(PropertyType):
    DEFINITION = "Definition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
    }

    definition: Optional[Union[list[str], Ref]] = None


@dataclass
class PublishMetricAction(PropertyType):
    DIMENSIONS = "Dimensions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimensions": "Dimensions",
    }

    dimensions: Optional[list[Dimension]] = None


@dataclass
class ReferenceSets(PropertyType):
    IP_SET_REFERENCES = "IPSetReferences"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_references": "IPSetReferences",
    }

    ip_set_references: Optional[dict[str, Any]] = None


@dataclass
class RuleDefinition(PropertyType):
    ACTIONS = "Actions"
    MATCH_ATTRIBUTES = "MatchAttributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "match_attributes": "MatchAttributes",
    }

    actions: Optional[Union[list[str], Ref]] = None
    match_attributes: Optional[MatchAttributes] = None


@dataclass
class RuleGroup(PropertyType):
    STATEFUL_RULE_OPTIONS = "StatefulRuleOptions"
    REFERENCE_SETS = "ReferenceSets"
    RULES_SOURCE = "RulesSource"
    RULE_VARIABLES = "RuleVariables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stateful_rule_options": "StatefulRuleOptions",
        "reference_sets": "ReferenceSets",
        "rules_source": "RulesSource",
        "rule_variables": "RuleVariables",
    }

    stateful_rule_options: Optional[StatefulRuleOptions] = None
    reference_sets: Optional[ReferenceSets] = None
    rules_source: Optional[RulesSource] = None
    rule_variables: Optional[RuleVariables] = None


@dataclass
class RuleOption(PropertyType):
    KEYWORD = "Keyword"
    SETTINGS = "Settings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "keyword": "Keyword",
        "settings": "Settings",
    }

    keyword: Optional[Union[str, Ref, GetAtt, Sub]] = None
    settings: Optional[Union[list[str], Ref]] = None


@dataclass
class RuleVariables(PropertyType):
    PORT_SETS = "PortSets"
    IP_SETS = "IPSets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port_sets": "PortSets",
        "ip_sets": "IPSets",
    }

    port_sets: Optional[dict[str, Any]] = None
    ip_sets: Optional[dict[str, Any]] = None


@dataclass
class RulesSource(PropertyType):
    STATELESS_RULES_AND_CUSTOM_ACTIONS = "StatelessRulesAndCustomActions"
    STATEFUL_RULES = "StatefulRules"
    RULES_STRING = "RulesString"
    RULES_SOURCE_LIST = "RulesSourceList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stateless_rules_and_custom_actions": "StatelessRulesAndCustomActions",
        "stateful_rules": "StatefulRules",
        "rules_string": "RulesString",
        "rules_source_list": "RulesSourceList",
    }

    stateless_rules_and_custom_actions: Optional[StatelessRulesAndCustomActions] = None
    stateful_rules: Optional[list[StatefulRule]] = None
    rules_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules_source_list: Optional[RulesSourceList] = None


@dataclass
class RulesSourceList(PropertyType):
    GENERATED_RULES_TYPE = "GeneratedRulesType"
    TARGET_TYPES = "TargetTypes"
    TARGETS = "Targets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "generated_rules_type": "GeneratedRulesType",
        "target_types": "TargetTypes",
        "targets": "Targets",
    }

    generated_rules_type: Optional[Union[str, GeneratedRulesType, Ref, GetAtt, Sub]] = None
    target_types: Optional[Union[list[str], Ref]] = None
    targets: Optional[Union[list[str], Ref]] = None


@dataclass
class StatefulRule(PropertyType):
    ACTION = "Action"
    HEADER = "Header"
    RULE_OPTIONS = "RuleOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "header": "Header",
        "rule_options": "RuleOptions",
    }

    action: Optional[Union[str, StatefulAction, Ref, GetAtt, Sub]] = None
    header: Optional[Header] = None
    rule_options: Optional[list[RuleOption]] = None


@dataclass
class StatefulRuleOptions(PropertyType):
    RULE_ORDER = "RuleOrder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_order": "RuleOrder",
    }

    rule_order: Optional[Union[str, RuleOrder, Ref, GetAtt, Sub]] = None


@dataclass
class StatelessRule(PropertyType):
    PRIORITY = "Priority"
    RULE_DEFINITION = "RuleDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "priority": "Priority",
        "rule_definition": "RuleDefinition",
    }

    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rule_definition: Optional[RuleDefinition] = None


@dataclass
class StatelessRulesAndCustomActions(PropertyType):
    STATELESS_RULES = "StatelessRules"
    CUSTOM_ACTIONS = "CustomActions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stateless_rules": "StatelessRules",
        "custom_actions": "CustomActions",
    }

    stateless_rules: Optional[list[StatelessRule]] = None
    custom_actions: Optional[list[CustomAction]] = None


@dataclass
class SummaryConfiguration(PropertyType):
    RULE_OPTIONS = "RuleOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rule_options": "RuleOptions",
    }

    rule_options: Optional[Union[list[str], Ref]] = None


@dataclass
class TCPFlagField(PropertyType):
    FLAGS = "Flags"
    MASKS = "Masks"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flags": "Flags",
        "masks": "Masks",
    }

    flags: Optional[Union[list[str], Ref]] = None
    masks: Optional[Union[list[str], Ref]] = None

