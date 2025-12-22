"""PropertyTypes for AWS::CodeDeploy::DeploymentConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationRevisionSortBy:
    """ApplicationRevisionSortBy enum values."""

    REGISTERTIME = "registerTime"
    FIRSTUSEDTIME = "firstUsedTime"
    LASTUSEDTIME = "lastUsedTime"


class AutoRollbackEvent:
    """AutoRollbackEvent enum values."""

    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    DEPLOYMENT_STOP_ON_ALARM = "DEPLOYMENT_STOP_ON_ALARM"
    DEPLOYMENT_STOP_ON_REQUEST = "DEPLOYMENT_STOP_ON_REQUEST"


class BundleType:
    """BundleType enum values."""

    TAR = "tar"
    TGZ = "tgz"
    ZIP = "zip"
    YAML = "YAML"
    JSON = "JSON"


class ComputePlatform:
    """ComputePlatform enum values."""

    SERVER = "Server"
    LAMBDA = "Lambda"
    ECS = "ECS"


class DeploymentCreator:
    """DeploymentCreator enum values."""

    USER = "user"
    AUTOSCALING = "autoscaling"
    CODEDEPLOYROLLBACK = "codeDeployRollback"
    CODEDEPLOY = "CodeDeploy"
    CODEDEPLOYAUTOUPDATE = "CodeDeployAutoUpdate"
    CLOUDFORMATION = "CloudFormation"
    CLOUDFORMATIONROLLBACK = "CloudFormationRollback"
    AUTOSCALINGTERMINATION = "autoscalingTermination"


class DeploymentOption:
    """DeploymentOption enum values."""

    WITH_TRAFFIC_CONTROL = "WITH_TRAFFIC_CONTROL"
    WITHOUT_TRAFFIC_CONTROL = "WITHOUT_TRAFFIC_CONTROL"


class DeploymentReadyAction:
    """DeploymentReadyAction enum values."""

    CONTINUE_DEPLOYMENT = "CONTINUE_DEPLOYMENT"
    STOP_DEPLOYMENT = "STOP_DEPLOYMENT"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    CREATED = "Created"
    QUEUED = "Queued"
    INPROGRESS = "InProgress"
    BAKING = "Baking"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    STOPPED = "Stopped"
    READY = "Ready"


class DeploymentTargetType:
    """DeploymentTargetType enum values."""

    INSTANCETARGET = "InstanceTarget"
    LAMBDATARGET = "LambdaTarget"
    ECSTARGET = "ECSTarget"
    CLOUDFORMATIONTARGET = "CloudFormationTarget"


class DeploymentType:
    """DeploymentType enum values."""

    IN_PLACE = "IN_PLACE"
    BLUE_GREEN = "BLUE_GREEN"


class DeploymentWaitType:
    """DeploymentWaitType enum values."""

    READY_WAIT = "READY_WAIT"
    TERMINATION_WAIT = "TERMINATION_WAIT"


class EC2TagFilterType:
    """EC2TagFilterType enum values."""

    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class ErrorCode:
    """ErrorCode enum values."""

    AGENT_ISSUE = "AGENT_ISSUE"
    ALARM_ACTIVE = "ALARM_ACTIVE"
    APPLICATION_MISSING = "APPLICATION_MISSING"
    AUTOSCALING_VALIDATION_ERROR = "AUTOSCALING_VALIDATION_ERROR"
    AUTO_SCALING_CONFIGURATION = "AUTO_SCALING_CONFIGURATION"
    AUTO_SCALING_IAM_ROLE_PERMISSIONS = "AUTO_SCALING_IAM_ROLE_PERMISSIONS"
    CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND = "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND"
    CUSTOMER_APPLICATION_UNHEALTHY = "CUSTOMER_APPLICATION_UNHEALTHY"
    DEPLOYMENT_GROUP_MISSING = "DEPLOYMENT_GROUP_MISSING"
    ECS_UPDATE_ERROR = "ECS_UPDATE_ERROR"
    ELASTIC_LOAD_BALANCING_INVALID = "ELASTIC_LOAD_BALANCING_INVALID"
    ELB_INVALID_INSTANCE = "ELB_INVALID_INSTANCE"
    HEALTH_CONSTRAINTS = "HEALTH_CONSTRAINTS"
    HEALTH_CONSTRAINTS_INVALID = "HEALTH_CONSTRAINTS_INVALID"
    HOOK_EXECUTION_FAILURE = "HOOK_EXECUTION_FAILURE"
    IAM_ROLE_MISSING = "IAM_ROLE_MISSING"
    IAM_ROLE_PERMISSIONS = "IAM_ROLE_PERMISSIONS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_ECS_SERVICE = "INVALID_ECS_SERVICE"
    INVALID_LAMBDA_CONFIGURATION = "INVALID_LAMBDA_CONFIGURATION"
    INVALID_LAMBDA_FUNCTION = "INVALID_LAMBDA_FUNCTION"
    INVALID_REVISION = "INVALID_REVISION"
    MANUAL_STOP = "MANUAL_STOP"
    MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION = "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION"
    MISSING_ELB_INFORMATION = "MISSING_ELB_INFORMATION"
    MISSING_GITHUB_TOKEN = "MISSING_GITHUB_TOKEN"
    NO_EC2_SUBSCRIPTION = "NO_EC2_SUBSCRIPTION"
    NO_INSTANCES = "NO_INSTANCES"
    OVER_MAX_INSTANCES = "OVER_MAX_INSTANCES"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    REVISION_MISSING = "REVISION_MISSING"
    THROTTLED = "THROTTLED"
    TIMEOUT = "TIMEOUT"
    CLOUDFORMATION_STACK_FAILURE = "CLOUDFORMATION_STACK_FAILURE"


class FileExistsBehavior:
    """FileExistsBehavior enum values."""

    DISALLOW = "DISALLOW"
    OVERWRITE = "OVERWRITE"
    RETAIN = "RETAIN"


class GreenFleetProvisioningAction:
    """GreenFleetProvisioningAction enum values."""

    DISCOVER_EXISTING = "DISCOVER_EXISTING"
    COPY_AUTO_SCALING_GROUP = "COPY_AUTO_SCALING_GROUP"


class InstanceAction:
    """InstanceAction enum values."""

    TERMINATE = "TERMINATE"
    KEEP_ALIVE = "KEEP_ALIVE"


class InstanceStatus:
    """InstanceStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    UNKNOWN = "Unknown"
    READY = "Ready"


