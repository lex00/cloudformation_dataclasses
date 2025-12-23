"""PropertyTypes for AWS::ElastiCache::ServerlessCache."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CacheUsageLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_storage": "DataStorage",
        "ecpu_per_second": "ECPUPerSecond",
    }

    data_storage: Optional[DataStorage] = None
    ecpu_per_second: Optional[ECPUPerSecond] = None


@dataclass
class DataStorage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
        "unit": "Unit",
    }

    minimum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DataStorageUnit, Ref, GetAtt, Sub]] = None


@dataclass
class ECPUPerSecond(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
    }

    minimum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None

