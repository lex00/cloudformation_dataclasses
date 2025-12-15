"""
CloudFormation intrinsic functions as type-safe dataclasses.

This module provides type-safe Python representations of AWS CloudFormation intrinsic functions:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html

All intrinsic functions are dataclasses that serialize to their CloudFormation JSON representation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Ref:
    """
    Fn::Ref - Returns the value of the specified parameter or resource.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html

    Example:
        >>> vpc_ref = Ref(logical_id="MyVPC")
        >>> vpc_ref.to_dict()
        {"Ref": "MyVPC"}
    """

    logical_id: str

    def to_dict(self) -> dict[str, str]:
        """Serialize to CloudFormation JSON format."""
        return {"Ref": self.logical_id}


@dataclass
class GetAtt:
    """
    Fn::GetAtt - Returns the value of an attribute from a resource.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html

    Example:
        >>> instance_ip = GetAtt(logical_id="MyInstance", attribute_name="PublicIp")
        >>> instance_ip.to_dict()
        {"Fn::GetAtt": ["MyInstance", "PublicIp"]}
    """

    logical_id: str
    attribute_name: str

    def to_dict(self) -> dict[str, list[str]]:
        """Serialize to CloudFormation JSON format."""
        return {"Fn::GetAtt": [self.logical_id, self.attribute_name]}


@dataclass
class Sub:
    """
    Fn::Sub - Substitutes variables in an input string with values you specify.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-sub.html

    Example with embedded references:
        >>> sub = Sub(template_string="arn:aws:s3:::${BucketName}")
        >>> sub.to_dict()
        {"Fn::Sub": "arn:aws:s3:::${BucketName}"}

    Example with explicit variables:
        >>> sub = Sub(
        ...     template_string="My ${Key1} is ${Key2}",
        ...     variables={"Key1": "value1", "Key2": Ref("Parameter")}
        ... )
        >>> sub.to_dict()
        {"Fn::Sub": ["My ${Key1} is ${Key2}", {"Key1": "value1", "Key2": {"Ref": "Parameter"}}]}
    """

    template_string: str
    variables: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, str | list[Any]]:
        """Serialize to CloudFormation JSON format."""
        if self.variables:
            # Serialize variable values (may contain intrinsic functions)
            serialized_vars = {}
            for key, value in self.variables.items():
                if hasattr(value, "to_dict"):
                    serialized_vars[key] = value.to_dict()
                else:
                    serialized_vars[key] = value
            return {"Fn::Sub": [self.template_string, serialized_vars]}
        return {"Fn::Sub": self.template_string}


@dataclass
class Join:
    """
    Fn::Join - Appends a set of values into a single value, separated by delimiter.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.html

    Example:
        >>> join = Join(delimiter="-", values=["a", "b", "c"])
        >>> join.to_dict()
        {"Fn::Join": ["-", ["a", "b", "c"]]}

    Example with intrinsic functions:
        >>> join = Join(delimiter=":", values=["arn", "aws", "s3", "", "", Ref("BucketName")])
        >>> join.to_dict()
        {"Fn::Join": [":", ["arn", "aws", "s3", "", "", {"Ref": "BucketName"}]]}
    """

    delimiter: str
    values: list[Any]

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        # Serialize values (may contain intrinsic functions)
        serialized_values = []
        for value in self.values:
            if hasattr(value, "to_dict"):
                serialized_values.append(value.to_dict())
            else:
                serialized_values.append(value)
        return {"Fn::Join": [self.delimiter, serialized_values]}


@dataclass
class Select:
    """
    Fn::Select - Returns a single object from a list of objects by index.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-select.html

    Example:
        >>> select = Select(index=2, objects=["a", "b", "c", "d"])
        >>> select.to_dict()
        {"Fn::Select": [2, ["a", "b", "c", "d"]]}
    """

    index: int
    objects: list[Any]

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        # Serialize objects (may contain intrinsic functions)
        serialized_objects = []
        for obj in self.objects:
            if hasattr(obj, "to_dict"):
                serialized_objects.append(obj.to_dict())
            else:
                serialized_objects.append(obj)
        return {"Fn::Select": [self.index, serialized_objects]}


@dataclass
class Split:
    """
    Fn::Split - Split a string into a list of strings.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-split.html

    Example:
        >>> split = Split(delimiter=",", source="a,b,c")
        >>> split.to_dict()
        {"Fn::Split": [",", "a,b,c"]}
    """

    delimiter: str
    source: str | Any

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        source_value = self.source.to_dict() if hasattr(self.source, "to_dict") else self.source
        return {"Fn::Split": [self.delimiter, source_value]}


@dataclass
class If:
    """
    Fn::If - Returns one value if condition is true, another if false.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-if

    Example:
        >>> if_func = If(
        ...     condition_name="IsProduction",
        ...     value_if_true="m5.large",
        ...     value_if_false="t3.micro"
        ... )
        >>> if_func.to_dict()
        {"Fn::If": ["IsProduction", "m5.large", "t3.micro"]}
    """

    condition_name: str
    value_if_true: Any
    value_if_false: Any

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        true_val = (
            self.value_if_true.to_dict()
            if hasattr(self.value_if_true, "to_dict")
            else self.value_if_true
        )
        false_val = (
            self.value_if_false.to_dict()
            if hasattr(self.value_if_false, "to_dict")
            else self.value_if_false
        )
        return {"Fn::If": [self.condition_name, true_val, false_val]}


@dataclass
class Equals:
    """
    Fn::Equals - Compares two values for equality (used in Conditions).

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-equals

    Example:
        >>> equals = Equals(value1=Ref("Environment"), value2="production")
        >>> equals.to_dict()
        {"Fn::Equals": [{"Ref": "Environment"}, "production"]}
    """

    value1: Any
    value2: Any

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        val1 = self.value1.to_dict() if hasattr(self.value1, "to_dict") else self.value1
        val2 = self.value2.to_dict() if hasattr(self.value2, "to_dict") else self.value2
        return {"Fn::Equals": [val1, val2]}


@dataclass
class And:
    """
    Fn::And - Returns true if all conditions evaluate to true (used in Conditions).

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-and

    Example:
        >>> and_func = And(conditions=[
        ...     Equals(Ref("Env"), "prod"),
        ...     Equals(Ref("Region"), "us-east-1")
        ... ])
        >>> and_func.to_dict()
        {"Fn::And": [{"Fn::Equals": [...]}, {"Fn::Equals": [...]}]}
    """

    conditions: list[Any]

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        serialized = [
            cond.to_dict() if hasattr(cond, "to_dict") else cond for cond in self.conditions
        ]
        return {"Fn::And": serialized}


@dataclass
class Or:
    """
    Fn::Or - Returns true if any condition evaluates to true (used in Conditions).

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-or

    Example:
        >>> or_func = Or(conditions=[
        ...     Equals(Ref("Env"), "dev"),
        ...     Equals(Ref("Env"), "test")
        ... ])
    """

    conditions: list[Any]

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        serialized = [
            cond.to_dict() if hasattr(cond, "to_dict") else cond for cond in self.conditions
        ]
        return {"Fn::Or": serialized}


@dataclass
class Not:
    """
    Fn::Not - Returns the negation of a condition (used in Conditions).

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#intrinsic-function-reference-conditions-not

    Example:
        >>> not_func = Not(condition=Equals(Ref("Env"), "production"))
    """

    condition: Any

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        cond_val = self.condition.to_dict() if hasattr(self.condition, "to_dict") else self.condition
        return {"Fn::Not": [cond_val]}


@dataclass
class Base64:
    """
    Fn::Base64 - Returns the Base64 representation of the input string.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-base64.html

    Example:
        >>> b64 = Base64(value_to_encode="Hello World")
        >>> b64.to_dict()
        {"Fn::Base64": "Hello World"}
    """

    value_to_encode: str | Any

    def to_dict(self) -> dict[str, Any]:
        """Serialize to CloudFormation JSON format."""
        value = (
            self.value_to_encode.to_dict()
            if hasattr(self.value_to_encode, "to_dict")
            else self.value_to_encode
        )
        return {"Fn::Base64": value}


@dataclass
class GetAZs:
    """
    Fn::GetAZs - Returns an array of availability zones for a region.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getavailabilityzones.html

    Example:
        >>> azs = GetAZs(region="us-east-1")
        >>> azs.to_dict()
        {"Fn::GetAZs": "us-east-1"}

        >>> azs = GetAZs()  # Current region
        >>> azs.to_dict()
        {"Fn::GetAZs": ""}
    """

    region: str = ""

    def to_dict(self) -> dict[str, str]:
        """Serialize to CloudFormation JSON format."""
        return {"Fn::GetAZs": self.region}


@dataclass
class ImportValue:
    """
    Fn::ImportValue - Returns the value of an output exported by another stack.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html

    Example:
        >>> import_val = ImportValue(shared_value_to_import="NetworkStackVPCId")
        >>> import_val.to_dict()
        {"Fn::ImportValue": "NetworkStackVPCId"}
    """

    shared_value_to_import: str | Any

    def to_dict(self) -> dict[str, Any]:
        """Serialize to CloudFormation JSON format."""
        value = (
            self.shared_value_to_import.to_dict()
            if hasattr(self.shared_value_to_import, "to_dict")
            else self.shared_value_to_import
        )
        return {"Fn::ImportValue": value}


@dataclass
class FindInMap:
    """
    Fn::FindInMap - Returns the value corresponding to keys in a two-level map.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-findinmap.html

    Example:
        >>> find = FindInMap(
        ...     map_name="RegionMap",
        ...     top_level_key="us-east-1",
        ...     second_level_key="AMI"
        ... )
        >>> find.to_dict()
        {"Fn::FindInMap": ["RegionMap", "us-east-1", "AMI"]}
    """

    map_name: str
    top_level_key: str | Any
    second_level_key: str | Any

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        top_key = (
            self.top_level_key.to_dict()
            if hasattr(self.top_level_key, "to_dict")
            else self.top_level_key
        )
        second_key = (
            self.second_level_key.to_dict()
            if hasattr(self.second_level_key, "to_dict")
            else self.second_level_key
        )
        return {"Fn::FindInMap": [self.map_name, top_key, second_key]}


@dataclass
class Cidr:
    """
    Fn::Cidr - Returns an array of CIDR address blocks.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html

    Example:
        >>> cidr = Cidr(ip_block="10.0.0.0/16", count=6, cidr_bits=8)
        >>> cidr.to_dict()
        {"Fn::Cidr": ["10.0.0.0/16", 6, 8]}
    """

    ip_block: str | Any
    count: int
    cidr_bits: int

    def to_dict(self) -> dict[str, list[Any]]:
        """Serialize to CloudFormation JSON format."""
        ip_val = self.ip_block.to_dict() if hasattr(self.ip_block, "to_dict") else self.ip_block
        return {"Fn::Cidr": [ip_val, self.count, self.cidr_bits]}


# Type alias for any intrinsic function
IntrinsicFunction = Union[
    Ref,
    GetAtt,
    Sub,
    Join,
    Select,
    Split,
    If,
    Equals,
    And,
    Or,
    Not,
    Base64,
    GetAZs,
    ImportValue,
    FindInMap,
    Cidr,
]
