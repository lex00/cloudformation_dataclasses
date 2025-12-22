"""PropertyTypes for AWS::PaymentCryptography::Key."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class KeyAttributes(PropertyType):
    KEY_CLASS = "KeyClass"
    KEY_USAGE = "KeyUsage"
    KEY_MODES_OF_USE = "KeyModesOfUse"
    KEY_ALGORITHM = "KeyAlgorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_class": "KeyClass",
        "key_usage": "KeyUsage",
        "key_modes_of_use": "KeyModesOfUse",
        "key_algorithm": "KeyAlgorithm",
    }

    key_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_usage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_modes_of_use: Optional[KeyModesOfUse] = None
    key_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyModesOfUse(PropertyType):
    UNWRAP = "Unwrap"
    WRAP = "Wrap"
    DECRYPT = "Decrypt"
    NO_RESTRICTIONS = "NoRestrictions"
    GENERATE = "Generate"
    SIGN = "Sign"
    VERIFY = "Verify"
    DERIVE_KEY = "DeriveKey"
    ENCRYPT = "Encrypt"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unwrap": "Unwrap",
        "wrap": "Wrap",
        "decrypt": "Decrypt",
        "no_restrictions": "NoRestrictions",
        "generate": "Generate",
        "sign": "Sign",
        "verify": "Verify",
        "derive_key": "DeriveKey",
        "encrypt": "Encrypt",
    }

    unwrap: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    wrap: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    decrypt: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    no_restrictions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    generate: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sign: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    verify: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    derive_key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    encrypt: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationStatusType(PropertyType):
    STATUS = "Status"
    STATUS_MESSAGE = "StatusMessage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "status_message": "StatusMessage",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_message: Optional[Union[str, Ref, GetAtt, Sub]] = None

