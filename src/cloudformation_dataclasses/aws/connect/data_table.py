"""PropertyTypes for AWS::Connect::DataTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LockVersion(PropertyType):
    DATA_TABLE = "DataTable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_table": "DataTable",
    }

    data_table: Optional[Union[str, Ref, GetAtt, Sub]] = None

