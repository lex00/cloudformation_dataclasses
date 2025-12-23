"""PropertyTypes for AWS::Backup::BackupSelection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BackupSelectionResourceType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "list_of_tags": "ListOfTags",
        "not_resources": "NotResources",
        "selection_name": "SelectionName",
        "iam_role_arn": "IamRoleArn",
        "resources": "Resources",
        "conditions": "Conditions",
    }

    list_of_tags: Optional[list[ConditionResourceType]] = None
    not_resources: Optional[Union[list[str], Ref]] = None
    selection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resources: Optional[Union[list[str], Ref]] = None
    conditions: Optional[Conditions] = None


@dataclass
class ConditionParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_value": "ConditionValue",
        "condition_key": "ConditionKey",
    }

    condition_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionResourceType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_value": "ConditionValue",
        "condition_key": "ConditionKey",
        "condition_type": "ConditionType",
    }

    condition_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Conditions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "string_equals": "StringEquals",
        "string_not_like": "StringNotLike",
        "string_like": "StringLike",
        "string_not_equals": "StringNotEquals",
    }

    string_equals: Optional[list[ConditionParameter]] = None
    string_not_like: Optional[list[ConditionParameter]] = None
    string_like: Optional[list[ConditionParameter]] = None
    string_not_equals: Optional[list[ConditionParameter]] = None

