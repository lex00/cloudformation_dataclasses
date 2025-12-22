"""PropertyTypes for AWS::ODB::OdbNetwork."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class Access:
    """Access enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ComputeModel:
    """ComputeModel enum values."""

    ECPU = "ECPU"
    OCPU = "OCPU"


class DayOfWeekName:
    """DayOfWeekName enum values."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class DbNodeMaintenanceType:
    """DbNodeMaintenanceType enum values."""

    VMDB_REBOOT_MIGRATION = "VMDB_REBOOT_MIGRATION"


class DbNodeResourceStatus:
    """DbNodeResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    STARTING = "STARTING"


class DbServerPatchingStatus:
    """DbServerPatchingStatus enum values."""

    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"
    SCHEDULED = "SCHEDULED"


class DiskRedundancy:
    """DiskRedundancy enum values."""

    HIGH = "HIGH"
    NORMAL = "NORMAL"


class IamRoleStatus:
    """IamRoleStatus enum values."""

    ASSOCIATING = "ASSOCIATING"
    DISASSOCIATING = "DISASSOCIATING"
    FAILED = "FAILED"
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    PARTIALLY_CONNECTED = "PARTIALLY_CONNECTED"
    UNKNOWN = "UNKNOWN"


class IormLifecycleState:
    """IormLifecycleState enum values."""

    BOOTSTRAPPING = "BOOTSTRAPPING"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    FAILED = "FAILED"
    UPDATING = "UPDATING"


class LicenseModel:
    """LicenseModel enum values."""

    BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"
    LICENSE_INCLUDED = "LICENSE_INCLUDED"


class ManagedResourceStatus:
    """ManagedResourceStatus enum values."""

    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"


class MonthName:
    """MonthName enum values."""

    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


class Objective:
    """Objective enum values."""

    AUTO = "AUTO"
    BALANCED = "BALANCED"
    BASIC = "BASIC"
    HIGH_THROUGHPUT = "HIGH_THROUGHPUT"
    LOW_LATENCY = "LOW_LATENCY"


class OciOnboardingStatus:
    """OciOnboardingStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    PENDING_LINK_GENERATION = "PENDING_LINK_GENERATION"
    PENDING_CUSTOMER_ACTION = "PENDING_CUSTOMER_ACTION"
    PENDING_INITIALIZATION = "PENDING_INITIALIZATION"
    ACTIVATING = "ACTIVATING"
    ACTIVE_IN_HOME_REGION = "ACTIVE_IN_HOME_REGION"
    ACTIVE = "ACTIVE"
    ACTIVE_LIMITED = "ACTIVE_LIMITED"
    FAILED = "FAILED"
    PUBLIC_OFFER_UNSUPPORTED = "PUBLIC_OFFER_UNSUPPORTED"
    SUSPENDED = "SUSPENDED"
    CANCELED = "CANCELED"


class PatchingModeType:
    """PatchingModeType enum values."""

    ROLLING = "ROLLING"
    NONROLLING = "NONROLLING"


class PreferenceType:
    """PreferenceType enum values."""

    NO_PREFERENCE = "NO_PREFERENCE"
    CUSTOM_PREFERENCE = "CUSTOM_PREFERENCE"


class ResourceStatus:
    """ResourceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"
    PROVISIONING = "PROVISIONING"
    TERMINATED = "TERMINATED"
    TERMINATING = "TERMINATING"
    UPDATING = "UPDATING"
    MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"


class ShapeType:
    """ShapeType enum values."""

    AMD = "AMD"
    INTEL = "INTEL"
    INTEL_FLEX_X9 = "INTEL_FLEX_X9"
    AMPERE_FLEX_A1 = "AMPERE_FLEX_A1"


class SupportedAwsIntegration:
    """SupportedAwsIntegration enum values."""

    KMSTDE = "KmsTde"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


class VpcEndpointType:
    """VpcEndpointType enum values."""

    SERVICENETWORK = "SERVICENETWORK"


@dataclass
class ManagedS3BackupAccess(PropertyType):
    STATUS = "Status"
    IPV4_ADDRESSES = "Ipv4Addresses"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "ipv4_addresses": "Ipv4Addresses",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv4_addresses: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedServices(PropertyType):
    MANAGED_SERVICES_IPV4_CIDRS = "ManagedServicesIpv4Cidrs"
    RESOURCE_GATEWAY_ARN = "ResourceGatewayArn"
    MANAGED_S3_BACKUP_ACCESS = "ManagedS3BackupAccess"
    SERVICE_NETWORK_ENDPOINT = "ServiceNetworkEndpoint"
    ZERO_ETL_ACCESS = "ZeroEtlAccess"
    SERVICE_NETWORK_ARN = "ServiceNetworkArn"
    S3_ACCESS = "S3Access"

    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_services_ipv4_cidrs": "ManagedServicesIpv4Cidrs",
        "resource_gateway_arn": "ResourceGatewayArn",
        "managed_s3_backup_access": "ManagedS3BackupAccess",
        "service_network_endpoint": "ServiceNetworkEndpoint",
        "zero_etl_access": "ZeroEtlAccess",
        "service_network_arn": "ServiceNetworkArn",
        "s3_access": "S3Access",
    }

    managed_services_ipv4_cidrs: Optional[Union[list[str], Ref]] = None
    resource_gateway_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_s3_backup_access: Optional[ManagedS3BackupAccess] = None
    service_network_endpoint: Optional[ServiceNetworkEndpoint] = None
    zero_etl_access: Optional[ZeroEtlAccess] = None
    service_network_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_access: Optional[S3Access] = None


@dataclass
class S3Access(PropertyType):
    STATUS = "Status"
    IPV4_ADDRESSES = "Ipv4Addresses"
    DOMAIN_NAME = "DomainName"
    S3_POLICY_DOCUMENT = "S3PolicyDocument"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "ipv4_addresses": "Ipv4Addresses",
        "domain_name": "DomainName",
        "s3_policy_document": "S3PolicyDocument",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv4_addresses: Optional[Union[list[str], Ref]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_policy_document: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNetworkEndpoint(PropertyType):
    VPC_ENDPOINT_TYPE = "VpcEndpointType"
    VPC_ENDPOINT_ID = "VpcEndpointId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint_type": "VpcEndpointType",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_endpoint_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZeroEtlAccess(PropertyType):
    STATUS = "Status"
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "cidr": "Cidr",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None

