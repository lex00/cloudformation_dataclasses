"""PropertyTypes for AWS::CloudFront::DistributionTenant."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Certificate(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Customizations(PropertyType):
    WEB_ACL = "WebAcl"
    GEO_RESTRICTIONS = "GeoRestrictions"
    CERTIFICATE = "Certificate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "web_acl": "WebAcl",
        "geo_restrictions": "GeoRestrictions",
        "certificate": "Certificate",
    }

    web_acl: Optional[WebAclCustomization] = None
    geo_restrictions: Optional[GeoRestrictionCustomization] = None
    certificate: Optional[Certificate] = None


@dataclass
class DomainResult(PropertyType):
    STATUS = "Status"
    DOMAIN = "Domain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "domain": "Domain",
    }

    status: Optional[Union[str, DomainStatus, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeoRestrictionCustomization(PropertyType):
    LOCATIONS = "Locations"
    RESTRICTION_TYPE = "RestrictionType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "locations": "Locations",
        "restriction_type": "RestrictionType",
    }

    locations: Optional[Union[list[str], Ref]] = None
    restriction_type: Optional[Union[str, GeoRestrictionType, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedCertificateRequest(PropertyType):
    CERTIFICATE_TRANSPARENCY_LOGGING_PREFERENCE = "CertificateTransparencyLoggingPreference"
    VALIDATION_TOKEN_HOST = "ValidationTokenHost"
    PRIMARY_DOMAIN_NAME = "PrimaryDomainName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_transparency_logging_preference": "CertificateTransparencyLoggingPreference",
        "validation_token_host": "ValidationTokenHost",
        "primary_domain_name": "PrimaryDomainName",
    }

    certificate_transparency_logging_preference: Optional[Union[str, CertificateTransparencyLoggingPreference, Ref, GetAtt, Sub]] = None
    validation_token_host: Optional[Union[str, ValidationTokenHost, Ref, GetAtt, Sub]] = None
    primary_domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WebAclCustomization(PropertyType):
    ACTION = "Action"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "arn": "Arn",
    }

    action: Optional[Union[str, CustomizationActionType, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

