"""PropertyTypes for AWS::Kinesis::Stream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ConsumerStatus:
    """ConsumerStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class EncryptionType:
    """EncryptionType enum values."""

    NONE = "NONE"
    KMS = "KMS"


class MetricsName:
    """MetricsName enum values."""

    INCOMINGBYTES = "IncomingBytes"
    INCOMINGRECORDS = "IncomingRecords"
    OUTGOINGBYTES = "OutgoingBytes"
    OUTGOINGRECORDS = "OutgoingRecords"
    WRITEPROVISIONEDTHROUGHPUTEXCEEDED = "WriteProvisionedThroughputExceeded"
    READPROVISIONEDTHROUGHPUTEXCEEDED = "ReadProvisionedThroughputExceeded"
    ITERATORAGEMILLISECONDS = "IteratorAgeMilliseconds"
    ALL = "ALL"


class MinimumThroughputBillingCommitmentInputStatus:
    """MinimumThroughputBillingCommitmentInputStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MinimumThroughputBillingCommitmentOutputStatus:
    """MinimumThroughputBillingCommitmentOutputStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLED_UNTIL_EARLIEST_ALLOWED_END = "ENABLED_UNTIL_EARLIEST_ALLOWED_END"


class ScalingType:
    """ScalingType enum values."""

    UNIFORM_SCALING = "UNIFORM_SCALING"


class ShardFilterType:
    """ShardFilterType enum values."""

    AFTER_SHARD_ID = "AFTER_SHARD_ID"
    AT_TRIM_HORIZON = "AT_TRIM_HORIZON"
    FROM_TRIM_HORIZON = "FROM_TRIM_HORIZON"
    AT_LATEST = "AT_LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"
    FROM_TIMESTAMP = "FROM_TIMESTAMP"


class ShardIteratorType:
    """ShardIteratorType enum values."""

    AT_SEQUENCE_NUMBER = "AT_SEQUENCE_NUMBER"
    AFTER_SEQUENCE_NUMBER = "AFTER_SEQUENCE_NUMBER"
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


class StreamMode:
    """StreamMode enum values."""

    PROVISIONED = "PROVISIONED"
    ON_DEMAND = "ON_DEMAND"


class StreamStatus:
    """StreamStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"


@dataclass
class StreamEncryption(PropertyType):
    ENCRYPTION_TYPE = "EncryptionType"
    KEY_ID = "KeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
        "key_id": "KeyId",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamModeDetails(PropertyType):
    STREAM_MODE = "StreamMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stream_mode": "StreamMode",
    }

    stream_mode: Optional[Union[str, StreamMode, Ref, GetAtt, Sub]] = None


@dataclass
class WarmThroughputObject(PropertyType):
    CURRENT_MI_BPS = "CurrentMiBps"
    TARGET_MI_BPS = "TargetMiBps"

    _property_mappings: ClassVar[dict[str, str]] = {
        "current_mi_bps": "CurrentMiBps",
        "target_mi_bps": "TargetMiBps",
    }

    current_mi_bps: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_mi_bps: Optional[Union[int, Ref, GetAtt, Sub]] = None

