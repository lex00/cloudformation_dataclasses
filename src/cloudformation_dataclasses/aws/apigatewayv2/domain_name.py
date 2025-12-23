"""PropertyTypes for AWS::ApiGatewayV2::DomainName."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DomainNameConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ownership_verification_certificate_arn": "OwnershipVerificationCertificateArn",
        "ip_address_type": "IpAddressType",
        "security_policy": "SecurityPolicy",
        "endpoint_type": "EndpointType",
        "certificate_name": "CertificateName",
        "certificate_arn": "CertificateArn",
    }

    ownership_verification_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_address_type: Optional[Union[str, IpAddressType, Ref, GetAtt, Sub]] = None
    security_policy: Optional[Union[str, SecurityPolicy, Ref, GetAtt, Sub]] = None
    endpoint_type: Optional[Union[str, EndpointType, Ref, GetAtt, Sub]] = None
    certificate_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MutualTlsAuthentication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "truststore_version": "TruststoreVersion",
        "truststore_uri": "TruststoreUri",
    }

    truststore_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    truststore_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

