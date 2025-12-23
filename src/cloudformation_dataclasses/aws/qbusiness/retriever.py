"""PropertyTypes for AWS::QBusiness::Retriever."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class KendraIndexConfiguration(PropertyType):
    INDEX_ID = "IndexId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_id": "IndexId",
    }

    index_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NativeIndexConfiguration(PropertyType):
    INDEX_ID = "IndexId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index_id": "IndexId",
    }

    index_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetrieverConfiguration(PropertyType):
    KENDRA_INDEX_CONFIGURATION = "KendraIndexConfiguration"
    NATIVE_INDEX_CONFIGURATION = "NativeIndexConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kendra_index_configuration": "KendraIndexConfiguration",
        "native_index_configuration": "NativeIndexConfiguration",
    }

    kendra_index_configuration: Optional[KendraIndexConfiguration] = None
    native_index_configuration: Optional[NativeIndexConfiguration] = None

