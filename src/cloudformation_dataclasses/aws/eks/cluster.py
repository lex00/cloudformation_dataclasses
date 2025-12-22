"""PropertyTypes for AWS::EKS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AMITypes:
    """AMITypes enum values."""

    AL2_X86_64 = "AL2_x86_64"
    AL2_X86_64_GPU = "AL2_x86_64_GPU"
    AL2_ARM_64 = "AL2_ARM_64"
    CUSTOM = "CUSTOM"
    BOTTLEROCKET_ARM_64 = "BOTTLEROCKET_ARM_64"
    BOTTLEROCKET_X86_64 = "BOTTLEROCKET_x86_64"
    BOTTLEROCKET_ARM_64_FIPS = "BOTTLEROCKET_ARM_64_FIPS"
    BOTTLEROCKET_X86_64_FIPS = "BOTTLEROCKET_x86_64_FIPS"
    BOTTLEROCKET_ARM_64_NVIDIA = "BOTTLEROCKET_ARM_64_NVIDIA"
    BOTTLEROCKET_X86_64_NVIDIA = "BOTTLEROCKET_x86_64_NVIDIA"
    WINDOWS_CORE_2019_X86_64 = "WINDOWS_CORE_2019_x86_64"
    WINDOWS_FULL_2019_X86_64 = "WINDOWS_FULL_2019_x86_64"
    WINDOWS_CORE_2022_X86_64 = "WINDOWS_CORE_2022_x86_64"
    WINDOWS_FULL_2022_X86_64 = "WINDOWS_FULL_2022_x86_64"
    AL2023_X86_64_STANDARD = "AL2023_x86_64_STANDARD"
    AL2023_ARM_64_STANDARD = "AL2023_ARM_64_STANDARD"
    AL2023_X86_64_NEURON = "AL2023_x86_64_NEURON"
    AL2023_X86_64_NVIDIA = "AL2023_x86_64_NVIDIA"
    AL2023_ARM_64_NVIDIA = "AL2023_ARM_64_NVIDIA"


class AccessScopeType:
    """AccessScopeType enum values."""

    CLUSTER = "cluster"
    NAMESPACE = "namespace"


class AddonIssueCode:
    """AddonIssueCode enum values."""

    ACCESSDENIED = "AccessDenied"
    INTERNALFAILURE = "InternalFailure"
    CLUSTERUNREACHABLE = "ClusterUnreachable"
    INSUFFICIENTNUMBEROFREPLICAS = "InsufficientNumberOfReplicas"
    CONFIGURATIONCONFLICT = "ConfigurationConflict"
    ADMISSIONREQUESTDENIED = "AdmissionRequestDenied"
    UNSUPPORTEDADDONMODIFICATION = "UnsupportedAddonModification"
    K8SRESOURCENOTFOUND = "K8sResourceNotFound"
    ADDONSUBSCRIPTIONNEEDED = "AddonSubscriptionNeeded"
    ADDONPERMISSIONFAILURE = "AddonPermissionFailure"


class AddonStatus:
    """AddonStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"
    UPDATE_FAILED = "UPDATE_FAILED"


class ArgoCdRole:
    """ArgoCdRole enum values."""

    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"


class AuthenticationMode:
    """AuthenticationMode enum values."""

    API = "API"
    API_AND_CONFIG_MAP = "API_AND_CONFIG_MAP"
    CONFIG_MAP = "CONFIG_MAP"


class CapabilityDeletePropagationPolicy:
    """CapabilityDeletePropagationPolicy enum values."""

    RETAIN = "RETAIN"


class CapabilityIssueCode:
    """CapabilityIssueCode enum values."""

    ACCESSDENIED = "AccessDenied"
    CLUSTERUNREACHABLE = "ClusterUnreachable"


