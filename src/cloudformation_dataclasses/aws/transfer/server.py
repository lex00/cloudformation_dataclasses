"""PropertyTypes for AWS::Transfer::Server."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgreementStatusType:
    """AgreementStatusType enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class As2Transport:
    """As2Transport enum values."""

    HTTP = "HTTP"


class CertificateStatusType:
    """CertificateStatusType enum values."""

    ACTIVE = "ACTIVE"
    PENDING_ROTATION = "PENDING_ROTATION"
    INACTIVE = "INACTIVE"


class CertificateType:
    """CertificateType enum values."""

    CERTIFICATE = "CERTIFICATE"
    CERTIFICATE_WITH_PRIVATE_KEY = "CERTIFICATE_WITH_PRIVATE_KEY"


class CertificateUsageType:
    """CertificateUsageType enum values."""

    SIGNING = "SIGNING"
    ENCRYPTION = "ENCRYPTION"
    TLS = "TLS"


class CompressionEnum:
    """CompressionEnum enum values."""

    ZLIB = "ZLIB"
    DISABLED = "DISABLED"


class ConnectorEgressType:
    """ConnectorEgressType enum values."""

    SERVICE_MANAGED = "SERVICE_MANAGED"
    VPC_LATTICE = "VPC_LATTICE"


class ConnectorStatus:
    """ConnectorStatus enum values."""

    ACTIVE = "ACTIVE"
    ERRORED = "ERRORED"
    PENDING = "PENDING"


class CustomStepStatus:
    """CustomStepStatus enum values."""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class DirectoryListingOptimization:
    """DirectoryListingOptimization enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Domain:
    """Domain enum values."""

    S3 = "S3"
    EFS = "EFS"


class EncryptionAlg:
    """EncryptionAlg enum values."""

    AES128_CBC = "AES128_CBC"
    AES192_CBC = "AES192_CBC"
    AES256_CBC = "AES256_CBC"
    DES_EDE3_CBC = "DES_EDE3_CBC"
    NONE = "NONE"


class EncryptionType:
    """EncryptionType enum values."""

    PGP = "PGP"


class EndpointType:
    """EndpointType enum values."""

    PUBLIC = "PUBLIC"
    VPC = "VPC"
    VPC_ENDPOINT = "VPC_ENDPOINT"


class EnforceMessageSigningType:
    """EnforceMessageSigningType enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ExecutionErrorType:
    """ExecutionErrorType enum values."""

    PERMISSION_DENIED = "PERMISSION_DENIED"
    CUSTOM_STEP_FAILED = "CUSTOM_STEP_FAILED"
    THROTTLED = "THROTTLED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    NOT_FOUND = "NOT_FOUND"
    BAD_REQUEST = "BAD_REQUEST"
    TIMEOUT = "TIMEOUT"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    EXCEPTION = "EXCEPTION"
    HANDLING_EXCEPTION = "HANDLING_EXCEPTION"


class HomeDirectoryType:
    """HomeDirectoryType enum values."""

    PATH = "PATH"
    LOGICAL = "LOGICAL"


class IdentityProviderType:
    """IdentityProviderType enum values."""

    SERVICE_MANAGED = "SERVICE_MANAGED"
    API_GATEWAY = "API_GATEWAY"
    AWS_DIRECTORY_SERVICE = "AWS_DIRECTORY_SERVICE"
    AWS_LAMBDA = "AWS_LAMBDA"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "IPV4"
    DUALSTACK = "DUALSTACK"


class MapType:
    """MapType enum values."""

    FILE = "FILE"
    DIRECTORY = "DIRECTORY"


class MdnResponse:
    """MdnResponse enum values."""

    SYNC = "SYNC"
    NONE = "NONE"


class MdnSigningAlg:
    """MdnSigningAlg enum values."""

    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"
    DEFAULT = "DEFAULT"


class OverwriteExisting:
    """OverwriteExisting enum values."""

    TRUE = "TRUE"
    FALSE = "FALSE"


class PreserveContentType:
    """PreserveContentType enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PreserveFilenameType:
    """PreserveFilenameType enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ProfileType:
    """ProfileType enum values."""

    LOCAL = "LOCAL"
    PARTNER = "PARTNER"


class Protocol:
    """Protocol enum values."""

    SFTP = "SFTP"
    FTP = "FTP"
    FTPS = "FTPS"
    AS2 = "AS2"


class SecurityPolicyProtocol:
    """SecurityPolicyProtocol enum values."""

    SFTP = "SFTP"
    FTPS = "FTPS"


