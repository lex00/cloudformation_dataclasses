"""PropertyTypes for AWS::CodeArtifact::PackageGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OriginConfiguration(PropertyType):
    RESTRICTIONS = "Restrictions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "restrictions": "Restrictions",
    }

    restrictions: Optional[Restrictions] = None


@dataclass
class RestrictionType(PropertyType):
    REPOSITORIES = "Repositories"
    RESTRICTION_MODE = "RestrictionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repositories": "Repositories",
        "restriction_mode": "RestrictionMode",
    }

    repositories: Optional[Union[list[str], Ref]] = None
    restriction_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Restrictions(PropertyType):
    EXTERNAL_UPSTREAM = "ExternalUpstream"
    PUBLISH = "Publish"
    INTERNAL_UPSTREAM = "InternalUpstream"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_upstream": "ExternalUpstream",
        "publish": "Publish",
        "internal_upstream": "InternalUpstream",
    }

    external_upstream: Optional[RestrictionType] = None
    publish: Optional[RestrictionType] = None
    internal_upstream: Optional[RestrictionType] = None