class CapabilityStatus:
    """CapabilityStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"


class CapabilityType:
    """CapabilityType enum values."""

    ACK = "ACK"
    KRO = "KRO"
    ARGOCD = "ARGOCD"


class CapacityTypes:
    """CapacityTypes enum values."""

    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"
    CAPACITY_BLOCK = "CAPACITY_BLOCK"


class Category:
    """Category enum values."""

    UPGRADE_READINESS = "UPGRADE_READINESS"
    MISCONFIGURATION = "MISCONFIGURATION"


class ClusterIssueCode:
    """ClusterIssueCode enum values."""

    ACCESSDENIED = "AccessDenied"
    CLUSTERUNREACHABLE = "ClusterUnreachable"
    CONFIGURATIONCONFLICT = "ConfigurationConflict"
    INTERNALFAILURE = "InternalFailure"
    RESOURCELIMITEXCEEDED = "ResourceLimitExceeded"
    RESOURCENOTFOUND = "ResourceNotFound"
    IAMROLENOTFOUND = "IamRoleNotFound"
    VPCNOTFOUND = "VpcNotFound"
    INSUFFICIENTFREEADDRESSES = "InsufficientFreeAddresses"
    EC2SERVICENOTSUBSCRIBED = "Ec2ServiceNotSubscribed"
    EC2SUBNETNOTFOUND = "Ec2SubnetNotFound"
    EC2SECURITYGROUPNOTFOUND = "Ec2SecurityGroupNotFound"
    KMSGRANTREVOKED = "KmsGrantRevoked"
    KMSKEYNOTFOUND = "KmsKeyNotFound"
    KMSKEYMARKEDFORDELETION = "KmsKeyMarkedForDeletion"
    KMSKEYDISABLED = "KmsKeyDisabled"
    STSREGIONALENDPOINTDISABLED = "StsRegionalEndpointDisabled"
    UNSUPPORTEDVERSION = "UnsupportedVersion"
    OTHER = "Other"


class ClusterStatus:
    """ClusterStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    PENDING = "PENDING"


class ClusterVersionStatus:
    """ClusterVersionStatus enum values."""

    UNSUPPORTED = "unsupported"
    STANDARD_SUPPORT = "standard-support"
    EXTENDED_SUPPORT = "extended-support"


class ConnectorConfigProvider:
    """ConnectorConfigProvider enum values."""

    EKS_ANYWHERE = "EKS_ANYWHERE"
    ANTHOS = "ANTHOS"
    GKE = "GKE"
    AKS = "AKS"
    OPENSHIFT = "OPENSHIFT"
    TANZU = "TANZU"
    RANCHER = "RANCHER"
    EC2 = "EC2"
    OTHER = "OTHER"


class EksAnywhereSubscriptionLicenseType:
    """EksAnywhereSubscriptionLicenseType enum values."""

    CLUSTER = "Cluster"


class EksAnywhereSubscriptionStatus:
    """EksAnywhereSubscriptionStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    EXPIRING = "EXPIRING"
    EXPIRED = "EXPIRED"
    DELETING = "DELETING"


class EksAnywhereSubscriptionTermUnit:
    """EksAnywhereSubscriptionTermUnit enum values."""

    MONTHS = "MONTHS"


class ErrorCode:
    """ErrorCode enum values."""

    SUBNETNOTFOUND = "SubnetNotFound"
    SECURITYGROUPNOTFOUND = "SecurityGroupNotFound"
    ENILIMITREACHED = "EniLimitReached"
    IPNOTAVAILABLE = "IpNotAvailable"
    ACCESSDENIED = "AccessDenied"
    OPERATIONNOTPERMITTED = "OperationNotPermitted"
    VPCIDNOTFOUND = "VpcIdNotFound"
    UNKNOWN = "Unknown"
    NODECREATIONFAILURE = "NodeCreationFailure"
    PODEVICTIONFAILURE = "PodEvictionFailure"
    INSUFFICIENTFREEADDRESSES = "InsufficientFreeAddresses"
    CLUSTERUNREACHABLE = "ClusterUnreachable"
    INSUFFICIENTNUMBEROFREPLICAS = "InsufficientNumberOfReplicas"
    CONFIGURATIONCONFLICT = "ConfigurationConflict"
    ADMISSIONREQUESTDENIED = "AdmissionRequestDenied"
    UNSUPPORTEDADDONMODIFICATION = "UnsupportedAddonModification"
    K8SRESOURCENOTFOUND = "K8sResourceNotFound"


class FargateProfileIssueCode:
    """FargateProfileIssueCode enum values."""

    PODEXECUTIONROLEALREADYINUSE = "PodExecutionRoleAlreadyInUse"
    ACCESSDENIED = "AccessDenied"
    CLUSTERUNREACHABLE = "ClusterUnreachable"
    INTERNALFAILURE = "InternalFailure"


class FargateProfileStatus:
    """FargateProfileStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class InsightStatusValue:
    """InsightStatusValue enum values."""

    PASSING = "PASSING"
    WARNING = "WARNING"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"


