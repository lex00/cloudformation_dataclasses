"""PropertyTypes for AWS::Transfer::WebApp."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IdentityProviderDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "application_arn": "ApplicationArn",
        "instance_arn": "InstanceArn",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebAppCustomization(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "favicon_file": "FaviconFile",
        "title": "Title",
        "logo_file": "LogoFile",
    }

    favicon_file: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logo_file: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebAppUnits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned": "Provisioned",
    }

    provisioned: Optional[Union[int, Ref, GetAtt, Sub]] = None

