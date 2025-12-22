"""PropertyTypes for AWS::IoTWireless::ServiceProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AggregationPeriod:
    """AggregationPeriod enum values."""

    ONEHOUR = "OneHour"
    ONEDAY = "OneDay"
    ONEWEEK = "OneWeek"


class ApplicationConfigType:
    """ApplicationConfigType enum values."""

    SEMTECHGEOLOCATION = "SemtechGeolocation"


class BatteryLevel:
    """BatteryLevel enum values."""

    NORMAL = "normal"
    LOW = "low"
    CRITICAL = "critical"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"


class DeviceProfileType:
    """DeviceProfileType enum values."""

    SIDEWALK = "Sidewalk"
    LORAWAN = "LoRaWAN"


class DeviceState:
    """DeviceState enum values."""

    PROVISIONED = "Provisioned"
    REGISTEREDNOTSEEN = "RegisteredNotSeen"
    REGISTEREDREACHABLE = "RegisteredReachable"
    REGISTEREDUNREACHABLE = "RegisteredUnreachable"


class DimensionName:
    """DimensionName enum values."""

    DEVICEID = "DeviceId"
    GATEWAYID = "GatewayId"


class DlClass:
    """DlClass enum values."""

    CLASSB = "ClassB"
    CLASSC = "ClassC"


class DownlinkMode:
    """DownlinkMode enum values."""

    SEQUENTIAL = "SEQUENTIAL"
    CONCURRENT = "CONCURRENT"
    USING_UPLINK_GATEWAY = "USING_UPLINK_GATEWAY"


class Event:
    """Event enum values."""

    DISCOVERED = "discovered"
    LOST = "lost"
    ACK = "ack"
    NACK = "nack"
    PASSTHROUGH = "passthrough"


class EventNotificationPartnerType:
    """EventNotificationPartnerType enum values."""

    SIDEWALK = "Sidewalk"


class EventNotificationResourceType:
    """EventNotificationResourceType enum values."""

    SIDEWALKACCOUNT = "SidewalkAccount"
    WIRELESSDEVICE = "WirelessDevice"
    WIRELESSGATEWAY = "WirelessGateway"


class EventNotificationTopicStatus:
    """EventNotificationTopicStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpressionType:
    """ExpressionType enum values."""

    RULENAME = "RuleName"
    MQTTTOPIC = "MqttTopic"


class FuotaDeviceStatus:
    """FuotaDeviceStatus enum values."""

    INITIAL = "Initial"
    PACKAGE_NOT_SUPPORTED = "Package_Not_Supported"
    FRAGALGO_UNSUPPORTED = "FragAlgo_unsupported"
    NOT_ENOUGH_MEMORY = "Not_enough_memory"
    FRAGINDEX_UNSUPPORTED = "FragIndex_unsupported"
    WRONG_DESCRIPTOR = "Wrong_descriptor"
    SESSIONCNT_REPLAY = "SessionCnt_replay"
    MISSINGFRAG = "MissingFrag"
    MEMORYERROR = "MemoryError"
    MICERROR = "MICError"
    SUCCESSFUL = "Successful"
    DEVICE_EXIST_IN_CONFLICT_FUOTA_TASK = "Device_exist_in_conflict_fuota_task"


class FuotaTaskEvent:
    """FuotaTaskEvent enum values."""

    FUOTA = "Fuota"


class FuotaTaskStatus:
    """FuotaTaskStatus enum values."""

    PENDING = "Pending"
    FUOTASESSION_WAITING = "FuotaSession_Waiting"
    IN_FUOTASESSION = "In_FuotaSession"
    FUOTADONE = "FuotaDone"
    DELETE_WAITING = "Delete_Waiting"


class FuotaTaskType:
    """FuotaTaskType enum values."""

    LORAWAN = "LoRaWAN"


class IdentifierType:
    """IdentifierType enum values."""

    PARTNERACCOUNTID = "PartnerAccountId"
    DEVEUI = "DevEui"
    GATEWAYEUI = "GatewayEui"
    WIRELESSDEVICEID = "WirelessDeviceId"
    WIRELESSGATEWAYID = "WirelessGatewayId"


class ImportTaskStatus:
    """ImportTaskStatus enum values."""

    INITIALIZING = "INITIALIZING"
    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    DELETING = "DELETING"


class LogLevel:
    """LogLevel enum values."""

    INFO = "INFO"
    ERROR = "ERROR"
    DISABLED = "DISABLED"


class MessageType:
    """MessageType enum values."""

    CUSTOM_COMMAND_ID_NOTIFY = "CUSTOM_COMMAND_ID_NOTIFY"
    CUSTOM_COMMAND_ID_GET = "CUSTOM_COMMAND_ID_GET"
    CUSTOM_COMMAND_ID_SET = "CUSTOM_COMMAND_ID_SET"
    CUSTOM_COMMAND_ID_RESP = "CUSTOM_COMMAND_ID_RESP"


