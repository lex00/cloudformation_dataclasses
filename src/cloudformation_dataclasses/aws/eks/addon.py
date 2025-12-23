"""PropertyTypes for AWS::EKS::Addon."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NamespaceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "namespace": "Namespace",
    }

    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PodIdentityAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_account": "ServiceAccount",
        "role_arn": "RoleArn",
    }

    service_account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

