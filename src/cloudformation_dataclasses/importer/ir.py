"""Intermediate Representation for parsed CloudFormation templates."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional


class IntrinsicType(Enum):
    """CloudFormation intrinsic function types."""

    REF = "Ref"
    GET_ATT = "GetAtt"
    SUB = "Sub"
    JOIN = "Join"
    SELECT = "Select"
    GET_AZS = "GetAZs"
    IF = "If"
    EQUALS = "Equals"
    AND = "And"
    OR = "Or"
    NOT = "Not"
    CONDITION = "Condition"
    FIND_IN_MAP = "FindInMap"
    BASE64 = "Base64"
    CIDR = "Cidr"
    IMPORT_VALUE = "ImportValue"
    SPLIT = "Split"
    TRANSFORM = "Transform"
    VALUE_OF = "ValueOf"


@dataclass
class IRIntrinsic:
    """Parsed intrinsic function."""

    type: IntrinsicType
    args: Any
    # For Ref: str (logical_id)
    # For GetAtt: tuple[str, str] (logical_id, attribute)
    # For Sub: str or tuple[str, dict[str, Any]] (template, variables)
    # For Join: tuple[str, list[Any]] (delimiter, values)
    # For Select: tuple[int, Any] (index, list)
    # For If: tuple[str, Any, Any] (condition_name, true_value, false_value)
    # For Equals: tuple[Any, Any] (value1, value2)
    # For And/Or: list[Any] (conditions)
    # For Not: Any (condition)
    # For FindInMap: tuple[str, Any, Any] (map_name, top_key, second_key)
    # For Base64: Any (value to encode)
    # For Cidr: tuple[Any, int, int] (ip_block, count, cidr_bits)
    # For ImportValue: Any (export name)
    # For Split: tuple[str, Any] (delimiter, source)
    # For GetAZs: str (region, empty string for current)


@dataclass
class IRProperty:
    """A single property value (may contain intrinsics)."""

    cf_name: str  # Original CloudFormation name (PascalCase)
    python_name: str  # Converted name (snake_case)
    value: Any  # Literal, IRIntrinsic, list, dict, or nested structure


@dataclass
class IRParameter:
    """Parsed CloudFormation parameter."""

    logical_id: str
    type: str
    description: Optional[str] = None
    default: Optional[Any] = None
    allowed_values: Optional[list[Any]] = None
    allowed_pattern: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    min_value: Optional[int] = None
    max_value: Optional[int] = None
    constraint_description: Optional[str] = None
    no_echo: bool = False


@dataclass
class IRResource:
    """Parsed CloudFormation resource."""

    logical_id: str
    resource_type: str  # e.g., "AWS::S3::Bucket"
    properties: dict[str, IRProperty] = field(default_factory=dict)
    depends_on: list[str] = field(default_factory=list)
    condition: Optional[str] = None
    deletion_policy: Optional[str] = None
    update_replace_policy: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None

    @property
    def service(self) -> str:
        """Extract service name from resource type (e.g., 'S3' from 'AWS::S3::Bucket')."""
        parts = self.resource_type.split("::")
        return parts[1] if len(parts) >= 2 else ""

    @property
    def type_name(self) -> str:
        """Extract type name from resource type (e.g., 'Bucket' from 'AWS::S3::Bucket')."""
        parts = self.resource_type.split("::")
        return parts[2] if len(parts) >= 3 else ""


@dataclass
class IROutput:
    """Parsed CloudFormation output."""

    logical_id: str
    value: Any  # Literal or IRIntrinsic
    description: Optional[str] = None
    export_name: Optional[Any] = None  # Can be intrinsic
    condition: Optional[str] = None


@dataclass
class IRMapping:
    """Parsed CloudFormation mapping."""

    logical_id: str
    map_data: dict[str, dict[str, Any]]


@dataclass
class IRCondition:
    """Parsed CloudFormation condition."""

    logical_id: str
    expression: Any  # IRIntrinsic (Fn::Equals, Fn::And, etc.)


@dataclass
class IRTemplate:
    """Complete parsed template - the main IR structure."""

    description: Optional[str] = None
    aws_template_format_version: str = "2010-09-09"

    parameters: dict[str, IRParameter] = field(default_factory=dict)
    mappings: dict[str, IRMapping] = field(default_factory=dict)
    conditions: dict[str, IRCondition] = field(default_factory=dict)
    resources: dict[str, IRResource] = field(default_factory=dict)
    outputs: dict[str, IROutput] = field(default_factory=dict)

    # Metadata for code generation
    source_file: Optional[str] = None

    # Analysis results (populated by resolver)
    reference_graph: dict[str, list[str]] = field(default_factory=dict)
