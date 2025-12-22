"""PropertyTypes for AWS::GroundStation::MissionProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgentStatus:
    """AgentStatus enum values."""

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class AngleUnits:
    """AngleUnits enum values."""

    DEGREE_ANGLE = "DEGREE_ANGLE"
    RADIAN = "RADIAN"


class AuditResults:
    """AuditResults enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class BandwidthUnits:
    """BandwidthUnits enum values."""

    GHZ = "GHz"
    MHZ = "MHz"
    KHZ = "kHz"


class CapabilityHealth:
    """CapabilityHealth enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class CapabilityHealthReason:
    """CapabilityHealthReason enum values."""

    NO_REGISTERED_AGENT = "NO_REGISTERED_AGENT"
    INVALID_IP_OWNERSHIP = "INVALID_IP_OWNERSHIP"
    NOT_AUTHORIZED_TO_CREATE_SLR = "NOT_AUTHORIZED_TO_CREATE_SLR"
    UNVERIFIED_IP_OWNERSHIP = "UNVERIFIED_IP_OWNERSHIP"
    INITIALIZING_DATAPLANE = "INITIALIZING_DATAPLANE"
    DATAPLANE_FAILURE = "DATAPLANE_FAILURE"
    HEALTHY = "HEALTHY"


class ConfigCapabilityType:
    """ConfigCapabilityType enum values."""

    ANTENNA_DOWNLINK = "antenna-downlink"
    ANTENNA_DOWNLINK_DEMOD_DECODE = "antenna-downlink-demod-decode"
    TRACKING = "tracking"
    DATAFLOW_ENDPOINT = "dataflow-endpoint"
    ANTENNA_UPLINK = "antenna-uplink"
    UPLINK_ECHO = "uplink-echo"
    S3_RECORDING = "s3-recording"


class ContactStatus:
    """ContactStatus enum values."""

    SCHEDULING = "SCHEDULING"
    FAILED_TO_SCHEDULE = "FAILED_TO_SCHEDULE"
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    AWS_CANCELLED = "AWS_CANCELLED"
    PREPASS = "PREPASS"
    PASS = "PASS"
    POSTPASS = "POSTPASS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    AVAILABLE = "AVAILABLE"
    CANCELLING = "CANCELLING"
    AWS_FAILED = "AWS_FAILED"


class Criticality:
    """Criticality enum values."""

    REQUIRED = "REQUIRED"
    PREFERRED = "PREFERRED"
    REMOVED = "REMOVED"


class EirpUnits:
    """EirpUnits enum values."""

    DBW = "dBW"


class EndpointStatus:
    """EndpointStatus enum values."""

    CREATED = "created"
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    FAILED = "failed"


class EphemerisErrorCode:
    """EphemerisErrorCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    MISMATCHED_SATCAT_ID = "MISMATCHED_SATCAT_ID"
    OEM_VERSION_UNSUPPORTED = "OEM_VERSION_UNSUPPORTED"
    ORIGINATOR_MISSING = "ORIGINATOR_MISSING"
    CREATION_DATE_MISSING = "CREATION_DATE_MISSING"
    OBJECT_NAME_MISSING = "OBJECT_NAME_MISSING"
    OBJECT_ID_MISSING = "OBJECT_ID_MISSING"
    REF_FRAME_UNSUPPORTED = "REF_FRAME_UNSUPPORTED"
    REF_FRAME_EPOCH_UNSUPPORTED = "REF_FRAME_EPOCH_UNSUPPORTED"
    TIME_SYSTEM_UNSUPPORTED = "TIME_SYSTEM_UNSUPPORTED"
    CENTER_BODY_UNSUPPORTED = "CENTER_BODY_UNSUPPORTED"
    INTERPOLATION_MISSING = "INTERPOLATION_MISSING"
    INTERPOLATION_DEGREE_INVALID = "INTERPOLATION_DEGREE_INVALID"
    AZ_EL_SEGMENT_LIST_MISSING = "AZ_EL_SEGMENT_LIST_MISSING"
    INSUFFICIENT_TIME_AZ_EL = "INSUFFICIENT_TIME_AZ_EL"
    START_TIME_IN_FUTURE = "START_TIME_IN_FUTURE"
    END_TIME_IN_PAST = "END_TIME_IN_PAST"
    EXPIRATION_TIME_TOO_EARLY = "EXPIRATION_TIME_TOO_EARLY"
    START_TIME_METADATA_TOO_EARLY = "START_TIME_METADATA_TOO_EARLY"
    STOP_TIME_METADATA_TOO_LATE = "STOP_TIME_METADATA_TOO_LATE"
    AZ_EL_SEGMENT_END_TIME_BEFORE_START_TIME = "AZ_EL_SEGMENT_END_TIME_BEFORE_START_TIME"
    AZ_EL_SEGMENT_TIMES_OVERLAP = "AZ_EL_SEGMENT_TIMES_OVERLAP"
    AZ_EL_SEGMENTS_OUT_OF_ORDER = "AZ_EL_SEGMENTS_OUT_OF_ORDER"
    TIME_AZ_EL_ITEMS_OUT_OF_ORDER = "TIME_AZ_EL_ITEMS_OUT_OF_ORDER"
    MEAN_MOTION_INVALID = "MEAN_MOTION_INVALID"
    TIME_AZ_EL_AZ_RADIAN_RANGE_INVALID = "TIME_AZ_EL_AZ_RADIAN_RANGE_INVALID"
    TIME_AZ_EL_EL_RADIAN_RANGE_INVALID = "TIME_AZ_EL_EL_RADIAN_RANGE_INVALID"
    TIME_AZ_EL_AZ_DEGREE_RANGE_INVALID = "TIME_AZ_EL_AZ_DEGREE_RANGE_INVALID"
    TIME_AZ_EL_EL_DEGREE_RANGE_INVALID = "TIME_AZ_EL_EL_DEGREE_RANGE_INVALID"
    TIME_AZ_EL_ANGLE_UNITS_INVALID = "TIME_AZ_EL_ANGLE_UNITS_INVALID"
    INSUFFICIENT_KMS_PERMISSIONS = "INSUFFICIENT_KMS_PERMISSIONS"
    FILE_FORMAT_INVALID = "FILE_FORMAT_INVALID"
    AZ_EL_SEGMENT_REFERENCE_EPOCH_INVALID = "AZ_EL_SEGMENT_REFERENCE_EPOCH_INVALID"
    AZ_EL_SEGMENT_START_TIME_INVALID = "AZ_EL_SEGMENT_START_TIME_INVALID"
    AZ_EL_SEGMENT_END_TIME_INVALID = "AZ_EL_SEGMENT_END_TIME_INVALID"
    AZ_EL_SEGMENT_VALID_TIME_RANGE_INVALID = "AZ_EL_SEGMENT_VALID_TIME_RANGE_INVALID"
    AZ_EL_SEGMENT_END_TIME_TOO_LATE = "AZ_EL_SEGMENT_END_TIME_TOO_LATE"
    AZ_EL_TOTAL_DURATION_EXCEEDED = "AZ_EL_TOTAL_DURATION_EXCEEDED"