class InsightsRefreshStatus:
    """InsightsRefreshStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class IpFamily:
    """IpFamily enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class LogType:
    """LogType enum values."""

    API = "api"
    AUDIT = "audit"
    AUTHENTICATOR = "authenticator"
    CONTROLLERMANAGER = "controllerManager"
    SCHEDULER = "scheduler"


class NodegroupIssueCode:
    """NodegroupIssueCode enum values."""

    AUTOSCALINGGROUPNOTFOUND = "AutoScalingGroupNotFound"
    AUTOSCALINGGROUPINVALIDCONFIGURATION = "AutoScalingGroupInvalidConfiguration"
    EC2SECURITYGROUPNOTFOUND = "Ec2SecurityGroupNotFound"
    EC2SECURITYGROUPDELETIONFAILURE = "Ec2SecurityGroupDeletionFailure"
    EC2LAUNCHTEMPLATENOTFOUND = "Ec2LaunchTemplateNotFound"
    EC2LAUNCHTEMPLATEVERSIONMISMATCH = "Ec2LaunchTemplateVersionMismatch"
    EC2SUBNETNOTFOUND = "Ec2SubnetNotFound"
    EC2SUBNETINVALIDCONFIGURATION = "Ec2SubnetInvalidConfiguration"
    IAMINSTANCEPROFILENOTFOUND = "IamInstanceProfileNotFound"
    EC2SUBNETMISSINGIPV6ASSIGNMENT = "Ec2SubnetMissingIpv6Assignment"
    IAMLIMITEXCEEDED = "IamLimitExceeded"
    IAMNODEROLENOTFOUND = "IamNodeRoleNotFound"
    NODECREATIONFAILURE = "NodeCreationFailure"
    ASGINSTANCELAUNCHFAILURES = "AsgInstanceLaunchFailures"
    INSTANCELIMITEXCEEDED = "InstanceLimitExceeded"
    INSUFFICIENTFREEADDRESSES = "InsufficientFreeAddresses"
    ACCESSDENIED = "AccessDenied"
    INTERNALFAILURE = "InternalFailure"
    CLUSTERUNREACHABLE = "ClusterUnreachable"
    AMIIDNOTFOUND = "AmiIdNotFound"
    AUTOSCALINGGROUPOPTINREQUIRED = "AutoScalingGroupOptInRequired"
    AUTOSCALINGGROUPRATELIMITEXCEEDED = "AutoScalingGroupRateLimitExceeded"
    EC2LAUNCHTEMPLATEDELETIONFAILURE = "Ec2LaunchTemplateDeletionFailure"
    EC2LAUNCHTEMPLATEINVALIDCONFIGURATION = "Ec2LaunchTemplateInvalidConfiguration"
    EC2LAUNCHTEMPLATEMAXLIMITEXCEEDED = "Ec2LaunchTemplateMaxLimitExceeded"
    EC2SUBNETLISTTOOLONG = "Ec2SubnetListTooLong"
    IAMTHROTTLING = "IamThrottling"
    NODETERMINATIONFAILURE = "NodeTerminationFailure"
    PODEVICTIONFAILURE = "PodEvictionFailure"
    SOURCEEC2LAUNCHTEMPLATENOTFOUND = "SourceEc2LaunchTemplateNotFound"
    LIMITEXCEEDED = "LimitExceeded"
    UNKNOWN = "Unknown"
    AUTOSCALINGGROUPINSTANCEREFRESHACTIVE = "AutoScalingGroupInstanceRefreshActive"
    KUBERNETESLABELINVALID = "KubernetesLabelInvalid"
    EC2LAUNCHTEMPLATEVERSIONMAXLIMITEXCEEDED = "Ec2LaunchTemplateVersionMaxLimitExceeded"
    EC2INSTANCETYPEDOESNOTEXIST = "Ec2InstanceTypeDoesNotExist"


