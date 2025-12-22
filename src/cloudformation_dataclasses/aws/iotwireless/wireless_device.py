"""PropertyTypes for AWS::IoTWireless::WirelessDevice."""

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
class AbpV10x(PropertyType):
    SESSION_KEYS = "SessionKeys"
    DEV_ADDR = "DevAddr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_keys": "SessionKeys",
        "dev_addr": "DevAddr",
    }

    session_keys: Optional[SessionKeysAbpV10x] = None
    dev_addr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AbpV11(PropertyType):
    SESSION_KEYS = "SessionKeys"
    DEV_ADDR = "DevAddr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_keys": "SessionKeys",
        "dev_addr": "DevAddr",
    }

    session_keys: Optional[SessionKeysAbpV11] = None
    dev_addr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Application(PropertyType):
    TYPE = "Type"
    F_PORT = "FPort"
    DESTINATION_NAME = "DestinationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "f_port": "FPort",
        "destination_name": "DestinationName",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    f_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FPorts(PropertyType):
    APPLICATIONS = "Applications"

    _property_mappings: ClassVar[dict[str, str]] = {
        "applications": "Applications",
    }

    applications: Optional[list[Application]] = None


@dataclass
class LoRaWANDevice(PropertyType):
    ABP_V10X = "AbpV10x"
    F_PORTS = "FPorts"
    OTAA_V11 = "OtaaV11"
    ABP_V11 = "AbpV11"
    DEVICE_PROFILE_ID = "DeviceProfileId"
    DEV_EUI = "DevEui"
    OTAA_V10X = "OtaaV10x"
    SERVICE_PROFILE_ID = "ServiceProfileId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "abp_v10x": "AbpV10x",
        "f_ports": "FPorts",
        "otaa_v11": "OtaaV11",
        "abp_v11": "AbpV11",
        "device_profile_id": "DeviceProfileId",
        "dev_eui": "DevEui",
        "otaa_v10x": "OtaaV10x",
        "service_profile_id": "ServiceProfileId",
    }

    abp_v10x: Optional[AbpV10x] = None
    f_ports: Optional[FPorts] = None
    otaa_v11: Optional[OtaaV11] = None
    abp_v11: Optional[AbpV11] = None
    device_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dev_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None
    otaa_v10x: Optional[OtaaV10x] = None
    service_profile_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OtaaV10x(PropertyType):
    APP_EUI = "AppEui"
    APP_KEY = "AppKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_eui": "AppEui",
        "app_key": "AppKey",
    }

    app_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OtaaV11(PropertyType):
    NWK_KEY = "NwkKey"
    APP_KEY = "AppKey"
    JOIN_EUI = "JoinEui"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nwk_key": "NwkKey",
        "app_key": "AppKey",
        "join_eui": "JoinEui",
    }

    nwk_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    join_eui: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionKeysAbpV10x(PropertyType):
    APP_S_KEY = "AppSKey"
    NWK_S_KEY = "NwkSKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_s_key": "AppSKey",
        "nwk_s_key": "NwkSKey",
    }

    app_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nwk_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SessionKeysAbpV11(PropertyType):
    F_NWK_S_INT_KEY = "FNwkSIntKey"
    APP_S_KEY = "AppSKey"
    S_NWK_S_INT_KEY = "SNwkSIntKey"
    NWK_S_ENC_KEY = "NwkSEncKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "f_nwk_s_int_key": "FNwkSIntKey",
        "app_s_key": "AppSKey",
        "s_nwk_s_int_key": "SNwkSIntKey",
        "nwk_s_enc_key": "NwkSEncKey",
    }

    f_nwk_s_int_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    app_s_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s_nwk_s_int_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nwk_s_enc_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

