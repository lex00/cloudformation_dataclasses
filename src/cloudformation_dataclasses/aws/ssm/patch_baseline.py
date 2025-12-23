"""PropertyTypes for AWS::SSM::PatchBaseline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PatchFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, PatchFilterKey, Ref, GetAtt, Sub]] = None


@dataclass
class PatchFilterGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "patch_filters": "PatchFilters",
    }

    patch_filters: Optional[list[PatchFilter]] = None


@dataclass
class PatchSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "products": "Products",
        "configuration": "Configuration",
        "name": "Name",
    }

    products: Optional[Union[list[str], Ref]] = None
    configuration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "approve_until_date": "ApproveUntilDate",
        "enable_non_security": "EnableNonSecurity",
        "patch_filter_group": "PatchFilterGroup",
        "approve_after_days": "ApproveAfterDays",
        "compliance_level": "ComplianceLevel",
    }

    approve_until_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_non_security: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    patch_filter_group: Optional[PatchFilterGroup] = None
    approve_after_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    compliance_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RuleGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "patch_rules": "PatchRules",
    }

    patch_rules: Optional[list[Rule]] = None

