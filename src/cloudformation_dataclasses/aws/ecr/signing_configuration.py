"""PropertyTypes for AWS::ECR::SigningConfiguration."""

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
class Rule(PropertyType):
    REPOSITORY_FILTERS = "RepositoryFilters"
    SIGNING_PROFILE_ARN = "SigningProfileArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repository_filters": "RepositoryFilters",
        "signing_profile_arn": "SigningProfileArn",
    }

    repository_filters: Optional[list[RepositoryFilter]] = None
    signing_profile_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

