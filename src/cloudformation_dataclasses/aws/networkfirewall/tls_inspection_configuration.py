"""PropertyTypes for AWS::NetworkFirewall::TLSInspectionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Address(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address_definition": "AddressDefinition",
    }

    address_definition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CheckCertificateRevocationStatus(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "unknown_status_action": "UnknownStatusAction",
        "revoked_status_action": "RevokedStatusAction",
    }

    unknown_status_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revoked_status_action: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerCertificateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_arn": "CertificateAuthorityArn",
        "check_certificate_revocation_status": "CheckCertificateRevocationStatus",
        "scopes": "Scopes",
        "server_certificates": "ServerCertificates",
    }

    certificate_authority_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    check_certificate_revocation_status: Optional[CheckCertificateRevocationStatus] = None
    scopes: Optional[list[ServerCertificateScope]] = None
    server_certificates: Optional[list[ServerCertificate]] = None


@dataclass
class ServerCertificateScope(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocols": "Protocols",
        "destination_ports": "DestinationPorts",
        "destinations": "Destinations",
        "sources": "Sources",
        "source_ports": "SourcePorts",
    }

    protocols: Optional[Union[list[int], Ref]] = None
    destination_ports: Optional[list[PortRange]] = None
    destinations: Optional[list[Address]] = None
    sources: Optional[list[Address]] = None
    source_ports: Optional[list[PortRange]] = None


@dataclass
class TLSInspectionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_certificate_configurations": "ServerCertificateConfigurations",
    }

    server_certificate_configurations: Optional[list[ServerCertificateConfiguration]] = None