class SecurityPolicyResourceType:
    """SecurityPolicyResourceType enum values."""

    SERVER = "SERVER"
    CONNECTOR = "CONNECTOR"


class SetStatOption:
    """SetStatOption enum values."""

    DEFAULT = "DEFAULT"
    ENABLE_NO_OP = "ENABLE_NO_OP"


class SftpAuthenticationMethods:
    """SftpAuthenticationMethods enum values."""

    PASSWORD = "PASSWORD"
    PUBLIC_KEY = "PUBLIC_KEY"
    PUBLIC_KEY_OR_PASSWORD = "PUBLIC_KEY_OR_PASSWORD"
    PUBLIC_KEY_AND_PASSWORD = "PUBLIC_KEY_AND_PASSWORD"


class SigningAlg:
    """SigningAlg enum values."""

    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"


class State:
    """State enum values."""

    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    START_FAILED = "START_FAILED"
    STOP_FAILED = "STOP_FAILED"


class TlsSessionResumptionMode:
    """TlsSessionResumptionMode enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    ENFORCED = "ENFORCED"


class TransferTableStatus:
    """TransferTableStatus enum values."""

    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class WebAppEndpointPolicy:
    """WebAppEndpointPolicy enum values."""

    FIPS = "FIPS"
    STANDARD = "STANDARD"


class WebAppEndpointType:
    """WebAppEndpointType enum values."""

    PUBLIC = "PUBLIC"
    VPC = "VPC"


class WorkflowStepType:
    """WorkflowStepType enum values."""

    COPY = "COPY"
    CUSTOM = "CUSTOM"
    TAG = "TAG"
    DELETE = "DELETE"
    DECRYPT = "DECRYPT"


@dataclass
class EndpointDetails(PropertyType):
    ADDRESS_ALLOCATION_IDS = "AddressAllocationIds"
    VPC_ID = "VpcId"
    VPC_ENDPOINT_ID = "VpcEndpointId"
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address_allocation_ids": "AddressAllocationIds",
        "vpc_id": "VpcId",
        "vpc_endpoint_id": "VpcEndpointId",
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    address_allocation_ids: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class IdentityProviderDetails(PropertyType):
    FUNCTION = "Function"
    DIRECTORY_ID = "DirectoryId"
    INVOCATION_ROLE = "InvocationRole"
    URL = "Url"
    SFTP_AUTHENTICATION_METHODS = "SftpAuthenticationMethods"

    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "directory_id": "DirectoryId",
        "invocation_role": "InvocationRole",
        "url": "Url",
        "sftp_authentication_methods": "SftpAuthenticationMethods",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    directory_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    invocation_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sftp_authentication_methods: Optional[Union[str, SftpAuthenticationMethods, Ref, GetAtt, Sub]] = None


@dataclass
class ProtocolDetails(PropertyType):
    AS2_TRANSPORTS = "As2Transports"
    PASSIVE_IP = "PassiveIp"
    SET_STAT_OPTION = "SetStatOption"
    TLS_SESSION_RESUMPTION_MODE = "TlsSessionResumptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "as2_transports": "As2Transports",
        "passive_ip": "PassiveIp",
        "set_stat_option": "SetStatOption",
        "tls_session_resumption_mode": "TlsSessionResumptionMode",
    }

    as2_transports: Optional[Union[list[str], Ref]] = None
    passive_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    set_stat_option: Optional[Union[str, SetStatOption, Ref, GetAtt, Sub]] = None
    tls_session_resumption_mode: Optional[Union[str, TlsSessionResumptionMode, Ref, GetAtt, Sub]] = None


@dataclass
class S3StorageOptions(PropertyType):
    DIRECTORY_LISTING_OPTIMIZATION = "DirectoryListingOptimization"

    _property_mappings: ClassVar[dict[str, str]] = {
        "directory_listing_optimization": "DirectoryListingOptimization",
    }

    directory_listing_optimization: Optional[Union[str, DirectoryListingOptimization, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowDetail(PropertyType):
    WORKFLOW_ID = "WorkflowId"
    EXECUTION_ROLE = "ExecutionRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workflow_id": "WorkflowId",
        "execution_role": "ExecutionRole",
    }

    workflow_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowDetails(PropertyType):
    ON_UPLOAD = "OnUpload"
    ON_PARTIAL_UPLOAD = "OnPartialUpload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_upload": "OnUpload",
        "on_partial_upload": "OnPartialUpload",
    }

    on_upload: Optional[list[WorkflowDetail]] = None
    on_partial_upload: Optional[list[WorkflowDetail]] = None

