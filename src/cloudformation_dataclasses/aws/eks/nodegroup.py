"""PropertyTypes for AWS::EKS::Nodegroup."""

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
class LaunchTemplateSpecification(PropertyType):
    VERSION = "Version"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "id": "Id",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NodeRepairConfig(PropertyType):
    NODE_REPAIR_CONFIG_OVERRIDES = "NodeRepairConfigOverrides"
    MAX_PARALLEL_NODES_REPAIRED_COUNT = "MaxParallelNodesRepairedCount"
    ENABLED = "Enabled"
    MAX_UNHEALTHY_NODE_THRESHOLD_PERCENTAGE = "MaxUnhealthyNodeThresholdPercentage"
    MAX_PARALLEL_NODES_REPAIRED_PERCENTAGE = "MaxParallelNodesRepairedPercentage"
    MAX_UNHEALTHY_NODE_THRESHOLD_COUNT = "MaxUnhealthyNodeThresholdCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_repair_config_overrides": "NodeRepairConfigOverrides",
        "max_parallel_nodes_repaired_count": "MaxParallelNodesRepairedCount",
        "enabled": "Enabled",
        "max_unhealthy_node_threshold_percentage": "MaxUnhealthyNodeThresholdPercentage",
        "max_parallel_nodes_repaired_percentage": "MaxParallelNodesRepairedPercentage",
        "max_unhealthy_node_threshold_count": "MaxUnhealthyNodeThresholdCount",
    }

    node_repair_config_overrides: Optional[list[NodeRepairConfigOverrides]] = None
    max_parallel_nodes_repaired_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_unhealthy_node_threshold_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_parallel_nodes_repaired_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_unhealthy_node_threshold_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NodeRepairConfigOverrides(PropertyType):
    NODE_UNHEALTHY_REASON = "NodeUnhealthyReason"
    REPAIR_ACTION = "RepairAction"
    MIN_REPAIR_WAIT_TIME_MINS = "MinRepairWaitTimeMins"
    NODE_MONITORING_CONDITION = "NodeMonitoringCondition"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_unhealthy_reason": "NodeUnhealthyReason",
        "repair_action": "RepairAction",
        "min_repair_wait_time_mins": "MinRepairWaitTimeMins",
        "node_monitoring_condition": "NodeMonitoringCondition",
    }

    node_unhealthy_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repair_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_repair_wait_time_mins: Optional[Union[int, Ref, GetAtt, Sub]] = None
    node_monitoring_condition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoteAccess(PropertyType):
    SOURCE_SECURITY_GROUPS = "SourceSecurityGroups"
    EC2_SSH_KEY = "Ec2SshKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source_security_groups": "SourceSecurityGroups",
        "ec2_ssh_key": "Ec2SshKey",
    }

    source_security_groups: Optional[Union[list[str], Ref]] = None
    ec2_ssh_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfig(PropertyType):
    MIN_SIZE = "MinSize"
    DESIRED_SIZE = "DesiredSize"
    MAX_SIZE = "MaxSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_size": "MinSize",
        "desired_size": "DesiredSize",
        "max_size": "MaxSize",
    }

    min_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    desired_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Taint(PropertyType):
    VALUE = "Value"
    EFFECT = "Effect"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "effect": "Effect",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effect: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateConfig(PropertyType):
    MAX_UNAVAILABLE_PERCENTAGE = "MaxUnavailablePercentage"
    UPDATE_STRATEGY = "UpdateStrategy"
    MAX_UNAVAILABLE = "MaxUnavailable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_unavailable_percentage": "MaxUnavailablePercentage",
        "update_strategy": "UpdateStrategy",
        "max_unavailable": "MaxUnavailable",
    }

    max_unavailable_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    update_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_unavailable: Optional[Union[float, Ref, GetAtt, Sub]] = None

