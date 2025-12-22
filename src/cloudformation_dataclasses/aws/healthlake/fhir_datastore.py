"""PropertyTypes for AWS::HealthLake::FHIRDatastore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AuthorizationStrategy:
    """AuthorizationStrategy enum values."""

    SMART_ON_FHIR_V1 = "SMART_ON_FHIR_V1"
    SMART_ON_FHIR = "SMART_ON_FHIR"
    AWS_AUTH = "AWS_AUTH"


class CmkType:
    """CmkType enum values."""

    CUSTOMER_MANAGED_KMS_KEY = "CUSTOMER_MANAGED_KMS_KEY"
    AWS_OWNED_KMS_KEY = "AWS_OWNED_KMS_KEY"


class DatastoreStatus:
    """DatastoreStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    CREATE_FAILED = "CREATE_FAILED"


class ErrorCategory:
    """ErrorCategory enum values."""

    RETRYABLE_ERROR = "RETRYABLE_ERROR"
    NON_RETRYABLE_ERROR = "NON_RETRYABLE_ERROR"


class FHIRVersion:
    """FHIRVersion enum values."""

    R4 = "R4"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCEL_SUBMITTED = "CANCEL_SUBMITTED"
    CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
    CANCEL_COMPLETED = "CANCEL_COMPLETED"
    CANCEL_FAILED = "CANCEL_FAILED"


class PreloadDataType:
    """PreloadDataType enum values."""

    SYNTHEA = "SYNTHEA"


class ValidationLevel:
    """ValidationLevel enum values."""

    STRICT = "strict"
    STRUCTURE_ONLY = "structure-only"
    MINIMAL = "minimal"


@dataclass
class CreatedAt(PropertyType):
    NANOS = "Nanos"
    SECONDS = "Seconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nanos": "Nanos",
        "seconds": "Seconds",
    }

    nanos: Optional[Union[int, Ref, GetAtt, Sub]] = None
    seconds: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    AUTHORIZATION_STRATEGY = "AuthorizationStrategy"
    IDP_LAMBDA_ARN = "IdpLambdaArn"
    FINE_GRAINED_AUTHORIZATION_ENABLED = "FineGrainedAuthorizationEnabled"
    METADATA = "Metadata"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authorization_strategy": "AuthorizationStrategy",
        "idp_lambda_arn": "IdpLambdaArn",
        "fine_grained_authorization_enabled": "FineGrainedAuthorizationEnabled",
        "metadata": "Metadata",
    }

    authorization_strategy: Optional[Union[str, AuthorizationStrategy, Ref, GetAtt, Sub]] = None
    idp_lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fine_grained_authorization_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    metadata: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KmsEncryptionConfig(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    CMK_TYPE = "CmkType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "cmk_type": "CmkType",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cmk_type: Optional[Union[str, CmkType, Ref, GetAtt, Sub]] = None


@dataclass
class PreloadDataConfig(PropertyType):
    PRELOAD_DATA_TYPE = "PreloadDataType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "preload_data_type": "PreloadDataType",
    }

    preload_data_type: Optional[Union[str, PreloadDataType, Ref, GetAtt, Sub]] = None


@dataclass
class SseConfiguration(PropertyType):
    KMS_ENCRYPTION_CONFIG = "KmsEncryptionConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_encryption_config": "KmsEncryptionConfig",
    }

    kms_encryption_config: Optional[KmsEncryptionConfig] = None

