"""PropertyTypes for AWS::VpcLattice::Rule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forward": "Forward",
        "fixed_response": "FixedResponse",
    }

    forward: Optional[Forward] = None
    fixed_response: Optional[FixedResponse] = None


@dataclass
class FixedResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status_code": "StatusCode",
    }

    status_code: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Forward(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_groups": "TargetGroups",
    }

    target_groups: Optional[list[WeightedTargetGroup]] = None


@dataclass
class HeaderMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "case_sensitive": "CaseSensitive",
        "name": "Name",
        "match": "Match",
    }

    case_sensitive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[HeaderMatchType] = None


@dataclass
class HeaderMatchType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contains": "Contains",
        "exact": "Exact",
        "prefix": "Prefix",
    }

    contains: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header_matches": "HeaderMatches",
        "path_match": "PathMatch",
        "method": "Method",
    }

    header_matches: Optional[list[HeaderMatch]] = None
    path_match: Optional[PathMatch] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Match(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_match": "HttpMatch",
    }

    http_match: Optional[HttpMatch] = None


@dataclass
class PathMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "case_sensitive": "CaseSensitive",
        "match": "Match",
    }

    case_sensitive: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    match: Optional[PathMatchType] = None


@dataclass
class PathMatchType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
        "prefix": "Prefix",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WeightedTargetGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "weight": "Weight",
        "target_group_identifier": "TargetGroupIdentifier",
    }

    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_group_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

