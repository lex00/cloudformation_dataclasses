"""PropertyTypes for AWS::EC2::VerifiedAccessGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SseSpecification(PropertyType):
    CUSTOMER_MANAGED_KEY_ENABLED = "CustomerManagedKeyEnabled"
    KMS_KEY_ARN = "KmsKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_key_enabled": "CustomerManagedKeyEnabled",
        "kms_key_arn": "KmsKeyArn",
    }

    customer_managed_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

