"""PropertyTypes for AWS::DSQL::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ClusterStatus:
    """ClusterStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    IDLE = "IDLE"
    INACTIVE = "INACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    PENDING_SETUP = "PENDING_SETUP"
    PENDING_DELETE = "PENDING_DELETE"


class EncryptionStatus:
    """EncryptionStatus enum values."""

    ENABLED = "ENABLED"
    UPDATING = "UPDATING"
    KMS_KEY_INACCESSIBLE = "KMS_KEY_INACCESSIBLE"
    ENABLING = "ENABLING"


class EncryptionType:
    """EncryptionType enum values."""

    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"
    CUSTOMER_MANAGED_KMS_KEY = "CUSTOMER_MANAGED_KMS_KEY"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    DELETIONPROTECTIONENABLED = "deletionProtectionEnabled"
    OTHER = "other"


@dataclass
class EncryptionDetails(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"
    ENCRYPTION_STATUS = "EncryptionStatus"
    KMS_KEY_ARN = "KmsKeyArn"

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
    CLUSTERS = "Clusters"
    WITNESS_REGION = "WitnessRegion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "clusters": "Clusters",
        "witness_region": "WitnessRegion",
    }

    clusters: Optional[Union[list[str], Ref]] = None
    witness_region: Optional[Union[str, Ref, GetAtt, Sub]] = None

