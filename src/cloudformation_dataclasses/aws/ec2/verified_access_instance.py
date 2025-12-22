"""PropertyTypes for AWS::EC2::VerifiedAccessInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorManufacturer:
    """AcceleratorManufacturer enum values."""

    AMAZON_WEB_SERVICES = "amazon-web-services"
    AMD = "amd"
    NVIDIA = "nvidia"
    XILINX = "xilinx"
    HABANA = "habana"


class AcceleratorName:
    """AcceleratorName enum values."""

    A100 = "a100"
    INFERENTIA = "inferentia"
    K520 = "k520"
    K80 = "k80"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    T4 = "t4"
    VU9P = "vu9p"
    V100 = "v100"
    A10G = "a10g"
    H100 = "h100"
    T4G = "t4g"
    L40S = "l40s"
    L4 = "l4"
    GAUDI_HL_205 = "gaudi-hl-205"
    INFERENTIA2 = "inferentia2"
    TRAINIUM = "trainium"
    TRAINIUM2 = "trainium2"
    U30 = "u30"


class AcceleratorType:
    """AcceleratorType enum values."""

    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"
    MEDIA = "media"


class AccountAttributeName:
    """AccountAttributeName enum values."""

    SUPPORTED_PLATFORMS = "supported-platforms"
    DEFAULT_VPC = "default-vpc"


class ActivityStatus:
    """ActivityStatus enum values."""

    ERROR = "error"
    PENDING_FULFILLMENT = "pending_fulfillment"
    PENDING_TERMINATION = "pending_termination"
    FULFILLED = "fulfilled"


class AddressAttributeName:
    """AddressAttributeName enum values."""

    DOMAIN_NAME = "domain-name"


class AddressFamily:
    """AddressFamily enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class AddressTransferStatus:
    """AddressTransferStatus enum values."""

    PENDING = "pending"
    DISABLED = "disabled"
    ACCEPTED = "accepted"


class Affinity:
    """Affinity enum values."""

    DEFAULT = "default"
    HOST = "host"


class AllocationState:
    """AllocationState enum values."""

    AVAILABLE = "available"
    UNDER_ASSESSMENT = "under-assessment"
    PERMANENT_FAILURE = "permanent-failure"
    RELEASED = "released"
    RELEASED_PERMANENT_FAILURE = "released-permanent-failure"
    PENDING = "pending"


class AllocationStrategy:
    """AllocationStrategy enum values."""

    LOWESTPRICE = "lowestPrice"
    DIVERSIFIED = "diversified"
    CAPACITYOPTIMIZED = "capacityOptimized"
    CAPACITYOPTIMIZEDPRIORITIZED = "capacityOptimizedPrioritized"
    PRICECAPACITYOPTIMIZED = "priceCapacityOptimized"


class AllocationType:
    """AllocationType enum values."""

    USED = "used"
    FUTURE = "future"


class AllowedImagesSettingsDisabledState:
    """AllowedImagesSettingsDisabledState enum values."""

    DISABLED = "disabled"


class AllowedImagesSettingsEnabledState:
    """AllowedImagesSettingsEnabledState enum values."""

    ENABLED = "enabled"
    AUDIT_MODE = "audit-mode"


class AllowsMultipleInstanceTypes:
    """AllowsMultipleInstanceTypes enum values."""

    ON = "on"
    OFF = "off"


class AmdSevSnpSpecification:
    """AmdSevSnpSpecification enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class AnalysisStatus:
    """AnalysisStatus enum values."""

    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class ApplianceModeSupportValue:
    """ApplianceModeSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class ArchitectureType:
    """ArchitectureType enum values."""

    I386 = "i386"
    X86_64 = "x86_64"
    ARM64 = "arm64"
    X86_64_MAC = "x86_64_mac"
    ARM64_MAC = "arm64_mac"


class ArchitectureValues:
    """ArchitectureValues enum values."""

    I386 = "i386"
    X86_64 = "x86_64"
    ARM64 = "arm64"
    X86_64_MAC = "x86_64_mac"
    ARM64_MAC = "arm64_mac"


class AsnAssociationState:
    """AsnAssociationState enum values."""

    DISASSOCIATED = "disassociated"
    FAILED_DISASSOCIATION = "failed-disassociation"
    FAILED_ASSOCIATION = "failed-association"
    PENDING_DISASSOCIATION = "pending-disassociation"
    PENDING_ASSOCIATION = "pending-association"
    ASSOCIATED = "associated"


class AsnState:
    """AsnState enum values."""

    DEPROVISIONED = "deprovisioned"
    FAILED_DEPROVISION = "failed-deprovision"
    FAILED_PROVISION = "failed-provision"
    PENDING_DEPROVISION = "pending-deprovision"
    PENDING_PROVISION = "pending-provision"
    PROVISIONED = "provisioned"


class AssociatedNetworkType:
    """AssociatedNetworkType enum values."""

    VPC = "vpc"


class AssociationStatusCode:
    """AssociationStatusCode enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    ASSOCIATION_FAILED = "association-failed"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"


class AttachmentLimitType:
    """AttachmentLimitType enum values."""

    SHARED = "shared"
    DEDICATED = "dedicated"


class AttachmentStatus:
    """AttachmentStatus enum values."""

    ATTACHING = "attaching"
    ATTACHED = "attached"
    DETACHING = "detaching"
    DETACHED = "detached"


class AutoAcceptSharedAssociationsValue:
    """AutoAcceptSharedAssociationsValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class AutoAcceptSharedAttachmentsValue:
    """AutoAcceptSharedAttachmentsValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class AutoPlacement:
    """AutoPlacement enum values."""

    ON = "on"
    OFF = "off"


class AutoProvisionZonesState:
    """AutoProvisionZonesState enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class AutoScalingIpsState:
    """AutoScalingIpsState enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class AvailabilityMode:
    """AvailabilityMode enum values."""

    ZONAL = "zonal"
    REGIONAL = "regional"


class AvailabilityZoneOptInStatus:
    """AvailabilityZoneOptInStatus enum values."""

    OPT_IN_NOT_REQUIRED = "opt-in-not-required"
    OPTED_IN = "opted-in"
    NOT_OPTED_IN = "not-opted-in"


class AvailabilityZoneState:
    """AvailabilityZoneState enum values."""

    AVAILABLE = "available"
    INFORMATION = "information"
    IMPAIRED = "impaired"
    UNAVAILABLE = "unavailable"
    CONSTRAINED = "constrained"


class BandwidthWeightingType:
    """BandwidthWeightingType enum values."""

    DEFAULT = "default"
    VPC_1 = "vpc-1"
    EBS_1 = "ebs-1"


class BareMetal:
    """BareMetal enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class BatchState:
    """BatchState enum values."""

    SUBMITTED = "submitted"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    FAILED = "failed"
    CANCELLED_RUNNING = "cancelled_running"
    CANCELLED_TERMINATING = "cancelled_terminating"
    MODIFYING = "modifying"


class BgpStatus:
    """BgpStatus enum values."""

    UP = "up"
    DOWN = "down"


class BlockPublicAccessMode:
    """BlockPublicAccessMode enum values."""

    OFF = "off"
    BLOCK_BIDIRECTIONAL = "block-bidirectional"
    BLOCK_INGRESS = "block-ingress"


class BootModeType:
    """BootModeType enum values."""

    LEGACY_BIOS = "legacy-bios"
    UEFI = "uefi"


class BootModeValues:
    """BootModeValues enum values."""

    LEGACY_BIOS = "legacy-bios"
    UEFI = "uefi"
    UEFI_PREFERRED = "uefi-preferred"


class BundleTaskState:
    """BundleTaskState enum values."""

    PENDING = "pending"
    WAITING_FOR_SHUTDOWN = "waiting-for-shutdown"
    BUNDLING = "bundling"
    STORING = "storing"
    CANCELLING = "cancelling"
    COMPLETE = "complete"
    FAILED = "failed"


class BurstablePerformance:
    """BurstablePerformance enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class ByoipCidrState:
    """ByoipCidrState enum values."""

    ADVERTISED = "advertised"
    DEPROVISIONED = "deprovisioned"
    FAILED_DEPROVISION = "failed-deprovision"
    FAILED_PROVISION = "failed-provision"
    PENDING_ADVERTISING = "pending-advertising"
    PENDING_DEPROVISION = "pending-deprovision"
    PENDING_PROVISION = "pending-provision"
    PENDING_WITHDRAWAL = "pending-withdrawal"
    PROVISIONED = "provisioned"
    PROVISIONED_NOT_PUBLICLY_ADVERTISABLE = "provisioned-not-publicly-advertisable"


class CallerRole:
    """CallerRole enum values."""

    ODCR_OWNER = "odcr-owner"
    UNUSED_RESERVATION_BILLING_OWNER = "unused-reservation-billing-owner"


class CancelBatchErrorCode:
    """CancelBatchErrorCode enum values."""

    FLEETREQUESTIDDOESNOTEXIST = "fleetRequestIdDoesNotExist"
    FLEETREQUESTIDMALFORMED = "fleetRequestIdMalformed"
    FLEETREQUESTNOTINCANCELLABLESTATE = "fleetRequestNotInCancellableState"
    UNEXPECTEDERROR = "unexpectedError"


class CancelSpotInstanceRequestState:
    """CancelSpotInstanceRequestState enum values."""

    ACTIVE = "active"
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class CapacityBlockExtensionStatus:
    """CapacityBlockExtensionStatus enum values."""

    PAYMENT_PENDING = "payment-pending"
    PAYMENT_FAILED = "payment-failed"
    PAYMENT_SUCCEEDED = "payment-succeeded"


class CapacityBlockInterconnectStatus:
    """CapacityBlockInterconnectStatus enum values."""

    OK = "ok"
    IMPAIRED = "impaired"
    INSUFFICIENT_DATA = "insufficient-data"


class CapacityBlockResourceState:
    """CapacityBlockResourceState enum values."""

    ACTIVE = "active"
    EXPIRED = "expired"
    UNAVAILABLE = "unavailable"
    CANCELLED = "cancelled"
    FAILED = "failed"
    SCHEDULED = "scheduled"
    PAYMENT_PENDING = "payment-pending"
    PAYMENT_FAILED = "payment-failed"


class CapacityManagerDataExportStatus:
    """CapacityManagerDataExportStatus enum values."""

    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    DELIVERED = "delivered"
    FAILED = "failed"


class CapacityManagerStatus:
    """CapacityManagerStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class CapacityReservationBillingRequestStatus:
    """CapacityReservationBillingRequestStatus enum values."""

    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    REVOKED = "revoked"
    EXPIRED = "expired"


class CapacityReservationDeliveryPreference:
    """CapacityReservationDeliveryPreference enum values."""

    FIXED = "fixed"
    INCREMENTAL = "incremental"


class CapacityReservationFleetState:
    """CapacityReservationFleetState enum values."""

    SUBMITTED = "submitted"
    MODIFYING = "modifying"
    ACTIVE = "active"
    PARTIALLY_FULFILLED = "partially_fulfilled"
    EXPIRING = "expiring"
    EXPIRED = "expired"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    FAILED = "failed"


class CapacityReservationInstancePlatform:
    """CapacityReservationInstancePlatform enum values."""

    LINUX_UNIX = "Linux/UNIX"
    RED_HAT_ENTERPRISE_LINUX = "Red Hat Enterprise Linux"
    SUSE_LINUX = "SUSE Linux"
    WINDOWS = "Windows"
    WINDOWS_WITH_SQL_SERVER = "Windows with SQL Server"
    WINDOWS_WITH_SQL_SERVER_ENTERPRISE = "Windows with SQL Server Enterprise"
    WINDOWS_WITH_SQL_SERVER_STANDARD = "Windows with SQL Server Standard"
    WINDOWS_WITH_SQL_SERVER_WEB = "Windows with SQL Server Web"
    LINUX_WITH_SQL_SERVER_STANDARD = "Linux with SQL Server Standard"
    LINUX_WITH_SQL_SERVER_WEB = "Linux with SQL Server Web"
    LINUX_WITH_SQL_SERVER_ENTERPRISE = "Linux with SQL Server Enterprise"
    RHEL_WITH_SQL_SERVER_STANDARD = "RHEL with SQL Server Standard"
    RHEL_WITH_SQL_SERVER_ENTERPRISE = "RHEL with SQL Server Enterprise"
    RHEL_WITH_SQL_SERVER_WEB = "RHEL with SQL Server Web"
    RHEL_WITH_HA = "RHEL with HA"
    RHEL_WITH_HA_AND_SQL_SERVER_STANDARD = "RHEL with HA and SQL Server Standard"
    RHEL_WITH_HA_AND_SQL_SERVER_ENTERPRISE = "RHEL with HA and SQL Server Enterprise"
    UBUNTU_PRO = "Ubuntu Pro"


class CapacityReservationPreference:
    """CapacityReservationPreference enum values."""

    CAPACITY_RESERVATIONS_ONLY = "capacity-reservations-only"
    OPEN = "open"
    NONE = "none"


class CapacityReservationState:
    """CapacityReservationState enum values."""

    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    PENDING = "pending"
    FAILED = "failed"
    SCHEDULED = "scheduled"
    PAYMENT_PENDING = "payment-pending"
    PAYMENT_FAILED = "payment-failed"
    ASSESSING = "assessing"
    DELAYED = "delayed"
    UNSUPPORTED = "unsupported"
    UNAVAILABLE = "unavailable"


class CapacityReservationTenancy:
    """CapacityReservationTenancy enum values."""

    DEFAULT = "default"
    DEDICATED = "dedicated"


class CapacityReservationType:
    """CapacityReservationType enum values."""

    DEFAULT = "default"
    CAPACITY_BLOCK = "capacity-block"


class CapacityTenancy:
    """CapacityTenancy enum values."""

    DEFAULT = "default"
    DEDICATED = "dedicated"


class CarrierGatewayState:
    """CarrierGatewayState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class ClientCertificateRevocationListStatusCode:
    """ClientCertificateRevocationListStatusCode enum values."""

    PENDING = "pending"
    ACTIVE = "active"


class ClientVpnAuthenticationType:
    """ClientVpnAuthenticationType enum values."""

    CERTIFICATE_AUTHENTICATION = "certificate-authentication"
    DIRECTORY_SERVICE_AUTHENTICATION = "directory-service-authentication"
    FEDERATED_AUTHENTICATION = "federated-authentication"


class ClientVpnAuthorizationRuleStatusCode:
    """ClientVpnAuthorizationRuleStatusCode enum values."""

    AUTHORIZING = "authorizing"
    ACTIVE = "active"
    FAILED = "failed"
    REVOKING = "revoking"


class ClientVpnConnectionStatusCode:
    """ClientVpnConnectionStatusCode enum values."""

    ACTIVE = "active"
    FAILED_TO_TERMINATE = "failed-to-terminate"
    TERMINATING = "terminating"
    TERMINATED = "terminated"


class ClientVpnEndpointAttributeStatusCode:
    """ClientVpnEndpointAttributeStatusCode enum values."""

    APPLYING = "applying"
    APPLIED = "applied"


class ClientVpnEndpointStatusCode:
    """ClientVpnEndpointStatusCode enum values."""

    PENDING_ASSOCIATE = "pending-associate"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class ClientVpnRouteStatusCode:
    """ClientVpnRouteStatusCode enum values."""

    CREATING = "creating"
    ACTIVE = "active"
    FAILED = "failed"
    DELETING = "deleting"


class Comparison:
    """Comparison enum values."""

    EQUALS = "equals"
    IN = "in"


class ConnectionNotificationState:
    """ConnectionNotificationState enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ConnectionNotificationType:
    """ConnectionNotificationType enum values."""

    TOPIC = "Topic"


class ConnectivityType:
    """ConnectivityType enum values."""

    PRIVATE = "private"
    PUBLIC = "public"


class ContainerFormat:
    """ContainerFormat enum values."""

    OVA = "ova"


class ConversionTaskState:
    """ConversionTaskState enum values."""

    ACTIVE = "active"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class CopyTagsFromSource:
    """CopyTagsFromSource enum values."""

    VOLUME = "volume"


class CpuManufacturer:
    """CpuManufacturer enum values."""

    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    APPLE = "apple"


class CurrencyCodeValues:
    """CurrencyCodeValues enum values."""

    USD = "USD"


class DatafeedSubscriptionState:
    """DatafeedSubscriptionState enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class DefaultInstanceMetadataEndpointState:
    """DefaultInstanceMetadataEndpointState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"
    NO_PREFERENCE = "no-preference"


class DefaultInstanceMetadataTagsState:
    """DefaultInstanceMetadataTagsState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"
    NO_PREFERENCE = "no-preference"


class DefaultRouteTableAssociationValue:
    """DefaultRouteTableAssociationValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class DefaultRouteTablePropagationValue:
    """DefaultRouteTablePropagationValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class DefaultTargetCapacityType:
    """DefaultTargetCapacityType enum values."""

    SPOT = "spot"
    ON_DEMAND = "on-demand"
    CAPACITY_BLOCK = "capacity-block"


class DeleteFleetErrorCode:
    """DeleteFleetErrorCode enum values."""

    FLEETIDDOESNOTEXIST = "fleetIdDoesNotExist"
    FLEETIDMALFORMED = "fleetIdMalformed"
    FLEETNOTINDELETABLESTATE = "fleetNotInDeletableState"
    UNEXPECTEDERROR = "unexpectedError"


class DeleteQueuedReservedInstancesErrorCode:
    """DeleteQueuedReservedInstancesErrorCode enum values."""

    RESERVED_INSTANCES_ID_INVALID = "reserved-instances-id-invalid"
    RESERVED_INSTANCES_NOT_IN_QUEUED_STATE = "reserved-instances-not-in-queued-state"
    UNEXPECTED_ERROR = "unexpected-error"


class DestinationFileFormat:
    """DestinationFileFormat enum values."""

    PLAIN_TEXT = "plain-text"
    PARQUET = "parquet"


class DeviceTrustProviderType:
    """DeviceTrustProviderType enum values."""

    JAMF = "jamf"
    CROWDSTRIKE = "crowdstrike"
    JUMPCLOUD = "jumpcloud"


class DeviceType:
    """DeviceType enum values."""

    EBS = "ebs"
    INSTANCE_STORE = "instance-store"


class DiskImageFormat:
    """DiskImageFormat enum values."""

    VMDK = "VMDK"
    RAW = "RAW"
    VHD = "VHD"


class DiskType:
    """DiskType enum values."""

    HDD = "hdd"
    SSD = "ssd"


class DnsNameState:
    """DnsNameState enum values."""

    PENDINGVERIFICATION = "pendingVerification"
    VERIFIED = "verified"
    FAILED = "failed"


class DnsRecordIpType:
    """DnsRecordIpType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"
    IPV6 = "ipv6"
    SERVICE_DEFINED = "service-defined"


class DnsSupportValue:
    """DnsSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class DomainType:
    """DomainType enum values."""

    VPC = "vpc"
    STANDARD = "standard"


class DynamicRoutingValue:
    """DynamicRoutingValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class EbsEncryptionSupport:
    """EbsEncryptionSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class EbsNvmeSupport:
    """EbsNvmeSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"
    REQUIRED = "required"


class EbsOptimizedSupport:
    """EbsOptimizedSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"
    DEFAULT = "default"


class Ec2InstanceConnectEndpointState:
    """Ec2InstanceConnectEndpointState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    UPDATE_IN_PROGRESS = "update-in-progress"
    UPDATE_COMPLETE = "update-complete"
    UPDATE_FAILED = "update-failed"


class EkPubKeyFormat:
    """EkPubKeyFormat enum values."""

    DER = "der"
    TPMT = "tpmt"


class EkPubKeyType:
    """EkPubKeyType enum values."""

    RSA_2048 = "rsa-2048"
    ECC_SEC_P384 = "ecc-sec-p384"


class ElasticGpuState:
    """ElasticGpuState enum values."""

    ATTACHED = "ATTACHED"


class ElasticGpuStatus:
    """ElasticGpuStatus enum values."""

    OK = "OK"
    IMPAIRED = "IMPAIRED"


