"""
CloudFormation template components.

This module provides classes for building complete CloudFormation templates:
- Template: The main template container
- Parameter: Template parameters
- Output: Template outputs
- Condition: Template conditions
- Mapping: Template mappings
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Optional

from cloudformation_dataclasses.core.base import CloudFormationResource


@dataclass
class Parameter:
    """
    CloudFormation template parameter.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html

    Example:
        @dataclass
        class EnvironmentParameter:
            parameter: Parameter
            type: str = "String"
            default: str = "dev"
            allowed_values: list[str] = field(default_factory=lambda: ["dev", "staging", "prod"])
            description: str = "Deployment environment"

        param = EnvironmentParameter()
    """

    type: str  # String, Number, List<Number>, CommaDelimitedList, AWS::EC2::*, etc.
    default: Optional[Any] = None
    allowed_values: Optional[list[Any]] = None
    allowed_pattern: Optional[str] = None
    constraint_description: Optional[str] = None
    description: Optional[str] = None
    max_length: Optional[int] = None
    max_value: Optional[int] = None
    min_length: Optional[int] = None
    min_value: Optional[int] = None
    no_echo: Optional[bool] = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize parameter to CloudFormation JSON format."""
        result: dict[str, Any] = {"Type": self.type}

        if self.default is not None:
            result["Default"] = self.default
        if self.allowed_values is not None:
            result["AllowedValues"] = self.allowed_values
        if self.allowed_pattern is not None:
            result["AllowedPattern"] = self.allowed_pattern
        if self.constraint_description is not None:
            result["ConstraintDescription"] = self.constraint_description
        if self.description is not None:
            result["Description"] = self.description
        if self.max_length is not None:
            result["MaxLength"] = self.max_length
        if self.max_value is not None:
            result["MaxValue"] = self.max_value
        if self.min_length is not None:
            result["MinLength"] = self.min_length
        if self.min_value is not None:
            result["MinValue"] = self.min_value
        if self.no_echo is not None:
            result["NoEcho"] = self.no_echo

        return result


