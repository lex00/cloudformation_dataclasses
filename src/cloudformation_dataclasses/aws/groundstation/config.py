"""PropertyTypes for AWS::GroundStation::Config."""

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
class AntennaDownlinkConfig(PropertyType):
    SPECTRUM_CONFIG = "SpectrumConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "spectrum_config": "SpectrumConfig",
    }

    spectrum_config: Optional[SpectrumConfig] = None


@dataclass
class AntennaDownlinkDemodDecodeConfig(PropertyType):
    DEMODULATION_CONFIG = "DemodulationConfig"
    SPECTRUM_CONFIG = "SpectrumConfig"
    DECODE_CONFIG = "DecodeConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "demodulation_config": "DemodulationConfig",
        "spectrum_config": "SpectrumConfig",
        "decode_config": "DecodeConfig",
    }

    demodulation_config: Optional[DemodulationConfig] = None
    spectrum_config: Optional[SpectrumConfig] = None
    decode_config: Optional[DecodeConfig] = None


@dataclass
class AntennaUplinkConfig(PropertyType):
    TRANSMIT_DISABLED = "TransmitDisabled"
    SPECTRUM_CONFIG = "SpectrumConfig"
    TARGET_EIRP = "TargetEirp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "transmit_disabled": "TransmitDisabled",
        "spectrum_config": "SpectrumConfig",
        "target_eirp": "TargetEirp",
    }

    transmit_disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    spectrum_config: Optional[UplinkSpectrumConfig] = None
    target_eirp: Optional[Eirp] = None


@dataclass
class ConfigData(PropertyType):
    DATAFLOW_ENDPOINT_CONFIG = "DataflowEndpointConfig"
    UPLINK_ECHO_CONFIG = "UplinkEchoConfig"
    ANTENNA_DOWNLINK_CONFIG = "AntennaDownlinkConfig"
    ANTENNA_DOWNLINK_DEMOD_DECODE_CONFIG = "AntennaDownlinkDemodDecodeConfig"
    TRACKING_CONFIG = "TrackingConfig"
    ANTENNA_UPLINK_CONFIG = "AntennaUplinkConfig"
    S3_RECORDING_CONFIG = "S3RecordingConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataflow_endpoint_config": "DataflowEndpointConfig",
        "uplink_echo_config": "UplinkEchoConfig",
        "antenna_downlink_config": "AntennaDownlinkConfig",
        "antenna_downlink_demod_decode_config": "AntennaDownlinkDemodDecodeConfig",
        "tracking_config": "TrackingConfig",
        "antenna_uplink_config": "AntennaUplinkConfig",
        "s3_recording_config": "S3RecordingConfig",
    }

    dataflow_endpoint_config: Optional[DataflowEndpointConfig] = None
    uplink_echo_config: Optional[UplinkEchoConfig] = None
    antenna_downlink_config: Optional[AntennaDownlinkConfig] = None
    antenna_downlink_demod_decode_config: Optional[AntennaDownlinkDemodDecodeConfig] = None
    tracking_config: Optional[TrackingConfig] = None
    antenna_uplink_config: Optional[AntennaUplinkConfig] = None
    s3_recording_config: Optional[S3RecordingConfig] = None


@dataclass
class DataflowEndpointConfig(PropertyType):
    DATAFLOW_ENDPOINT_NAME = "DataflowEndpointName"
    DATAFLOW_ENDPOINT_REGION = "DataflowEndpointRegion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dataflow_endpoint_name": "DataflowEndpointName",
        "dataflow_endpoint_region": "DataflowEndpointRegion",
    }

    dataflow_endpoint_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dataflow_endpoint_region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecodeConfig(PropertyType):
    UNVALIDATED_JSON = "UnvalidatedJSON"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DemodulationConfig(PropertyType):
    UNVALIDATED_JSON = "UnvalidatedJSON"

    _property_mappings: ClassVar[dict[str, str]] = {
        "unvalidated_json": "UnvalidatedJSON",
    }

    unvalidated_json: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Eirp(PropertyType):
    VALUE = "Value"
    UNITS = "Units"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Frequency(PropertyType):
    VALUE = "Value"
    UNITS = "Units"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FrequencyBandwidth(PropertyType):
    VALUE = "Value"
    UNITS = "Units"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "units": "Units",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    units: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3RecordingConfig(PropertyType):
    BUCKET_ARN = "BucketArn"
    PREFIX = "Prefix"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "prefix": "Prefix",
        "role_arn": "RoleArn",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpectrumConfig(PropertyType):
    POLARIZATION = "Polarization"
    BANDWIDTH = "Bandwidth"
    CENTER_FREQUENCY = "CenterFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "polarization": "Polarization",
        "bandwidth": "Bandwidth",
        "center_frequency": "CenterFrequency",
    }

    polarization: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bandwidth: Optional[FrequencyBandwidth] = None
    center_frequency: Optional[Frequency] = None


@dataclass
class TrackingConfig(PropertyType):
    AUTOTRACK = "Autotrack"

    _property_mappings: ClassVar[dict[str, str]] = {
        "autotrack": "Autotrack",
    }

    autotrack: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UplinkEchoConfig(PropertyType):
    ENABLED = "Enabled"
    ANTENNA_UPLINK_CONFIG_ARN = "AntennaUplinkConfigArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "antenna_uplink_config_arn": "AntennaUplinkConfigArn",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    antenna_uplink_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UplinkSpectrumConfig(PropertyType):
    POLARIZATION = "Polarization"
    CENTER_FREQUENCY = "CenterFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "polarization": "Polarization",
        "center_frequency": "CenterFrequency",
    }

    polarization: Optional[Union[str, Ref, GetAtt, Sub]] = None
    center_frequency: Optional[Frequency] = None

