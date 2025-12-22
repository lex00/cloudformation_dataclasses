"""PropertyTypes for AWS::Billing::BillingView."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BillingViewStatus:
    """BillingViewStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    CREATING = "CREATING"
    UPDATING = "UPDATING"


class BillingViewStatusReason:
    """BillingViewStatusReason enum values."""

    SOURCE_VIEW_UNHEALTHY = "SOURCE_VIEW_UNHEALTHY"
    SOURCE_VIEW_UPDATING = "SOURCE_VIEW_UPDATING"
    SOURCE_VIEW_ACCESS_DENIED = "SOURCE_VIEW_ACCESS_DENIED"
    SOURCE_VIEW_NOT_FOUND = "SOURCE_VIEW_NOT_FOUND"
    CYCLIC_DEPENDENCY = "CYCLIC_DEPENDENCY"
    SOURCE_VIEW_DEPTH_EXCEEDED = "SOURCE_VIEW_DEPTH_EXCEEDED"
    AGGREGATE_SOURCE = "AGGREGATE_SOURCE"
    VIEW_OWNER_NOT_MANAGEMENT_ACCOUNT = "VIEW_OWNER_NOT_MANAGEMENT_ACCOUNT"


class BillingViewType:
    """BillingViewType enum values."""

    PRIMARY = "PRIMARY"
    BILLING_GROUP = "BILLING_GROUP"
    CUSTOM = "CUSTOM"
    BILLING_TRANSFER = "BILLING_TRANSFER"
    BILLING_TRANSFER_SHOWBACK = "BILLING_TRANSFER_SHOWBACK"


class Dimension:
    """Dimension enum values."""

    LINKED_ACCOUNT = "LINKED_ACCOUNT"


class SearchOption:
    """SearchOption enum values."""

    STARTS_WITH = "STARTS_WITH"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


@dataclass
class DataFilterExpression(PropertyType):
    DIMENSIONS = "Dimensions"
    TAGS = "Tags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimensions": "Dimensions",
        "tags": "Tags",
    }

    dimensions: Optional[Dimensions] = None
    tags: Optional[Tags] = None


@dataclass
class Dimensions(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