class NodegroupStatus:
    """NodegroupStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"


class NodegroupUpdateStrategies:
    """NodegroupUpdateStrategies enum values."""

    DEFAULT = "DEFAULT"
    MINIMAL = "MINIMAL"


class ProvisionedControlPlaneTier:
    """ProvisionedControlPlaneTier enum values."""

    STANDARD = "standard"
    TIER_XL = "tier-xl"
    TIER_2XL = "tier-2xl"
    TIER_4XL = "tier-4xl"


class RepairAction:
    """RepairAction enum values."""

    REPLACE = "Replace"
    REBOOT = "Reboot"
    NOACTION = "NoAction"


class ResolveConflicts:
    """ResolveConflicts enum values."""

    OVERWRITE = "OVERWRITE"
    NONE = "NONE"
    PRESERVE = "PRESERVE"


class SsoIdentityType:
    """SsoIdentityType enum values."""

    SSO_USER = "SSO_USER"
    SSO_GROUP = "SSO_GROUP"


class SupportType:
    """SupportType enum values."""

    STANDARD = "STANDARD"
    EXTENDED = "EXTENDED"


class TaintEffect:
    """TaintEffect enum values."""

    NO_SCHEDULE = "NO_SCHEDULE"
    NO_EXECUTE = "NO_EXECUTE"
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"


class UpdateParamType:
    """UpdateParamType enum values."""

    VERSION = "Version"
    PLATFORMVERSION = "PlatformVersion"
    ENDPOINTPRIVATEACCESS = "EndpointPrivateAccess"
    ENDPOINTPUBLICACCESS = "EndpointPublicAccess"
    CLUSTERLOGGING = "ClusterLogging"
    DESIREDSIZE = "DesiredSize"
    LABELSTOADD = "LabelsToAdd"
    LABELSTOREMOVE = "LabelsToRemove"
    TAINTSTOADD = "TaintsToAdd"
    TAINTSTOREMOVE = "TaintsToRemove"
    MAXSIZE = "MaxSize"
    MINSIZE = "MinSize"
    RELEASEVERSION = "ReleaseVersion"
    PUBLICACCESSCIDRS = "PublicAccessCidrs"
    LAUNCHTEMPLATENAME = "LaunchTemplateName"
    LAUNCHTEMPLATEVERSION = "LaunchTemplateVersion"
    IDENTITYPROVIDERCONFIG = "IdentityProviderConfig"
    ENCRYPTIONCONFIG = "EncryptionConfig"
    ADDONVERSION = "AddonVersion"
    SERVICEACCOUNTROLEARN = "ServiceAccountRoleArn"
    RESOLVECONFLICTS = "ResolveConflicts"
    MAXUNAVAILABLE = "MaxUnavailable"
    MAXUNAVAILABLEPERCENTAGE = "MaxUnavailablePercentage"
    NODEREPAIRENABLED = "NodeRepairEnabled"
    UPDATESTRATEGY = "UpdateStrategy"
    CONFIGURATIONVALUES = "ConfigurationValues"
    SECURITYGROUPS = "SecurityGroups"
    SUBNETS = "Subnets"
    AUTHENTICATIONMODE = "AuthenticationMode"
    PODIDENTITYASSOCIATIONS = "PodIdentityAssociations"
    UPGRADEPOLICY = "UpgradePolicy"
    ZONALSHIFTCONFIG = "ZonalShiftConfig"
    COMPUTECONFIG = "ComputeConfig"
    STORAGECONFIG = "StorageConfig"
    KUBERNETESNETWORKCONFIG = "KubernetesNetworkConfig"
    REMOTENETWORKCONFIG = "RemoteNetworkConfig"
    DELETIONPROTECTION = "DeletionProtection"
    NODEREPAIRCONFIG = "NodeRepairConfig"
    UPDATEDTIER = "UpdatedTier"
    PREVIOUSTIER = "PreviousTier"


class UpdateStatus:
    """UpdateStatus enum values."""

    INPROGRESS = "InProgress"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    SUCCESSFUL = "Successful"


class UpdateType:
    """UpdateType enum values."""

    VERSIONUPDATE = "VersionUpdate"
    ENDPOINTACCESSUPDATE = "EndpointAccessUpdate"
    LOGGINGUPDATE = "LoggingUpdate"
    CONFIGUPDATE = "ConfigUpdate"
    ASSOCIATEIDENTITYPROVIDERCONFIG = "AssociateIdentityProviderConfig"
    DISASSOCIATEIDENTITYPROVIDERCONFIG = "DisassociateIdentityProviderConfig"
    ASSOCIATEENCRYPTIONCONFIG = "AssociateEncryptionConfig"
    ADDONUPDATE = "AddonUpdate"
    VPCCONFIGUPDATE = "VpcConfigUpdate"
    ACCESSCONFIGUPDATE = "AccessConfigUpdate"
    UPGRADEPOLICYUPDATE = "UpgradePolicyUpdate"
    ZONALSHIFTCONFIGUPDATE = "ZonalShiftConfigUpdate"
    AUTOMODEUPDATE = "AutoModeUpdate"
    REMOTENETWORKCONFIGUPDATE = "RemoteNetworkConfigUpdate"
    DELETIONPROTECTIONUPDATE = "DeletionProtectionUpdate"
    CONTROLPLANESCALINGCONFIGUPDATE = "ControlPlaneScalingConfigUpdate"


class VersionStatus:
    """VersionStatus enum values."""

    UNSUPPORTED = "UNSUPPORTED"
    STANDARD_SUPPORT = "STANDARD_SUPPORT"
    EXTENDED_SUPPORT = "EXTENDED_SUPPORT"


class configStatus:
    """configStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclass
class AccessConfig(PropertyType):
    AUTHENTICATION_MODE = "AuthenticationMode"
    BOOTSTRAP_CLUSTER_CREATOR_ADMIN_PERMISSIONS = "BootstrapClusterCreatorAdminPermissions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_mode": "AuthenticationMode",
        "bootstrap_cluster_creator_admin_permissions": "BootstrapClusterCreatorAdminPermissions",
    }

    authentication_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bootstrap_cluster_creator_admin_permissions: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BlockStorage(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterLogging(PropertyType):
    ENABLED_TYPES = "EnabledTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_types": "EnabledTypes",
    }

    enabled_types: Optional[list[LoggingTypeConfig]] = None


@dataclass
class ComputeConfig(PropertyType):
    NODE_POOLS = "NodePools"
    NODE_ROLE_ARN = "NodeRoleArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_pools": "NodePools",
        "node_role_arn": "NodeRoleArn",
        "enabled": "Enabled",
    }

    node_pools: Optional[Union[list[str], Ref]] = None
    node_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ControlPlanePlacement(PropertyType):
    GROUP_NAME = "GroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ControlPlaneScalingConfig(PropertyType):
    TIER = "Tier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier": "Tier",
    }

    tier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticLoadBalancing(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfig(PropertyType):
    RESOURCES = "Resources"
    PROVIDER = "Provider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resources": "Resources",
        "provider": "Provider",
    }

    resources: Optional[Union[list[str], Ref]] = None
    provider: Optional[Provider] = None