class EnaSupport:
    """EnaSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"
    REQUIRED = "required"


class EncryptionStateValue:
    """EncryptionStateValue enum values."""

    ENABLING = "enabling"
    ENABLED = "enabled"
    DISABLING = "disabling"
    DISABLED = "disabled"


class EncryptionSupportOptionValue:
    """EncryptionSupportOptionValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class EndDateType:
    """EndDateType enum values."""

    UNLIMITED = "unlimited"
    LIMITED = "limited"


class EndpointIpAddressType:
    """EndpointIpAddressType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUAL_STACK = "dual-stack"


class EphemeralNvmeSupport:
    """EphemeralNvmeSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"
    REQUIRED = "required"


class EventCode:
    """EventCode enum values."""

    INSTANCE_REBOOT = "instance-reboot"
    SYSTEM_REBOOT = "system-reboot"
    SYSTEM_MAINTENANCE = "system-maintenance"
    INSTANCE_RETIREMENT = "instance-retirement"
    INSTANCE_STOP = "instance-stop"


class EventType:
    """EventType enum values."""

    INSTANCECHANGE = "instanceChange"
    FLEETREQUESTCHANGE = "fleetRequestChange"
    ERROR = "error"
    INFORMATION = "information"


class ExcessCapacityTerminationPolicy:
    """ExcessCapacityTerminationPolicy enum values."""

    NOTERMINATION = "noTermination"
    DEFAULT = "default"


class ExportEnvironment:
    """ExportEnvironment enum values."""

    CITRIX = "citrix"
    VMWARE = "vmware"
    MICROSOFT = "microsoft"


class ExportTaskState:
    """ExportTaskState enum values."""

    ACTIVE = "active"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class FastLaunchResourceType:
    """FastLaunchResourceType enum values."""

    SNAPSHOT = "snapshot"


class FastLaunchStateCode:
    """FastLaunchStateCode enum values."""

    ENABLING = "enabling"
    ENABLING_FAILED = "enabling-failed"
    ENABLED = "enabled"
    ENABLED_FAILED = "enabled-failed"
    DISABLING = "disabling"
    DISABLING_FAILED = "disabling-failed"


class FastSnapshotRestoreStateCode:
    """FastSnapshotRestoreStateCode enum values."""

    ENABLING = "enabling"
    OPTIMIZING = "optimizing"
    ENABLED = "enabled"
    DISABLING = "disabling"
    DISABLED = "disabled"


class FilterByDimension:
    """FilterByDimension enum values."""

    RESOURCE_REGION = "resource-region"
    AVAILABILITY_ZONE_ID = "availability-zone-id"
    ACCOUNT_ID = "account-id"
    INSTANCE_FAMILY = "instance-family"
    INSTANCE_TYPE = "instance-type"
    INSTANCE_PLATFORM = "instance-platform"
    RESERVATION_ARN = "reservation-arn"
    RESERVATION_ID = "reservation-id"
    RESERVATION_TYPE = "reservation-type"
    RESERVATION_CREATE_TIMESTAMP = "reservation-create-timestamp"
    RESERVATION_START_TIMESTAMP = "reservation-start-timestamp"
    RESERVATION_END_TIMESTAMP = "reservation-end-timestamp"
    RESERVATION_END_DATE_TYPE = "reservation-end-date-type"
    TENANCY = "tenancy"
    RESERVATION_STATE = "reservation-state"
    RESERVATION_INSTANCE_MATCH_CRITERIA = "reservation-instance-match-criteria"
    RESERVATION_UNUSED_FINANCIAL_OWNER = "reservation-unused-financial-owner"


class FindingsFound:
    """FindingsFound enum values."""

    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"


class FleetActivityStatus:
    """FleetActivityStatus enum values."""

    ERROR = "error"
    PENDING_FULFILLMENT = "pending_fulfillment"
    PENDING_TERMINATION = "pending_termination"
    FULFILLED = "fulfilled"


class FleetCapacityReservationTenancy:
    """FleetCapacityReservationTenancy enum values."""

    DEFAULT = "default"


class FleetCapacityReservationUsageStrategy:
    """FleetCapacityReservationUsageStrategy enum values."""

    USE_CAPACITY_RESERVATIONS_FIRST = "use-capacity-reservations-first"


class FleetEventType:
    """FleetEventType enum values."""

    INSTANCE_CHANGE = "instance-change"
    FLEET_CHANGE = "fleet-change"
    SERVICE_ERROR = "service-error"


class FleetExcessCapacityTerminationPolicy:
    """FleetExcessCapacityTerminationPolicy enum values."""

    NO_TERMINATION = "no-termination"
    TERMINATION = "termination"


class FleetInstanceMatchCriteria:
    """FleetInstanceMatchCriteria enum values."""

    OPEN = "open"


class FleetOnDemandAllocationStrategy:
    """FleetOnDemandAllocationStrategy enum values."""

    LOWEST_PRICE = "lowest-price"
    PRIORITIZED = "prioritized"


class FleetReplacementStrategy:
    """FleetReplacementStrategy enum values."""

    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class FleetStateCode:
    """FleetStateCode enum values."""

    SUBMITTED = "submitted"
    ACTIVE = "active"
    DELETED = "deleted"
    FAILED = "failed"
    DELETED_RUNNING = "deleted_running"
    DELETED_TERMINATING = "deleted_terminating"
    MODIFYING = "modifying"


class FleetType:
    """FleetType enum values."""

    REQUEST = "request"
    MAINTAIN = "maintain"
    INSTANT = "instant"


class FlexibleEnaQueuesSupport:
    """FlexibleEnaQueuesSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class FlowLogsResourceType:
    """FlowLogsResourceType enum values."""

    VPC = "VPC"
    SUBNET = "Subnet"
    NETWORKINTERFACE = "NetworkInterface"
    TRANSITGATEWAY = "TransitGateway"
    TRANSITGATEWAYATTACHMENT = "TransitGatewayAttachment"
    REGIONALNATGATEWAY = "RegionalNatGateway"


class FpgaImageAttributeName:
    """FpgaImageAttributeName enum values."""

    DESCRIPTION = "description"
    NAME = "name"
    LOADPERMISSION = "loadPermission"
    PRODUCTCODES = "productCodes"


class FpgaImageStateCode:
    """FpgaImageStateCode enum values."""

    PENDING = "pending"
    FAILED = "failed"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class GatewayAssociationState:
    """GatewayAssociationState enum values."""

    ASSOCIATED = "associated"
    NOT_ASSOCIATED = "not-associated"
    ASSOCIATING = "associating"
    DISASSOCIATING = "disassociating"


class GatewayType:
    """GatewayType enum values."""

    IPSEC_1 = "ipsec.1"


class GroupBy:
    """GroupBy enum values."""

    RESOURCE_REGION = "resource-region"
    AVAILABILITY_ZONE_ID = "availability-zone-id"
    ACCOUNT_ID = "account-id"
    INSTANCE_FAMILY = "instance-family"
    INSTANCE_TYPE = "instance-type"
    INSTANCE_PLATFORM = "instance-platform"
    RESERVATION_ARN = "reservation-arn"
    RESERVATION_ID = "reservation-id"
    RESERVATION_TYPE = "reservation-type"
    RESERVATION_CREATE_TIMESTAMP = "reservation-create-timestamp"
    RESERVATION_START_TIMESTAMP = "reservation-start-timestamp"
    RESERVATION_END_TIMESTAMP = "reservation-end-timestamp"
    RESERVATION_END_DATE_TYPE = "reservation-end-date-type"
    TENANCY = "tenancy"
    RESERVATION_STATE = "reservation-state"
    RESERVATION_INSTANCE_MATCH_CRITERIA = "reservation-instance-match-criteria"
    RESERVATION_UNUSED_FINANCIAL_OWNER = "reservation-unused-financial-owner"


class HaStatus:
    """HaStatus enum values."""

    PROCESSING = "processing"
    ACTIVE = "active"
    STANDBY = "standby"
    INVALID = "invalid"


class HostMaintenance:
    """HostMaintenance enum values."""

    ON = "on"
    OFF = "off"


class HostRecovery:
    """HostRecovery enum values."""

    ON = "on"
    OFF = "off"


class HostTenancy:
    """HostTenancy enum values."""

    DEFAULT = "default"
    DEDICATED = "dedicated"
    HOST = "host"


class HostnameType:
    """HostnameType enum values."""

    IP_NAME = "ip-name"
    RESOURCE_NAME = "resource-name"


class HttpTokensState:
    """HttpTokensState enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"


class HypervisorType:
    """HypervisorType enum values."""

    OVM = "ovm"
    XEN = "xen"


class IamInstanceProfileAssociationState:
    """IamInstanceProfileAssociationState enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"


class Igmpv2SupportValue:
    """Igmpv2SupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class ImageAttributeName:
    """ImageAttributeName enum values."""

    DESCRIPTION = "description"
    KERNEL = "kernel"
    RAMDISK = "ramdisk"
    LAUNCHPERMISSION = "launchPermission"
    PRODUCTCODES = "productCodes"
    BLOCKDEVICEMAPPING = "blockDeviceMapping"
    SRIOVNETSUPPORT = "sriovNetSupport"
    BOOTMODE = "bootMode"
    TPMSUPPORT = "tpmSupport"
    UEFIDATA = "uefiData"
    LASTLAUNCHEDTIME = "lastLaunchedTime"
    IMDSSUPPORT = "imdsSupport"
    DEREGISTRATIONPROTECTION = "deregistrationProtection"


class ImageBlockPublicAccessDisabledState:
    """ImageBlockPublicAccessDisabledState enum values."""

    UNBLOCKED = "unblocked"


class ImageBlockPublicAccessEnabledState:
    """ImageBlockPublicAccessEnabledState enum values."""

    BLOCK_NEW_SHARING = "block-new-sharing"


class ImageReferenceOptionName:
    """ImageReferenceOptionName enum values."""

    STATE_NAME = "state-name"
    VERSION_DEPTH = "version-depth"


class ImageReferenceResourceType:
    """ImageReferenceResourceType enum values."""

    EC2_INSTANCE = "ec2:Instance"
    EC2_LAUNCHTEMPLATE = "ec2:LaunchTemplate"
    SSM_PARAMETER = "ssm:Parameter"
    IMAGEBUILDER_IMAGERECIPE = "imagebuilder:ImageRecipe"
    IMAGEBUILDER_CONTAINERRECIPE = "imagebuilder:ContainerRecipe"


class ImageState:
    """ImageState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    INVALID = "invalid"
    DEREGISTERED = "deregistered"
    TRANSIENT = "transient"
    FAILED = "failed"
    ERROR = "error"
    DISABLED = "disabled"


class ImageTypeValues:
    """ImageTypeValues enum values."""

    MACHINE = "machine"
    KERNEL = "kernel"
    RAMDISK = "ramdisk"


class ImdsSupportValues:
    """ImdsSupportValues enum values."""

    V2_0 = "v2.0"


class IngestionStatus:
    """IngestionStatus enum values."""

    INITIAL_INGESTION_IN_PROGRESS = "initial-ingestion-in-progress"
    INGESTION_COMPLETE = "ingestion-complete"
    INGESTION_FAILED = "ingestion-failed"


class InitializationType:
    """InitializationType enum values."""

    DEFAULT = "default"
    PROVISIONED_RATE = "provisioned-rate"
    VOLUME_COPY = "volume-copy"


class InstanceAttributeName:
    """InstanceAttributeName enum values."""

    INSTANCETYPE = "instanceType"
    KERNEL = "kernel"
    RAMDISK = "ramdisk"
    USERDATA = "userData"
    DISABLEAPITERMINATION = "disableApiTermination"
    INSTANCEINITIATEDSHUTDOWNBEHAVIOR = "instanceInitiatedShutdownBehavior"
    ROOTDEVICENAME = "rootDeviceName"
    BLOCKDEVICEMAPPING = "blockDeviceMapping"
    PRODUCTCODES = "productCodes"
    SOURCEDESTCHECK = "sourceDestCheck"
    GROUPSET = "groupSet"
    EBSOPTIMIZED = "ebsOptimized"
    SRIOVNETSUPPORT = "sriovNetSupport"
    ENASUPPORT = "enaSupport"
    ENCLAVEOPTIONS = "enclaveOptions"
    DISABLEAPISTOP = "disableApiStop"


class InstanceAutoRecoveryState:
    """InstanceAutoRecoveryState enum values."""

    DISABLED = "disabled"
    DEFAULT = "default"


class InstanceBandwidthWeighting:
    """InstanceBandwidthWeighting enum values."""

    DEFAULT = "default"
    VPC_1 = "vpc-1"
    EBS_1 = "ebs-1"


class InstanceBootModeValues:
    """InstanceBootModeValues enum values."""

    LEGACY_BIOS = "legacy-bios"
    UEFI = "uefi"


class InstanceEventWindowState:
    """InstanceEventWindowState enum values."""

    CREATING = "creating"
    DELETING = "deleting"
    ACTIVE = "active"
    DELETED = "deleted"


class InstanceGeneration:
    """InstanceGeneration enum values."""

    CURRENT = "current"
    PREVIOUS = "previous"


class InstanceHealthStatus:
    """InstanceHealthStatus enum values."""

    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


class InstanceInterruptionBehavior:
    """InstanceInterruptionBehavior enum values."""

    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class InstanceLifecycle:
    """InstanceLifecycle enum values."""

    SPOT = "spot"
    ON_DEMAND = "on-demand"


class InstanceLifecycleType:
    """InstanceLifecycleType enum values."""

    SPOT = "spot"
    SCHEDULED = "scheduled"
    CAPACITY_BLOCK = "capacity-block"
    INTERRUPTIBLE_CAPACITY_RESERVATION = "interruptible-capacity-reservation"


class InstanceMatchCriteria:
    """InstanceMatchCriteria enum values."""

    OPEN = "open"
    TARGETED = "targeted"


class InstanceMetadataEndpointState:
    """InstanceMetadataEndpointState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class InstanceMetadataOptionsState:
    """InstanceMetadataOptionsState enum values."""

    PENDING = "pending"
    APPLIED = "applied"


class InstanceMetadataProtocolState:
    """InstanceMetadataProtocolState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class InstanceMetadataTagsState:
    """InstanceMetadataTagsState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class InstanceRebootMigrationState:
    """InstanceRebootMigrationState enum values."""

    DISABLED = "disabled"
    DEFAULT = "default"


class InstanceStateName:
    """InstanceStateName enum values."""

    PENDING = "pending"
    RUNNING = "running"
    SHUTTING_DOWN = "shutting-down"
    TERMINATED = "terminated"
    STOPPING = "stopping"
    STOPPED = "stopped"


class InstanceStorageEncryptionSupport:
    """InstanceStorageEncryptionSupport enum values."""

    UNSUPPORTED = "unsupported"
    REQUIRED = "required"


