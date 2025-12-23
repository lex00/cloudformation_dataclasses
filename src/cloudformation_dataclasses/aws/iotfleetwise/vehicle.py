"""PropertyTypes for AWS::IoTFleetWise::Vehicle."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PeriodicStateTemplateUpdateStrategy(PropertyType):
    STATE_TEMPLATE_UPDATE_RATE = "StateTemplateUpdateRate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state_template_update_rate": "StateTemplateUpdateRate",
    }

    state_template_update_rate: Optional[TimePeriod] = None


@dataclass
class StateTemplateAssociation(PropertyType):
    IDENTIFIER = "Identifier"
    STATE_TEMPLATE_UPDATE_STRATEGY = "StateTemplateUpdateStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "identifier": "Identifier",
        "state_template_update_strategy": "StateTemplateUpdateStrategy",
    }

    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state_template_update_strategy: Optional[StateTemplateUpdateStrategy] = None


@dataclass
class StateTemplateUpdateStrategy(PropertyType):
    ON_CHANGE = "OnChange"
    PERIODIC = "Periodic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "periodic": "Periodic",
    }

    on_change: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    periodic: Optional[PeriodicStateTemplateUpdateStrategy] = None


@dataclass
class TimePeriod(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None

