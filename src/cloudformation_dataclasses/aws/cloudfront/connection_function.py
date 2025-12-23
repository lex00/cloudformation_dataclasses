"""PropertyTypes for AWS::CloudFront::ConnectionFunction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionFunctionConfig(PropertyType):
    COMMENT = "Comment"
    RUNTIME = "Runtime"
    KEY_VALUE_STORE_ASSOCIATIONS = "KeyValueStoreAssociations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "runtime": "Runtime",
        "key_value_store_associations": "KeyValueStoreAssociations",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_value_store_associations: Optional[list[KeyValueStoreAssociation]] = None


@dataclass
class KeyValueStoreAssociation(PropertyType):
    KEY_VALUE_STORE_ARN = "KeyValueStoreARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_value_store_arn": "KeyValueStoreARN",
    }

    key_value_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

