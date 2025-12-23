"""PropertyTypes for AWS::Connect::UserHierarchyStructure."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LevelFive(PropertyType):
    HIERARCHY_LEVEL_ID = "HierarchyLevelId"
    HIERARCHY_LEVEL_ARN = "HierarchyLevelArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_level_id": "HierarchyLevelId",
        "hierarchy_level_arn": "HierarchyLevelArn",
        "name": "Name",
    }

    hierarchy_level_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_level_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LevelFour(PropertyType):
    HIERARCHY_LEVEL_ID = "HierarchyLevelId"
    HIERARCHY_LEVEL_ARN = "HierarchyLevelArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_level_id": "HierarchyLevelId",
        "hierarchy_level_arn": "HierarchyLevelArn",
        "name": "Name",
    }

    hierarchy_level_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_level_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LevelOne(PropertyType):
    HIERARCHY_LEVEL_ID = "HierarchyLevelId"
    HIERARCHY_LEVEL_ARN = "HierarchyLevelArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_level_id": "HierarchyLevelId",
        "hierarchy_level_arn": "HierarchyLevelArn",
        "name": "Name",
    }

    hierarchy_level_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_level_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LevelThree(PropertyType):
    HIERARCHY_LEVEL_ID = "HierarchyLevelId"
    HIERARCHY_LEVEL_ARN = "HierarchyLevelArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_level_id": "HierarchyLevelId",
        "hierarchy_level_arn": "HierarchyLevelArn",
        "name": "Name",
    }

    hierarchy_level_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_level_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LevelTwo(PropertyType):
    HIERARCHY_LEVEL_ID = "HierarchyLevelId"
    HIERARCHY_LEVEL_ARN = "HierarchyLevelArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hierarchy_level_id": "HierarchyLevelId",
        "hierarchy_level_arn": "HierarchyLevelArn",
        "name": "Name",
    }

    hierarchy_level_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hierarchy_level_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserHierarchyStructure(PropertyType):
    LEVEL_THREE = "LevelThree"
    LEVEL_TWO = "LevelTwo"
    LEVEL_FIVE = "LevelFive"
    LEVEL_FOUR = "LevelFour"
    LEVEL_ONE = "LevelOne"

    _property_mappings: ClassVar[dict[str, str]] = {
        "level_three": "LevelThree",
        "level_two": "LevelTwo",
        "level_five": "LevelFive",
        "level_four": "LevelFour",
        "level_one": "LevelOne",
    }

    level_three: Optional[LevelThree] = None
    level_two: Optional[LevelTwo] = None
    level_five: Optional[LevelFive] = None
    level_four: Optional[LevelFour] = None
    level_one: Optional[LevelOne] = None