class InstanceType:
    """InstanceType enum values."""

    BLUE = "Blue"
    GREEN = "Green"


class LifecycleErrorCode:
    """LifecycleErrorCode enum values."""

    SUCCESS = "Success"
    SCRIPTMISSING = "ScriptMissing"
    SCRIPTNOTEXECUTABLE = "ScriptNotExecutable"
    SCRIPTTIMEDOUT = "ScriptTimedOut"
    SCRIPTFAILED = "ScriptFailed"
    UNKNOWNERROR = "UnknownError"


class LifecycleEventStatus:
    """LifecycleEventStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    UNKNOWN = "Unknown"


class ListStateFilterAction:
    """ListStateFilterAction enum values."""

    INCLUDE = "include"
    EXCLUDE = "exclude"
    IGNORE = "ignore"


class MinimumHealthyHostsPerZoneType:
    """MinimumHealthyHostsPerZoneType enum values."""

    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class MinimumHealthyHostsType:
    """MinimumHealthyHostsType enum values."""

    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class OutdatedInstancesStrategy:
    """OutdatedInstancesStrategy enum values."""

    UPDATE = "UPDATE"
    IGNORE = "IGNORE"


class RegistrationStatus:
    """RegistrationStatus enum values."""

    REGISTERED = "Registered"
    DEREGISTERED = "Deregistered"


class RevisionLocationType:
    """RevisionLocationType enum values."""

    S3 = "S3"
    GITHUB = "GitHub"
    STRING = "String"
    APPSPECCONTENT = "AppSpecContent"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "ascending"
    DESCENDING = "descending"


class StopStatus:
    """StopStatus enum values."""

    PENDING = "Pending"
    SUCCEEDED = "Succeeded"


class TagFilterType:
    """TagFilterType enum values."""

    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class TargetFilterName:
    """TargetFilterName enum values."""

    TARGETSTATUS = "TargetStatus"
    SERVERINSTANCELABEL = "ServerInstanceLabel"


class TargetLabel:
    """TargetLabel enum values."""

    BLUE = "Blue"
    GREEN = "Green"


class TargetStatus:
    """TargetStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    UNKNOWN = "Unknown"
    READY = "Ready"


class TrafficRoutingType:
    """TrafficRoutingType enum values."""

    TIMEBASEDCANARY = "TimeBasedCanary"
    TIMEBASEDLINEAR = "TimeBasedLinear"
    ALLATONCE = "AllAtOnce"


class TriggerEventType:
    """TriggerEventType enum values."""

    DEPLOYMENTSTART = "DeploymentStart"
    DEPLOYMENTSUCCESS = "DeploymentSuccess"
    DEPLOYMENTFAILURE = "DeploymentFailure"
    DEPLOYMENTSTOP = "DeploymentStop"
    DEPLOYMENTROLLBACK = "DeploymentRollback"
    DEPLOYMENTREADY = "DeploymentReady"
    INSTANCESTART = "InstanceStart"
    INSTANCESUCCESS = "InstanceSuccess"
    INSTANCEFAILURE = "InstanceFailure"
    INSTANCEREADY = "InstanceReady"


@dataclass
class MinimumHealthyHosts(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MinimumHealthyHostsPerZone(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedCanary(PropertyType):
    CANARY_PERCENTAGE = "CanaryPercentage"
    CANARY_INTERVAL = "CanaryInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "canary_percentage": "CanaryPercentage",
        "canary_interval": "CanaryInterval",
    }

    canary_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    canary_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedLinear(PropertyType):
    LINEAR_INTERVAL = "LinearInterval"
    LINEAR_PERCENTAGE = "LinearPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "linear_interval": "LinearInterval",
        "linear_percentage": "LinearPercentage",
    }

    linear_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    linear_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    TYPE = "Type"
    TIME_BASED_LINEAR = "TimeBasedLinear"
    TIME_BASED_CANARY = "TimeBasedCanary"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "time_based_linear": "TimeBasedLinear",
        "time_based_canary": "TimeBasedCanary",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_based_linear: Optional[TimeBasedLinear] = None
    time_based_canary: Optional[TimeBasedCanary] = None


@dataclass
class ZonalConfig(PropertyType):
    MONITOR_DURATION_IN_SECONDS = "MonitorDurationInSeconds"
    MINIMUM_HEALTHY_HOSTS_PER_ZONE = "MinimumHealthyHostsPerZone"
    FIRST_ZONE_MONITOR_DURATION_IN_SECONDS = "FirstZoneMonitorDurationInSeconds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "monitor_duration_in_seconds": "MonitorDurationInSeconds",
        "minimum_healthy_hosts_per_zone": "MinimumHealthyHostsPerZone",
        "first_zone_monitor_duration_in_seconds": "FirstZoneMonitorDurationInSeconds",
    }

    monitor_duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minimum_healthy_hosts_per_zone: Optional[MinimumHealthyHostsPerZone] = None
    first_zone_monitor_duration_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None