class MetricName:
    """MetricName enum values."""

    DEVICERSSI = "DeviceRSSI"
    DEVICESNR = "DeviceSNR"
    DEVICEROAMINGRSSI = "DeviceRoamingRSSI"
    DEVICEROAMINGSNR = "DeviceRoamingSNR"
    DEVICEUPLINKCOUNT = "DeviceUplinkCount"
    DEVICEDOWNLINKCOUNT = "DeviceDownlinkCount"
    DEVICEUPLINKLOSTCOUNT = "DeviceUplinkLostCount"
    DEVICEUPLINKLOSTRATE = "DeviceUplinkLostRate"
    DEVICEJOINREQUESTCOUNT = "DeviceJoinRequestCount"
    DEVICEJOINACCEPTCOUNT = "DeviceJoinAcceptCount"
    DEVICEROAMINGUPLINKCOUNT = "DeviceRoamingUplinkCount"
    DEVICEROAMINGDOWNLINKCOUNT = "DeviceRoamingDownlinkCount"
    GATEWAYUPTIME = "GatewayUpTime"
    GATEWAYDOWNTIME = "GatewayDownTime"
    GATEWAYRSSI = "GatewayRSSI"
    GATEWAYSNR = "GatewaySNR"
    GATEWAYUPLINKCOUNT = "GatewayUplinkCount"
    GATEWAYDOWNLINKCOUNT = "GatewayDownlinkCount"
    GATEWAYJOINREQUESTCOUNT = "GatewayJoinRequestCount"
    GATEWAYJOINACCEPTCOUNT = "GatewayJoinAcceptCount"
    AWSACCOUNTUPLINKCOUNT = "AwsAccountUplinkCount"
    AWSACCOUNTDOWNLINKCOUNT = "AwsAccountDownlinkCount"
    AWSACCOUNTUPLINKLOSTCOUNT = "AwsAccountUplinkLostCount"
    AWSACCOUNTUPLINKLOSTRATE = "AwsAccountUplinkLostRate"
    AWSACCOUNTJOINREQUESTCOUNT = "AwsAccountJoinRequestCount"
    AWSACCOUNTJOINACCEPTCOUNT = "AwsAccountJoinAcceptCount"
    AWSACCOUNTROAMINGUPLINKCOUNT = "AwsAccountRoamingUplinkCount"
    AWSACCOUNTROAMINGDOWNLINKCOUNT = "AwsAccountRoamingDownlinkCount"
    AWSACCOUNTDEVICECOUNT = "AwsAccountDeviceCount"
    AWSACCOUNTGATEWAYCOUNT = "AwsAccountGatewayCount"
    AWSACCOUNTACTIVEDEVICECOUNT = "AwsAccountActiveDeviceCount"
    AWSACCOUNTACTIVEGATEWAYCOUNT = "AwsAccountActiveGatewayCount"


class MetricQueryStatus:
    """MetricQueryStatus enum values."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class MulticastFrameInfo:
    """MulticastFrameInfo enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OnboardStatus:
    """OnboardStatus enum values."""

    INITIALIZED = "INITIALIZED"
    PENDING = "PENDING"
    ONBOARDED = "ONBOARDED"
    FAILED = "FAILED"


class PartnerType:
    """PartnerType enum values."""

    SIDEWALK = "Sidewalk"


class PositionConfigurationFec:
    """PositionConfigurationFec enum values."""

    ROSE = "ROSE"
    NONE = "NONE"


class PositionConfigurationStatus:
    """PositionConfigurationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PositionResourceType:
    """PositionResourceType enum values."""

    WIRELESSDEVICE = "WirelessDevice"
    WIRELESSGATEWAY = "WirelessGateway"


class PositionSolverProvider:
    """PositionSolverProvider enum values."""

    SEMTECH = "Semtech"


class PositionSolverType:
    """PositionSolverType enum values."""

    GNSS = "GNSS"


class PositioningConfigStatus:
    """PositioningConfigStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SigningAlg:
    """SigningAlg enum values."""

    ED25519 = "Ed25519"
    P256R1 = "P256r1"


