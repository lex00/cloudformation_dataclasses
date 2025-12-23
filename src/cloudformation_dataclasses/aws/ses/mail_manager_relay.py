"""PropertyTypes for AWS::SES::MailManagerRelay."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RelayAuthentication(PropertyType):
    SECRET_ARN = "SecretArn"
    NO_AUTHENTICATION = "NoAuthentication"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "no_authentication": "NoAuthentication",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    no_authentication: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

