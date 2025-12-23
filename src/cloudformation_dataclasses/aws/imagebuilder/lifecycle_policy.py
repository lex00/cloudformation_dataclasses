"""PropertyTypes for AWS::ImageBuilder::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    TYPE = "Type"
    INCLUDE_RESOURCES = "IncludeResources"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "include_resources": "IncludeResources",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    include_resources: Optional[IncludeResources] = None


@dataclass
class AmiExclusionRules(PropertyType):
    IS_PUBLIC = "IsPublic"
    LAST_LAUNCHED = "LastLaunched"
    REGIONS = "Regions"
    SHARED_ACCOUNTS = "SharedAccounts"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_public": "IsPublic",
        "last_launched": "LastLaunched",
        "regions": "Regions",
        "shared_accounts": "SharedAccounts",
        "tag_map": "TagMap",
    }

    is_public: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    last_launched: Optional[LastLaunched] = None
    regions: Optional[Union[list[str], Ref]] = None
    shared_accounts: Optional[Union[list[str], Ref]] = None
    tag_map: Optional[dict[str, str]] = None


@dataclass
class ExclusionRules(PropertyType):
    AMIS = "Amis"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "amis": "Amis",
        "tag_map": "TagMap",
    }

    amis: Optional[AmiExclusionRules] = None
    tag_map: Optional[dict[str, str]] = None


@dataclass
class Filter(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    RETAIN_AT_LEAST = "RetainAtLeast"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "retain_at_least": "RetainAtLeast",
        "unit": "Unit",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    retain_at_least: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IncludeResources(PropertyType):
    CONTAINERS = "Containers"
    AMIS = "Amis"
    SNAPSHOTS = "Snapshots"

    _property_mappings: ClassVar[dict[str, str]] = {
        "containers": "Containers",
        "amis": "Amis",
        "snapshots": "Snapshots",
    }

    containers: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    amis: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    snapshots: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LastLaunched(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDetail(PropertyType):
    ACTION = "Action"
    EXCLUSION_RULES = "ExclusionRules"
    FILTER = "Filter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "exclusion_rules": "ExclusionRules",
        "filter": "Filter",
    }

    action: Optional[Action] = None
    exclusion_rules: Optional[ExclusionRules] = None
    filter: Optional[Filter] = None


@dataclass
class RecipeSelection(PropertyType):
    NAME = "Name"
    SEMANTIC_VERSION = "SemanticVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "semantic_version": "SemanticVersion",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    semantic_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceSelection(PropertyType):
    RECIPES = "Recipes"
    TAG_MAP = "TagMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recipes": "Recipes",
        "tag_map": "TagMap",
    }

    recipes: Optional[list[RecipeSelection]] = None
    tag_map: Optional[dict[str, str]] = None

