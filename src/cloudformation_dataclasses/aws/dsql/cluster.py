"""PropertyTypes for AWS::DSQL::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EncryptionDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "encryption_status": "EncryptionStatus",
        "kms_key_arn": "KmsKeyArn",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MultiRegionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "clusters": "Clusters",
        "witness_region": "WitnessRegion",
    }

    clusters: Optional[Union[list[str], Ref]] = None
    witness_region: Optional[Union[str, Ref, GetAtt, Sub]] = None