@dataclass
class Output:
    """
    CloudFormation template output.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html

    Example:
        @dataclass
        class VPCIdOutput:
            output: Output
            value: MyVPC.ref()
            description: str = "VPC ID"
            export_name: str = "MyApp-VPC-ID"

        output = VPCIdOutput()
    """

    value: Any  # Can be literal value or intrinsic function
    description: Optional[str] = None
    export_name: Any = None  # Can be str or intrinsic function
    condition: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize output to CloudFormation JSON format."""
        result: dict[str, Any] = {}

        # Serialize value (may be intrinsic function)
        if hasattr(self.value, "to_dict"):
            result["Value"] = self.value.to_dict()
        else:
            result["Value"] = self.value

        if self.description is not None:
            result["Description"] = self.description
        if self.export_name is not None:
            if hasattr(self.export_name, "to_dict"):
                result["Export"] = {"Name": self.export_name.to_dict()}
            else:
                result["Export"] = {"Name": self.export_name}
        if self.condition is not None:
            result["Condition"] = self.condition

        return result


@dataclass
class Condition:
    """
    CloudFormation template condition.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html

    Example:
        @dataclass
        class IsProductionCondition:
            condition: Condition
            expression: Equals(Ref("Environment"), "production")

        cond = IsProductionCondition()
    """

    expression: Any  # Condition intrinsic function (Equals, And, Or, Not, If)

    def to_dict(self) -> dict[str, Any]:
        """Serialize condition to CloudFormation JSON format."""
        if hasattr(self.expression, "to_dict"):
            return self.expression.to_dict()
        return self.expression


@dataclass
class Mapping:
    """
    CloudFormation template mapping.

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html

    Example:
        @dataclass
        class RegionAMIMapping:
            mapping: Mapping
            map_data: dict[str, dict[str, Any]] = field(default_factory=lambda: {
                "us-east-1": {"AMI": "ami-0c55b159cbfafe1f0"},
                "us-west-2": {"AMI": "ami-0d1cd67c26f5fca19"}
            })

        mapping = RegionAMIMapping()
    """

    map_data: dict[str, dict[str, Any]]

    def to_dict(self) -> dict[str, dict[str, Any]]:
        """Serialize mapping to CloudFormation JSON format."""
        return self.map_data


@dataclass
class Template:
    """
    CloudFormation template container.

    Aggregates all template components (resources, parameters, outputs, conditions, mappings)
    and provides serialization to CloudFormation JSON/YAML format.

    Example (declarative style with lists - recommended):
        template = Template(
            description="My application infrastructure",
            parameters=[EnvironmentParam, InstanceTypeParam],
            resources=[MyVPC, MySubnet, MyInstance],
            outputs=[VPCIdOutput, SubnetIdOutput],
        )

    Example (dict-based style):
        template = Template(
            description="My application infrastructure",
            resources=[my_vpc, my_subnet, my_instance],
            parameters={"Environment": environment_param},
            outputs={"VPCId": vpc_output}
        )

        # Generate JSON
        json_str = template.to_json()

        # Generate YAML (requires pyyaml)
        yaml_str = template.to_yaml()
    """

    description: Optional[str] = None
    resources: list[CloudFormationResource] = field(default_factory=list)
    parameters: dict[str, Parameter] | list[Any] = field(default_factory=dict)
    outputs: dict[str, Output] | list[Any] = field(default_factory=dict)
    conditions: dict[str, Condition] | list[Any] = field(default_factory=dict)
    mappings: dict[str, Mapping] | list[Any] = field(default_factory=dict)
    metadata: Optional[dict[str, Any]] = None
    transform: Optional[str | list[str]] = None
    format_version: str = "2010-09-09"

    def __post_init__(self) -> None:
        """Process list-based initialization to dict-based storage."""
        from cloudformation_dataclasses.core.wrapper import (
            create_wrapped_resource,
            is_wrapper_dataclass,
        )

        # Process parameters list to dict
        # Note: When using the @cloudformation_dataclass wrapper, the wrapper's
        # create_wrapped_resource already converts lists to dicts. This code handles
        # direct Template() instantiation with lists.
        if isinstance(self.parameters, list):
            params_dict: dict[str, Parameter] = {}
            for param in self.parameters:
                if is_wrapper_dataclass(type(param)):
                    name = type(param).__name__
                    wrapped = create_wrapped_resource(param)
                    if isinstance(wrapped, Parameter):
                        params_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {type(param).__name__} wraps "
                            f"{type(wrapped).__name__}, expected Parameter"
                        )
                elif isinstance(param, type) and is_wrapper_dataclass(param):
                    # Handle class reference (not instance)
                    name = param.__name__
                    instance = param()
                    wrapped = create_wrapped_resource(instance)
                    if isinstance(wrapped, Parameter):
                        params_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {param.__name__} wraps "
                            f"{type(wrapped).__name__}, expected Parameter"
                        )
                else:
                    raise TypeError(
                        f"Expected Parameter wrapper class or instance, "
                        f"got {type(param).__name__}"
                    )
            self.parameters = params_dict

        # Process outputs list to dict
        if isinstance(self.outputs, list):
            outputs_dict: dict[str, Output] = {}
            for out in self.outputs:
                if is_wrapper_dataclass(type(out)):
                    name = type(out).__name__
                    wrapped = create_wrapped_resource(out)
                    if isinstance(wrapped, Output):
                        outputs_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {type(out).__name__} wraps "
                            f"{type(wrapped).__name__}, expected Output"
                        )
                elif isinstance(out, type) and is_wrapper_dataclass(out):
                    # Handle class reference (not instance)
                    name = out.__name__
                    instance = out()
                    wrapped = create_wrapped_resource(instance)
                    if isinstance(wrapped, Output):
                        outputs_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {out.__name__} wraps "
                            f"{type(wrapped).__name__}, expected Output"
                        )
                else:
                    raise TypeError(
                        f"Expected Output wrapper class or instance, "
                        f"got {type(out).__name__}"
                    )
            self.outputs = outputs_dict

        # Process conditions list to dict
        if isinstance(self.conditions, list):
            conditions_dict: dict[str, Condition] = {}
            for cond in self.conditions:
                if is_wrapper_dataclass(type(cond)):
                    name = type(cond).__name__
                    wrapped = create_wrapped_resource(cond)
                    if isinstance(wrapped, Condition):
                        conditions_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {type(cond).__name__} wraps "
                            f"{type(wrapped).__name__}, expected Condition"
                        )
                elif isinstance(cond, type) and is_wrapper_dataclass(cond):
                    name = cond.__name__
                    instance = cond()
                    wrapped = create_wrapped_resource(instance)
                    if isinstance(wrapped, Condition):
                        conditions_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {cond.__name__} wraps "
                            f"{type(wrapped).__name__}, expected Condition"
                        )
                else:
                    raise TypeError(
                        f"Expected Condition wrapper class or instance, "
                        f"got {type(cond).__name__}"
                    )
            self.conditions = conditions_dict

        # Process mappings list to dict
        if isinstance(self.mappings, list):
            mappings_dict: dict[str, Mapping] = {}
            for mapping in self.mappings:
                if is_wrapper_dataclass(type(mapping)):
                    name = type(mapping).__name__
                    wrapped = create_wrapped_resource(mapping)
                    if isinstance(wrapped, Mapping):
                        mappings_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {type(mapping).__name__} wraps "
                            f"{type(wrapped).__name__}, expected Mapping"
                        )
                elif isinstance(mapping, type) and is_wrapper_dataclass(mapping):
                    name = mapping.__name__
                    instance = mapping()
                    wrapped = create_wrapped_resource(instance)
                    if isinstance(wrapped, Mapping):
                        mappings_dict[name] = wrapped
                    else:
                        raise TypeError(
                            f"Wrapper {mapping.__name__} wraps "
                            f"{type(wrapped).__name__}, expected Mapping"
                        )
                else:
                    raise TypeError(
                        f"Expected Mapping wrapper class or instance, "
                        f"got {type(mapping).__name__}"
                    )
            self.mappings = mappings_dict

        # Process resources list (handle class references)
        if isinstance(self.resources, list):
            processed_resources: list[CloudFormationResource] = []
            for resource in self.resources:
                if isinstance(resource, CloudFormationResource):
                    processed_resources.append(resource)
                elif is_wrapper_dataclass(type(resource)):
                    wrapped = create_wrapped_resource(resource)
                    if isinstance(wrapped, CloudFormationResource):
                        processed_resources.append(wrapped)
                    else:
                        raise TypeError(
                            f"Wrapper {type(resource).__name__} wraps "
                            f"{type(wrapped).__name__}, expected CloudFormationResource"
                        )
                elif isinstance(resource, type) and is_wrapper_dataclass(resource):
                    # Handle class reference (not instance)
                    instance = resource()
                    wrapped = create_wrapped_resource(instance)
                    if isinstance(wrapped, CloudFormationResource):
                        processed_resources.append(wrapped)
                    else:
                        raise TypeError(
                            f"Wrapper {resource.__name__} wraps "
                            f"{type(wrapped).__name__}, expected CloudFormationResource"
                        )
                else:
                    raise TypeError(
                        f"Expected CloudFormationResource or wrapper class, "
                        f"got {type(resource).__name__}"
                    )
            self.resources = processed_resources

    def add_resource(self, resource: CloudFormationResource | Any) -> None:
        """
        Add a resource to the template.

        Supports both direct CloudFormation resources and wrapper dataclasses.

        Args:
            resource: CloudFormation resource or wrapper dataclass instance to add

        Example (direct resource):
            >>> bucket = Bucket(bucket_name="my-bucket")
            >>> template.add_resource(bucket)

        Example (wrapper dataclass):
            >>> @dataclass
            >>> class MyBucket:
            >>>     resource: Bucket
            >>>     bucket_name: str = "my-bucket"
            >>>
            >>> my_bucket = MyBucket()
            >>> template.add_resource(my_bucket)
        """
        from cloudformation_dataclasses.core.wrapper import (
            create_wrapped_resource,
            is_wrapper_dataclass,
        )

        # Check if this is a wrapper dataclass
        if is_wrapper_dataclass(type(resource)):
            # Convert wrapper to underlying CloudFormation resource
            cf_resource = create_wrapped_resource(resource)
            if isinstance(cf_resource, CloudFormationResource):
                self.resources.append(cf_resource)
            else:
                raise TypeError(
                    f"Wrapper {type(resource).__name__} wraps {type(cf_resource).__name__}, "
                    "which is not a CloudFormation resource"
                )
        elif isinstance(resource, CloudFormationResource):
            # Direct CloudFormation resource
            self.resources.append(resource)
        else:
            raise TypeError(
                f"Expected CloudFormationResource or wrapper dataclass, "
                f"got {type(resource).__name__}"
            )

    def add_parameter(
        self, name_or_parameter: str | Parameter | Any, parameter: Parameter | Any | None = None
    ) -> None:
        """
        Add a parameter to the template.

        Supports both direct Parameter objects and wrapper dataclasses.
        When passing a wrapper dataclass, the name can be inferred from the class name.

        Args:
            name_or_parameter: Parameter name (logical ID) or wrapper dataclass instance
            parameter: Parameter definition (only when name is provided as first arg)

        Example (direct parameter):
            >>> template.add_parameter("Environment", Parameter(type="String"))

        Example (wrapper dataclass with explicit name):
            >>> template.add_parameter("Environment", Environment())

        Example (wrapper dataclass with inferred name):
            >>> @cloudformation_dataclass
            >>> class Environment:
            >>>     resource: Parameter
            >>>     type = "String"
            >>>     default = "dev"
            >>>
            >>> template.add_parameter(Environment())  # name inferred as "Environment"
        """
        from cloudformation_dataclasses.core.wrapper import (
            create_wrapped_resource,
            is_wrapper_dataclass,
        )

        # Handle single-argument form: add_parameter(WrapperClass())
        if parameter is None:
            if is_wrapper_dataclass(type(name_or_parameter)):
                name = type(name_or_parameter).__name__
                param = create_wrapped_resource(name_or_parameter)
                if isinstance(param, Parameter):
                    self.parameters[name] = param
                else:
                    raise TypeError(
                        f"Wrapper {type(name_or_parameter).__name__} wraps "
                        f"{type(param).__name__}, expected Parameter"
                    )
            else:
                raise TypeError(
                    f"Single argument must be a wrapper dataclass, "
                    f"got {type(name_or_parameter).__name__}"
                )
            return

        # Handle two-argument form: add_parameter("Name", param)
        name = name_or_parameter
        if not isinstance(name, str):
            raise TypeError(f"Parameter name must be a string, got {type(name).__name__}")

        if is_wrapper_dataclass(type(parameter)):
            param = create_wrapped_resource(parameter)
            if isinstance(param, Parameter):
                self.parameters[name] = param
            else:
                raise TypeError(
                    f"Wrapper {type(parameter).__name__} wraps {type(param).__name__}, "
                    "expected Parameter"
                )
        elif isinstance(parameter, Parameter):
            self.parameters[name] = parameter
        else:
            raise TypeError(
                f"Expected Parameter or wrapper dataclass, got {type(parameter).__name__}"
            )

    def add_output(
        self, name_or_output: str | Output | Any, output: Output | Any | None = None
    ) -> None:
        """
        Add an output to the template.

        Supports both direct Output objects and wrapper dataclasses.
        When passing a wrapper dataclass, the name can be inferred from the class name.

        Args:
            name_or_output: Output name (logical ID) or wrapper dataclass instance
            output: Output definition (only when name is provided as first arg)

        Example (direct output):
            >>> template.add_output("VPCId", Output(value=Ref("MyVPC")))

        Example (wrapper dataclass with explicit name):
            >>> template.add_output("VPCId", VPCId())

        Example (wrapper dataclass with inferred name):
            >>> @cloudformation_dataclass
            >>> class VPCId:
            >>>     resource: Output
            >>>     value = ref(MyVPC)
            >>>
            >>> template.add_output(VPCId())  # name inferred as "VPCId"
        """
        from cloudformation_dataclasses.core.wrapper import (
            create_wrapped_resource,
            is_wrapper_dataclass,
        )

        # Handle single-argument form: add_output(WrapperClass())
        if output is None:
            if is_wrapper_dataclass(type(name_or_output)):
                name = type(name_or_output).__name__
                out = create_wrapped_resource(name_or_output)
                if isinstance(out, Output):
                    self.outputs[name] = out
                else:
                    raise TypeError(
                        f"Wrapper {type(name_or_output).__name__} wraps "
                        f"{type(out).__name__}, expected Output"
                    )
            else:
                raise TypeError(
                    f"Single argument must be a wrapper dataclass, "
                    f"got {type(name_or_output).__name__}"
                )
            return

        # Handle two-argument form: add_output("Name", output)
        name = name_or_output
        if not isinstance(name, str):
            raise TypeError(f"Output name must be a string, got {type(name).__name__}")

        if is_wrapper_dataclass(type(output)):
            out = create_wrapped_resource(output)
            if isinstance(out, Output):
                self.outputs[name] = out
            else:
                raise TypeError(
                    f"Wrapper {type(output).__name__} wraps {type(out).__name__}, "
                    "expected Output"
                )
        elif isinstance(output, Output):
            self.outputs[name] = output
        else:
            raise TypeError(f"Expected Output or wrapper dataclass, got {type(output).__name__}")

    def add_condition(self, name: str, condition: Condition) -> None:
        """
        Add a condition to the template.

        Args:
            name: Condition name (logical ID)
            condition: Condition definition

        Example:
            >>> template.add_condition("IsProduction", is_prod_condition)
        """
        self.conditions[name] = condition

    def add_mapping(self, name: str, mapping: Mapping) -> None:
        """
        Add a mapping to the template.

        Args:
            name: Mapping name (logical ID)
            mapping: Mapping definition

        Example:
            >>> template.add_mapping("RegionAMI", region_ami_mapping)
        """
        self.mappings[name] = mapping

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize template to CloudFormation dictionary format.

        Returns:
            Dictionary representation of CloudFormation template

        Example:
            >>> template_dict = template.to_dict()
            >>> template_dict.keys()
            dict_keys(['AWSTemplateFormatVersion', 'Description', 'Resources', ...])
        """
        result: dict[str, Any] = {"AWSTemplateFormatVersion": self.format_version}

        if self.description:
            result["Description"] = self.description

        if self.metadata:
            result["Metadata"] = self.metadata

        if self.transform:
            result["Transform"] = self.transform

        # Serialize parameters
        if self.parameters:
            result["Parameters"] = {
                name: param.to_dict() for name, param in self.parameters.items()
            }

        # Serialize conditions
        if self.conditions:
            result["Conditions"] = {name: cond.to_dict() for name, cond in self.conditions.items()}

        # Serialize mappings
        if self.mappings:
            result["Mappings"] = {
                name: mapping.to_dict() for name, mapping in self.mappings.items()
            }

        # Serialize resources
        if self.resources:
            result["Resources"] = {}
            for resource in self.resources:
                logical_id = resource.effective_logical_id
                result["Resources"][logical_id] = resource.to_dict()

        # Serialize outputs
        if self.outputs:
            result["Outputs"] = {name: output.to_dict() for name, output in self.outputs.items()}

        return result

    def to_json(self, indent: int = 2) -> str:
        """
        Serialize template to CloudFormation JSON format.

        Args:
            indent: JSON indentation level (default: 2)

        Returns:
            JSON string representation

        Example:
            >>> json_str = template.to_json()
            >>> print(json_str)
            {
              "AWSTemplateFormatVersion": "2010-09-09",
              "Resources": { ... }
            }
        """
        return json.dumps(self.to_dict(), indent=indent)

    def to_yaml(self) -> str:
        """
        Serialize template to CloudFormation YAML format.

        Requires pyyaml to be installed:
            pip install cloudformation_dataclasses[yaml]

        Returns:
            YAML string representation

        Raises:
            ImportError: If pyyaml is not installed

        Example:
            >>> yaml_str = template.to_yaml()
            >>> print(yaml_str)
            AWSTemplateFormatVersion: '2010-09-09'
            Resources:
              ...
        """
        try:
            import yaml
        except ImportError as e:
            raise ImportError(
                "pyyaml is required for YAML serialization. "
                "Install it with: pip install cloudformation_dataclasses[yaml]"
            ) from e

        return yaml.dump(self.to_dict(), default_flow_style=False, sort_keys=False)

    def validate(self) -> list[str]:
        """
        Basic validation of template structure.

        Returns a list of validation errors. Empty list means no errors found.

        Note: This is basic validation only. Full validation happens via AWS CloudFormation
        when you deploy or use the validate-template API.

        Returns:
            List of validation error messages

        Example:
            >>> errors = template.validate()
            >>> if errors:
            ...     print("Validation errors:", errors)
        """
        errors: list[str] = []

        # Check if template has at least one resource
        if not self.resources:
            errors.append("Template must contain at least one resource")

        # Check for duplicate resource logical IDs
        logical_ids = [r.effective_logical_id for r in self.resources]
        duplicates = {lid for lid in logical_ids if logical_ids.count(lid) > 1}
        if duplicates:
            errors.append(f"Duplicate resource logical IDs found: {duplicates}")

        # Check DependsOn references exist
        for resource in self.resources:
            for dep in resource.depends_on:
                if dep not in logical_ids:
                    errors.append(
                        f"Resource {resource.effective_logical_id} depends on "
                        f"non-existent resource: {dep}"
                    )

        # Check Condition references exist
        for resource in self.resources:
            if resource.condition and resource.condition not in self.conditions:
                errors.append(
                    f"Resource {resource.effective_logical_id} references "
                    f"non-existent condition: {resource.condition}"
                )

        return errors
