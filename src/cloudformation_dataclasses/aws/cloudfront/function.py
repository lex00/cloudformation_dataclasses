"""PropertyTypes for AWS::CloudFront::Function."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FunctionConfig(PropertyType):
    COMMENT = "Comment"
    RUNTIME = "Runtime"
    KEY_VALUE_STORE_ASSOCIATIONS = "KeyValueStoreAssociations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "runtime": "Runtime",
        "key_value_store_associations": "KeyValueStoreAssociations",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime: Optional[Union[str, FunctionRuntime, Ref, GetAtt, Sub]] = None
    key_value_store_associations: Optional[list[KeyValueStoreAssociation]] = None


@dataclass
class FunctionMetadata(PropertyType):
    FUNCTION_ARN = "FunctionARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionARN",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValueStoreAssociation(PropertyType):
    KEY_VALUE_STORE_ARN = "KeyValueStoreARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_value_store_arn": "KeyValueStoreARN",
    }

    key_value_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

