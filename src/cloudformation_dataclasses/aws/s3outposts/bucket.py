"""PropertyTypes for AWS::S3Outposts::Bucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days_after_initiation": "DaysAfterInitiation",
    }

    days_after_initiation: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "and_operator": "AndOperator",
        "prefix": "Prefix",
        "tag": "Tag",
    }

    and_operator: Optional[FilterAndOperator] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag: Optional[FilterTag] = None


@dataclass
class FilterAndOperator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix": "Prefix",
        "tags": "Tags",
    }

    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[FilterTag]] = None


@dataclass
class FilterTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[Rule]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "expiration_date": "ExpirationDate",
        "filter": "Filter",
        "expiration_in_days": "ExpirationInDays",
        "id": "Id",
        "abort_incomplete_multipart_upload": "AbortIncompleteMultipartUpload",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    expiration_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter: Optional[Filter] = None
    expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None

