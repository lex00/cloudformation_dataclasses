"""PropertyTypes for AWS::Budgets::BudgetsAction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionThreshold(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Definition(PropertyType):
    SSM_ACTION_DEFINITION = "SsmActionDefinition"
    IAM_ACTION_DEFINITION = "IamActionDefinition"
    SCP_ACTION_DEFINITION = "ScpActionDefinition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssm_action_definition": "SsmActionDefinition",
        "iam_action_definition": "IamActionDefinition",
        "scp_action_definition": "ScpActionDefinition",
    }

    ssm_action_definition: Optional[SsmActionDefinition] = None
    iam_action_definition: Optional[IamActionDefinition] = None
    scp_action_definition: Optional[ScpActionDefinition] = None


@dataclass
class IamActionDefinition(PropertyType):
    POLICY_ARN = "PolicyArn"
    GROUPS = "Groups"
    ROLES = "Roles"
    USERS = "Users"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_arn": "PolicyArn",
        "groups": "Groups",
        "roles": "Roles",
        "users": "Users",
    }

    policy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    groups: Optional[Union[list[str], Ref]] = None
    roles: Optional[Union[list[str], Ref]] = None
    users: Optional[Union[list[str], Ref]] = None


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScpActionDefinition(PropertyType):
    TARGET_IDS = "TargetIds"
    POLICY_ID = "PolicyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_ids": "TargetIds",
        "policy_id": "PolicyId",
    }

    target_ids: Optional[Union[list[str], Ref]] = None
    policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsmActionDefinition(PropertyType):
    REGION = "Region"
    INSTANCE_IDS = "InstanceIds"
    SUBTYPE = "Subtype"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
        "instance_ids": "InstanceIds",
        "subtype": "Subtype",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_ids: Optional[Union[list[str], Ref]] = None
    subtype: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Subscriber(PropertyType):
    TYPE = "Type"
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "address": "Address",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None

