"""PropertyTypes for AWS::SSO::PermissionSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomerManagedPolicyReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "name": "Name",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PermissionsBoundary(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_policy_reference": "CustomerManagedPolicyReference",
        "managed_policy_arn": "ManagedPolicyArn",
    }

    customer_managed_policy_reference: Optional[CustomerManagedPolicyReference] = None
    managed_policy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