@dataclass
class KubernetesNetworkConfig(PropertyType):
    SERVICE_IPV4_CIDR = "ServiceIpv4Cidr"
    SERVICE_IPV6_CIDR = "ServiceIpv6Cidr"
    IP_FAMILY = "IpFamily"
    ELASTIC_LOAD_BALANCING = "ElasticLoadBalancing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_ipv4_cidr": "ServiceIpv4Cidr",
        "service_ipv6_cidr": "ServiceIpv6Cidr",
        "ip_family": "IpFamily",
        "elastic_load_balancing": "ElasticLoadBalancing",
    }

    service_ipv4_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_ipv6_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    elastic_load_balancing: Optional[ElasticLoadBalancing] = None


@dataclass
class Logging(PropertyType):
    CLUSTER_LOGGING = "ClusterLogging"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_logging": "ClusterLogging",
    }

    cluster_logging: Optional[ClusterLogging] = None


@dataclass
class LoggingTypeConfig(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutpostConfig(PropertyType):
    OUTPOST_ARNS = "OutpostArns"
    CONTROL_PLANE_PLACEMENT = "ControlPlanePlacement"
    CONTROL_PLANE_INSTANCE_TYPE = "ControlPlaneInstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outpost_arns": "OutpostArns",
        "control_plane_placement": "ControlPlanePlacement",
        "control_plane_instance_type": "ControlPlaneInstanceType",
    }

    outpost_arns: Optional[Union[list[str], Ref]] = None
    control_plane_placement: Optional[ControlPlanePlacement] = None
    control_plane_instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Provider(PropertyType):
    KEY_ARN = "KeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_arn": "KeyArn",
    }

    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoteNetworkConfig(PropertyType):
    REMOTE_NODE_NETWORKS = "RemoteNodeNetworks"
    REMOTE_POD_NETWORKS = "RemotePodNetworks"

    _property_mappings: ClassVar[dict[str, str]] = {
        "remote_node_networks": "RemoteNodeNetworks",
        "remote_pod_networks": "RemotePodNetworks",
    }

    remote_node_networks: Optional[list[RemoteNodeNetwork]] = None
    remote_pod_networks: Optional[list[RemotePodNetwork]] = None


@dataclass
class RemoteNodeNetwork(PropertyType):
    CIDRS = "Cidrs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrs": "Cidrs",
    }

    cidrs: Optional[Union[list[str], Ref]] = None


@dataclass
class RemotePodNetwork(PropertyType):
    CIDRS = "Cidrs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrs": "Cidrs",
    }

    cidrs: Optional[Union[list[str], Ref]] = None


@dataclass
class ResourcesVpcConfig(PropertyType):
    ENDPOINT_PUBLIC_ACCESS = "EndpointPublicAccess"
    PUBLIC_ACCESS_CIDRS = "PublicAccessCidrs"
    ENDPOINT_PRIVATE_ACCESS = "EndpointPrivateAccess"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_public_access": "EndpointPublicAccess",
        "public_access_cidrs": "PublicAccessCidrs",
        "endpoint_private_access": "EndpointPrivateAccess",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    endpoint_public_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    public_access_cidrs: Optional[Union[list[str], Ref]] = None
    endpoint_private_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class StorageConfig(PropertyType):
    BLOCK_STORAGE = "BlockStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "block_storage": "BlockStorage",
    }

    block_storage: Optional[BlockStorage] = None


@dataclass
class UpgradePolicy(PropertyType):
    SUPPORT_TYPE = "SupportType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "support_type": "SupportType",
    }

    support_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZonalShiftConfig(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

