"""PropertyTypes for AWS::FinSpace::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeMapItems(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FederationParameters(PropertyType):
    ATTRIBUTE_MAP = "AttributeMap"
    FEDERATION_PROVIDER_NAME = "FederationProviderName"
    SAML_METADATA_URL = "SamlMetadataURL"
    FEDERATION_URN = "FederationURN"
    SAML_METADATA_DOCUMENT = "SamlMetadataDocument"
    APPLICATION_CALL_BACK_URL = "ApplicationCallBackURL"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_map": "AttributeMap",
        "federation_provider_name": "FederationProviderName",
        "saml_metadata_url": "SamlMetadataURL",
        "federation_urn": "FederationURN",
        "saml_metadata_document": "SamlMetadataDocument",
        "application_call_back_url": "ApplicationCallBackURL",
    }

    attribute_map: Optional[list[AttributeMapItems]] = None
    federation_provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    saml_metadata_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    federation_urn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    saml_metadata_document: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_call_back_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuperuserParameters(PropertyType):
    FIRST_NAME = "FirstName"
    LAST_NAME = "LastName"
    EMAIL_ADDRESS = "EmailAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "email_address": "EmailAddress",
    }

    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

