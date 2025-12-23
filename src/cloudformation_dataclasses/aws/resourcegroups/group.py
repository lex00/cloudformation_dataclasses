"""PropertyTypes for AWS::ResourceGroups::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationItem(PropertyType):
    TYPE = "Type"
    PARAMETERS = "Parameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "parameters": "Parameters",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[list[ConfigurationParameter]] = None


@dataclass
class ConfigurationParameter(PropertyType):
    VALUES = "Values"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Query(PropertyType):
    TAG_FILTERS = "TagFilters"
    RESOURCE_TYPE_FILTERS = "ResourceTypeFilters"
    STACK_IDENTIFIER = "StackIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_filters": "TagFilters",
        "resource_type_filters": "ResourceTypeFilters",
        "stack_identifier": "StackIdentifier",
    }

    tag_filters: Optional[list[TagFilter]] = None
    resource_type_filters: Optional[Union[list[str], Ref]] = None
    stack_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceQuery(PropertyType):
    TYPE = "Type"
    QUERY = "Query"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "query": "Query",
    }

    type_: Optional[Union[str, QueryType, Ref, GetAtt, Sub]] = None
    query: Optional[Query] = None


@dataclass
class TagFilter(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

