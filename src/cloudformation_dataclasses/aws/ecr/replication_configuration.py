"""PropertyTypes for AWS::ECR::ReplicationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ReplicationConfiguration(PropertyType):
    RULES = "Rules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[ReplicationRule]] = None


@dataclass
class ReplicationDestination(PropertyType):
    REGION = "Region"
    REGISTRY_ID = "RegistryId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
        "registry_id": "RegistryId",
    }

    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    registry_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationRule(PropertyType):
    REPOSITORY_FILTERS = "RepositoryFilters"
    DESTINATIONS = "Destinations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_filters": "RepositoryFilters",
        "destinations": "Destinations",
    }

    repository_filters: Optional[list[RepositoryFilter]] = None
    destinations: Optional[list[ReplicationDestination]] = None


@dataclass
class RepositoryFilter(PropertyType):
    FILTER_TYPE = "FilterType"
    FILTER = "Filter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_type": "FilterType",
        "filter": "Filter",
    }

    filter_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter: Optional[Union[str, Ref, GetAtt, Sub]] = None

