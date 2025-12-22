"""PropertyTypes for AWS::PCAConnectorSCEP::Connector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IntuneConfiguration(PropertyType):
    AZURE_APPLICATION_ID = "AzureApplicationId"
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "azure_application_id": "AzureApplicationId",
        "domain": "Domain",
    }

    azure_application_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MobileDeviceManagement(PropertyType):
    INTUNE = "Intune"

    _property_mappings: ClassVar[dict[str, str]] = {
        "intune": "Intune",
    }

    intune: Optional[IntuneConfiguration] = None


@dataclass
class OpenIdConfiguration(PropertyType):
    ISSUER = "Issuer"
    AUDIENCE = "Audience"
    SUBJECT = "Subject"

    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer": "Issuer",
        "audience": "Audience",
        "subject": "Subject",
    }

    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audience: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subject: Optional[Union[str, Ref, GetAtt, Sub]] = None

