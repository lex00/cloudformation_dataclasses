"""PropertyTypes for AWS::MediaConnect::FlowEntitlement."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Algorithm:
    """Algorithm enum values."""

    AES128 = "aes128"
    AES192 = "aes192"
    AES256 = "aes256"


class BridgePlacement:
    """BridgePlacement enum values."""

    AVAILABLE = "AVAILABLE"
    LOCKED = "LOCKED"


class BridgeState:
    """BridgeState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    DEPLOYING = "DEPLOYING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    START_FAILED = "START_FAILED"
    START_PENDING = "START_PENDING"
    STOP_FAILED = "STOP_FAILED"
    UPDATING = "UPDATING"


class Colorimetry:
    """Colorimetry enum values."""

    BT601 = "BT601"
    BT709 = "BT709"
    BT2020 = "BT2020"
    BT2100 = "BT2100"
    ST2065_1 = "ST2065-1"
    ST2065_3 = "ST2065-3"
    XYZ = "XYZ"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


class ContentQualityAnalysisState:
    """ContentQualityAnalysisState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Day:
    """Day enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DesiredState:
    """DesiredState enum values."""

    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    DELETED = "DELETED"


class DurationUnits:
    """DurationUnits enum values."""

    MONTHS = "MONTHS"


class EncoderProfile:
    """EncoderProfile enum values."""

    MAIN = "main"
    HIGH = "high"


class EncodingName:
    """EncodingName enum values."""

    JXSV = "jxsv"
    RAW = "raw"
    SMPTE291 = "smpte291"
    PCM = "pcm"


class EntitlementStatus:
    """EntitlementStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FailoverInputSourcePriorityMode:
    """FailoverInputSourcePriorityMode enum values."""

    NO_PRIORITY = "NO_PRIORITY"
    PRIMARY_SECONDARY = "PRIMARY_SECONDARY"


class FailoverMode:
    """FailoverMode enum values."""

    MERGE = "MERGE"
    FAILOVER = "FAILOVER"


class FlowSize:
    """FlowSize enum values."""

    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class FlowTransitEncryptionKeyType:
    """FlowTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class ForwardErrorCorrectionState:
    """ForwardErrorCorrectionState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GatewayState:
    """GatewayState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InstanceState:
    """InstanceState enum values."""

    REGISTERING = "REGISTERING"
    ACTIVE = "ACTIVE"
    DEREGISTERING = "DEREGISTERING"
    DEREGISTERED = "DEREGISTERED"
    REGISTRATION_ERROR = "REGISTRATION_ERROR"
    DEREGISTRATION_ERROR = "DEREGISTRATION_ERROR"


class KeyType:
    """KeyType enum values."""

    SPEKE = "speke"
    STATIC_KEY = "static-key"
    SRT_PASSWORD = "srt-password"


class MaintenanceDay:
    """MaintenanceDay enum values."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class MaintenanceScheduleType:
    """MaintenanceScheduleType enum values."""

    WINDOW = "WINDOW"


class MaintenanceType:
    """MaintenanceType enum values."""

    PREFERRED_DAY_TIME = "PREFERRED_DAY_TIME"
    DEFAULT = "DEFAULT"


class MediaLiveInputPipelineId:
    """MediaLiveInputPipelineId enum values."""

    PIPELINE_0 = "PIPELINE_0"
    PIPELINE_1 = "PIPELINE_1"


class MediaLiveTransitEncryptionKeyType:
    """MediaLiveTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class MediaStreamType:
    """MediaStreamType enum values."""

    VIDEO = "video"
    AUDIO = "audio"
    ANCILLARY_DATA = "ancillary-data"


class NdiState:
    """NdiState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class NetworkInterfaceType:
    """NetworkInterfaceType enum values."""

    ENA = "ena"
    EFA = "efa"


class OutputStatus:
    """OutputStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PriceUnits:
    """PriceUnits enum values."""

    HOURLY = "HOURLY"


class Protocol:
    """Protocol enum values."""

    ZIXI_PUSH = "zixi-push"
    RTP_FEC = "rtp-fec"
    RTP = "rtp"
    ZIXI_PULL = "zixi-pull"
    RIST = "rist"
    ST2110_JPEGXS = "st2110-jpegxs"
    CDI = "cdi"
    SRT_LISTENER = "srt-listener"
    SRT_CALLER = "srt-caller"
    FUJITSU_QOS = "fujitsu-qos"
    UDP = "udp"
    NDI_SPEED_HQ = "ndi-speed-hq"


