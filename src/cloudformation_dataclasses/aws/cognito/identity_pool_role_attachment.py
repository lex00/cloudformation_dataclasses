"""PropertyTypes for AWS::Cognito::IdentityPoolRoleAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MappingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match_type": "MatchType",
        "value": "Value",
        "claim": "Claim",
        "role_arn": "RoleARN",
    }

    match_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    claim: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RoleMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "ambiguous_role_resolution": "AmbiguousRoleResolution",
        "rules_configuration": "RulesConfiguration",
        "identity_provider": "IdentityProvider",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ambiguous_role_resolution: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules_configuration: Optional[RulesConfigurationType] = None
    identity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RulesConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[MappingRule]] = None

