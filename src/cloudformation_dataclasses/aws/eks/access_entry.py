"""PropertyTypes for AWS::EKS::AccessEntry."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_arn": "PolicyArn",
        "access_scope": "AccessScope",
    }

    policy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_scope: Optional[AccessScope] = None


@dataclass
class AccessScope(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "namespaces": "Namespaces",
        "type_": "Type",
    }

    namespaces: Optional[Union[list[str], Ref]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None