class SummaryMetricConfigurationStatus:
    """SummaryMetricConfigurationStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SupportedRfRegion:
    """SupportedRfRegion enum values."""

    EU868 = "EU868"
    US915 = "US915"
    AU915 = "AU915"
    AS923_1 = "AS923-1"
    AS923_2 = "AS923-2"
    AS923_3 = "AS923-3"
    AS923_4 = "AS923-4"
    EU433 = "EU433"
    CN470 = "CN470"
    CN779 = "CN779"
    RU864 = "RU864"
    KR920 = "KR920"
    IN865 = "IN865"


class WirelessDeviceEvent:
    """WirelessDeviceEvent enum values."""

    JOIN = "Join"
    REJOIN = "Rejoin"
    UPLINK_DATA = "Uplink_Data"
    DOWNLINK_DATA = "Downlink_Data"
    REGISTRATION = "Registration"


class WirelessDeviceFrameInfo:
    """WirelessDeviceFrameInfo enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WirelessDeviceIdType:
    """WirelessDeviceIdType enum values."""

    WIRELESSDEVICEID = "WirelessDeviceId"
    DEVEUI = "DevEui"
    THINGNAME = "ThingName"
    SIDEWALKMANUFACTURINGSN = "SidewalkManufacturingSn"


class WirelessDeviceSidewalkStatus:
    """WirelessDeviceSidewalkStatus enum values."""

    PROVISIONED = "PROVISIONED"
    REGISTERED = "REGISTERED"
    ACTIVATED = "ACTIVATED"
    UNKNOWN = "UNKNOWN"


class WirelessDeviceType:
    """WirelessDeviceType enum values."""

    SIDEWALK = "Sidewalk"
    LORAWAN = "LoRaWAN"


class WirelessGatewayEvent:
    """WirelessGatewayEvent enum values."""

    CUPS_REQUEST = "CUPS_Request"
    CERTIFICATE = "Certificate"


class WirelessGatewayIdType:
    """WirelessGatewayIdType enum values."""

    GATEWAYEUI = "GatewayEui"
    WIRELESSGATEWAYID = "WirelessGatewayId"
    THINGNAME = "ThingName"


class WirelessGatewayServiceType:
    """WirelessGatewayServiceType enum values."""

    CUPS = "CUPS"
    LNS = "LNS"


class WirelessGatewayTaskDefinitionType:
    """WirelessGatewayTaskDefinitionType enum values."""

    UPDATE = "UPDATE"


class WirelessGatewayTaskStatus:
    """WirelessGatewayTaskStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FIRST_RETRY = "FIRST_RETRY"
    SECOND_RETRY = "SECOND_RETRY"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class WirelessGatewayType:
    """WirelessGatewayType enum values."""

    LORAWAN = "LoRaWAN"


@dataclass
class LoRaWANServiceProfile(PropertyType):
    DL_BUCKET_SIZE = "DlBucketSize"
    MIN_GW_DIVERSITY = "MinGwDiversity"
    DR_MAX = "DrMax"
    REPORT_DEV_STATUS_MARGIN = "ReportDevStatusMargin"
    PR_ALLOWED = "PrAllowed"
    DL_RATE = "DlRate"
    UL_RATE_POLICY = "UlRatePolicy"
    REPORT_DEV_STATUS_BATTERY = "ReportDevStatusBattery"
    CHANNEL_MASK = "ChannelMask"
    UL_RATE = "UlRate"
    ADD_GW_METADATA = "AddGwMetadata"
    DL_RATE_POLICY = "DlRatePolicy"
    HR_ALLOWED = "HrAllowed"
    DR_MIN = "DrMin"
    TARGET_PER = "TargetPer"
    NWK_GEO_LOC = "NwkGeoLoc"
    DEV_STATUS_REQ_FREQ = "DevStatusReqFreq"
    UL_BUCKET_SIZE = "UlBucketSize"
    RA_ALLOWED = "RaAllowed"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dl_bucket_size": "DlBucketSize",
        "min_gw_diversity": "MinGwDiversity",
        "dr_max": "DrMax",
        "report_dev_status_margin": "ReportDevStatusMargin",
        "pr_allowed": "PrAllowed",
        "dl_rate": "DlRate",
        "ul_rate_policy": "UlRatePolicy",
        "report_dev_status_battery": "ReportDevStatusBattery",
        "channel_mask": "ChannelMask",
        "ul_rate": "UlRate",
        "add_gw_metadata": "AddGwMetadata",
        "dl_rate_policy": "DlRatePolicy",
        "hr_allowed": "HrAllowed",
        "dr_min": "DrMin",
        "target_per": "TargetPer",
        "nwk_geo_loc": "NwkGeoLoc",
        "dev_status_req_freq": "DevStatusReqFreq",
        "ul_bucket_size": "UlBucketSize",
        "ra_allowed": "RaAllowed",
    }

    dl_bucket_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_gw_diversity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    dr_max: Optional[Union[int, Ref, GetAtt, Sub]] = None
    report_dev_status_margin: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    pr_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dl_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ul_rate_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    report_dev_status_battery: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    channel_mask: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ul_rate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    add_gw_metadata: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dl_rate_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hr_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dr_min: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target_per: Optional[Union[int, Ref, GetAtt, Sub]] = None
    nwk_geo_loc: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dev_status_req_freq: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ul_bucket_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ra_allowed: Optional[Union[bool, Ref, GetAtt, Sub]] = None