class EphemerisInvalidReason:
    """EphemerisInvalidReason enum values."""

    METADATA_INVALID = "METADATA_INVALID"
    TIME_RANGE_INVALID = "TIME_RANGE_INVALID"
    TRAJECTORY_INVALID = "TRAJECTORY_INVALID"
    KMS_KEY_INVALID = "KMS_KEY_INVALID"
    VALIDATION_ERROR = "VALIDATION_ERROR"


class EphemerisSource:
    """EphemerisSource enum values."""

    CUSTOMER_PROVIDED = "CUSTOMER_PROVIDED"
    SPACE_TRACK = "SPACE_TRACK"


class EphemerisStatus:
    """EphemerisStatus enum values."""

    VALIDATING = "VALIDATING"
    INVALID = "INVALID"
    ERROR = "ERROR"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"


class EphemerisType:
    """EphemerisType enum values."""

    TLE = "TLE"
    OEM = "OEM"
    AZ_EL = "AZ_EL"
    SERVICE_MANAGED = "SERVICE_MANAGED"


class FrequencyUnits:
    """FrequencyUnits enum values."""

    GHZ = "GHz"
    MHZ = "MHz"
    KHZ = "kHz"


class Polarization:
    """Polarization enum values."""

    RIGHT_HAND = "RIGHT_HAND"
    LEFT_HAND = "LEFT_HAND"
    NONE = "NONE"


@dataclass
class DataflowEdge(PropertyType):
    DESTINATION = "Destination"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "source": "Source",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StreamsKmsKey(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    KMS_ALIAS_ARN = "KmsAliasArn"
    KMS_ALIAS_NAME = "KmsAliasName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "kms_alias_arn": "KmsAliasArn",
        "kms_alias_name": "KmsAliasName",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_alias_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_alias_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

