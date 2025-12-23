"""PropertyTypes for AWS::EMR::Step."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HadoopJarStepConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "args": "Args",
        "main_class": "MainClass",
        "step_properties": "StepProperties",
        "jar": "Jar",
    }

    args: Optional[Union[list[str], Ref]] = None
    main_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    step_properties: Optional[list[KeyValue]] = None
    jar: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

