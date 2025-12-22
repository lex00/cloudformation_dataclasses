"""PropertyTypes for AWS::Signer::SigningProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Category:
    """Category enum values."""

    AWSIOT = "AWSIoT"


class EncryptionAlgorithm:
    """EncryptionAlgorithm enum values."""

    RSA = "RSA"
    ECDSA = "ECDSA"


class HashAlgorithm:
    """HashAlgorithm enum values."""

    SHA1 = "SHA1"
    SHA256 = "SHA256"


class ImageFormat:
    """ImageFormat enum values."""

    JSON = "JSON"
    JSONEMBEDDED = "JSONEmbedded"
    JSONDETACHED = "JSONDetached"


class SigningProfileStatus:
    """SigningProfileStatus enum values."""

    ACTIVE = "Active"
    CANCELED = "Canceled"
    REVOKED = "Revoked"


class SigningStatus:
    """SigningStatus enum values."""

    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class ValidityType:
    """ValidityType enum values."""

    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"


@dataclass
class SignatureValidityPeriod(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None

