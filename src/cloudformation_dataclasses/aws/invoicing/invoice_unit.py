"""PropertyTypes for AWS::Invoicing::InvoiceUnit."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ResourceTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    LINKED_ACCOUNTS = "LinkedAccounts"

    _property_mappings: ClassVar[dict[str, str]] = {
        "linked_accounts": "LinkedAccounts",
    }

    linked_accounts: Optional[Union[list[str], Ref]] = None

