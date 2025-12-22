"""PropertyTypes for AWS::Transfer::Workflow."""

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
class CopyStepDetails(PropertyType):
    DESTINATION_FILE_LOCATION = "DestinationFileLocation"
    SOURCE_FILE_LOCATION = "SourceFileLocation"
    NAME = "Name"
    OVERWRITE_EXISTING = "OverwriteExisting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_file_location": "DestinationFileLocation",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
        "overwrite_existing": "OverwriteExisting",
    }

    destination_file_location: Optional[S3FileLocation] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_existing: Optional[Union[str, OverwriteExisting, Ref, GetAtt, Sub]] = None


@dataclass
class CustomStepDetails(PropertyType):
    TIMEOUT_SECONDS = "TimeoutSeconds"
    TARGET = "Target"
    SOURCE_FILE_LOCATION = "SourceFileLocation"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_seconds": "TimeoutSeconds",
        "target": "Target",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
    }

    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecryptStepDetails(PropertyType):
    DESTINATION_FILE_LOCATION = "DestinationFileLocation"
    TYPE = "Type"
    SOURCE_FILE_LOCATION = "SourceFileLocation"
    NAME = "Name"
    OVERWRITE_EXISTING = "OverwriteExisting"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_file_location": "DestinationFileLocation",
        "type_": "Type",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
        "overwrite_existing": "OverwriteExisting",
    }

    destination_file_location: Optional[InputFileLocation] = None
    type_: Optional[Union[str, EncryptionType, Ref, GetAtt, Sub]] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_existing: Optional[Union[str, OverwriteExisting, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteStepDetails(PropertyType):
    SOURCE_FILE_LOCATION = "SourceFileLocation"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_file_location": "SourceFileLocation",
        "name": "Name",
    }

    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EfsInputFileLocation(PropertyType):
    PATH = "Path"
    FILE_SYSTEM_ID = "FileSystemId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "file_system_id": "FileSystemId",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputFileLocation(PropertyType):
    EFS_FILE_LOCATION = "EfsFileLocation"
    S3_FILE_LOCATION = "S3FileLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_location": "EfsFileLocation",
        "s3_file_location": "S3FileLocation",
    }

    efs_file_location: Optional[EfsInputFileLocation] = None
    s3_file_location: Optional[S3InputFileLocation] = None


@dataclass
class S3FileLocation(PropertyType):
    S3_FILE_LOCATION = "S3FileLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_file_location": "S3FileLocation",
    }

    s3_file_location: Optional[S3InputFileLocation] = None


@dataclass
class S3InputFileLocation(PropertyType):
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Tag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagStepDetails(PropertyType):
    SOURCE_FILE_LOCATION = "SourceFileLocation"
    TAGS = "Tags"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_file_location": "SourceFileLocation",
        "tags": "Tags",
        "name": "Name",
    }

    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[S3Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowStep(PropertyType):
    CUSTOM_STEP_DETAILS = "CustomStepDetails"
    COPY_STEP_DETAILS = "CopyStepDetails"
    DECRYPT_STEP_DETAILS = "DecryptStepDetails"
    TYPE = "Type"
    TAG_STEP_DETAILS = "TagStepDetails"
    DELETE_STEP_DETAILS = "DeleteStepDetails"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_step_details": "CustomStepDetails",
        "copy_step_details": "CopyStepDetails",
        "decrypt_step_details": "DecryptStepDetails",
        "type_": "Type",
        "tag_step_details": "TagStepDetails",
        "delete_step_details": "DeleteStepDetails",
    }

    custom_step_details: Optional[CustomStepDetails] = None
    copy_step_details: Optional[CopyStepDetails] = None
    decrypt_step_details: Optional[DecryptStepDetails] = None
    type_: Optional[Union[str, WorkflowStepType, Ref, GetAtt, Sub]] = None
    tag_step_details: Optional[TagStepDetails] = None
    delete_step_details: Optional[DeleteStepDetails] = None

