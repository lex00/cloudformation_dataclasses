"""PropertyTypes for AWS::Transfer::Connector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class As2Config(PropertyType):
    COMPRESSION = "Compression"
    MESSAGE_SUBJECT = "MessageSubject"
    BASIC_AUTH_SECRET_ID = "BasicAuthSecretId"
    PARTNER_PROFILE_ID = "PartnerProfileId"
    ENCRYPTION_ALGORITHM = "EncryptionAlgorithm"
    SIGNING_ALGORITHM = "SigningAlgorithm"
    LOCAL_PROFILE_ID = "LocalProfileId"
    MDN_RESPONSE = "MdnResponse"
    MDN_SIGNING_ALGORITHM = "MdnSigningAlgorithm"
    PRESERVE_CONTENT_TYPE = "PreserveContentType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compression": "Compression",
        "message_subject": "MessageSubject",
        "basic_auth_secret_id": "BasicAuthSecretId",
        "partner_profile_id": "PartnerProfileId",
        "encryption_algorithm": "EncryptionAlgorithm",
        "signing_algorithm": "SigningAlgorithm",
        "local_profile_id": "LocalProfileId",
        "mdn_response": "MdnResponse",
        "mdn_signing_algorithm": "MdnSigningAlgorithm",
        "preserve_content_type": "PreserveContentType",
    }

    compression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message_subject: Optional[Union[str, Ref, GetAtt, Sub]] = None
    basic_auth_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    partner_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signing_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    local_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mdn_response: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mdn_signing_algorithm: Optional[Union[str, Ref, GetAtt, Sub]] = None
    preserve_content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectorEgressConfig(PropertyType):
    VPC_LATTICE = "VpcLattice"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_lattice": "VpcLattice",
    }

    vpc_lattice: Optional[ConnectorVpcLatticeEgressConfig] = None


@dataclass
class ConnectorVpcLatticeEgressConfig(PropertyType):
    RESOURCE_CONFIGURATION_ARN = "ResourceConfigurationArn"
    PORT_NUMBER = "PortNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_configuration_arn": "ResourceConfigurationArn",
        "port_number": "PortNumber",
    }

    resource_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SftpConfig(PropertyType):
    TRUSTED_HOST_KEYS = "TrustedHostKeys"
    USER_SECRET_ID = "UserSecretId"
    MAX_CONCURRENT_CONNECTIONS = "MaxConcurrentConnections"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trusted_host_keys": "TrustedHostKeys",
        "user_secret_id": "UserSecretId",
        "max_concurrent_connections": "MaxConcurrentConnections",
    }

    trusted_host_keys: Optional[Union[list[str], Ref]] = None
    user_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_concurrent_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None

