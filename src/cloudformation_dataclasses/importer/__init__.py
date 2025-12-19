"""CloudFormation template importer - convert YAML/JSON to Python dataclasses."""

from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRCondition,
    IRIntrinsic,
    IRMapping,
    IROutput,
    IRParameter,
    IRProperty,
    IRResource,
    IRTemplate,
)
from cloudformation_dataclasses.importer.parser import parse_template
from cloudformation_dataclasses.importer.codegen import generate_code

__all__ = [
    "IntrinsicType",
    "IRCondition",
    "IRIntrinsic",
    "IRMapping",
    "IROutput",
    "IRParameter",
    "IRProperty",
    "IRResource",
    "IRTemplate",
    "generate_code",
    "parse_template",
]
