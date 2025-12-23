"""PropertyTypes for AWS::S3::StorageLensGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class And(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_object_age": "MatchObjectAge",
        "match_any_prefix": "MatchAnyPrefix",
        "match_any_tag": "MatchAnyTag",
        "match_any_suffix": "MatchAnySuffix",
        "match_object_size": "MatchObjectSize",
    }

    match_object_age: Optional[MatchObjectAge] = None
    match_any_prefix: Optional[Union[list[str], Ref]] = None
    match_any_tag: Optional[list[Tag]] = None
    match_any_suffix: Optional[Union[list[str], Ref]] = None
    match_object_size: Optional[MatchObjectSize] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_object_age": "MatchObjectAge",
        "or_": "Or",
        "and_": "And",
        "match_any_prefix": "MatchAnyPrefix",
        "match_any_tag": "MatchAnyTag",
        "match_any_suffix": "MatchAnySuffix",
        "match_object_size": "MatchObjectSize",
    }

    match_object_age: Optional[MatchObjectAge] = None
    or_: Optional[Or] = None
    and_: Optional[And] = None
    match_any_prefix: Optional[Union[list[str], Ref]] = None
    match_any_tag: Optional[list[Tag]] = None
    match_any_suffix: Optional[Union[list[str], Ref]] = None
    match_object_size: Optional[MatchObjectSize] = None


@dataclass
class MatchObjectAge(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days_less_than": "DaysLessThan",
        "days_greater_than": "DaysGreaterThan",
    }

    days_less_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    days_greater_than: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MatchObjectSize(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bytes_less_than": "BytesLessThan",
        "bytes_greater_than": "BytesGreaterThan",
    }

    bytes_less_than: Optional[Union[int, Ref, GetAtt, Sub]] = None
    bytes_greater_than: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Or(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_object_age": "MatchObjectAge",
        "match_any_prefix": "MatchAnyPrefix",
        "match_any_tag": "MatchAnyTag",
        "match_any_suffix": "MatchAnySuffix",
        "match_object_size": "MatchObjectSize",
    }

    match_object_age: Optional[MatchObjectAge] = None
    match_any_prefix: Optional[Union[list[str], Ref]] = None
    match_any_tag: Optional[list[Tag]] = None
    match_any_suffix: Optional[Union[list[str], Ref]] = None
    match_object_size: Optional[MatchObjectSize] = None

