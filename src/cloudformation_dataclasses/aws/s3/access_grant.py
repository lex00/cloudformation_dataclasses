"""PropertyTypes for AWS::S3::AccessGrant."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessGrantsLocationConfiguration(PropertyType):
    S3_SUB_PREFIX = "S3SubPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_sub_prefix": "S3SubPrefix",
    }

    s3_sub_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Grantee(PropertyType):
    GRANTEE_TYPE = "GranteeType"
    GRANTEE_IDENTIFIER = "GranteeIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "grantee_type": "GranteeType",
        "grantee_identifier": "GranteeIdentifier",
    }

    grantee_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grantee_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

