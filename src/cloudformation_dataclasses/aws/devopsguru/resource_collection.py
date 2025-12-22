"""PropertyTypes for AWS::DevOpsGuru::ResourceCollection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudFormationCollectionFilter(PropertyType):
    STACK_NAMES = "StackNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stack_names": "StackNames",
    }

    stack_names: Optional[Union[list[str], Ref]] = None


@dataclass
class ResourceCollectionFilter(PropertyType):
    CLOUD_FORMATION = "CloudFormation"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_formation": "CloudFormation",
        "tags": "Tags",
    }

    cloud_formation: Optional[CloudFormationCollectionFilter] = None
    tags: Optional[list[TagCollection]] = None


@dataclass
class TagCollection(PropertyType):
    APP_BOUNDARY_KEY = "AppBoundaryKey"
    TAG_VALUES = "TagValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_boundary_key": "AppBoundaryKey",
        "tag_values": "TagValues",
    }

    app_boundary_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_values: Optional[Union[list[str], Ref]] = None