class Range:
    """Range enum values."""

    NARROW = "NARROW"
    FULL = "FULL"
    FULLPROTECT = "FULLPROTECT"


class ReservationState:
    """ReservationState enum values."""

    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"


class ResourceType:
    """ResourceType enum values."""

    MBPS_OUTBOUND_BANDWIDTH = "Mbps_Outbound_Bandwidth"


class RouterInputProtocol:
    """RouterInputProtocol enum values."""

    RTP = "RTP"
    RIST = "RIST"
    SRT_CALLER = "SRT_CALLER"
    SRT_LISTENER = "SRT_LISTENER"


class RouterInputState:
    """RouterInputState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"
    MIGRATING = "MIGRATING"


class RouterInputTier:
    """RouterInputTier enum values."""

    INPUT_100 = "INPUT_100"
    INPUT_50 = "INPUT_50"
    INPUT_20 = "INPUT_20"


class RouterInputTransitEncryptionKeyType:
    """RouterInputTransitEncryptionKeyType enum values."""

    SECRETS_MANAGER = "SECRETS_MANAGER"
    AUTOMATIC = "AUTOMATIC"


class RouterInputType:
    """RouterInputType enum values."""

    STANDARD = "STANDARD"
    FAILOVER = "FAILOVER"
    MERGE = "MERGE"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"


class RouterNetworkInterfaceState:
    """RouterNetworkInterfaceState enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"


class RouterNetworkInterfaceType:
    """RouterNetworkInterfaceType enum values."""

    PUBLIC = "PUBLIC"
    VPC = "VPC"


class RouterOutputProtocol:
    """RouterOutputProtocol enum values."""

    RTP = "RTP"
    RIST = "RIST"
    SRT_CALLER = "SRT_CALLER"
    SRT_LISTENER = "SRT_LISTENER"


class RouterOutputRoutedState:
    """RouterOutputRoutedState enum values."""

    ROUTED = "ROUTED"
    ROUTING = "ROUTING"
    UNROUTED = "UNROUTED"


class RouterOutputState:
    """RouterOutputState enum values."""

    CREATING = "CREATING"
    STANDBY = "STANDBY"
    STARTING = "STARTING"
    ACTIVE = "ACTIVE"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ERROR = "ERROR"
    RECOVERING = "RECOVERING"
    MIGRATING = "MIGRATING"


class RouterOutputTier:
    """RouterOutputTier enum values."""

    OUTPUT_100 = "OUTPUT_100"
    OUTPUT_50 = "OUTPUT_50"
    OUTPUT_20 = "OUTPUT_20"


class RouterOutputType:
    """RouterOutputType enum values."""

    STANDARD = "STANDARD"
    MEDIACONNECT_FLOW = "MEDIACONNECT_FLOW"
    MEDIALIVE_INPUT = "MEDIALIVE_INPUT"


class RoutingScope:
    """RoutingScope enum values."""

    REGIONAL = "REGIONAL"
    GLOBAL = "GLOBAL"


class ScanMode:
    """ScanMode enum values."""

    PROGRESSIVE = "progressive"
    INTERLACE = "interlace"
    PROGRESSIVE_SEGMENTED_FRAME = "progressive-segmented-frame"


class SourceType:
    """SourceType enum values."""

    OWNED = "OWNED"
    ENTITLED = "ENTITLED"


class State:
    """State enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Status:
    """Status enum values."""

    STANDBY = "STANDBY"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    ERROR = "ERROR"


class Tcs:
    """Tcs enum values."""

    SDR = "SDR"
    PQ = "PQ"
    HLG = "HLG"
    LINEAR = "LINEAR"
    BT2100LINPQ = "BT2100LINPQ"
    BT2100LINHLG = "BT2100LINHLG"
    ST2065_1 = "ST2065-1"
    ST428_1 = "ST428-1"
    DENSITY = "DENSITY"


class ThumbnailState:
    """ThumbnailState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class Encryption(PropertyType):
    SECRET_ARN = "SecretArn"
    KEY_TYPE = "KeyType"
    RESOURCE_ID = "ResourceId"
    DEVICE_ID = "DeviceId"
    REGION = "Region"
    CONSTANT_INITIALIZATION_VECTOR = "ConstantInitializationVector"
    ALGORITHM = "Algorithm"
    ROLE_ARN = "RoleArn"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "key_type": "KeyType",
        "resource_id": "ResourceId",
        "device_id": "DeviceId",
        "region": "Region",
        "constant_initialization_vector": "ConstantInitializationVector",
        "algorithm": "Algorithm",
        "role_arn": "RoleArn",
        "url": "Url",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None

