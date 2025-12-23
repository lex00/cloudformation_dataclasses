"""PropertyTypes for AWS::CloudFormation::LambdaHook."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HookTarget(PropertyType):
    INVOCATION_POINT = "InvocationPoint"
    ACTION = "Action"
    TARGET_NAME = "TargetName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invocation_point": "InvocationPoint",
        "action": "Action",
        "target_name": "TargetName",
    }

    invocation_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    action: Optional[Union[str, HookTargetAction, Ref, GetAtt, Sub]] = None
    target_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StackFilters(PropertyType):
    FILTERING_CRITERIA = "FilteringCriteria"
    STACK_NAMES = "StackNames"
    STACK_ROLES = "StackRoles"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filtering_criteria": "FilteringCriteria",
        "stack_names": "StackNames",
        "stack_roles": "StackRoles",
    }

    filtering_criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stack_names: Optional[StackNames] = None
    stack_roles: Optional[StackRoles] = None


@dataclass
class StackNames(PropertyType):
    EXCLUDE = "Exclude"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class StackRoles(PropertyType):
    EXCLUDE = "Exclude"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class TargetFilters(PropertyType):
    ACTIONS = "Actions"
    TARGET_NAMES = "TargetNames"
    TARGETS = "Targets"
    INVOCATION_POINTS = "InvocationPoints"

    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "target_names": "TargetNames",
        "targets": "Targets",
        "invocation_points": "InvocationPoints",
    }

    actions: Optional[Union[list[str], Ref]] = None
    target_names: Optional[Union[list[str], Ref]] = None
    targets: Optional[list[HookTarget]] = None
    invocation_points: Optional[Union[list[str], Ref]] = None

