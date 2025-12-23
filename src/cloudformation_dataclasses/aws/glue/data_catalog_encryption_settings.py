"""PropertyTypes for AWS::Glue::DataCatalogEncryptionSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionPasswordEncryption(PropertyType):
    RETURN_CONNECTION_PASSWORD_ENCRYPTED = "ReturnConnectionPasswordEncrypted"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "return_connection_password_encrypted": "ReturnConnectionPasswordEncrypted",
        "kms_key_id": "KmsKeyId",
    }

    return_connection_password_encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataCatalogEncryptionSettings(PropertyType):
    CONNECTION_PASSWORD_ENCRYPTION = "ConnectionPasswordEncryption"
    ENCRYPTION_AT_REST = "EncryptionAtRest"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_password_encryption": "ConnectionPasswordEncryption",
        "encryption_at_rest": "EncryptionAtRest",
    }

    connection_password_encryption: Optional[ConnectionPasswordEncryption] = None
    encryption_at_rest: Optional[EncryptionAtRest] = None


@dataclass
class EncryptionAtRest(PropertyType):
    CATALOG_ENCRYPTION_MODE = "CatalogEncryptionMode"
    CATALOG_ENCRYPTION_SERVICE_ROLE = "CatalogEncryptionServiceRole"
    SSE_AWS_KMS_KEY_ID = "SseAwsKmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_encryption_mode": "CatalogEncryptionMode",
        "catalog_encryption_service_role": "CatalogEncryptionServiceRole",
        "sse_aws_kms_key_id": "SseAwsKmsKeyId",
    }

    catalog_encryption_mode: Optional[Union[str, CatalogEncryptionMode, Ref, GetAtt, Sub]] = None
    catalog_encryption_service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_aws_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

