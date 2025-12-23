"""PropertyTypes for AWS::RolesAnywhere::Profile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeMapping(PropertyType):
    MAPPING_RULES = "MappingRules"
    CERTIFICATE_FIELD = "CertificateField"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping_rules": "MappingRules",
        "certificate_field": "CertificateField",
    }

    mapping_rules: Optional[list[MappingRule]] = None
    certificate_field: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MappingRule(PropertyType):
    SPECIFIER = "Specifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "specifier": "Specifier",
    }

    specifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