class InstanceType:
    """InstanceType enum values."""

    A1_MEDIUM = "a1.medium"
    A1_LARGE = "a1.large"
    A1_XLARGE = "a1.xlarge"
    A1_2XLARGE = "a1.2xlarge"
    A1_4XLARGE = "a1.4xlarge"
    A1_METAL = "a1.metal"
    C1_MEDIUM = "c1.medium"
    C1_XLARGE = "c1.xlarge"
    C3_LARGE = "c3.large"
    C3_XLARGE = "c3.xlarge"
    C3_2XLARGE = "c3.2xlarge"
    C3_4XLARGE = "c3.4xlarge"
    C3_8XLARGE = "c3.8xlarge"
    C4_LARGE = "c4.large"
    C4_XLARGE = "c4.xlarge"
    C4_2XLARGE = "c4.2xlarge"
    C4_4XLARGE = "c4.4xlarge"
    C4_8XLARGE = "c4.8xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"
    C5_2XLARGE = "c5.2xlarge"
    C5_4XLARGE = "c5.4xlarge"
    C5_9XLARGE = "c5.9xlarge"
    C5_12XLARGE = "c5.12xlarge"
    C5_18XLARGE = "c5.18xlarge"
    C5_24XLARGE = "c5.24xlarge"
    C5_METAL = "c5.metal"
    C5A_LARGE = "c5a.large"
    C5A_XLARGE = "c5a.xlarge"
    C5A_2XLARGE = "c5a.2xlarge"
    C5A_4XLARGE = "c5a.4xlarge"
    C5A_8XLARGE = "c5a.8xlarge"
    C5A_12XLARGE = "c5a.12xlarge"
    C5A_16XLARGE = "c5a.16xlarge"
    C5A_24XLARGE = "c5a.24xlarge"
    C5AD_LARGE = "c5ad.large"
    C5AD_XLARGE = "c5ad.xlarge"
    C5AD_2XLARGE = "c5ad.2xlarge"
    C5AD_4XLARGE = "c5ad.4xlarge"
    C5AD_8XLARGE = "c5ad.8xlarge"
    C5AD_12XLARGE = "c5ad.12xlarge"
    C5AD_16XLARGE = "c5ad.16xlarge"
    C5AD_24XLARGE = "c5ad.24xlarge"
    C5D_LARGE = "c5d.large"
    C5D_XLARGE = "c5d.xlarge"
    C5D_2XLARGE = "c5d.2xlarge"
    C5D_4XLARGE = "c5d.4xlarge"
    C5D_9XLARGE = "c5d.9xlarge"
    C5D_12XLARGE = "c5d.12xlarge"
    C5D_18XLARGE = "c5d.18xlarge"
    C5D_24XLARGE = "c5d.24xlarge"
    C5D_METAL = "c5d.metal"
    C5N_LARGE = "c5n.large"
    C5N_XLARGE = "c5n.xlarge"
    C5N_2XLARGE = "c5n.2xlarge"
    C5N_4XLARGE = "c5n.4xlarge"
    C5N_9XLARGE = "c5n.9xlarge"
    C5N_18XLARGE = "c5n.18xlarge"
    C5N_METAL = "c5n.metal"
    C6G_MEDIUM = "c6g.medium"
    C6G_LARGE = "c6g.large"
    C6G_XLARGE = "c6g.xlarge"
    C6G_2XLARGE = "c6g.2xlarge"
    C6G_4XLARGE = "c6g.4xlarge"
    C6G_8XLARGE = "c6g.8xlarge"
    C6G_12XLARGE = "c6g.12xlarge"
    C6G_16XLARGE = "c6g.16xlarge"
    C6G_METAL = "c6g.metal"
    C6GD_MEDIUM = "c6gd.medium"
    C6GD_LARGE = "c6gd.large"
    C6GD_XLARGE = "c6gd.xlarge"
    C6GD_2XLARGE = "c6gd.2xlarge"
    C6GD_4XLARGE = "c6gd.4xlarge"
    C6GD_8XLARGE = "c6gd.8xlarge"
    C6GD_12XLARGE = "c6gd.12xlarge"
    C6GD_16XLARGE = "c6gd.16xlarge"
    C6GD_METAL = "c6gd.metal"
    C6GN_MEDIUM = "c6gn.medium"
    C6GN_LARGE = "c6gn.large"
    C6GN_XLARGE = "c6gn.xlarge"
    C6GN_2XLARGE = "c6gn.2xlarge"
    C6GN_4XLARGE = "c6gn.4xlarge"
    C6GN_8XLARGE = "c6gn.8xlarge"
    C6GN_12XLARGE = "c6gn.12xlarge"
    C6GN_16XLARGE = "c6gn.16xlarge"
    C6I_LARGE = "c6i.large"
    C6I_XLARGE = "c6i.xlarge"
    C6I_2XLARGE = "c6i.2xlarge"
    C6I_4XLARGE = "c6i.4xlarge"
    C6I_8XLARGE = "c6i.8xlarge"
    C6I_12XLARGE = "c6i.12xlarge"
    C6I_16XLARGE = "c6i.16xlarge"
    C6I_24XLARGE = "c6i.24xlarge"
    C6I_32XLARGE = "c6i.32xlarge"
    C6I_METAL = "c6i.metal"
    CC1_4XLARGE = "cc1.4xlarge"
    CC2_8XLARGE = "cc2.8xlarge"
    CG1_4XLARGE = "cg1.4xlarge"
    CR1_8XLARGE = "cr1.8xlarge"
    D2_XLARGE = "d2.xlarge"
    D2_2XLARGE = "d2.2xlarge"
    D2_4XLARGE = "d2.4xlarge"
    D2_8XLARGE = "d2.8xlarge"
    D3_XLARGE = "d3.xlarge"
    D3_2XLARGE = "d3.2xlarge"
    D3_4XLARGE = "d3.4xlarge"
    D3_8XLARGE = "d3.8xlarge"
    D3EN_XLARGE = "d3en.xlarge"
    D3EN_2XLARGE = "d3en.2xlarge"
    D3EN_4XLARGE = "d3en.4xlarge"
    D3EN_6XLARGE = "d3en.6xlarge"
    D3EN_8XLARGE = "d3en.8xlarge"
    D3EN_12XLARGE = "d3en.12xlarge"
    DL1_24XLARGE = "dl1.24xlarge"
    F1_2XLARGE = "f1.2xlarge"
    F1_4XLARGE = "f1.4xlarge"
    F1_16XLARGE = "f1.16xlarge"
    G2_2XLARGE = "g2.2xlarge"
    G2_8XLARGE = "g2.8xlarge"
    G3_4XLARGE = "g3.4xlarge"
    G3_8XLARGE = "g3.8xlarge"
    G3_16XLARGE = "g3.16xlarge"
    G3S_XLARGE = "g3s.xlarge"
    G4AD_XLARGE = "g4ad.xlarge"
    G4AD_2XLARGE = "g4ad.2xlarge"
    G4AD_4XLARGE = "g4ad.4xlarge"
    G4AD_8XLARGE = "g4ad.8xlarge"
    G4AD_16XLARGE = "g4ad.16xlarge"
    G4DN_XLARGE = "g4dn.xlarge"
    G4DN_2XLARGE = "g4dn.2xlarge"
    G4DN_4XLARGE = "g4dn.4xlarge"
    G4DN_8XLARGE = "g4dn.8xlarge"
    G4DN_12XLARGE = "g4dn.12xlarge"
    G4DN_16XLARGE = "g4dn.16xlarge"
    G4DN_METAL = "g4dn.metal"
    G5_XLARGE = "g5.xlarge"
    G5_2XLARGE = "g5.2xlarge"
    G5_4XLARGE = "g5.4xlarge"
    G5_8XLARGE = "g5.8xlarge"
    G5_12XLARGE = "g5.12xlarge"
    G5_16XLARGE = "g5.16xlarge"
    G5_24XLARGE = "g5.24xlarge"
    G5_48XLARGE = "g5.48xlarge"
    G5G_XLARGE = "g5g.xlarge"
    G5G_2XLARGE = "g5g.2xlarge"
    G5G_4XLARGE = "g5g.4xlarge"
    G5G_8XLARGE = "g5g.8xlarge"
    G5G_16XLARGE = "g5g.16xlarge"
    G5G_METAL = "g5g.metal"
    HI1_4XLARGE = "hi1.4xlarge"
    HPC6A_48XLARGE = "hpc6a.48xlarge"
    HS1_8XLARGE = "hs1.8xlarge"
    H1_2XLARGE = "h1.2xlarge"
    H1_4XLARGE = "h1.4xlarge"
    H1_8XLARGE = "h1.8xlarge"
    H1_16XLARGE = "h1.16xlarge"
    I2_XLARGE = "i2.xlarge"
    I2_2XLARGE = "i2.2xlarge"
    I2_4XLARGE = "i2.4xlarge"
    I2_8XLARGE = "i2.8xlarge"
    I3_LARGE = "i3.large"
    I3_XLARGE = "i3.xlarge"
    I3_2XLARGE = "i3.2xlarge"
    I3_4XLARGE = "i3.4xlarge"
    I3_8XLARGE = "i3.8xlarge"
    I3_16XLARGE = "i3.16xlarge"
    I3_METAL = "i3.metal"
    I3EN_LARGE = "i3en.large"
    I3EN_XLARGE = "i3en.xlarge"
    I3EN_2XLARGE = "i3en.2xlarge"
    I3EN_3XLARGE = "i3en.3xlarge"
    I3EN_6XLARGE = "i3en.6xlarge"
    I3EN_12XLARGE = "i3en.12xlarge"
    I3EN_24XLARGE = "i3en.24xlarge"
    I3EN_METAL = "i3en.metal"
    IM4GN_LARGE = "im4gn.large"
    IM4GN_XLARGE = "im4gn.xlarge"
    IM4GN_2XLARGE = "im4gn.2xlarge"
    IM4GN_4XLARGE = "im4gn.4xlarge"
    IM4GN_8XLARGE = "im4gn.8xlarge"
    IM4GN_16XLARGE = "im4gn.16xlarge"
    INF1_XLARGE = "inf1.xlarge"
    INF1_2XLARGE = "inf1.2xlarge"
    INF1_6XLARGE = "inf1.6xlarge"
    INF1_24XLARGE = "inf1.24xlarge"
    IS4GEN_MEDIUM = "is4gen.medium"
    IS4GEN_LARGE = "is4gen.large"
    IS4GEN_XLARGE = "is4gen.xlarge"
    IS4GEN_2XLARGE = "is4gen.2xlarge"
    IS4GEN_4XLARGE = "is4gen.4xlarge"
    IS4GEN_8XLARGE = "is4gen.8xlarge"
    M1_SMALL = "m1.small"
    M1_MEDIUM = "m1.medium"
    M1_LARGE = "m1.large"
    M1_XLARGE = "m1.xlarge"
    M2_XLARGE = "m2.xlarge"
    M2_2XLARGE = "m2.2xlarge"
    M2_4XLARGE = "m2.4xlarge"
    M3_MEDIUM = "m3.medium"
    M3_LARGE = "m3.large"
    M3_XLARGE = "m3.xlarge"
    M3_2XLARGE = "m3.2xlarge"
    M4_LARGE = "m4.large"
    M4_XLARGE = "m4.xlarge"
    M4_2XLARGE = "m4.2xlarge"
    M4_4XLARGE = "m4.4xlarge"
    M4_10XLARGE = "m4.10xlarge"
    M4_16XLARGE = "m4.16xlarge"
    M5_LARGE = "m5.large"
    M5_XLARGE = "m5.xlarge"
    M5_2XLARGE = "m5.2xlarge"
    M5_4XLARGE = "m5.4xlarge"
    M5_8XLARGE = "m5.8xlarge"
    M5_12XLARGE = "m5.12xlarge"
    M5_16XLARGE = "m5.16xlarge"
    M5_24XLARGE = "m5.24xlarge"
    M5_METAL = "m5.metal"
    M5A_LARGE = "m5a.large"
    M5A_XLARGE = "m5a.xlarge"
    M5A_2XLARGE = "m5a.2xlarge"
    M5A_4XLARGE = "m5a.4xlarge"
    M5A_8XLARGE = "m5a.8xlarge"
    M5A_12XLARGE = "m5a.12xlarge"
    M5A_16XLARGE = "m5a.16xlarge"
    M5A_24XLARGE = "m5a.24xlarge"
    M5AD_LARGE = "m5ad.large"
    M5AD_XLARGE = "m5ad.xlarge"
    M5AD_2XLARGE = "m5ad.2xlarge"
    M5AD_4XLARGE = "m5ad.4xlarge"
    M5AD_8XLARGE = "m5ad.8xlarge"
    M5AD_12XLARGE = "m5ad.12xlarge"
    M5AD_16XLARGE = "m5ad.16xlarge"
    M5AD_24XLARGE = "m5ad.24xlarge"
    M5D_LARGE = "m5d.large"
    M5D_XLARGE = "m5d.xlarge"
    M5D_2XLARGE = "m5d.2xlarge"
    M5D_4XLARGE = "m5d.4xlarge"
    M5D_8XLARGE = "m5d.8xlarge"
    M5D_12XLARGE = "m5d.12xlarge"
    M5D_16XLARGE = "m5d.16xlarge"
    M5D_24XLARGE = "m5d.24xlarge"
    M5D_METAL = "m5d.metal"
    M5DN_LARGE = "m5dn.large"
    M5DN_XLARGE = "m5dn.xlarge"
    M5DN_2XLARGE = "m5dn.2xlarge"
    M5DN_4XLARGE = "m5dn.4xlarge"
    M5DN_8XLARGE = "m5dn.8xlarge"
    M5DN_12XLARGE = "m5dn.12xlarge"
    M5DN_16XLARGE = "m5dn.16xlarge"
    M5DN_24XLARGE = "m5dn.24xlarge"
    M5DN_METAL = "m5dn.metal"
    M5N_LARGE = "m5n.large"
    M5N_XLARGE = "m5n.xlarge"
    M5N_2XLARGE = "m5n.2xlarge"
    M5N_4XLARGE = "m5n.4xlarge"
    M5N_8XLARGE = "m5n.8xlarge"
    M5N_12XLARGE = "m5n.12xlarge"
    M5N_16XLARGE = "m5n.16xlarge"
    M5N_24XLARGE = "m5n.24xlarge"
    M5N_METAL = "m5n.metal"
    M5ZN_LARGE = "m5zn.large"
    M5ZN_XLARGE = "m5zn.xlarge"
    M5ZN_2XLARGE = "m5zn.2xlarge"
    M5ZN_3XLARGE = "m5zn.3xlarge"
    M5ZN_6XLARGE = "m5zn.6xlarge"
    M5ZN_12XLARGE = "m5zn.12xlarge"
    M5ZN_METAL = "m5zn.metal"
    M6A_LARGE = "m6a.large"
    M6A_XLARGE = "m6a.xlarge"
    M6A_2XLARGE = "m6a.2xlarge"
    M6A_4XLARGE = "m6a.4xlarge"
    M6A_8XLARGE = "m6a.8xlarge"
    M6A_12XLARGE = "m6a.12xlarge"
    M6A_16XLARGE = "m6a.16xlarge"
    M6A_24XLARGE = "m6a.24xlarge"
    M6A_32XLARGE = "m6a.32xlarge"
    M6A_48XLARGE = "m6a.48xlarge"
    M6G_METAL = "m6g.metal"
    M6G_MEDIUM = "m6g.medium"
    M6G_LARGE = "m6g.large"
    M6G_XLARGE = "m6g.xlarge"
    M6G_2XLARGE = "m6g.2xlarge"
    M6G_4XLARGE = "m6g.4xlarge"
    M6G_8XLARGE = "m6g.8xlarge"
    M6G_12XLARGE = "m6g.12xlarge"
    M6G_16XLARGE = "m6g.16xlarge"
    M6GD_METAL = "m6gd.metal"
    M6GD_MEDIUM = "m6gd.medium"
    M6GD_LARGE = "m6gd.large"
    M6GD_XLARGE = "m6gd.xlarge"
    M6GD_2XLARGE = "m6gd.2xlarge"
    M6GD_4XLARGE = "m6gd.4xlarge"
    M6GD_8XLARGE = "m6gd.8xlarge"
    M6GD_12XLARGE = "m6gd.12xlarge"
    M6GD_16XLARGE = "m6gd.16xlarge"
    M6I_LARGE = "m6i.large"
    M6I_XLARGE = "m6i.xlarge"
    M6I_2XLARGE = "m6i.2xlarge"
    M6I_4XLARGE = "m6i.4xlarge"
    M6I_8XLARGE = "m6i.8xlarge"
    M6I_12XLARGE = "m6i.12xlarge"
    M6I_16XLARGE = "m6i.16xlarge"
    M6I_24XLARGE = "m6i.24xlarge"
    M6I_32XLARGE = "m6i.32xlarge"
    M6I_METAL = "m6i.metal"
    MAC1_METAL = "mac1.metal"
    P2_XLARGE = "p2.xlarge"
    P2_8XLARGE = "p2.8xlarge"
    P2_16XLARGE = "p2.16xlarge"
    P3_2XLARGE = "p3.2xlarge"
    P3_8XLARGE = "p3.8xlarge"
    P3_16XLARGE = "p3.16xlarge"
    P3DN_24XLARGE = "p3dn.24xlarge"
    P4D_24XLARGE = "p4d.24xlarge"
    R3_LARGE = "r3.large"
    R3_XLARGE = "r3.xlarge"
    R3_2XLARGE = "r3.2xlarge"
    R3_4XLARGE = "r3.4xlarge"
    R3_8XLARGE = "r3.8xlarge"
    R4_LARGE = "r4.large"
    R4_XLARGE = "r4.xlarge"
    R4_2XLARGE = "r4.2xlarge"
    R4_4XLARGE = "r4.4xlarge"
    R4_8XLARGE = "r4.8xlarge"
    R4_16XLARGE = "r4.16xlarge"
    R5_LARGE = "r5.large"
    R5_XLARGE = "r5.xlarge"
    R5_2XLARGE = "r5.2xlarge"
    R5_4XLARGE = "r5.4xlarge"
    R5_8XLARGE = "r5.8xlarge"
    R5_12XLARGE = "r5.12xlarge"
    R5_16XLARGE = "r5.16xlarge"
    R5_24XLARGE = "r5.24xlarge"
    R5_METAL = "r5.metal"
    R5A_LARGE = "r5a.large"
    R5A_XLARGE = "r5a.xlarge"
    R5A_2XLARGE = "r5a.2xlarge"
    R5A_4XLARGE = "r5a.4xlarge"
    R5A_8XLARGE = "r5a.8xlarge"
    R5A_12XLARGE = "r5a.12xlarge"
    R5A_16XLARGE = "r5a.16xlarge"
    R5A_24XLARGE = "r5a.24xlarge"
    R5AD_LARGE = "r5ad.large"
    R5AD_XLARGE = "r5ad.xlarge"
    R5AD_2XLARGE = "r5ad.2xlarge"
    R5AD_4XLARGE = "r5ad.4xlarge"
    R5AD_8XLARGE = "r5ad.8xlarge"
    R5AD_12XLARGE = "r5ad.12xlarge"
    R5AD_16XLARGE = "r5ad.16xlarge"
    R5AD_24XLARGE = "r5ad.24xlarge"
    R5B_LARGE = "r5b.large"
    R5B_XLARGE = "r5b.xlarge"
    R5B_2XLARGE = "r5b.2xlarge"
    R5B_4XLARGE = "r5b.4xlarge"
    R5B_8XLARGE = "r5b.8xlarge"
    R5B_12XLARGE = "r5b.12xlarge"
    R5B_16XLARGE = "r5b.16xlarge"
    R5B_24XLARGE = "r5b.24xlarge"
    R5B_METAL = "r5b.metal"
    R5D_LARGE = "r5d.large"
    R5D_XLARGE = "r5d.xlarge"
    R5D_2XLARGE = "r5d.2xlarge"
    R5D_4XLARGE = "r5d.4xlarge"
    R5D_8XLARGE = "r5d.8xlarge"
    R5D_12XLARGE = "r5d.12xlarge"
    R5D_16XLARGE = "r5d.16xlarge"
    R5D_24XLARGE = "r5d.24xlarge"
    R5D_METAL = "r5d.metal"
    R5DN_LARGE = "r5dn.large"
    R5DN_XLARGE = "r5dn.xlarge"
    R5DN_2XLARGE = "r5dn.2xlarge"
    R5DN_4XLARGE = "r5dn.4xlarge"
    R5DN_8XLARGE = "r5dn.8xlarge"
    R5DN_12XLARGE = "r5dn.12xlarge"
    R5DN_16XLARGE = "r5dn.16xlarge"
    R5DN_24XLARGE = "r5dn.24xlarge"
    R5DN_METAL = "r5dn.metal"
    R5N_LARGE = "r5n.large"
    R5N_XLARGE = "r5n.xlarge"
    R5N_2XLARGE = "r5n.2xlarge"
    R5N_4XLARGE = "r5n.4xlarge"
    R5N_8XLARGE = "r5n.8xlarge"
    R5N_12XLARGE = "r5n.12xlarge"
    R5N_16XLARGE = "r5n.16xlarge"
    R5N_24XLARGE = "r5n.24xlarge"
    R5N_METAL = "r5n.metal"
    R6G_MEDIUM = "r6g.medium"
    R6G_LARGE = "r6g.large"
    R6G_XLARGE = "r6g.xlarge"
    R6G_2XLARGE = "r6g.2xlarge"
    R6G_4XLARGE = "r6g.4xlarge"
    R6G_8XLARGE = "r6g.8xlarge"
    R6G_12XLARGE = "r6g.12xlarge"
    R6G_16XLARGE = "r6g.16xlarge"
    R6G_METAL = "r6g.metal"
    R6GD_MEDIUM = "r6gd.medium"
    R6GD_LARGE = "r6gd.large"
    R6GD_XLARGE = "r6gd.xlarge"
    R6GD_2XLARGE = "r6gd.2xlarge"
    R6GD_4XLARGE = "r6gd.4xlarge"
    R6GD_8XLARGE = "r6gd.8xlarge"
    R6GD_12XLARGE = "r6gd.12xlarge"
    R6GD_16XLARGE = "r6gd.16xlarge"
    R6GD_METAL = "r6gd.metal"
    R6I_LARGE = "r6i.large"
    R6I_XLARGE = "r6i.xlarge"
    R6I_2XLARGE = "r6i.2xlarge"
    R6I_4XLARGE = "r6i.4xlarge"
    R6I_8XLARGE = "r6i.8xlarge"
    R6I_12XLARGE = "r6i.12xlarge"
    R6I_16XLARGE = "r6i.16xlarge"
    R6I_24XLARGE = "r6i.24xlarge"
    R6I_32XLARGE = "r6i.32xlarge"
    R6I_METAL = "r6i.metal"
    T1_MICRO = "t1.micro"
    T2_NANO = "t2.nano"
    T2_MICRO = "t2.micro"
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    T2_LARGE = "t2.large"
    T2_XLARGE = "t2.xlarge"
    T2_2XLARGE = "t2.2xlarge"
    T3_NANO = "t3.nano"
    T3_MICRO = "t3.micro"
    T3_SMALL = "t3.small"
    T3_MEDIUM = "t3.medium"
    T3_LARGE = "t3.large"
    T3_XLARGE = "t3.xlarge"
    T3_2XLARGE = "t3.2xlarge"
    T3A_NANO = "t3a.nano"
    T3A_MICRO = "t3a.micro"
    T3A_SMALL = "t3a.small"
    T3A_MEDIUM = "t3a.medium"
    T3A_LARGE = "t3a.large"
    T3A_XLARGE = "t3a.xlarge"
    T3A_2XLARGE = "t3a.2xlarge"
    T4G_NANO = "t4g.nano"
    T4G_MICRO = "t4g.micro"
    T4G_SMALL = "t4g.small"
    T4G_MEDIUM = "t4g.medium"
    T4G_LARGE = "t4g.large"
    T4G_XLARGE = "t4g.xlarge"
    T4G_2XLARGE = "t4g.2xlarge"
    U_6TB1_56XLARGE = "u-6tb1.56xlarge"
    U_6TB1_112XLARGE = "u-6tb1.112xlarge"
    U_9TB1_112XLARGE = "u-9tb1.112xlarge"
    U_12TB1_112XLARGE = "u-12tb1.112xlarge"
    U_6TB1_METAL = "u-6tb1.metal"
    U_9TB1_METAL = "u-9tb1.metal"
    U_12TB1_METAL = "u-12tb1.metal"
    U_18TB1_METAL = "u-18tb1.metal"
    U_24TB1_METAL = "u-24tb1.metal"
    VT1_3XLARGE = "vt1.3xlarge"
    VT1_6XLARGE = "vt1.6xlarge"
    VT1_24XLARGE = "vt1.24xlarge"
    X1_16XLARGE = "x1.16xlarge"
    X1_32XLARGE = "x1.32xlarge"
    X1E_XLARGE = "x1e.xlarge"
    X1E_2XLARGE = "x1e.2xlarge"
    X1E_4XLARGE = "x1e.4xlarge"
    X1E_8XLARGE = "x1e.8xlarge"
    X1E_16XLARGE = "x1e.16xlarge"
    X1E_32XLARGE = "x1e.32xlarge"
    X2IEZN_2XLARGE = "x2iezn.2xlarge"
    X2IEZN_4XLARGE = "x2iezn.4xlarge"
    X2IEZN_6XLARGE = "x2iezn.6xlarge"
    X2IEZN_8XLARGE = "x2iezn.8xlarge"
    X2IEZN_12XLARGE = "x2iezn.12xlarge"
    X2IEZN_METAL = "x2iezn.metal"
    X2GD_MEDIUM = "x2gd.medium"
    X2GD_LARGE = "x2gd.large"
    X2GD_XLARGE = "x2gd.xlarge"
    X2GD_2XLARGE = "x2gd.2xlarge"
    X2GD_4XLARGE = "x2gd.4xlarge"
    X2GD_8XLARGE = "x2gd.8xlarge"
    X2GD_12XLARGE = "x2gd.12xlarge"
    X2GD_16XLARGE = "x2gd.16xlarge"
    X2GD_METAL = "x2gd.metal"
    Z1D_LARGE = "z1d.large"
    Z1D_XLARGE = "z1d.xlarge"
    Z1D_2XLARGE = "z1d.2xlarge"
    Z1D_3XLARGE = "z1d.3xlarge"
    Z1D_6XLARGE = "z1d.6xlarge"
    Z1D_12XLARGE = "z1d.12xlarge"
    Z1D_METAL = "z1d.metal"
    X2IDN_16XLARGE = "x2idn.16xlarge"
    X2IDN_24XLARGE = "x2idn.24xlarge"
    X2IDN_32XLARGE = "x2idn.32xlarge"
    X2IEDN_XLARGE = "x2iedn.xlarge"
    X2IEDN_2XLARGE = "x2iedn.2xlarge"
    X2IEDN_4XLARGE = "x2iedn.4xlarge"
    X2IEDN_8XLARGE = "x2iedn.8xlarge"
    X2IEDN_16XLARGE = "x2iedn.16xlarge"
    X2IEDN_24XLARGE = "x2iedn.24xlarge"
    X2IEDN_32XLARGE = "x2iedn.32xlarge"
    C6A_LARGE = "c6a.large"
    C6A_XLARGE = "c6a.xlarge"
    C6A_2XLARGE = "c6a.2xlarge"
    C6A_4XLARGE = "c6a.4xlarge"
    C6A_8XLARGE = "c6a.8xlarge"
    C6A_12XLARGE = "c6a.12xlarge"
    C6A_16XLARGE = "c6a.16xlarge"
    C6A_24XLARGE = "c6a.24xlarge"
    C6A_32XLARGE = "c6a.32xlarge"
    C6A_48XLARGE = "c6a.48xlarge"
    C6A_METAL = "c6a.metal"
    M6A_METAL = "m6a.metal"
    I4I_LARGE = "i4i.large"
    I4I_XLARGE = "i4i.xlarge"
    I4I_2XLARGE = "i4i.2xlarge"
    I4I_4XLARGE = "i4i.4xlarge"
    I4I_8XLARGE = "i4i.8xlarge"
    I4I_16XLARGE = "i4i.16xlarge"
    I4I_32XLARGE = "i4i.32xlarge"
    I4I_METAL = "i4i.metal"
    X2IDN_METAL = "x2idn.metal"
    X2IEDN_METAL = "x2iedn.metal"
    C7G_MEDIUM = "c7g.medium"
    C7G_LARGE = "c7g.large"
    C7G_XLARGE = "c7g.xlarge"
    C7G_2XLARGE = "c7g.2xlarge"
    C7G_4XLARGE = "c7g.4xlarge"
    C7G_8XLARGE = "c7g.8xlarge"
    C7G_12XLARGE = "c7g.12xlarge"
    C7G_16XLARGE = "c7g.16xlarge"
    MAC2_METAL = "mac2.metal"
    C6ID_LARGE = "c6id.large"
    C6ID_XLARGE = "c6id.xlarge"
    C6ID_2XLARGE = "c6id.2xlarge"
    C6ID_4XLARGE = "c6id.4xlarge"
    C6ID_8XLARGE = "c6id.8xlarge"
    C6ID_12XLARGE = "c6id.12xlarge"
    C6ID_16XLARGE = "c6id.16xlarge"
    C6ID_24XLARGE = "c6id.24xlarge"
    C6ID_32XLARGE = "c6id.32xlarge"
    C6ID_METAL = "c6id.metal"
    M6ID_LARGE = "m6id.large"
    M6ID_XLARGE = "m6id.xlarge"
    M6ID_2XLARGE = "m6id.2xlarge"
    M6ID_4XLARGE = "m6id.4xlarge"
    M6ID_8XLARGE = "m6id.8xlarge"
    M6ID_12XLARGE = "m6id.12xlarge"
    M6ID_16XLARGE = "m6id.16xlarge"
    M6ID_24XLARGE = "m6id.24xlarge"
    M6ID_32XLARGE = "m6id.32xlarge"
    M6ID_METAL = "m6id.metal"
    R6ID_LARGE = "r6id.large"
    R6ID_XLARGE = "r6id.xlarge"
    R6ID_2XLARGE = "r6id.2xlarge"
    R6ID_4XLARGE = "r6id.4xlarge"
    R6ID_8XLARGE = "r6id.8xlarge"
    R6ID_12XLARGE = "r6id.12xlarge"
    R6ID_16XLARGE = "r6id.16xlarge"
    R6ID_24XLARGE = "r6id.24xlarge"
    R6ID_32XLARGE = "r6id.32xlarge"
    R6ID_METAL = "r6id.metal"
    R6A_LARGE = "r6a.large"
    R6A_XLARGE = "r6a.xlarge"
    R6A_2XLARGE = "r6a.2xlarge"
    R6A_4XLARGE = "r6a.4xlarge"
    R6A_8XLARGE = "r6a.8xlarge"
    R6A_12XLARGE = "r6a.12xlarge"
    R6A_16XLARGE = "r6a.16xlarge"
    R6A_24XLARGE = "r6a.24xlarge"
    R6A_32XLARGE = "r6a.32xlarge"
    R6A_48XLARGE = "r6a.48xlarge"
    R6A_METAL = "r6a.metal"
    P4DE_24XLARGE = "p4de.24xlarge"
    U_3TB1_56XLARGE = "u-3tb1.56xlarge"
    U_18TB1_112XLARGE = "u-18tb1.112xlarge"
    U_24TB1_112XLARGE = "u-24tb1.112xlarge"
    TRN1_2XLARGE = "trn1.2xlarge"
    TRN1_32XLARGE = "trn1.32xlarge"
    HPC6ID_32XLARGE = "hpc6id.32xlarge"
    C6IN_LARGE = "c6in.large"
    C6IN_XLARGE = "c6in.xlarge"
    C6IN_2XLARGE = "c6in.2xlarge"
    C6IN_4XLARGE = "c6in.4xlarge"
    C6IN_8XLARGE = "c6in.8xlarge"
    C6IN_12XLARGE = "c6in.12xlarge"
    C6IN_16XLARGE = "c6in.16xlarge"
    C6IN_24XLARGE = "c6in.24xlarge"
    C6IN_32XLARGE = "c6in.32xlarge"
    M6IN_LARGE = "m6in.large"
    M6IN_XLARGE = "m6in.xlarge"
    M6IN_2XLARGE = "m6in.2xlarge"
    M6IN_4XLARGE = "m6in.4xlarge"
    M6IN_8XLARGE = "m6in.8xlarge"
    M6IN_12XLARGE = "m6in.12xlarge"
    M6IN_16XLARGE = "m6in.16xlarge"
    M6IN_24XLARGE = "m6in.24xlarge"
    M6IN_32XLARGE = "m6in.32xlarge"
    M6IDN_LARGE = "m6idn.large"
    M6IDN_XLARGE = "m6idn.xlarge"
    M6IDN_2XLARGE = "m6idn.2xlarge"
    M6IDN_4XLARGE = "m6idn.4xlarge"
    M6IDN_8XLARGE = "m6idn.8xlarge"
    M6IDN_12XLARGE = "m6idn.12xlarge"
    M6IDN_16XLARGE = "m6idn.16xlarge"
    M6IDN_24XLARGE = "m6idn.24xlarge"
    M6IDN_32XLARGE = "m6idn.32xlarge"
    R6IN_LARGE = "r6in.large"
    R6IN_XLARGE = "r6in.xlarge"
    R6IN_2XLARGE = "r6in.2xlarge"
    R6IN_4XLARGE = "r6in.4xlarge"
    R6IN_8XLARGE = "r6in.8xlarge"
    R6IN_12XLARGE = "r6in.12xlarge"
    R6IN_16XLARGE = "r6in.16xlarge"
    R6IN_24XLARGE = "r6in.24xlarge"
    R6IN_32XLARGE = "r6in.32xlarge"
    R6IDN_LARGE = "r6idn.large"
    R6IDN_XLARGE = "r6idn.xlarge"
    R6IDN_2XLARGE = "r6idn.2xlarge"
    R6IDN_4XLARGE = "r6idn.4xlarge"
    R6IDN_8XLARGE = "r6idn.8xlarge"
    R6IDN_12XLARGE = "r6idn.12xlarge"
    R6IDN_16XLARGE = "r6idn.16xlarge"
    R6IDN_24XLARGE = "r6idn.24xlarge"
    R6IDN_32XLARGE = "r6idn.32xlarge"
    C7G_METAL = "c7g.metal"
    M7G_MEDIUM = "m7g.medium"
    M7G_LARGE = "m7g.large"
    M7G_XLARGE = "m7g.xlarge"
    M7G_2XLARGE = "m7g.2xlarge"
    M7G_4XLARGE = "m7g.4xlarge"
    M7G_8XLARGE = "m7g.8xlarge"
    M7G_12XLARGE = "m7g.12xlarge"
    M7G_16XLARGE = "m7g.16xlarge"
    M7G_METAL = "m7g.metal"
    R7G_MEDIUM = "r7g.medium"
    R7G_LARGE = "r7g.large"
    R7G_XLARGE = "r7g.xlarge"
    R7G_2XLARGE = "r7g.2xlarge"
    R7G_4XLARGE = "r7g.4xlarge"
    R7G_8XLARGE = "r7g.8xlarge"
    R7G_12XLARGE = "r7g.12xlarge"
    R7G_16XLARGE = "r7g.16xlarge"
    R7G_METAL = "r7g.metal"
    C6IN_METAL = "c6in.metal"
    M6IN_METAL = "m6in.metal"
    M6IDN_METAL = "m6idn.metal"
    R6IN_METAL = "r6in.metal"
    R6IDN_METAL = "r6idn.metal"
    INF2_XLARGE = "inf2.xlarge"
    INF2_8XLARGE = "inf2.8xlarge"
    INF2_24XLARGE = "inf2.24xlarge"
    INF2_48XLARGE = "inf2.48xlarge"
    TRN1N_32XLARGE = "trn1n.32xlarge"
    I4G_LARGE = "i4g.large"
    I4G_XLARGE = "i4g.xlarge"
    I4G_2XLARGE = "i4g.2xlarge"
    I4G_4XLARGE = "i4g.4xlarge"
    I4G_8XLARGE = "i4g.8xlarge"
    I4G_16XLARGE = "i4g.16xlarge"
    HPC7G_4XLARGE = "hpc7g.4xlarge"
    HPC7G_8XLARGE = "hpc7g.8xlarge"
    HPC7G_16XLARGE = "hpc7g.16xlarge"
    C7GN_MEDIUM = "c7gn.medium"
    C7GN_LARGE = "c7gn.large"
    C7GN_XLARGE = "c7gn.xlarge"
    C7GN_2XLARGE = "c7gn.2xlarge"
    C7GN_4XLARGE = "c7gn.4xlarge"
    C7GN_8XLARGE = "c7gn.8xlarge"
    C7GN_12XLARGE = "c7gn.12xlarge"
    C7GN_16XLARGE = "c7gn.16xlarge"
    P5_48XLARGE = "p5.48xlarge"
    M7I_LARGE = "m7i.large"
    M7I_XLARGE = "m7i.xlarge"
    M7I_2XLARGE = "m7i.2xlarge"
    M7I_4XLARGE = "m7i.4xlarge"
    M7I_8XLARGE = "m7i.8xlarge"
    M7I_12XLARGE = "m7i.12xlarge"
    M7I_16XLARGE = "m7i.16xlarge"
    M7I_24XLARGE = "m7i.24xlarge"
    M7I_48XLARGE = "m7i.48xlarge"
    M7I_FLEX_LARGE = "m7i-flex.large"
    M7I_FLEX_XLARGE = "m7i-flex.xlarge"
    M7I_FLEX_2XLARGE = "m7i-flex.2xlarge"
    M7I_FLEX_4XLARGE = "m7i-flex.4xlarge"
    M7I_FLEX_8XLARGE = "m7i-flex.8xlarge"
    M7A_MEDIUM = "m7a.medium"
    M7A_LARGE = "m7a.large"
    M7A_XLARGE = "m7a.xlarge"
    M7A_2XLARGE = "m7a.2xlarge"
    M7A_4XLARGE = "m7a.4xlarge"
    M7A_8XLARGE = "m7a.8xlarge"
    M7A_12XLARGE = "m7a.12xlarge"
    M7A_16XLARGE = "m7a.16xlarge"
    M7A_24XLARGE = "m7a.24xlarge"
    M7A_32XLARGE = "m7a.32xlarge"
    M7A_48XLARGE = "m7a.48xlarge"
    M7A_METAL_48XL = "m7a.metal-48xl"
    HPC7A_12XLARGE = "hpc7a.12xlarge"
    HPC7A_24XLARGE = "hpc7a.24xlarge"
    HPC7A_48XLARGE = "hpc7a.48xlarge"
    HPC7A_96XLARGE = "hpc7a.96xlarge"
    C7GD_MEDIUM = "c7gd.medium"
    C7GD_LARGE = "c7gd.large"
    C7GD_XLARGE = "c7gd.xlarge"
    C7GD_2XLARGE = "c7gd.2xlarge"
    C7GD_4XLARGE = "c7gd.4xlarge"
    C7GD_8XLARGE = "c7gd.8xlarge"
    C7GD_12XLARGE = "c7gd.12xlarge"
    C7GD_16XLARGE = "c7gd.16xlarge"
    M7GD_MEDIUM = "m7gd.medium"
    M7GD_LARGE = "m7gd.large"
    M7GD_XLARGE = "m7gd.xlarge"
    M7GD_2XLARGE = "m7gd.2xlarge"
    M7GD_4XLARGE = "m7gd.4xlarge"
    M7GD_8XLARGE = "m7gd.8xlarge"
    M7GD_12XLARGE = "m7gd.12xlarge"
    M7GD_16XLARGE = "m7gd.16xlarge"
    R7GD_MEDIUM = "r7gd.medium"
    R7GD_LARGE = "r7gd.large"
    R7GD_XLARGE = "r7gd.xlarge"
    R7GD_2XLARGE = "r7gd.2xlarge"
    R7GD_4XLARGE = "r7gd.4xlarge"
    R7GD_8XLARGE = "r7gd.8xlarge"
    R7GD_12XLARGE = "r7gd.12xlarge"
    R7GD_16XLARGE = "r7gd.16xlarge"
    R7A_MEDIUM = "r7a.medium"
    R7A_LARGE = "r7a.large"
    R7A_XLARGE = "r7a.xlarge"
    R7A_2XLARGE = "r7a.2xlarge"
    R7A_4XLARGE = "r7a.4xlarge"
    R7A_8XLARGE = "r7a.8xlarge"
    R7A_12XLARGE = "r7a.12xlarge"
    R7A_16XLARGE = "r7a.16xlarge"
    R7A_24XLARGE = "r7a.24xlarge"
    R7A_32XLARGE = "r7a.32xlarge"
    R7A_48XLARGE = "r7a.48xlarge"
    C7I_LARGE = "c7i.large"
    C7I_XLARGE = "c7i.xlarge"
    C7I_2XLARGE = "c7i.2xlarge"
    C7I_4XLARGE = "c7i.4xlarge"
    C7I_8XLARGE = "c7i.8xlarge"
    C7I_12XLARGE = "c7i.12xlarge"
    C7I_16XLARGE = "c7i.16xlarge"
    C7I_24XLARGE = "c7i.24xlarge"
    C7I_48XLARGE = "c7i.48xlarge"
    MAC2_M2PRO_METAL = "mac2-m2pro.metal"
    R7IZ_LARGE = "r7iz.large"
    R7IZ_XLARGE = "r7iz.xlarge"
    R7IZ_2XLARGE = "r7iz.2xlarge"
    R7IZ_4XLARGE = "r7iz.4xlarge"
    R7IZ_8XLARGE = "r7iz.8xlarge"
    R7IZ_12XLARGE = "r7iz.12xlarge"
    R7IZ_16XLARGE = "r7iz.16xlarge"
    R7IZ_32XLARGE = "r7iz.32xlarge"
    C7A_MEDIUM = "c7a.medium"
    C7A_LARGE = "c7a.large"
    C7A_XLARGE = "c7a.xlarge"
    C7A_2XLARGE = "c7a.2xlarge"
    C7A_4XLARGE = "c7a.4xlarge"
    C7A_8XLARGE = "c7a.8xlarge"
    C7A_12XLARGE = "c7a.12xlarge"
    C7A_16XLARGE = "c7a.16xlarge"
    C7A_24XLARGE = "c7a.24xlarge"
    C7A_32XLARGE = "c7a.32xlarge"
    C7A_48XLARGE = "c7a.48xlarge"
    C7A_METAL_48XL = "c7a.metal-48xl"
    R7A_METAL_48XL = "r7a.metal-48xl"
    R7I_LARGE = "r7i.large"
    R7I_XLARGE = "r7i.xlarge"
    R7I_2XLARGE = "r7i.2xlarge"
    R7I_4XLARGE = "r7i.4xlarge"
    R7I_8XLARGE = "r7i.8xlarge"
    R7I_12XLARGE = "r7i.12xlarge"
    R7I_16XLARGE = "r7i.16xlarge"
    R7I_24XLARGE = "r7i.24xlarge"
    R7I_48XLARGE = "r7i.48xlarge"
    DL2Q_24XLARGE = "dl2q.24xlarge"
    MAC2_M2_METAL = "mac2-m2.metal"
    I4I_12XLARGE = "i4i.12xlarge"
    I4I_24XLARGE = "i4i.24xlarge"
    C7I_METAL_24XL = "c7i.metal-24xl"
    C7I_METAL_48XL = "c7i.metal-48xl"
    M7I_METAL_24XL = "m7i.metal-24xl"
    M7I_METAL_48XL = "m7i.metal-48xl"
    R7I_METAL_24XL = "r7i.metal-24xl"
    R7I_METAL_48XL = "r7i.metal-48xl"
    R7IZ_METAL_16XL = "r7iz.metal-16xl"
    R7IZ_METAL_32XL = "r7iz.metal-32xl"
    C7GD_METAL = "c7gd.metal"
    M7GD_METAL = "m7gd.metal"
    R7GD_METAL = "r7gd.metal"
    G6_XLARGE = "g6.xlarge"
    G6_2XLARGE = "g6.2xlarge"
    G6_4XLARGE = "g6.4xlarge"
    G6_8XLARGE = "g6.8xlarge"
    G6_12XLARGE = "g6.12xlarge"
    G6_16XLARGE = "g6.16xlarge"
    G6_24XLARGE = "g6.24xlarge"
    G6_48XLARGE = "g6.48xlarge"
    GR6_4XLARGE = "gr6.4xlarge"
    GR6_8XLARGE = "gr6.8xlarge"
    C7I_FLEX_LARGE = "c7i-flex.large"
    C7I_FLEX_XLARGE = "c7i-flex.xlarge"
    C7I_FLEX_2XLARGE = "c7i-flex.2xlarge"
    C7I_FLEX_4XLARGE = "c7i-flex.4xlarge"
    C7I_FLEX_8XLARGE = "c7i-flex.8xlarge"
    U7I_12TB_224XLARGE = "u7i-12tb.224xlarge"
    U7IN_16TB_224XLARGE = "u7in-16tb.224xlarge"
    U7IN_24TB_224XLARGE = "u7in-24tb.224xlarge"
    U7IN_32TB_224XLARGE = "u7in-32tb.224xlarge"
    U7IB_12TB_224XLARGE = "u7ib-12tb.224xlarge"
    C7GN_METAL = "c7gn.metal"
    R8G_MEDIUM = "r8g.medium"
    R8G_LARGE = "r8g.large"
    R8G_XLARGE = "r8g.xlarge"
    R8G_2XLARGE = "r8g.2xlarge"
    R8G_4XLARGE = "r8g.4xlarge"
    R8G_8XLARGE = "r8g.8xlarge"
    R8G_12XLARGE = "r8g.12xlarge"
    R8G_16XLARGE = "r8g.16xlarge"
    R8G_24XLARGE = "r8g.24xlarge"
    R8G_48XLARGE = "r8g.48xlarge"
    R8G_METAL_24XL = "r8g.metal-24xl"
    R8G_METAL_48XL = "r8g.metal-48xl"
    MAC2_M1ULTRA_METAL = "mac2-m1ultra.metal"
    G6E_XLARGE = "g6e.xlarge"
    G6E_2XLARGE = "g6e.2xlarge"
    G6E_4XLARGE = "g6e.4xlarge"
    G6E_8XLARGE = "g6e.8xlarge"
    G6E_12XLARGE = "g6e.12xlarge"
    G6E_16XLARGE = "g6e.16xlarge"
    G6E_24XLARGE = "g6e.24xlarge"
    G6E_48XLARGE = "g6e.48xlarge"
    C8G_MEDIUM = "c8g.medium"
    C8G_LARGE = "c8g.large"
    C8G_XLARGE = "c8g.xlarge"
    C8G_2XLARGE = "c8g.2xlarge"
    C8G_4XLARGE = "c8g.4xlarge"
    C8G_8XLARGE = "c8g.8xlarge"
    C8G_12XLARGE = "c8g.12xlarge"
    C8G_16XLARGE = "c8g.16xlarge"
    C8G_24XLARGE = "c8g.24xlarge"
    C8G_48XLARGE = "c8g.48xlarge"
    C8G_METAL_24XL = "c8g.metal-24xl"
    C8G_METAL_48XL = "c8g.metal-48xl"
    M8G_MEDIUM = "m8g.medium"
    M8G_LARGE = "m8g.large"
    M8G_XLARGE = "m8g.xlarge"
    M8G_2XLARGE = "m8g.2xlarge"
    M8G_4XLARGE = "m8g.4xlarge"
    M8G_8XLARGE = "m8g.8xlarge"
    M8G_12XLARGE = "m8g.12xlarge"
    M8G_16XLARGE = "m8g.16xlarge"
    M8G_24XLARGE = "m8g.24xlarge"
    M8G_48XLARGE = "m8g.48xlarge"
    M8G_METAL_24XL = "m8g.metal-24xl"
    M8G_METAL_48XL = "m8g.metal-48xl"
    X8G_MEDIUM = "x8g.medium"
    X8G_LARGE = "x8g.large"
    X8G_XLARGE = "x8g.xlarge"
    X8G_2XLARGE = "x8g.2xlarge"
    X8G_4XLARGE = "x8g.4xlarge"
    X8G_8XLARGE = "x8g.8xlarge"
    X8G_12XLARGE = "x8g.12xlarge"
    X8G_16XLARGE = "x8g.16xlarge"
    X8G_24XLARGE = "x8g.24xlarge"
    X8G_48XLARGE = "x8g.48xlarge"
    X8G_METAL_24XL = "x8g.metal-24xl"
    X8G_METAL_48XL = "x8g.metal-48xl"
    I7IE_LARGE = "i7ie.large"
    I7IE_XLARGE = "i7ie.xlarge"
    I7IE_2XLARGE = "i7ie.2xlarge"
    I7IE_3XLARGE = "i7ie.3xlarge"
    I7IE_6XLARGE = "i7ie.6xlarge"
    I7IE_12XLARGE = "i7ie.12xlarge"
    I7IE_18XLARGE = "i7ie.18xlarge"
    I7IE_24XLARGE = "i7ie.24xlarge"
    I7IE_48XLARGE = "i7ie.48xlarge"
    I8G_LARGE = "i8g.large"
    I8G_XLARGE = "i8g.xlarge"
    I8G_2XLARGE = "i8g.2xlarge"
    I8G_4XLARGE = "i8g.4xlarge"
    I8G_8XLARGE = "i8g.8xlarge"
    I8G_12XLARGE = "i8g.12xlarge"
    I8G_16XLARGE = "i8g.16xlarge"
    I8G_24XLARGE = "i8g.24xlarge"
    I8G_METAL_24XL = "i8g.metal-24xl"
    U7I_6TB_112XLARGE = "u7i-6tb.112xlarge"
    U7I_8TB_112XLARGE = "u7i-8tb.112xlarge"
    U7INH_32TB_480XLARGE = "u7inh-32tb.480xlarge"
    P5E_48XLARGE = "p5e.48xlarge"
    P5EN_48XLARGE = "p5en.48xlarge"
    F2_12XLARGE = "f2.12xlarge"
    F2_48XLARGE = "f2.48xlarge"
    TRN2_48XLARGE = "trn2.48xlarge"
    C7I_FLEX_12XLARGE = "c7i-flex.12xlarge"
    C7I_FLEX_16XLARGE = "c7i-flex.16xlarge"
    M7I_FLEX_12XLARGE = "m7i-flex.12xlarge"
    M7I_FLEX_16XLARGE = "m7i-flex.16xlarge"
    I7IE_METAL_24XL = "i7ie.metal-24xl"
    I7IE_METAL_48XL = "i7ie.metal-48xl"
    I8G_48XLARGE = "i8g.48xlarge"
    C8GD_MEDIUM = "c8gd.medium"
    C8GD_LARGE = "c8gd.large"
    C8GD_XLARGE = "c8gd.xlarge"
    C8GD_2XLARGE = "c8gd.2xlarge"
    C8GD_4XLARGE = "c8gd.4xlarge"
    C8GD_8XLARGE = "c8gd.8xlarge"
    C8GD_12XLARGE = "c8gd.12xlarge"
    C8GD_16XLARGE = "c8gd.16xlarge"
    C8GD_24XLARGE = "c8gd.24xlarge"
    C8GD_48XLARGE = "c8gd.48xlarge"
    C8GD_METAL_24XL = "c8gd.metal-24xl"
    C8GD_METAL_48XL = "c8gd.metal-48xl"
    I7I_LARGE = "i7i.large"
    I7I_XLARGE = "i7i.xlarge"
    I7I_2XLARGE = "i7i.2xlarge"
    I7I_4XLARGE = "i7i.4xlarge"
    I7I_8XLARGE = "i7i.8xlarge"
    I7I_12XLARGE = "i7i.12xlarge"
    I7I_16XLARGE = "i7i.16xlarge"
    I7I_24XLARGE = "i7i.24xlarge"
    I7I_48XLARGE = "i7i.48xlarge"
    I7I_METAL_24XL = "i7i.metal-24xl"
    I7I_METAL_48XL = "i7i.metal-48xl"
    P6_B200_48XLARGE = "p6-b200.48xlarge"
    M8GD_MEDIUM = "m8gd.medium"
    M8GD_LARGE = "m8gd.large"
    M8GD_XLARGE = "m8gd.xlarge"
    M8GD_2XLARGE = "m8gd.2xlarge"
    M8GD_4XLARGE = "m8gd.4xlarge"
    M8GD_8XLARGE = "m8gd.8xlarge"
    M8GD_12XLARGE = "m8gd.12xlarge"
    M8GD_16XLARGE = "m8gd.16xlarge"
    M8GD_24XLARGE = "m8gd.24xlarge"
    M8GD_48XLARGE = "m8gd.48xlarge"
    M8GD_METAL_24XL = "m8gd.metal-24xl"
    M8GD_METAL_48XL = "m8gd.metal-48xl"
    R8GD_MEDIUM = "r8gd.medium"
    R8GD_LARGE = "r8gd.large"
    R8GD_XLARGE = "r8gd.xlarge"
    R8GD_2XLARGE = "r8gd.2xlarge"
    R8GD_4XLARGE = "r8gd.4xlarge"
    R8GD_8XLARGE = "r8gd.8xlarge"
    R8GD_12XLARGE = "r8gd.12xlarge"
    R8GD_16XLARGE = "r8gd.16xlarge"
    R8GD_24XLARGE = "r8gd.24xlarge"
    R8GD_48XLARGE = "r8gd.48xlarge"
    R8GD_METAL_24XL = "r8gd.metal-24xl"
    R8GD_METAL_48XL = "r8gd.metal-48xl"
    C8GN_MEDIUM = "c8gn.medium"
    C8GN_LARGE = "c8gn.large"
    C8GN_XLARGE = "c8gn.xlarge"
    C8GN_2XLARGE = "c8gn.2xlarge"
    C8GN_4XLARGE = "c8gn.4xlarge"
    C8GN_8XLARGE = "c8gn.8xlarge"
    C8GN_12XLARGE = "c8gn.12xlarge"
    C8GN_16XLARGE = "c8gn.16xlarge"
    C8GN_24XLARGE = "c8gn.24xlarge"
    C8GN_48XLARGE = "c8gn.48xlarge"
    C8GN_METAL_24XL = "c8gn.metal-24xl"
    C8GN_METAL_48XL = "c8gn.metal-48xl"
    F2_6XLARGE = "f2.6xlarge"
    P6E_GB200_36XLARGE = "p6e-gb200.36xlarge"
    G6F_LARGE = "g6f.large"
    G6F_XLARGE = "g6f.xlarge"
    G6F_2XLARGE = "g6f.2xlarge"
    G6F_4XLARGE = "g6f.4xlarge"
    GR6F_4XLARGE = "gr6f.4xlarge"
    P5_4XLARGE = "p5.4xlarge"
    R8I_LARGE = "r8i.large"
    R8I_XLARGE = "r8i.xlarge"
    R8I_2XLARGE = "r8i.2xlarge"
    R8I_4XLARGE = "r8i.4xlarge"
    R8I_8XLARGE = "r8i.8xlarge"
    R8I_12XLARGE = "r8i.12xlarge"
    R8I_16XLARGE = "r8i.16xlarge"
    R8I_24XLARGE = "r8i.24xlarge"
    R8I_32XLARGE = "r8i.32xlarge"
    R8I_48XLARGE = "r8i.48xlarge"
    R8I_96XLARGE = "r8i.96xlarge"
    R8I_METAL_48XL = "r8i.metal-48xl"
    R8I_METAL_96XL = "r8i.metal-96xl"
    R8I_FLEX_LARGE = "r8i-flex.large"
    R8I_FLEX_XLARGE = "r8i-flex.xlarge"
    R8I_FLEX_2XLARGE = "r8i-flex.2xlarge"
    R8I_FLEX_4XLARGE = "r8i-flex.4xlarge"
    R8I_FLEX_8XLARGE = "r8i-flex.8xlarge"
    R8I_FLEX_12XLARGE = "r8i-flex.12xlarge"
    R8I_FLEX_16XLARGE = "r8i-flex.16xlarge"
    M8I_LARGE = "m8i.large"
    M8I_XLARGE = "m8i.xlarge"
    M8I_2XLARGE = "m8i.2xlarge"
    M8I_4XLARGE = "m8i.4xlarge"
    M8I_8XLARGE = "m8i.8xlarge"
    M8I_12XLARGE = "m8i.12xlarge"
    M8I_16XLARGE = "m8i.16xlarge"
    M8I_24XLARGE = "m8i.24xlarge"
    M8I_32XLARGE = "m8i.32xlarge"
    M8I_48XLARGE = "m8i.48xlarge"
    M8I_96XLARGE = "m8i.96xlarge"
    M8I_METAL_48XL = "m8i.metal-48xl"
    M8I_METAL_96XL = "m8i.metal-96xl"
    M8I_FLEX_LARGE = "m8i-flex.large"
    M8I_FLEX_XLARGE = "m8i-flex.xlarge"
    M8I_FLEX_2XLARGE = "m8i-flex.2xlarge"
    M8I_FLEX_4XLARGE = "m8i-flex.4xlarge"
    M8I_FLEX_8XLARGE = "m8i-flex.8xlarge"
    M8I_FLEX_12XLARGE = "m8i-flex.12xlarge"
    M8I_FLEX_16XLARGE = "m8i-flex.16xlarge"
    I8GE_LARGE = "i8ge.large"
    I8GE_XLARGE = "i8ge.xlarge"
    I8GE_2XLARGE = "i8ge.2xlarge"
    I8GE_3XLARGE = "i8ge.3xlarge"
    I8GE_6XLARGE = "i8ge.6xlarge"
    I8GE_12XLARGE = "i8ge.12xlarge"
    I8GE_18XLARGE = "i8ge.18xlarge"
    I8GE_24XLARGE = "i8ge.24xlarge"
    I8GE_48XLARGE = "i8ge.48xlarge"
    I8GE_METAL_24XL = "i8ge.metal-24xl"
    I8GE_METAL_48XL = "i8ge.metal-48xl"
    MAC_M4_METAL = "mac-m4.metal"
    MAC_M4PRO_METAL = "mac-m4pro.metal"
    R8GN_MEDIUM = "r8gn.medium"
    R8GN_LARGE = "r8gn.large"
    R8GN_XLARGE = "r8gn.xlarge"
    R8GN_2XLARGE = "r8gn.2xlarge"
    R8GN_4XLARGE = "r8gn.4xlarge"
    R8GN_8XLARGE = "r8gn.8xlarge"
    R8GN_12XLARGE = "r8gn.12xlarge"
    R8GN_16XLARGE = "r8gn.16xlarge"
    R8GN_24XLARGE = "r8gn.24xlarge"
    R8GN_48XLARGE = "r8gn.48xlarge"
    R8GN_METAL_24XL = "r8gn.metal-24xl"
    R8GN_METAL_48XL = "r8gn.metal-48xl"
    C8I_LARGE = "c8i.large"
    C8I_XLARGE = "c8i.xlarge"
    C8I_2XLARGE = "c8i.2xlarge"
    C8I_4XLARGE = "c8i.4xlarge"
    C8I_8XLARGE = "c8i.8xlarge"
    C8I_12XLARGE = "c8i.12xlarge"
    C8I_16XLARGE = "c8i.16xlarge"
    C8I_24XLARGE = "c8i.24xlarge"
    C8I_32XLARGE = "c8i.32xlarge"
    C8I_48XLARGE = "c8i.48xlarge"
    C8I_96XLARGE = "c8i.96xlarge"
    C8I_METAL_48XL = "c8i.metal-48xl"
    C8I_METAL_96XL = "c8i.metal-96xl"
    C8I_FLEX_LARGE = "c8i-flex.large"
    C8I_FLEX_XLARGE = "c8i-flex.xlarge"
    C8I_FLEX_2XLARGE = "c8i-flex.2xlarge"
    C8I_FLEX_4XLARGE = "c8i-flex.4xlarge"
    C8I_FLEX_8XLARGE = "c8i-flex.8xlarge"
    C8I_FLEX_12XLARGE = "c8i-flex.12xlarge"
    C8I_FLEX_16XLARGE = "c8i-flex.16xlarge"
    R8GB_MEDIUM = "r8gb.medium"
    R8GB_LARGE = "r8gb.large"
    R8GB_XLARGE = "r8gb.xlarge"
    R8GB_2XLARGE = "r8gb.2xlarge"
    R8GB_4XLARGE = "r8gb.4xlarge"
    R8GB_8XLARGE = "r8gb.8xlarge"
    R8GB_12XLARGE = "r8gb.12xlarge"
    R8GB_16XLARGE = "r8gb.16xlarge"
    R8GB_24XLARGE = "r8gb.24xlarge"
    R8GB_METAL_24XL = "r8gb.metal-24xl"
    M8A_MEDIUM = "m8a.medium"
    M8A_LARGE = "m8a.large"
    M8A_XLARGE = "m8a.xlarge"
    M8A_2XLARGE = "m8a.2xlarge"
    M8A_4XLARGE = "m8a.4xlarge"
    M8A_8XLARGE = "m8a.8xlarge"
    M8A_12XLARGE = "m8a.12xlarge"
    M8A_16XLARGE = "m8a.16xlarge"
    M8A_24XLARGE = "m8a.24xlarge"
    M8A_48XLARGE = "m8a.48xlarge"
    M8A_METAL_24XL = "m8a.metal-24xl"
    M8A_METAL_48XL = "m8a.metal-48xl"
    TRN2_3XLARGE = "trn2.3xlarge"
    R8A_MEDIUM = "r8a.medium"
    R8A_LARGE = "r8a.large"
    R8A_XLARGE = "r8a.xlarge"
    R8A_2XLARGE = "r8a.2xlarge"
    R8A_4XLARGE = "r8a.4xlarge"
    R8A_8XLARGE = "r8a.8xlarge"
    R8A_12XLARGE = "r8a.12xlarge"
    R8A_16XLARGE = "r8a.16xlarge"
    R8A_24XLARGE = "r8a.24xlarge"
    R8A_48XLARGE = "r8a.48xlarge"
    R8A_METAL_24XL = "r8a.metal-24xl"
    R8A_METAL_48XL = "r8a.metal-48xl"
    P6_B300_48XLARGE = "p6-b300.48xlarge"
    C8A_MEDIUM = "c8a.medium"
    C8A_LARGE = "c8a.large"
    C8A_XLARGE = "c8a.xlarge"
    C8A_2XLARGE = "c8a.2xlarge"
    C8A_4XLARGE = "c8a.4xlarge"
    C8A_8XLARGE = "c8a.8xlarge"
    C8A_12XLARGE = "c8a.12xlarge"
    C8A_16XLARGE = "c8a.16xlarge"
    C8A_24XLARGE = "c8a.24xlarge"
    C8A_48XLARGE = "c8a.48xlarge"
    C8A_METAL_24XL = "c8a.metal-24xl"
    C8A_METAL_48XL = "c8a.metal-48xl"


