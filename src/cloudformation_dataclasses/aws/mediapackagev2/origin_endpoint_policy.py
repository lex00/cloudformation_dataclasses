"""PropertyTypes for AWS::MediaPackageV2::OriginEndpointPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CdnAuthConfiguration(PropertyType):
    SECRETS_ROLE_ARN = "SecretsRoleArn"
    CDN_IDENTIFIER_SECRET_ARNS = "CdnIdentifierSecretArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_role_arn": "SecretsRoleArn",
        "cdn_identifier_secret_arns": "CdnIdentifierSecretArns",
    }

    secrets_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdn_identifier_secret_arns: Optional[Union[list[str], Ref]] = None

