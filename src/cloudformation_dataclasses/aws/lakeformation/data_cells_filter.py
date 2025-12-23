"""PropertyTypes for AWS::LakeFormation::DataCellsFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ColumnWildcard(PropertyType):
    EXCLUDED_COLUMN_NAMES = "ExcludedColumnNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "excluded_column_names": "ExcludedColumnNames",
    }

    excluded_column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class RowFilter(PropertyType):
    ALL_ROWS_WILDCARD = "AllRowsWildcard"
    FILTER_EXPRESSION = "FilterExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_rows_wildcard": "AllRowsWildcard",
        "filter_expression": "FilterExpression",
    }

    all_rows_wildcard: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    filter_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None