class InstanceTypeHypervisor:
    """InstanceTypeHypervisor enum values."""

    NITRO = "nitro"
    XEN = "xen"


class InterfacePermissionType:
    """InterfacePermissionType enum values."""

    INSTANCE_ATTACH = "INSTANCE-ATTACH"
    EIP_ASSOCIATE = "EIP-ASSOCIATE"


class InterfaceProtocolType:
    """InterfaceProtocolType enum values."""

    VLAN = "VLAN"
    GRE = "GRE"


class InternetGatewayBlockMode:
    """InternetGatewayBlockMode enum values."""

    OFF = "off"
    BLOCK_BIDIRECTIONAL = "block-bidirectional"
    BLOCK_INGRESS = "block-ingress"


class InternetGatewayExclusionMode:
    """InternetGatewayExclusionMode enum values."""

    ALLOW_BIDIRECTIONAL = "allow-bidirectional"
    ALLOW_EGRESS = "allow-egress"


class InterruptibleCapacityReservationAllocationStatus:
    """InterruptibleCapacityReservationAllocationStatus enum values."""

    PENDING = "pending"
    ACTIVE = "active"
    UPDATING = "updating"
    CANCELING = "canceling"
    CANCELED = "canceled"
    FAILED = "failed"


class InterruptionType:
    """InterruptionType enum values."""

    ADHOC = "adhoc"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"
    IPV6 = "ipv6"


