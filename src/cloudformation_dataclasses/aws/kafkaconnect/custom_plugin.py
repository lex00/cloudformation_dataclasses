"""PropertyTypes for AWS::KafkaConnect::CustomPlugin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ConnectorOperationState:
    """ConnectorOperationState enum values."""

    PENDING = "PENDING"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"


class ConnectorOperationStepState:
    """ConnectorOperationStepState enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class ConnectorOperationStepType:
    """ConnectorOperationStepType enum values."""

    INITIALIZE_UPDATE = "INITIALIZE_UPDATE"
    FINALIZE_UPDATE = "FINALIZE_UPDATE"
    UPDATE_WORKER_SETTING = "UPDATE_WORKER_SETTING"
    UPDATE_CONNECTOR_CONFIGURATION = "UPDATE_CONNECTOR_CONFIGURATION"
    VALIDATE_UPDATE = "VALIDATE_UPDATE"


class ConnectorOperationType:
    """ConnectorOperationType enum values."""

    UPDATE_WORKER_SETTING = "UPDATE_WORKER_SETTING"
    UPDATE_CONNECTOR_CONFIGURATION = "UPDATE_CONNECTOR_CONFIGURATION"
    ISOLATE_CONNECTOR = "ISOLATE_CONNECTOR"
    RESTORE_CONNECTOR = "RESTORE_CONNECTOR"


class ConnectorState:
    """ConnectorState enum values."""

    RUNNING = "RUNNING"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class CustomPluginContentType:
    """CustomPluginContentType enum values."""

    JAR = "JAR"
    ZIP = "ZIP"


class CustomPluginState:
    """CustomPluginState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"


class KafkaClusterClientAuthenticationType:
    """KafkaClusterClientAuthenticationType enum values."""

    NONE = "NONE"
    IAM = "IAM"


class KafkaClusterEncryptionInTransitType:
    """KafkaClusterEncryptionInTransitType enum values."""

    PLAINTEXT = "PLAINTEXT"
    TLS = "TLS"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "IPV4"
    DUAL = "DUAL"


class WorkerConfigurationState:
    """WorkerConfigurationState enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


@dataclass
class CustomPluginFileDescription(PropertyType):
    FILE_MD5 = "FileMd5"
    FILE_SIZE = "FileSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file_md5": "FileMd5",
        "file_size": "FileSize",
    }

    file_md5: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPluginLocation(PropertyType):
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_location": "S3Location",
    }

    s3_location: Optional[S3Location] = None


@dataclass
class S3Location(PropertyType):
    BUCKET_ARN = "BucketArn"
    FILE_KEY = "FileKey"
    OBJECT_VERSION = "ObjectVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "file_key": "FileKey",
        "object_version": "ObjectVersion",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

