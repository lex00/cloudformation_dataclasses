"""PropertyTypes for AWS::SSO::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PortalOptionsConfiguration(PropertyType):
    SIGN_IN_OPTIONS = "SignInOptions"
    VISIBILITY = "Visibility"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sign_in_options": "SignInOptions",
        "visibility": "Visibility",
    }

    sign_in_options: Optional[SignInOptions] = None
    visibility: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignInOptions(PropertyType):
    ORIGIN = "Origin"
    APPLICATION_URL = "ApplicationUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "origin": "Origin",
        "application_url": "ApplicationUrl",
    }

    origin: Optional[Union[str, SignInOrigin, Ref, GetAtt, Sub]] = None
    application_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