class IpSource:
    """IpSource enum values."""

    AMAZON = "amazon"
    BYOIP = "byoip"
    NONE = "none"


class IpamAddressHistoryResourceType:
    """IpamAddressHistoryResourceType enum values."""

    EIP = "eip"
    VPC = "vpc"
    SUBNET = "subnet"
    NETWORK_INTERFACE = "network-interface"
    INSTANCE = "instance"


class IpamAssociatedResourceDiscoveryStatus:
    """IpamAssociatedResourceDiscoveryStatus enum values."""

    ACTIVE = "active"
    NOT_FOUND = "not-found"


class IpamComplianceStatus:
    """IpamComplianceStatus enum values."""

    COMPLIANT = "compliant"
    NONCOMPLIANT = "noncompliant"
    UNMANAGED = "unmanaged"
    IGNORED = "ignored"


class IpamDiscoveryFailureCode:
    """IpamDiscoveryFailureCode enum values."""

    ASSUME_ROLE_FAILURE = "assume-role-failure"
    THROTTLING_FAILURE = "throttling-failure"
    UNAUTHORIZED_FAILURE = "unauthorized-failure"


class IpamExternalResourceVerificationTokenState:
    """IpamExternalResourceVerificationTokenState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"


class IpamManagementState:
    """IpamManagementState enum values."""

    MANAGED = "managed"
    UNMANAGED = "unmanaged"
    IGNORED = "ignored"


class IpamMeteredAccount:
    """IpamMeteredAccount enum values."""

    IPAM_OWNER = "ipam-owner"
    RESOURCE_OWNER = "resource-owner"


class IpamNetworkInterfaceAttachmentStatus:
    """IpamNetworkInterfaceAttachmentStatus enum values."""

    AVAILABLE = "available"
    IN_USE = "in-use"


class IpamOverlapStatus:
    """IpamOverlapStatus enum values."""

    OVERLAPPING = "overlapping"
    NONOVERLAPPING = "nonoverlapping"
    IGNORED = "ignored"


class IpamPolicyManagedBy:
    """IpamPolicyManagedBy enum values."""

    ACCOUNT = "account"
    DELEGATED_ADMINISTRATOR_FOR_IPAM = "delegated-administrator-for-ipam"


class IpamPolicyResourceType:
    """IpamPolicyResourceType enum values."""

    ALB = "alb"
    EIP = "eip"
    RDS = "rds"
    RNAT = "rnat"


class IpamPolicyState:
    """IpamPolicyState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamPoolAllocationResourceType:
    """IpamPoolAllocationResourceType enum values."""

    IPAM_POOL = "ipam-pool"
    VPC = "vpc"
    EC2_PUBLIC_IPV4_POOL = "ec2-public-ipv4-pool"
    CUSTOM = "custom"
    SUBNET = "subnet"
    EIP = "eip"
    ANYCAST_IP_LIST = "anycast-ip-list"


