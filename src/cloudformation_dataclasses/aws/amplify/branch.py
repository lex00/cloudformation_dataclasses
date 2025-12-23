"""PropertyTypes for AWS::Amplify::Branch."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Backend(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stack_arn": "StackArn",
    }

    stack_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "enable_basic_auth": "EnableBasicAuth",
        "password": "Password",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enable_basic_auth: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentVariable(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

