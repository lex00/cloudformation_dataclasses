"""PropertyTypes for AWS::SecretsManager::Secret."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GenerateSecretString(PropertyType):
    EXCLUDE_UPPERCASE = "ExcludeUppercase"
    REQUIRE_EACH_INCLUDED_TYPE = "RequireEachIncludedType"
    INCLUDE_SPACE = "IncludeSpace"
    EXCLUDE_CHARACTERS = "ExcludeCharacters"
    GENERATE_STRING_KEY = "GenerateStringKey"
    PASSWORD_LENGTH = "PasswordLength"
    EXCLUDE_PUNCTUATION = "ExcludePunctuation"
    EXCLUDE_LOWERCASE = "ExcludeLowercase"
    SECRET_STRING_TEMPLATE = "SecretStringTemplate"
    EXCLUDE_NUMBERS = "ExcludeNumbers"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude_uppercase": "ExcludeUppercase",
        "require_each_included_type": "RequireEachIncludedType",
        "include_space": "IncludeSpace",
        "exclude_characters": "ExcludeCharacters",
        "generate_string_key": "GenerateStringKey",
        "password_length": "PasswordLength",
        "exclude_punctuation": "ExcludePunctuation",
        "exclude_lowercase": "ExcludeLowercase",
        "secret_string_template": "SecretStringTemplate",
        "exclude_numbers": "ExcludeNumbers",
    }

    exclude_uppercase: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    require_each_included_type: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include_space: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclude_characters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    generate_string_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_length: Optional[Union[int, Ref, GetAtt, Sub]] = None
    exclude_punctuation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclude_lowercase: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    secret_string_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_numbers: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaRegion(PropertyType):
    KMS_KEY_ID = "KmsKeyId"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_id": "KmsKeyId",
        "region": "Region",
    }

    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None