class IpamPoolAwsService:
    """IpamPoolAwsService enum values."""

    EC2 = "ec2"
    GLOBAL_SERVICES = "global-services"


class IpamPoolCidrFailureCode:
    """IpamPoolCidrFailureCode enum values."""

    CIDR_NOT_AVAILABLE = "cidr-not-available"
    LIMIT_EXCEEDED = "limit-exceeded"


class IpamPoolCidrState:
    """IpamPoolCidrState enum values."""

    PENDING_PROVISION = "pending-provision"
    PROVISIONED = "provisioned"
    FAILED_PROVISION = "failed-provision"
    PENDING_DEPROVISION = "pending-deprovision"
    DEPROVISIONED = "deprovisioned"
    FAILED_DEPROVISION = "failed-deprovision"
    PENDING_IMPORT = "pending-import"
    FAILED_IMPORT = "failed-import"


class IpamPoolPublicIpSource:
    """IpamPoolPublicIpSource enum values."""

    AMAZON = "amazon"
    BYOIP = "byoip"


class IpamPoolSourceResourceType:
    """IpamPoolSourceResourceType enum values."""

    VPC = "vpc"


class IpamPoolState:
    """IpamPoolState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamPrefixListResolverRuleConditionOperation:
    """IpamPrefixListResolverRuleConditionOperation enum values."""

    EQUALS = "equals"
    NOT_EQUALS = "not-equals"
    SUBNET_OF = "subnet-of"


class IpamPrefixListResolverRuleType:
    """IpamPrefixListResolverRuleType enum values."""

    STATIC_CIDR = "static-cidr"
    IPAM_RESOURCE_CIDR = "ipam-resource-cidr"
    IPAM_POOL_CIDR = "ipam-pool-cidr"


class IpamPrefixListResolverState:
    """IpamPrefixListResolverState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamPrefixListResolverTargetState:
    """IpamPrefixListResolverTargetState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    SYNC_IN_PROGRESS = "sync-in-progress"
    SYNC_COMPLETE = "sync-complete"
    SYNC_FAILED = "sync-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamPrefixListResolverVersionCreationStatus:
    """IpamPrefixListResolverVersionCreationStatus enum values."""

    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"


class IpamPublicAddressAssociationStatus:
    """IpamPublicAddressAssociationStatus enum values."""

    ASSOCIATED = "associated"
    DISASSOCIATED = "disassociated"


class IpamPublicAddressAwsService:
    """IpamPublicAddressAwsService enum values."""

    NAT_GATEWAY = "nat-gateway"
    DATABASE_MIGRATION_SERVICE = "database-migration-service"
    REDSHIFT = "redshift"
    ELASTIC_CONTAINER_SERVICE = "elastic-container-service"
    RELATIONAL_DATABASE_SERVICE = "relational-database-service"
    SITE_TO_SITE_VPN = "site-to-site-vpn"
    LOAD_BALANCER = "load-balancer"
    GLOBAL_ACCELERATOR = "global-accelerator"
    CLOUDFRONT = "cloudfront"
    OTHER = "other"


class IpamPublicAddressType:
    """IpamPublicAddressType enum values."""

    SERVICE_MANAGED_IP = "service-managed-ip"
    SERVICE_MANAGED_BYOIP = "service-managed-byoip"
    AMAZON_OWNED_EIP = "amazon-owned-eip"
    AMAZON_OWNED_CONTIG = "amazon-owned-contig"
    BYOIP = "byoip"
    EC2_PUBLIC_IP = "ec2-public-ip"
    ANYCAST_IP_LIST_IP = "anycast-ip-list-ip"


class IpamResourceCidrIpSource:
    """IpamResourceCidrIpSource enum values."""

    AMAZON = "amazon"
    BYOIP = "byoip"
    NONE = "none"


class IpamResourceDiscoveryAssociationState:
    """IpamResourceDiscoveryAssociationState enum values."""

    ASSOCIATE_IN_PROGRESS = "associate-in-progress"
    ASSOCIATE_COMPLETE = "associate-complete"
    ASSOCIATE_FAILED = "associate-failed"
    DISASSOCIATE_IN_PROGRESS = "disassociate-in-progress"
    DISASSOCIATE_COMPLETE = "disassociate-complete"
    DISASSOCIATE_FAILED = "disassociate-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamResourceDiscoveryState:
    """IpamResourceDiscoveryState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamResourceType:
    """IpamResourceType enum values."""

    VPC = "vpc"
    SUBNET = "subnet"
    EIP = "eip"
    PUBLIC_IPV4_POOL = "public-ipv4-pool"
    IPV6_POOL = "ipv6-pool"
    ENI = "eni"
    ANYCAST_IP_LIST = "anycast-ip-list"


class IpamScopeExternalAuthorityType:
    """IpamScopeExternalAuthorityType enum values."""

    INFOBLOX = "infoblox"


class IpamScopeState:
    """IpamScopeState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamScopeType:
    """IpamScopeType enum values."""

    PUBLIC = "public"
    PRIVATE = "private"


class IpamState:
    """IpamState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"
    ISOLATE_IN_PROGRESS = "isolate-in-progress"
    ISOLATE_COMPLETE = "isolate-complete"
    RESTORE_IN_PROGRESS = "restore-in-progress"


class IpamTier:
    """IpamTier enum values."""

    FREE = "free"
    ADVANCED = "advanced"


class Ipv6AddressAttribute:
    """Ipv6AddressAttribute enum values."""

    PUBLIC = "public"
    PRIVATE = "private"


class Ipv6SupportValue:
    """Ipv6SupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class KeyFormat:
    """KeyFormat enum values."""

    PEM = "pem"
    PPK = "ppk"


class KeyType:
    """KeyType enum values."""

    RSA = "rsa"
    ED25519 = "ed25519"


class LaunchTemplateAutoRecoveryState:
    """LaunchTemplateAutoRecoveryState enum values."""

    DEFAULT = "default"
    DISABLED = "disabled"


class LaunchTemplateErrorCode:
    """LaunchTemplateErrorCode enum values."""

    LAUNCHTEMPLATEIDDOESNOTEXIST = "launchTemplateIdDoesNotExist"
    LAUNCHTEMPLATEIDMALFORMED = "launchTemplateIdMalformed"
    LAUNCHTEMPLATENAMEDOESNOTEXIST = "launchTemplateNameDoesNotExist"
    LAUNCHTEMPLATENAMEMALFORMED = "launchTemplateNameMalformed"
    LAUNCHTEMPLATEVERSIONDOESNOTEXIST = "launchTemplateVersionDoesNotExist"
    UNEXPECTEDERROR = "unexpectedError"


class LaunchTemplateHttpTokensState:
    """LaunchTemplateHttpTokensState enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"


class LaunchTemplateInstanceMetadataEndpointState:
    """LaunchTemplateInstanceMetadataEndpointState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class LaunchTemplateInstanceMetadataOptionsState:
    """LaunchTemplateInstanceMetadataOptionsState enum values."""

    PENDING = "pending"
    APPLIED = "applied"


class LaunchTemplateInstanceMetadataProtocolIpv6:
    """LaunchTemplateInstanceMetadataProtocolIpv6 enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class LaunchTemplateInstanceMetadataTagsState:
    """LaunchTemplateInstanceMetadataTagsState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class ListingState:
    """ListingState enum values."""

    AVAILABLE = "available"
    SOLD = "sold"
    CANCELLED = "cancelled"
    PENDING = "pending"


class ListingStatus:
    """ListingStatus enum values."""

    ACTIVE = "active"
    PENDING = "pending"
    CANCELLED = "cancelled"
    CLOSED = "closed"


class LocalGatewayRouteState:
    """LocalGatewayRouteState enum values."""

    PENDING = "pending"
    ACTIVE = "active"
    BLACKHOLE = "blackhole"
    DELETING = "deleting"
    DELETED = "deleted"


class LocalGatewayRouteTableMode:
    """LocalGatewayRouteTableMode enum values."""

    DIRECT_VPC_ROUTING = "direct-vpc-routing"
    COIP = "coip"


class LocalGatewayRouteType:
    """LocalGatewayRouteType enum values."""

    STATIC = "static"
    PROPAGATED = "propagated"


class LocalGatewayVirtualInterfaceConfigurationState:
    """LocalGatewayVirtualInterfaceConfigurationState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class LocalGatewayVirtualInterfaceGroupConfigurationState:
    """LocalGatewayVirtualInterfaceGroupConfigurationState enum values."""

    PENDING = "pending"
    INCOMPLETE = "incomplete"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class LocalStorage:
    """LocalStorage enum values."""

    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class LocalStorageType:
    """LocalStorageType enum values."""

    HDD = "hdd"
    SSD = "ssd"


class LocationType:
    """LocationType enum values."""

    REGION = "region"
    AVAILABILITY_ZONE = "availability-zone"
    AVAILABILITY_ZONE_ID = "availability-zone-id"
    OUTPOST = "outpost"


class LockMode:
    """LockMode enum values."""

    COMPLIANCE = "compliance"
    GOVERNANCE = "governance"


class LockState:
    """LockState enum values."""

    COMPLIANCE = "compliance"
    GOVERNANCE = "governance"
    COMPLIANCE_COOLOFF = "compliance-cooloff"
    EXPIRED = "expired"


class LogDestinationType:
    """LogDestinationType enum values."""

    CLOUD_WATCH_LOGS = "cloud-watch-logs"
    S3 = "s3"
    KINESIS_DATA_FIREHOSE = "kinesis-data-firehose"


class MacModificationTaskState:
    """MacModificationTaskState enum values."""

    SUCCESSFUL = "successful"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    PENDING = "pending"


class MacModificationTaskType:
    """MacModificationTaskType enum values."""

    SIP_MODIFICATION = "sip-modification"
    VOLUME_OWNERSHIP_DELEGATION = "volume-ownership-delegation"


class MacSystemIntegrityProtectionSettingStatus:
    """MacSystemIntegrityProtectionSettingStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ManagedBy:
    """ManagedBy enum values."""

    ACCOUNT = "account"
    DECLARATIVE_POLICY = "declarative-policy"


class MarketType:
    """MarketType enum values."""

    SPOT = "spot"
    CAPACITY_BLOCK = "capacity-block"
    INTERRUPTIBLE_CAPACITY_RESERVATION = "interruptible-capacity-reservation"


class MembershipType:
    """MembershipType enum values."""

    STATIC = "static"
    IGMP = "igmp"


class MetadataDefaultHttpTokensState:
    """MetadataDefaultHttpTokensState enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"
    NO_PREFERENCE = "no-preference"


class Metric:
    """Metric enum values."""

    RESERVATION_TOTAL_CAPACITY_HRS_VCPU = "reservation-total-capacity-hrs-vcpu"
    RESERVATION_TOTAL_CAPACITY_HRS_INST = "reservation-total-capacity-hrs-inst"
    RESERVATION_MAX_SIZE_VCPU = "reservation-max-size-vcpu"
    RESERVATION_MAX_SIZE_INST = "reservation-max-size-inst"
    RESERVATION_MIN_SIZE_VCPU = "reservation-min-size-vcpu"
    RESERVATION_MIN_SIZE_INST = "reservation-min-size-inst"
    RESERVATION_UNUSED_TOTAL_CAPACITY_HRS_VCPU = "reservation-unused-total-capacity-hrs-vcpu"
    RESERVATION_UNUSED_TOTAL_CAPACITY_HRS_INST = "reservation-unused-total-capacity-hrs-inst"
    RESERVATION_UNUSED_TOTAL_ESTIMATED_COST = "reservation-unused-total-estimated-cost"
    RESERVATION_MAX_UNUSED_SIZE_VCPU = "reservation-max-unused-size-vcpu"
    RESERVATION_MAX_UNUSED_SIZE_INST = "reservation-max-unused-size-inst"
    RESERVATION_MIN_UNUSED_SIZE_VCPU = "reservation-min-unused-size-vcpu"
    RESERVATION_MIN_UNUSED_SIZE_INST = "reservation-min-unused-size-inst"
    RESERVATION_MAX_UTILIZATION = "reservation-max-utilization"
    RESERVATION_MIN_UTILIZATION = "reservation-min-utilization"
    RESERVATION_AVG_UTILIZATION_VCPU = "reservation-avg-utilization-vcpu"
    RESERVATION_AVG_UTILIZATION_INST = "reservation-avg-utilization-inst"
    RESERVATION_TOTAL_COUNT = "reservation-total-count"
    RESERVATION_TOTAL_ESTIMATED_COST = "reservation-total-estimated-cost"
    RESERVATION_AVG_FUTURE_SIZE_VCPU = "reservation-avg-future-size-vcpu"
    RESERVATION_AVG_FUTURE_SIZE_INST = "reservation-avg-future-size-inst"
    RESERVATION_MIN_FUTURE_SIZE_VCPU = "reservation-min-future-size-vcpu"
    RESERVATION_MIN_FUTURE_SIZE_INST = "reservation-min-future-size-inst"
    RESERVATION_MAX_FUTURE_SIZE_VCPU = "reservation-max-future-size-vcpu"
    RESERVATION_MAX_FUTURE_SIZE_INST = "reservation-max-future-size-inst"
    RESERVATION_AVG_COMMITTED_SIZE_VCPU = "reservation-avg-committed-size-vcpu"
    RESERVATION_AVG_COMMITTED_SIZE_INST = "reservation-avg-committed-size-inst"
    RESERVATION_MAX_COMMITTED_SIZE_VCPU = "reservation-max-committed-size-vcpu"
    RESERVATION_MAX_COMMITTED_SIZE_INST = "reservation-max-committed-size-inst"
    RESERVATION_MIN_COMMITTED_SIZE_VCPU = "reservation-min-committed-size-vcpu"
    RESERVATION_MIN_COMMITTED_SIZE_INST = "reservation-min-committed-size-inst"
    RESERVED_TOTAL_USAGE_HRS_VCPU = "reserved-total-usage-hrs-vcpu"
    RESERVED_TOTAL_USAGE_HRS_INST = "reserved-total-usage-hrs-inst"
    RESERVED_TOTAL_ESTIMATED_COST = "reserved-total-estimated-cost"
    UNRESERVED_TOTAL_USAGE_HRS_VCPU = "unreserved-total-usage-hrs-vcpu"
    UNRESERVED_TOTAL_USAGE_HRS_INST = "unreserved-total-usage-hrs-inst"
    UNRESERVED_TOTAL_ESTIMATED_COST = "unreserved-total-estimated-cost"
    SPOT_TOTAL_USAGE_HRS_VCPU = "spot-total-usage-hrs-vcpu"
    SPOT_TOTAL_USAGE_HRS_INST = "spot-total-usage-hrs-inst"
    SPOT_TOTAL_ESTIMATED_COST = "spot-total-estimated-cost"
    SPOT_AVG_RUN_TIME_BEFORE_INTERRUPTION_INST = "spot-avg-run-time-before-interruption-inst"
    SPOT_MAX_RUN_TIME_BEFORE_INTERRUPTION_INST = "spot-max-run-time-before-interruption-inst"
    SPOT_MIN_RUN_TIME_BEFORE_INTERRUPTION_INST = "spot-min-run-time-before-interruption-inst"
    SPOT_TOTAL_INTERRUPTIONS_INST = "spot-total-interruptions-inst"
    SPOT_TOTAL_INTERRUPTIONS_VCPU = "spot-total-interruptions-vcpu"
    SPOT_TOTAL_COUNT_INST = "spot-total-count-inst"
    SPOT_TOTAL_COUNT_VCPU = "spot-total-count-vcpu"
    SPOT_INTERRUPTION_RATE_INST = "spot-interruption-rate-inst"
    SPOT_INTERRUPTION_RATE_VCPU = "spot-interruption-rate-vcpu"


class MetricType:
    """MetricType enum values."""

    AGGREGATE_LATENCY = "aggregate-latency"


class ModifyAvailabilityZoneOptInStatus:
    """ModifyAvailabilityZoneOptInStatus enum values."""

    OPTED_IN = "opted-in"
    NOT_OPTED_IN = "not-opted-in"


class MonitoringState:
    """MonitoringState enum values."""

    DISABLED = "disabled"
    DISABLING = "disabling"
    ENABLED = "enabled"
    PENDING = "pending"


class MoveStatus:
    """MoveStatus enum values."""

    MOVINGTOVPC = "movingToVpc"
    RESTORINGTOCLASSIC = "restoringToClassic"


