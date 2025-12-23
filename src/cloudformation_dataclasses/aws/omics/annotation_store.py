"""PropertyTypes for AWS::Omics::AnnotationStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ReferenceItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "reference_arn": "ReferenceArn",
    }

    reference_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SseConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "key_arn": "KeyArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StoreOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tsv_store_options": "TsvStoreOptions",
    }

    tsv_store_options: Optional[TsvStoreOptions] = None


@dataclass
class TsvStoreOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schema": "Schema",
        "format_to_header": "FormatToHeader",
        "annotation_type": "AnnotationType",
    }

    schema: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    format_to_header: Optional[dict[str, str]] = None
    annotation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

