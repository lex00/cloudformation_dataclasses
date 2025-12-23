"""PropertyTypes for AWS::QBusiness::Index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DocumentAttributeConfiguration(PropertyType):
    TYPE = "Type"
    SEARCH = "Search"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "search": "Search",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    search: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IndexCapacityConfiguration(PropertyType):
    UNITS = "Units"

    _property_mappings: ClassVar[dict[str, str]] = {
        "units": "Units",
    }

    units: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class IndexStatistics(PropertyType):
    TEXT_DOCUMENT_STATISTICS = "TextDocumentStatistics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text_document_statistics": "TextDocumentStatistics",
    }

    text_document_statistics: Optional[TextDocumentStatistics] = None


@dataclass
class TextDocumentStatistics(PropertyType):
    INDEXED_TEXT_BYTES = "IndexedTextBytes"
    INDEXED_TEXT_DOCUMENT_COUNT = "IndexedTextDocumentCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "indexed_text_bytes": "IndexedTextBytes",
        "indexed_text_document_count": "IndexedTextDocumentCount",
    }

    indexed_text_bytes: Optional[Union[float, Ref, GetAtt, Sub]] = None
    indexed_text_document_count: Optional[Union[float, Ref, GetAtt, Sub]] = None

