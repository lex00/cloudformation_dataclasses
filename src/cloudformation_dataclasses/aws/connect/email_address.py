"""PropertyTypes for AWS::Connect::EmailAddress."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AliasConfiguration(PropertyType):
    EMAIL_ADDRESS_ARN = "EmailAddressArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_address_arn": "EmailAddressArn",
    }

    email_address_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

