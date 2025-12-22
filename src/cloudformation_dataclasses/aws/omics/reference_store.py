"""PropertyTypes for AWS::Omics::ReferenceStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Accelerators:
    """Accelerators enum values."""

    GPU = "GPU"


class AnnotationType:
    """AnnotationType enum values."""

    GENERIC = "GENERIC"
    CHR_POS = "CHR_POS"
    CHR_POS_REF_ALT = "CHR_POS_REF_ALT"
    CHR_START_END_ONE_BASE = "CHR_START_END_ONE_BASE"
    CHR_START_END_REF_ALT_ONE_BASE = "CHR_START_END_REF_ALT_ONE_BASE"
    CHR_START_END_ZERO_BASE = "CHR_START_END_ZERO_BASE"
    CHR_START_END_REF_ALT_ZERO_BASE = "CHR_START_END_REF_ALT_ZERO_BASE"


class CacheBehavior:
    """CacheBehavior enum values."""

    CACHE_ON_FAILURE = "CACHE_ON_FAILURE"
    CACHE_ALWAYS = "CACHE_ALWAYS"


class CreationType:
    """CreationType enum values."""

    IMPORT = "IMPORT"
    UPLOAD = "UPLOAD"


class ETagAlgorithm:
    """ETagAlgorithm enum values."""

    FASTQ_MD5UP = "FASTQ_MD5up"
    BAM_MD5UP = "BAM_MD5up"
    CRAM_MD5UP = "CRAM_MD5up"
    FASTQ_SHA256UP = "FASTQ_SHA256up"
    BAM_SHA256UP = "BAM_SHA256up"
    CRAM_SHA256UP = "CRAM_SHA256up"
    FASTQ_SHA512UP = "FASTQ_SHA512up"
    BAM_SHA512UP = "BAM_SHA512up"
    CRAM_SHA512UP = "CRAM_SHA512up"


class ETagAlgorithmFamily:
    """ETagAlgorithmFamily enum values."""

    MD5UP = "MD5up"
    SHA256UP = "SHA256up"
    SHA512UP = "SHA512up"


class EncryptionType:
    """EncryptionType enum values."""

    KMS = "KMS"


class FileType:
    """FileType enum values."""

    FASTQ = "FASTQ"
    BAM = "BAM"
    CRAM = "CRAM"
    UBAM = "UBAM"


class FormatToHeaderKey:
    """FormatToHeaderKey enum values."""

    CHR = "CHR"
    START = "START"
    END = "END"
    REF = "REF"
    ALT = "ALT"
    POS = "POS"


class JobStatus:
    """JobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ReadSetActivationJobItemStatus:
    """ReadSetActivationJobItemStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class ReadSetActivationJobStatus:
    """ReadSetActivationJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ReadSetExportJobItemStatus:
    """ReadSetExportJobItemStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class ReadSetExportJobStatus:
    """ReadSetExportJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ReadSetFile:
    """ReadSetFile enum values."""

    SOURCE1 = "SOURCE1"
    SOURCE2 = "SOURCE2"
    INDEX = "INDEX"


class ReadSetImportJobItemStatus:
    """ReadSetImportJobItemStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class ReadSetImportJobStatus:
    """ReadSetImportJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ReadSetPartSource:
    """ReadSetPartSource enum values."""

    SOURCE1 = "SOURCE1"
    SOURCE2 = "SOURCE2"


class ReadSetStatus:
    """ReadSetStatus enum values."""

    ARCHIVED = "ARCHIVED"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    PROCESSING_UPLOAD = "PROCESSING_UPLOAD"
    UPLOAD_FAILED = "UPLOAD_FAILED"


class ReferenceCreationType:
    """ReferenceCreationType enum values."""

    IMPORT = "IMPORT"


class ReferenceFile:
    """ReferenceFile enum values."""

    SOURCE = "SOURCE"
    INDEX = "INDEX"


class ReferenceImportJobItemStatus:
    """ReferenceImportJobItemStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class ReferenceImportJobStatus:
    """ReferenceImportJobStatus enum values."""

    SUBMITTED = "SUBMITTED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_FAILURES = "COMPLETED_WITH_FAILURES"


class ReferenceStatus:
    """ReferenceStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"


class ResourceOwner:
    """ResourceOwner enum values."""

    SELF = "SELF"
    OTHER = "OTHER"


class RunCacheStatus:
    """RunCacheStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    FAILED = "FAILED"


class RunExport:
    """RunExport enum values."""

    DEFINITION = "DEFINITION"


class RunLogLevel:
    """RunLogLevel enum values."""

    OFF = "OFF"
    FATAL = "FATAL"
    ERROR = "ERROR"
    ALL = "ALL"


class RunRetentionMode:
    """RunRetentionMode enum values."""

    RETAIN = "RETAIN"
    REMOVE = "REMOVE"


class RunStatus:
    """RunStatus enum values."""

    PENDING = "PENDING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    COMPLETED = "COMPLETED"
    DELETED = "DELETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class SchemaValueType:
    """SchemaValueType enum values."""

    LONG = "LONG"
    INT = "INT"
    STRING = "STRING"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"


class SequenceStoreStatus:
    """SequenceStoreStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ShareResourceType:
    """ShareResourceType enum values."""

    VARIANT_STORE = "VARIANT_STORE"
    ANNOTATION_STORE = "ANNOTATION_STORE"
    WORKFLOW = "WORKFLOW"


class ShareStatus:
    """ShareStatus enum values."""

    PENDING = "PENDING"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"


class SourceReferenceType:
    """SourceReferenceType enum values."""

    BRANCH = "BRANCH"
    TAG = "TAG"
    COMMIT = "COMMIT"


class StorageType:
    """StorageType enum values."""

    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


class StoreFormat:
    """StoreFormat enum values."""

    GFF = "GFF"
    TSV = "TSV"
    VCF = "VCF"


class StoreStatus:
    """StoreStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class StoreType:
    """StoreType enum values."""

    SEQUENCE_STORE = "SEQUENCE_STORE"
    REFERENCE_STORE = "REFERENCE_STORE"


class TaskStatus:
    """TaskStatus enum values."""

    PENDING = "PENDING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class VersionStatus:
    """VersionStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class WorkflowEngine:
    """WorkflowEngine enum values."""

    WDL = "WDL"
    NEXTFLOW = "NEXTFLOW"
    CWL = "CWL"
    WDL_LENIENT = "WDL_LENIENT"


class WorkflowExport:
    """WorkflowExport enum values."""

    DEFINITION = "DEFINITION"
    README = "README"


class WorkflowStatus:
    """WorkflowStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"


class WorkflowType:
    """WorkflowType enum values."""

    PRIVATE = "PRIVATE"
    READY2RUN = "READY2RUN"


@dataclass
class SseConfig(PropertyType):
    TYPE = "Type"
    KEY_ARN = "KeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "key_arn": "KeyArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