class MulticastSupportValue:
    """MulticastSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class NatGatewayAddressStatus:
    """NatGatewayAddressStatus enum values."""

    ASSIGNING = "assigning"
    UNASSIGNING = "unassigning"
    ASSOCIATING = "associating"
    DISASSOCIATING = "disassociating"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class NatGatewayApplianceModifyState:
    """NatGatewayApplianceModifyState enum values."""

    MODIFYING = "modifying"
    COMPLETED = "completed"
    FAILED = "failed"


class NatGatewayApplianceState:
    """NatGatewayApplianceState enum values."""

    ATTACHING = "attaching"
    ATTACHED = "attached"
    DETACHING = "detaching"
    DETACHED = "detached"
    ATTACH_FAILED = "attach-failed"
    DETACH_FAILED = "detach-failed"


class NatGatewayApplianceType:
    """NatGatewayApplianceType enum values."""

    NETWORK_FIREWALL_PROXY = "network-firewall-proxy"


class NatGatewayState:
    """NatGatewayState enum values."""

    PENDING = "pending"
    FAILED = "failed"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class NetworkInterfaceAttribute:
    """NetworkInterfaceAttribute enum values."""

    DESCRIPTION = "description"
    GROUPSET = "groupSet"
    SOURCEDESTCHECK = "sourceDestCheck"
    ATTACHMENT = "attachment"
    ASSOCIATEPUBLICIPADDRESS = "associatePublicIpAddress"


class NetworkInterfaceCreationType:
    """NetworkInterfaceCreationType enum values."""

    EFA = "efa"
    EFA_ONLY = "efa-only"
    BRANCH = "branch"
    TRUNK = "trunk"


class NetworkInterfacePermissionStateCode:
    """NetworkInterfacePermissionStateCode enum values."""

    PENDING = "pending"
    GRANTED = "granted"
    REVOKING = "revoking"
    REVOKED = "revoked"


class NetworkInterfaceStatus:
    """NetworkInterfaceStatus enum values."""

    AVAILABLE = "available"
    ASSOCIATED = "associated"
    ATTACHING = "attaching"
    IN_USE = "in-use"
    DETACHING = "detaching"


class NetworkInterfaceType:
    """NetworkInterfaceType enum values."""

    INTERFACE = "interface"
    NATGATEWAY = "natGateway"
    EFA = "efa"
    EFA_ONLY = "efa-only"
    TRUNK = "trunk"
    LOAD_BALANCER = "load_balancer"
    NETWORK_LOAD_BALANCER = "network_load_balancer"
    VPC_ENDPOINT = "vpc_endpoint"
    BRANCH = "branch"
    TRANSIT_GATEWAY = "transit_gateway"
    LAMBDA = "lambda"
    QUICKSIGHT = "quicksight"
    GLOBAL_ACCELERATOR_MANAGED = "global_accelerator_managed"
    API_GATEWAY_MANAGED = "api_gateway_managed"
    GATEWAY_LOAD_BALANCER = "gateway_load_balancer"
    GATEWAY_LOAD_BALANCER_ENDPOINT = "gateway_load_balancer_endpoint"
    IOT_RULES_MANAGED = "iot_rules_managed"
    AWS_CODESTAR_CONNECTIONS_MANAGED = "aws_codestar_connections_managed"


class NitroEnclavesSupport:
    """NitroEnclavesSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class NitroTpmSupport:
    """NitroTpmSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class OfferingClassType:
    """OfferingClassType enum values."""

    STANDARD = "standard"
    CONVERTIBLE = "convertible"


class OfferingTypeValues:
    """OfferingTypeValues enum values."""

    HEAVY_UTILIZATION = "Heavy Utilization"
    MEDIUM_UTILIZATION = "Medium Utilization"
    LIGHT_UTILIZATION = "Light Utilization"
    NO_UPFRONT = "No Upfront"
    PARTIAL_UPFRONT = "Partial Upfront"
    ALL_UPFRONT = "All Upfront"


class OnDemandAllocationStrategy:
    """OnDemandAllocationStrategy enum values."""

    LOWESTPRICE = "lowestPrice"
    PRIORITIZED = "prioritized"


class OperationType:
    """OperationType enum values."""

    ADD = "add"
    REMOVE = "remove"


class OutputFormat:
    """OutputFormat enum values."""

    CSV = "csv"
    PARQUET = "parquet"


class PartitionLoadFrequency:
    """PartitionLoadFrequency enum values."""

    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class PayerResponsibility:
    """PayerResponsibility enum values."""

    SERVICEOWNER = "ServiceOwner"


class PaymentOption:
    """PaymentOption enum values."""

    ALLUPFRONT = "AllUpfront"
    PARTIALUPFRONT = "PartialUpfront"
    NOUPFRONT = "NoUpfront"


class PeriodType:
    """PeriodType enum values."""

    FIVE_MINUTES = "five-minutes"
    FIFTEEN_MINUTES = "fifteen-minutes"
    ONE_HOUR = "one-hour"
    THREE_HOURS = "three-hours"
    ONE_DAY = "one-day"
    ONE_WEEK = "one-week"


class PermissionGroup:
    """PermissionGroup enum values."""

    ALL = "all"


class PhcSupport:
    """PhcSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class PlacementGroupState:
    """PlacementGroupState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class PlacementGroupStrategy:
    """PlacementGroupStrategy enum values."""

    CLUSTER = "cluster"
    PARTITION = "partition"
    SPREAD = "spread"


class PlacementStrategy:
    """PlacementStrategy enum values."""

    CLUSTER = "cluster"
    SPREAD = "spread"
    PARTITION = "partition"


class PlatformValues:
    """PlatformValues enum values."""

    WINDOWS = "Windows"


class PrefixListState:
    """PrefixListState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    MODIFY_FAILED = "modify-failed"
    RESTORE_IN_PROGRESS = "restore-in-progress"
    RESTORE_COMPLETE = "restore-complete"
    RESTORE_FAILED = "restore-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DELETE_FAILED = "delete-failed"


class PrincipalType:
    """PrincipalType enum values."""

    ALL = "All"
    SERVICE = "Service"
    ORGANIZATIONUNIT = "OrganizationUnit"
    ACCOUNT = "Account"
    USER = "User"
    ROLE = "Role"


class ProductCodeValues:
    """ProductCodeValues enum values."""

    DEVPAY = "devpay"
    MARKETPLACE = "marketplace"


class Protocol:
    """Protocol enum values."""

    TCP = "tcp"
    UDP = "udp"


class ProtocolValue:
    """ProtocolValue enum values."""

    GRE = "gre"


class PublicIpDnsOption:
    """PublicIpDnsOption enum values."""

    PUBLIC_DUAL_STACK_DNS_NAME = "public-dual-stack-dns-name"
    PUBLIC_IPV4_DNS_NAME = "public-ipv4-dns-name"
    PUBLIC_IPV6_DNS_NAME = "public-ipv6-dns-name"


class RIProductDescription:
    """RIProductDescription enum values."""

    LINUX_UNIX = "Linux/UNIX"
    LINUX_UNIX_AMAZON_VPC = "Linux/UNIX (Amazon VPC)"
    WINDOWS = "Windows"
    WINDOWS_AMAZON_VPC = "Windows (Amazon VPC)"


class RebootMigrationSupport:
    """RebootMigrationSupport enum values."""

    UNSUPPORTED = "unsupported"
    SUPPORTED = "supported"


class RecurringChargeFrequency:
    """RecurringChargeFrequency enum values."""

    HOURLY = "Hourly"


class ReplaceRootVolumeTaskState:
    """ReplaceRootVolumeTaskState enum values."""

    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    FAILING = "failing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    FAILED_DETACHED = "failed-detached"


class ReplacementStrategy:
    """ReplacementStrategy enum values."""

    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class ReportInstanceReasonCodes:
    """ReportInstanceReasonCodes enum values."""

    INSTANCE_STUCK_IN_STATE = "instance-stuck-in-state"
    UNRESPONSIVE = "unresponsive"
    NOT_ACCEPTING_CREDENTIALS = "not-accepting-credentials"
    PASSWORD_NOT_AVAILABLE = "password-not-available"
    PERFORMANCE_NETWORK = "performance-network"
    PERFORMANCE_INSTANCE_STORE = "performance-instance-store"
    PERFORMANCE_EBS_VOLUME = "performance-ebs-volume"
    PERFORMANCE_OTHER = "performance-other"
    OTHER = "other"


class ReportState:
    """ReportState enum values."""

    RUNNING = "running"
    CANCELLED = "cancelled"
    COMPLETE = "complete"
    ERROR = "error"


class ReportStatusType:
    """ReportStatusType enum values."""

    OK = "ok"
    IMPAIRED = "impaired"


class ReservationEndDateType:
    """ReservationEndDateType enum values."""

    LIMITED = "limited"
    UNLIMITED = "unlimited"


class ReservationState:
    """ReservationState enum values."""

    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    SCHEDULED = "scheduled"
    PENDING = "pending"
    FAILED = "failed"
    DELAYED = "delayed"
    UNSUPPORTED = "unsupported"
    PAYMENT_PENDING = "payment-pending"
    PAYMENT_FAILED = "payment-failed"
    RETIRED = "retired"


class ReservationType:
    """ReservationType enum values."""

    CAPACITY_BLOCK = "capacity-block"
    ODCR = "odcr"


class ReservedInstanceState:
    """ReservedInstanceState enum values."""

    PAYMENT_PENDING = "payment-pending"
    ACTIVE = "active"
    PAYMENT_FAILED = "payment-failed"
    RETIRED = "retired"
    QUEUED = "queued"
    QUEUED_DELETED = "queued-deleted"


class ResetFpgaImageAttributeName:
    """ResetFpgaImageAttributeName enum values."""

    LOADPERMISSION = "loadPermission"


class ResetImageAttributeName:
    """ResetImageAttributeName enum values."""

    LAUNCHPERMISSION = "launchPermission"


class ResourceType:
    """ResourceType enum values."""

    CAPACITY_RESERVATION = "capacity-reservation"
    CLIENT_VPN_ENDPOINT = "client-vpn-endpoint"
    CUSTOMER_GATEWAY = "customer-gateway"
    CARRIER_GATEWAY = "carrier-gateway"
    COIP_POOL = "coip-pool"
    DECLARATIVE_POLICIES_REPORT = "declarative-policies-report"
    DEDICATED_HOST = "dedicated-host"
    DHCP_OPTIONS = "dhcp-options"
    EGRESS_ONLY_INTERNET_GATEWAY = "egress-only-internet-gateway"
    ELASTIC_IP = "elastic-ip"
    ELASTIC_GPU = "elastic-gpu"
    EXPORT_IMAGE_TASK = "export-image-task"
    EXPORT_INSTANCE_TASK = "export-instance-task"
    FLEET = "fleet"
    FPGA_IMAGE = "fpga-image"
    HOST_RESERVATION = "host-reservation"
    IMAGE = "image"
    IMAGE_USAGE_REPORT = "image-usage-report"
    IMPORT_IMAGE_TASK = "import-image-task"
    IMPORT_SNAPSHOT_TASK = "import-snapshot-task"
    INSTANCE = "instance"
    INSTANCE_EVENT_WINDOW = "instance-event-window"
    INTERNET_GATEWAY = "internet-gateway"
    IPAM = "ipam"
    IPAM_POOL = "ipam-pool"
    IPAM_SCOPE = "ipam-scope"
    IPV4POOL_EC2 = "ipv4pool-ec2"
    IPV6POOL_EC2 = "ipv6pool-ec2"
    KEY_PAIR = "key-pair"
    LAUNCH_TEMPLATE = "launch-template"
    LOCAL_GATEWAY = "local-gateway"
    LOCAL_GATEWAY_ROUTE_TABLE = "local-gateway-route-table"
    LOCAL_GATEWAY_VIRTUAL_INTERFACE = "local-gateway-virtual-interface"
    LOCAL_GATEWAY_VIRTUAL_INTERFACE_GROUP = "local-gateway-virtual-interface-group"
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "local-gateway-route-table-vpc-association"
    LOCAL_GATEWAY_ROUTE_TABLE_VIRTUAL_INTERFACE_GROUP_ASSOCIATION = "local-gateway-route-table-virtual-interface-group-association"
    NATGATEWAY = "natgateway"
    NETWORK_ACL = "network-acl"
    NETWORK_INTERFACE = "network-interface"
    NETWORK_INSIGHTS_ANALYSIS = "network-insights-analysis"
    NETWORK_INSIGHTS_PATH = "network-insights-path"
    NETWORK_INSIGHTS_ACCESS_SCOPE = "network-insights-access-scope"
    NETWORK_INSIGHTS_ACCESS_SCOPE_ANALYSIS = "network-insights-access-scope-analysis"
    OUTPOST_LAG = "outpost-lag"
    PLACEMENT_GROUP = "placement-group"
    PREFIX_LIST = "prefix-list"
    REPLACE_ROOT_VOLUME_TASK = "replace-root-volume-task"
    RESERVED_INSTANCES = "reserved-instances"
    ROUTE_TABLE = "route-table"
    SECURITY_GROUP = "security-group"
    SECURITY_GROUP_RULE = "security-group-rule"
    SERVICE_LINK_VIRTUAL_INTERFACE = "service-link-virtual-interface"
    SNAPSHOT = "snapshot"
    SPOT_FLEET_REQUEST = "spot-fleet-request"
    SPOT_INSTANCES_REQUEST = "spot-instances-request"
    SUBNET = "subnet"
    SUBNET_CIDR_RESERVATION = "subnet-cidr-reservation"
    TRAFFIC_MIRROR_FILTER = "traffic-mirror-filter"
    TRAFFIC_MIRROR_SESSION = "traffic-mirror-session"
    TRAFFIC_MIRROR_TARGET = "traffic-mirror-target"
    TRANSIT_GATEWAY = "transit-gateway"
    TRANSIT_GATEWAY_ATTACHMENT = "transit-gateway-attachment"
    TRANSIT_GATEWAY_CONNECT_PEER = "transit-gateway-connect-peer"
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = "transit-gateway-multicast-domain"
    TRANSIT_GATEWAY_POLICY_TABLE = "transit-gateway-policy-table"
    TRANSIT_GATEWAY_METERING_POLICY = "transit-gateway-metering-policy"
    TRANSIT_GATEWAY_ROUTE_TABLE = "transit-gateway-route-table"
    TRANSIT_GATEWAY_ROUTE_TABLE_ANNOUNCEMENT = "transit-gateway-route-table-announcement"
    VOLUME = "volume"
    VPC = "vpc"
    VPC_ENDPOINT = "vpc-endpoint"
    VPC_ENDPOINT_CONNECTION = "vpc-endpoint-connection"
    VPC_ENDPOINT_SERVICE = "vpc-endpoint-service"
    VPC_ENDPOINT_SERVICE_PERMISSION = "vpc-endpoint-service-permission"
    VPC_PEERING_CONNECTION = "vpc-peering-connection"
    VPN_CONNECTION = "vpn-connection"
    VPN_GATEWAY = "vpn-gateway"
    VPC_FLOW_LOG = "vpc-flow-log"
    CAPACITY_RESERVATION_FLEET = "capacity-reservation-fleet"
    TRAFFIC_MIRROR_FILTER_RULE = "traffic-mirror-filter-rule"
    VPC_ENDPOINT_CONNECTION_DEVICE_TYPE = "vpc-endpoint-connection-device-type"
    VERIFIED_ACCESS_INSTANCE = "verified-access-instance"
    VERIFIED_ACCESS_GROUP = "verified-access-group"
    VERIFIED_ACCESS_ENDPOINT = "verified-access-endpoint"
    VERIFIED_ACCESS_POLICY = "verified-access-policy"
    VERIFIED_ACCESS_TRUST_PROVIDER = "verified-access-trust-provider"
    VPN_CONNECTION_DEVICE_TYPE = "vpn-connection-device-type"
    VPC_BLOCK_PUBLIC_ACCESS_EXCLUSION = "vpc-block-public-access-exclusion"
    VPC_ENCRYPTION_CONTROL = "vpc-encryption-control"
    ROUTE_SERVER = "route-server"
    ROUTE_SERVER_ENDPOINT = "route-server-endpoint"
    ROUTE_SERVER_PEER = "route-server-peer"
    IPAM_RESOURCE_DISCOVERY = "ipam-resource-discovery"
    IPAM_RESOURCE_DISCOVERY_ASSOCIATION = "ipam-resource-discovery-association"
    INSTANCE_CONNECT_ENDPOINT = "instance-connect-endpoint"
    VERIFIED_ACCESS_ENDPOINT_TARGET = "verified-access-endpoint-target"
    IPAM_EXTERNAL_RESOURCE_VERIFICATION_TOKEN = "ipam-external-resource-verification-token"
    CAPACITY_BLOCK = "capacity-block"
    MAC_MODIFICATION_TASK = "mac-modification-task"
    IPAM_PREFIX_LIST_RESOLVER = "ipam-prefix-list-resolver"
    IPAM_POLICY = "ipam-policy"
    IPAM_PREFIX_LIST_RESOLVER_TARGET = "ipam-prefix-list-resolver-target"
    CAPACITY_MANAGER_DATA_EXPORT = "capacity-manager-data-export"
    VPN_CONCENTRATOR = "vpn-concentrator"


class RootDeviceType:
    """RootDeviceType enum values."""

    EBS = "ebs"
    INSTANCE_STORE = "instance-store"


class RouteOrigin:
    """RouteOrigin enum values."""

    CREATEROUTETABLE = "CreateRouteTable"
    CREATEROUTE = "CreateRoute"
    ENABLEVGWROUTEPROPAGATION = "EnableVgwRoutePropagation"
    ADVERTISEMENT = "Advertisement"


class RouteServerAssociationState:
    """RouteServerAssociationState enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"


class RouteServerBfdState:
    """RouteServerBfdState enum values."""

    UP = "up"
    DOWN = "down"


class RouteServerBgpState:
    """RouteServerBgpState enum values."""

    UP = "up"
    DOWN = "down"


class RouteServerEndpointState:
    """RouteServerEndpointState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"
    FAILING = "failing"
    FAILED = "failed"
    DELETE_FAILED = "delete-failed"


class RouteServerPeerLivenessMode:
    """RouteServerPeerLivenessMode enum values."""

    BFD = "bfd"
    BGP_KEEPALIVE = "bgp-keepalive"


class RouteServerPeerState:
    """RouteServerPeerState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"
    FAILING = "failing"
    FAILED = "failed"


class RouteServerPersistRoutesAction:
    """RouteServerPersistRoutesAction enum values."""

    ENABLE = "enable"
    DISABLE = "disable"
    RESET = "reset"


class RouteServerPersistRoutesState:
    """RouteServerPersistRoutesState enum values."""

    ENABLING = "enabling"
    ENABLED = "enabled"
    RESETTING = "resetting"
    DISABLING = "disabling"
    DISABLED = "disabled"
    MODIFYING = "modifying"


class RouteServerPropagationState:
    """RouteServerPropagationState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"


class RouteServerRouteInstallationStatus:
    """RouteServerRouteInstallationStatus enum values."""

    INSTALLED = "installed"
    REJECTED = "rejected"


class RouteServerRouteStatus:
    """RouteServerRouteStatus enum values."""

    IN_RIB = "in-rib"
    IN_FIB = "in-fib"


class RouteServerState:
    """RouteServerState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    MODIFYING = "modifying"
    DELETING = "deleting"
    DELETED = "deleted"


class RouteState:
    """RouteState enum values."""

    ACTIVE = "active"
    BLACKHOLE = "blackhole"
    FILTERED = "filtered"


class RouteTableAssociationStateCode:
    """RouteTableAssociationStateCode enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"
    FAILED = "failed"


class RuleAction:
    """RuleAction enum values."""

    ALLOW = "allow"
    DENY = "deny"


class SSEType:
    """SSEType enum values."""

    SSE_EBS = "sse-ebs"
    SSE_KMS = "sse-kms"
    NONE = "none"


class Schedule:
    """Schedule enum values."""

    HOURLY = "hourly"


class SecurityGroupReferencingSupportValue:
    """SecurityGroupReferencingSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class SecurityGroupVpcAssociationState:
    """SecurityGroupVpcAssociationState enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    ASSOCIATION_FAILED = "association-failed"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"
    DISASSOCIATION_FAILED = "disassociation-failed"


class SelfServicePortal:
    """SelfServicePortal enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ServiceConnectivityType:
    """ServiceConnectivityType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class ServiceLinkVirtualInterfaceConfigurationState:
    """ServiceLinkVirtualInterfaceConfigurationState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class ServiceManaged:
    """ServiceManaged enum values."""

    ALB = "alb"
    NLB = "nlb"
    RNAT = "rnat"
    RDS = "rds"


class ServiceState:
    """ServiceState enum values."""

    PENDING = "Pending"
    AVAILABLE = "Available"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"


class ServiceType:
    """ServiceType enum values."""

    INTERFACE = "Interface"
    GATEWAY = "Gateway"
    GATEWAYLOADBALANCER = "GatewayLoadBalancer"


class ShutdownBehavior:
    """ShutdownBehavior enum values."""

    STOP = "stop"
    TERMINATE = "terminate"


class SnapshotAttributeName:
    """SnapshotAttributeName enum values."""

    PRODUCTCODES = "productCodes"
    CREATEVOLUMEPERMISSION = "createVolumePermission"


class SnapshotBlockPublicAccessState:
    """SnapshotBlockPublicAccessState enum values."""

    BLOCK_ALL_SHARING = "block-all-sharing"
    BLOCK_NEW_SHARING = "block-new-sharing"
    UNBLOCKED = "unblocked"


class SnapshotLocationEnum:
    """SnapshotLocationEnum enum values."""

    REGIONAL = "regional"
    LOCAL = "local"


class SnapshotReturnCodes:
    """SnapshotReturnCodes enum values."""

    SUCCESS = "success"
    SKIPPED = "skipped"
    MISSING_PERMISSIONS = "missing-permissions"
    INTERNAL_ERROR = "internal-error"
    CLIENT_ERROR = "client-error"


class SnapshotState:
    """SnapshotState enum values."""

    PENDING = "pending"
    COMPLETED = "completed"
    ERROR = "error"
    RECOVERABLE = "recoverable"
    RECOVERING = "recovering"


class SpotAllocationStrategy:
    """SpotAllocationStrategy enum values."""

    LOWEST_PRICE = "lowest-price"
    DIVERSIFIED = "diversified"
    CAPACITY_OPTIMIZED = "capacity-optimized"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacity-optimized-prioritized"
    PRICE_CAPACITY_OPTIMIZED = "price-capacity-optimized"


class SpotInstanceInterruptionBehavior:
    """SpotInstanceInterruptionBehavior enum values."""

    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class SpotInstanceState:
    """SpotInstanceState enum values."""

    OPEN = "open"
    ACTIVE = "active"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    FAILED = "failed"
    DISABLED = "disabled"


class SpotInstanceType:
    """SpotInstanceType enum values."""

    ONE_TIME = "one-time"
    PERSISTENT = "persistent"


class SpreadLevel:
    """SpreadLevel enum values."""

    HOST = "host"
    RACK = "rack"


class SqlServerLicenseUsage:
    """SqlServerLicenseUsage enum values."""

    FULL = "full"
    WAIVED = "waived"


class State:
    """State enum values."""

    PENDINGACCEPTANCE = "PendingAcceptance"
    PENDING = "Pending"
    AVAILABLE = "Available"
    DELETING = "Deleting"
    DELETED = "Deleted"
    REJECTED = "Rejected"
    FAILED = "Failed"
    EXPIRED = "Expired"
    PARTIAL = "Partial"


class StaticSourcesSupportValue:
    """StaticSourcesSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class StatisticType:
    """StatisticType enum values."""

    P50 = "p50"


