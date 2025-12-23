"""PropertyTypes for AWS::MediaPackage::PackagingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Authorization(PropertyType):
    SECRETS_ROLE_ARN = "SecretsRoleArn"
    CDN_IDENTIFIER_SECRET = "CdnIdentifierSecret"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_role_arn": "SecretsRoleArn",
        "cdn_identifier_secret": "CdnIdentifierSecret",
    }

    secrets_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdn_identifier_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfiguration(PropertyType):
    LOG_GROUP_NAME = "LogGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_name": "LogGroupName",
    }

    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

