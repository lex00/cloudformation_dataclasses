"""PropertyTypes for AWS::ResourceGroups::Group."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class GroupConfigurationStatus:
    """GroupConfigurationStatus enum values."""

    UPDATING = "UPDATING"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"


class GroupFilterName:
    """GroupFilterName enum values."""

    RESOURCE_TYPE = "resource-type"
    CONFIGURATION_TYPE = "configuration-type"
    OWNER = "owner"
    DISPLAY_NAME = "display-name"
    CRITICALITY = "criticality"


class GroupLifecycleEventsDesiredStatus:
    """GroupLifecycleEventsDesiredStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class GroupLifecycleEventsStatus:
    """GroupLifecycleEventsStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    IN_PROGRESS = "IN_PROGRESS"
    ERROR = "ERROR"


class GroupingStatus:
    """GroupingStatus enum values."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SKIPPED = "SKIPPED"


class GroupingType:
    """GroupingType enum values."""

    GROUP = "GROUP"
    UNGROUP = "UNGROUP"


class ListGroupingStatusesFilterName:
    """ListGroupingStatusesFilterName enum values."""

    STATUS = "status"
    RESOURCE_ARN = "resource-arn"


class QueryErrorCode:
    """QueryErrorCode enum values."""

    CLOUDFORMATION_STACK_INACTIVE = "CLOUDFORMATION_STACK_INACTIVE"
    CLOUDFORMATION_STACK_NOT_EXISTING = "CLOUDFORMATION_STACK_NOT_EXISTING"
    CLOUDFORMATION_STACK_UNASSUMABLE_ROLE = "CLOUDFORMATION_STACK_UNASSUMABLE_ROLE"
    RESOURCE_TYPE_NOT_SUPPORTED = "RESOURCE_TYPE_NOT_SUPPORTED"


class QueryType:
    """QueryType enum values."""

    TAG_FILTERS_1_0 = "TAG_FILTERS_1_0"
    CLOUDFORMATION_STACK_1_0 = "CLOUDFORMATION_STACK_1_0"


class ResourceFilterName:
    """ResourceFilterName enum values."""

    RESOURCE_TYPE = "resource-type"


class ResourceStatusValue:
    """ResourceStatusValue enum values."""

    PENDING = "PENDING"


class TagSyncTaskStatus:
    """TagSyncTaskStatus enum values."""

    ACTIVE = "ACTIVE"
    ERROR = "ERROR"


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

