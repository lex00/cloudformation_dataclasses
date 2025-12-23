"""PropertyTypes for AWS::ElasticLoadBalancingV2::TrustStoreRevocation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RevocationContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_object_version": "S3ObjectVersion",
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
        "revocation_type": "RevocationType",
    }

    s3_object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revocation_type: Optional[Union[str, RevocationType, Ref, GetAtt, Sub]] = None


@dataclass
class TrustStoreRevocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "number_of_revoked_entries": "NumberOfRevokedEntries",
        "trust_store_arn": "TrustStoreArn",
        "revocation_type": "RevocationType",
        "revocation_id": "RevocationId",
    }

    number_of_revoked_entries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    trust_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revocation_type: Optional[Union[str, RevocationType, Ref, GetAtt, Sub]] = None
    revocation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

