"""PropertyTypes for AWS::ECR::RegistryScanningConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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


@dataclass
class ScanningRule(PropertyType):
    REPOSITORY_FILTERS = "RepositoryFilters"
    SCAN_FREQUENCY = "ScanFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_filters": "RepositoryFilters",
        "scan_frequency": "ScanFrequency",
    }

    repository_filters: Optional[list[RepositoryFilter]] = None
    scan_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None