class Status:
    """Status enum values."""

    MOVEINPROGRESS = "MoveInProgress"
    INVPC = "InVpc"
    INCLASSIC = "InClassic"


class StatusName:
    """StatusName enum values."""

    REACHABILITY = "reachability"


class StatusType:
    """StatusType enum values."""

    PASSED = "passed"
    FAILED = "failed"
    INSUFFICIENT_DATA = "insufficient-data"
    INITIALIZING = "initializing"


class StorageTier:
    """StorageTier enum values."""

    ARCHIVE = "archive"
    STANDARD = "standard"


class SubnetCidrBlockStateCode:
    """SubnetCidrBlockStateCode enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"
    FAILING = "failing"
    FAILED = "failed"


class SubnetCidrReservationType:
    """SubnetCidrReservationType enum values."""

    PREFIX = "prefix"
    EXPLICIT = "explicit"


class SubnetState:
    """SubnetState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    FAILED = "failed"
    FAILED_INSUFFICIENT_CAPACITY = "failed-insufficient-capacity"


class SummaryStatus:
    """SummaryStatus enum values."""

    OK = "ok"
    IMPAIRED = "impaired"
    INSUFFICIENT_DATA = "insufficient-data"
    NOT_APPLICABLE = "not-applicable"
    INITIALIZING = "initializing"


class SupportedAdditionalProcessorFeature:
    """SupportedAdditionalProcessorFeature enum values."""

    AMD_SEV_SNP = "amd-sev-snp"


class TargetCapacityUnitType:
    """TargetCapacityUnitType enum values."""

    VCPU = "vcpu"
    MEMORY_MIB = "memory-mib"
    UNITS = "units"


class TargetStorageTier:
    """TargetStorageTier enum values."""

    ARCHIVE = "archive"


class TelemetryStatus:
    """TelemetryStatus enum values."""

    UP = "UP"
    DOWN = "DOWN"


class Tenancy:
    """Tenancy enum values."""

    DEFAULT = "default"
    DEDICATED = "dedicated"
    HOST = "host"


class TieringOperationStatus:
    """TieringOperationStatus enum values."""

    ARCHIVAL_IN_PROGRESS = "archival-in-progress"
    ARCHIVAL_COMPLETED = "archival-completed"
    ARCHIVAL_FAILED = "archival-failed"
    TEMPORARY_RESTORE_IN_PROGRESS = "temporary-restore-in-progress"
    TEMPORARY_RESTORE_COMPLETED = "temporary-restore-completed"
    TEMPORARY_RESTORE_FAILED = "temporary-restore-failed"
    PERMANENT_RESTORE_IN_PROGRESS = "permanent-restore-in-progress"
    PERMANENT_RESTORE_COMPLETED = "permanent-restore-completed"
    PERMANENT_RESTORE_FAILED = "permanent-restore-failed"


class TokenState:
    """TokenState enum values."""

    VALID = "valid"
    EXPIRED = "expired"


class TpmSupportValues:
    """TpmSupportValues enum values."""

    V2_0 = "v2.0"


class TrafficDirection:
    """TrafficDirection enum values."""

    INGRESS = "ingress"
    EGRESS = "egress"


class TrafficIpAddressType:
    """TrafficIpAddressType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUAL_STACK = "dual-stack"


class TrafficMirrorFilterRuleField:
    """TrafficMirrorFilterRuleField enum values."""

    DESTINATION_PORT_RANGE = "destination-port-range"
    SOURCE_PORT_RANGE = "source-port-range"
    PROTOCOL = "protocol"
    DESCRIPTION = "description"


class TrafficMirrorNetworkService:
    """TrafficMirrorNetworkService enum values."""

    AMAZON_DNS = "amazon-dns"


class TrafficMirrorRuleAction:
    """TrafficMirrorRuleAction enum values."""

    ACCEPT = "accept"
    REJECT = "reject"


class TrafficMirrorSessionField:
    """TrafficMirrorSessionField enum values."""

    PACKET_LENGTH = "packet-length"
    DESCRIPTION = "description"
    VIRTUAL_NETWORK_ID = "virtual-network-id"


class TrafficMirrorTargetType:
    """TrafficMirrorTargetType enum values."""

    NETWORK_INTERFACE = "network-interface"
    NETWORK_LOAD_BALANCER = "network-load-balancer"
    GATEWAY_LOAD_BALANCER_ENDPOINT = "gateway-load-balancer-endpoint"


class TrafficType:
    """TrafficType enum values."""

    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    ALL = "ALL"


class TransferType:
    """TransferType enum values."""

    TIME_BASED = "time-based"
    STANDARD = "standard"


class TransitGatewayAssociationState:
    """TransitGatewayAssociationState enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"


class TransitGatewayAttachmentResourceType:
    """TransitGatewayAttachmentResourceType enum values."""

    VPC = "vpc"
    VPN = "vpn"
    VPN_CONCENTRATOR = "vpn-concentrator"
    DIRECT_CONNECT_GATEWAY = "direct-connect-gateway"
    CONNECT = "connect"
    PEERING = "peering"
    TGW_PEERING = "tgw-peering"
    NETWORK_FUNCTION = "network-function"


class TransitGatewayAttachmentState:
    """TransitGatewayAttachmentState enum values."""

    INITIATING = "initiating"
    INITIATINGREQUEST = "initiatingRequest"
    PENDINGACCEPTANCE = "pendingAcceptance"
    ROLLINGBACK = "rollingBack"
    PENDING = "pending"
    AVAILABLE = "available"
    MODIFYING = "modifying"
    DELETING = "deleting"
    DELETED = "deleted"
    FAILED = "failed"
    REJECTED = "rejected"
    REJECTING = "rejecting"
    FAILING = "failing"


class TransitGatewayConnectPeerState:
    """TransitGatewayConnectPeerState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayMeteringPayerType:
    """TransitGatewayMeteringPayerType enum values."""

    SOURCE_ATTACHMENT_OWNER = "source-attachment-owner"
    DESTINATION_ATTACHMENT_OWNER = "destination-attachment-owner"
    TRANSIT_GATEWAY_OWNER = "transit-gateway-owner"


class TransitGatewayMeteringPolicyEntryState:
    """TransitGatewayMeteringPolicyEntryState enum values."""

    AVAILABLE = "available"
    DELETED = "deleted"


class TransitGatewayMeteringPolicyState:
    """TransitGatewayMeteringPolicyState enum values."""

    AVAILABLE = "available"
    DELETED = "deleted"
    PENDING = "pending"
    MODIFYING = "modifying"
    DELETING = "deleting"


class TransitGatewayMulitcastDomainAssociationState:
    """TransitGatewayMulitcastDomainAssociationState enum values."""

    PENDINGACCEPTANCE = "pendingAcceptance"
    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"
    REJECTED = "rejected"
    FAILED = "failed"


class TransitGatewayMulticastDomainState:
    """TransitGatewayMulticastDomainState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayPolicyTableState:
    """TransitGatewayPolicyTableState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayPrefixListReferenceState:
    """TransitGatewayPrefixListReferenceState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    MODIFYING = "modifying"
    DELETING = "deleting"


class TransitGatewayPropagationState:
    """TransitGatewayPropagationState enum values."""

    ENABLING = "enabling"
    ENABLED = "enabled"
    DISABLING = "disabling"
    DISABLED = "disabled"


class TransitGatewayRouteState:
    """TransitGatewayRouteState enum values."""

    PENDING = "pending"
    ACTIVE = "active"
    BLACKHOLE = "blackhole"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayRouteTableAnnouncementDirection:
    """TransitGatewayRouteTableAnnouncementDirection enum values."""

    OUTGOING = "outgoing"
    INCOMING = "incoming"


class TransitGatewayRouteTableAnnouncementState:
    """TransitGatewayRouteTableAnnouncementState enum values."""

    AVAILABLE = "available"
    PENDING = "pending"
    FAILING = "failing"
    FAILED = "failed"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayRouteTableState:
    """TransitGatewayRouteTableState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class TransitGatewayRouteType:
    """TransitGatewayRouteType enum values."""

    STATIC = "static"
    PROPAGATED = "propagated"


class TransitGatewayState:
    """TransitGatewayState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    MODIFYING = "modifying"
    DELETING = "deleting"
    DELETED = "deleted"


class TransportProtocol:
    """TransportProtocol enum values."""

    TCP = "tcp"
    UDP = "udp"


class TrustProviderType:
    """TrustProviderType enum values."""

    USER = "user"
    DEVICE = "device"


class TunnelInsideIpVersion:
    """TunnelInsideIpVersion enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class UnlimitedSupportedInstanceFamily:
    """UnlimitedSupportedInstanceFamily enum values."""

    T2 = "t2"
    T3 = "t3"
    T3A = "t3a"
    T4G = "t4g"


class UnsuccessfulInstanceCreditSpecificationErrorCode:
    """UnsuccessfulInstanceCreditSpecificationErrorCode enum values."""

    INVALIDINSTANCEID_MALFORMED = "InvalidInstanceID.Malformed"
    INVALIDINSTANCEID_NOTFOUND = "InvalidInstanceID.NotFound"
    INCORRECTINSTANCESTATE = "IncorrectInstanceState"
    INSTANCECREDITSPECIFICATION_NOTSUPPORTED = "InstanceCreditSpecification.NotSupported"


class UsageClassType:
    """UsageClassType enum values."""

    SPOT = "spot"
    ON_DEMAND = "on-demand"
    CAPACITY_BLOCK = "capacity-block"


class UserTrustProviderType:
    """UserTrustProviderType enum values."""

    IAM_IDENTITY_CENTER = "iam-identity-center"
    OIDC = "oidc"


class VerificationMethod:
    """VerificationMethod enum values."""

    REMARKS_X509 = "remarks-x509"
    DNS_TOKEN = "dns-token"


class VerifiedAccessEndpointAttachmentType:
    """VerifiedAccessEndpointAttachmentType enum values."""

    VPC = "vpc"


class VerifiedAccessEndpointProtocol:
    """VerifiedAccessEndpointProtocol enum values."""

    HTTP = "http"
    HTTPS = "https"
    TCP = "tcp"


class VerifiedAccessEndpointStatusCode:
    """VerifiedAccessEndpointStatusCode enum values."""

    PENDING = "pending"
    ACTIVE = "active"
    UPDATING = "updating"
    DELETING = "deleting"
    DELETED = "deleted"


class VerifiedAccessEndpointType:
    """VerifiedAccessEndpointType enum values."""

    LOAD_BALANCER = "load-balancer"
    NETWORK_INTERFACE = "network-interface"
    RDS = "rds"
    CIDR = "cidr"


class VerifiedAccessLogDeliveryStatusCode:
    """VerifiedAccessLogDeliveryStatusCode enum values."""

    SUCCESS = "success"
    FAILED = "failed"


class VirtualizationType:
    """VirtualizationType enum values."""

    HVM = "hvm"
    PARAVIRTUAL = "paravirtual"


class VolumeAttachmentState:
    """VolumeAttachmentState enum values."""

    ATTACHING = "attaching"
    ATTACHED = "attached"
    DETACHING = "detaching"
    DETACHED = "detached"
    BUSY = "busy"


class VolumeAttributeName:
    """VolumeAttributeName enum values."""

    AUTOENABLEIO = "autoEnableIO"
    PRODUCTCODES = "productCodes"


class VolumeModificationState:
    """VolumeModificationState enum values."""

    MODIFYING = "modifying"
    OPTIMIZING = "optimizing"
    COMPLETED = "completed"
    FAILED = "failed"


class VolumeState:
    """VolumeState enum values."""

    CREATING = "creating"
    AVAILABLE = "available"
    IN_USE = "in-use"
    DELETING = "deleting"
    DELETED = "deleted"
    ERROR = "error"


class VolumeStatusInfoStatus:
    """VolumeStatusInfoStatus enum values."""

    OK = "ok"
    IMPAIRED = "impaired"
    INSUFFICIENT_DATA = "insufficient-data"
    WARNING = "warning"


class VolumeStatusName:
    """VolumeStatusName enum values."""

    IO_ENABLED = "io-enabled"
    IO_PERFORMANCE = "io-performance"
    INITIALIZATION_STATE = "initialization-state"


class VolumeType:
    """VolumeType enum values."""

    STANDARD = "standard"
    IO1 = "io1"
    IO2 = "io2"
    GP2 = "gp2"
    SC1 = "sc1"
    ST1 = "st1"
    GP3 = "gp3"


class VpcAttributeName:
    """VpcAttributeName enum values."""

    ENABLEDNSSUPPORT = "enableDnsSupport"
    ENABLEDNSHOSTNAMES = "enableDnsHostnames"
    ENABLENETWORKADDRESSUSAGEMETRICS = "enableNetworkAddressUsageMetrics"


class VpcBlockPublicAccessExclusionState:
    """VpcBlockPublicAccessExclusionState enum values."""

    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    CREATE_FAILED = "create-failed"
    UPDATE_IN_PROGRESS = "update-in-progress"
    UPDATE_COMPLETE = "update-complete"
    UPDATE_FAILED = "update-failed"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"
    DISABLE_IN_PROGRESS = "disable-in-progress"
    DISABLE_COMPLETE = "disable-complete"


class VpcBlockPublicAccessExclusionsAllowed:
    """VpcBlockPublicAccessExclusionsAllowed enum values."""

    ALLOWED = "allowed"
    NOT_ALLOWED = "not-allowed"


class VpcBlockPublicAccessState:
    """VpcBlockPublicAccessState enum values."""

    DEFAULT_STATE = "default-state"
    UPDATE_IN_PROGRESS = "update-in-progress"
    UPDATE_COMPLETE = "update-complete"


class VpcCidrBlockStateCode:
    """VpcCidrBlockStateCode enum values."""

    ASSOCIATING = "associating"
    ASSOCIATED = "associated"
    DISASSOCIATING = "disassociating"
    DISASSOCIATED = "disassociated"
    FAILING = "failing"
    FAILED = "failed"


class VpcEncryptionControlExclusionState:
    """VpcEncryptionControlExclusionState enum values."""

    ENABLING = "enabling"
    ENABLED = "enabled"
    DISABLING = "disabling"
    DISABLED = "disabled"


class VpcEncryptionControlExclusionStateInput:
    """VpcEncryptionControlExclusionStateInput enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class VpcEncryptionControlMode:
    """VpcEncryptionControlMode enum values."""

    MONITOR = "monitor"
    ENFORCE = "enforce"


class VpcEncryptionControlState:
    """VpcEncryptionControlState enum values."""

    ENFORCE_IN_PROGRESS = "enforce-in-progress"
    MONITOR_IN_PROGRESS = "monitor-in-progress"
    ENFORCE_FAILED = "enforce-failed"
    MONITOR_FAILED = "monitor-failed"
    DELETING = "deleting"
    DELETED = "deleted"
    AVAILABLE = "available"
    CREATING = "creating"
    DELETE_FAILED = "delete-failed"


class VpcEndpointType:
    """VpcEndpointType enum values."""

    INTERFACE = "Interface"
    GATEWAY = "Gateway"
    GATEWAYLOADBALANCER = "GatewayLoadBalancer"
    RESOURCE = "Resource"
    SERVICENETWORK = "ServiceNetwork"


class VpcPeeringConnectionStateReasonCode:
    """VpcPeeringConnectionStateReasonCode enum values."""

    INITIATING_REQUEST = "initiating-request"
    PENDING_ACCEPTANCE = "pending-acceptance"
    ACTIVE = "active"
    DELETED = "deleted"
    REJECTED = "rejected"
    FAILED = "failed"
    EXPIRED = "expired"
    PROVISIONING = "provisioning"
    DELETING = "deleting"


class VpcState:
    """VpcState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"


class VpcTenancy:
    """VpcTenancy enum values."""

    DEFAULT = "default"


class VpnConcentratorType:
    """VpnConcentratorType enum values."""

    IPSEC_1 = "ipsec.1"


class VpnEcmpSupportValue:
    """VpnEcmpSupportValue enum values."""

    ENABLE = "enable"
    DISABLE = "disable"


class VpnProtocol:
    """VpnProtocol enum values."""

    OPENVPN = "openvpn"


class VpnState:
    """VpnState enum values."""

    PENDING = "pending"
    AVAILABLE = "available"
    DELETING = "deleting"
    DELETED = "deleted"


class VpnStaticRouteSource:
    """VpnStaticRouteSource enum values."""

    STATIC = "Static"


class VpnTunnelBandwidth:
    """VpnTunnelBandwidth enum values."""

    STANDARD = "standard"
    LARGE = "large"


class VpnTunnelProvisioningStatus:
    """VpnTunnelProvisioningStatus enum values."""

    AVAILABLE = "available"
    PENDING = "pending"
    FAILED = "failed"


class WeekDay:
    """WeekDay enum values."""

    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


class scope:
    """scope enum values."""

    AVAILABILITY_ZONE = "Availability Zone"
    REGION = "Region"


@dataclass
class CloudWatchLogs(PropertyType):
    LOG_GROUP = "LogGroup"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KinesisDataFirehose(PropertyType):
    DELIVERY_STREAM = "DeliveryStream"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
        "enabled": "Enabled",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
    BUCKET_NAME = "BucketName"
    ENABLED = "Enabled"
    PREFIX = "Prefix"
    BUCKET_OWNER = "BucketOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "enabled": "Enabled",
        "prefix": "Prefix",
        "bucket_owner": "BucketOwner",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VerifiedAccessLogs(PropertyType):
    S3 = "S3"
    LOG_VERSION = "LogVersion"
    KINESIS_DATA_FIREHOSE = "KinesisDataFirehose"
    CLOUD_WATCH_LOGS = "CloudWatchLogs"
    INCLUDE_TRUST_CONTEXT = "IncludeTrustContext"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "log_version": "LogVersion",
        "kinesis_data_firehose": "KinesisDataFirehose",
        "cloud_watch_logs": "CloudWatchLogs",
        "include_trust_context": "IncludeTrustContext",
    }

    s3: Optional[S3] = None
    log_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kinesis_data_firehose: Optional[KinesisDataFirehose] = None
    cloud_watch_logs: Optional[CloudWatchLogs] = None
    include_trust_context: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VerifiedAccessTrustProvider(PropertyType):
    DESCRIPTION = "Description"
    DEVICE_TRUST_PROVIDER_TYPE = "DeviceTrustProviderType"
    VERIFIED_ACCESS_TRUST_PROVIDER_ID = "VerifiedAccessTrustProviderId"
    TRUST_PROVIDER_TYPE = "TrustProviderType"
    USER_TRUST_PROVIDER_TYPE = "UserTrustProviderType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "device_trust_provider_type": "DeviceTrustProviderType",
        "verified_access_trust_provider_id": "VerifiedAccessTrustProviderId",
        "trust_provider_type": "TrustProviderType",
        "user_trust_provider_type": "UserTrustProviderType",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_trust_provider_type: Optional[Union[str, DeviceTrustProviderType, Ref, GetAtt, Sub]] = None
    verified_access_trust_provider_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trust_provider_type: Optional[Union[str, TrustProviderType, Ref, GetAtt, Sub]] = None
    user_trust_provider_type: Optional[Union[str, UserTrustProviderType, Ref, GetAtt, Sub]] = None

