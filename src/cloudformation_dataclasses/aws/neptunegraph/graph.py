"""PropertyTypes for AWS::NeptuneGraph::Graph."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class VectorSearchConfiguration(PropertyType):
    VECTOR_SEARCH_DIMENSION = "VectorSearchDimension"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vector_search_dimension": "VectorSearchDimension",
    }

    vector_search_dimension: Optional[Union[int, Ref, GetAtt, Sub]] = None

