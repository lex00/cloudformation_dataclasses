"""PropertyTypes for AWS::CodeDeploy::DeploymentGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Alarm(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AlarmConfiguration(PropertyType):
    ALARMS = "Alarms"
    ENABLED = "Enabled"
    IGNORE_POLL_ALARM_FAILURE = "IgnorePollAlarmFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alarms": "Alarms",
        "enabled": "Enabled",
        "ignore_poll_alarm_failure": "IgnorePollAlarmFailure",
    }

    alarms: Optional[list[Alarm]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ignore_poll_alarm_failure: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    ENABLED = "Enabled"
    EVENTS = "Events"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "events": "Events",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    events: Optional[Union[list[str], Ref]] = None


@dataclass
class BlueGreenDeploymentConfiguration(PropertyType):
    DEPLOYMENT_READY_OPTION = "DeploymentReadyOption"
    GREEN_FLEET_PROVISIONING_OPTION = "GreenFleetProvisioningOption"
    TERMINATE_BLUE_INSTANCES_ON_DEPLOYMENT_SUCCESS = "TerminateBlueInstancesOnDeploymentSuccess"

    _property_mappings: ClassVar[dict[str, str]] = {
        "deployment_ready_option": "DeploymentReadyOption",
        "green_fleet_provisioning_option": "GreenFleetProvisioningOption",
        "terminate_blue_instances_on_deployment_success": "TerminateBlueInstancesOnDeploymentSuccess",
    }

    deployment_ready_option: Optional[DeploymentReadyOption] = None
    green_fleet_provisioning_option: Optional[GreenFleetProvisioningOption] = None
    terminate_blue_instances_on_deployment_success: Optional[BlueInstanceTerminationOption] = None


@dataclass
class BlueInstanceTerminationOption(PropertyType):
    ACTION = "Action"
    TERMINATION_WAIT_TIME_IN_MINUTES = "TerminationWaitTimeInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "termination_wait_time_in_minutes": "TerminationWaitTimeInMinutes",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    termination_wait_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Deployment(PropertyType):
    DESCRIPTION = "Description"
    IGNORE_APPLICATION_STOP_FAILURES = "IgnoreApplicationStopFailures"
    REVISION = "Revision"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "ignore_application_stop_failures": "IgnoreApplicationStopFailures",
        "revision": "Revision",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ignore_application_stop_failures: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    revision: Optional[RevisionLocation] = None


@dataclass
class DeploymentReadyOption(PropertyType):
    ACTION_ON_TIMEOUT = "ActionOnTimeout"
    WAIT_TIME_IN_MINUTES = "WaitTimeInMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action_on_timeout": "ActionOnTimeout",
        "wait_time_in_minutes": "WaitTimeInMinutes",
    }

    action_on_timeout: Optional[Union[str, Ref, GetAtt, Sub]] = None
    wait_time_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentStyle(PropertyType):
    DEPLOYMENT_OPTION = "DeploymentOption"
    DEPLOYMENT_TYPE = "DeploymentType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "deployment_option": "DeploymentOption",
        "deployment_type": "DeploymentType",
    }

    deployment_option: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deployment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EC2TagFilter(PropertyType):
    KEY = "Key"
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "type_": "Type",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, EC2TagFilterType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EC2TagSet(PropertyType):
    EC2_TAG_SET_LIST = "Ec2TagSetList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ec2_tag_set_list": "Ec2TagSetList",
    }

    ec2_tag_set_list: Optional[list[EC2TagSetListObject]] = None


@dataclass
class EC2TagSetListObject(PropertyType):
    EC2_TAG_GROUP = "Ec2TagGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ec2_tag_group": "Ec2TagGroup",
    }

    ec2_tag_group: Optional[list[EC2TagFilter]] = None


@dataclass
class ECSService(PropertyType):
    CLUSTER_NAME = "ClusterName"
    SERVICE_NAME = "ServiceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_name": "ClusterName",
        "service_name": "ServiceName",
    }

    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ELBInfo(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GitHubLocation(PropertyType):
    COMMIT_ID = "CommitId"
    REPOSITORY = "Repository"

    _property_mappings: ClassVar[dict[str, str]] = {
        "commit_id": "CommitId",
        "repository": "Repository",
    }

    commit_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GreenFleetProvisioningOption(PropertyType):
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoadBalancerInfo(PropertyType):
    ELB_INFO_LIST = "ElbInfoList"
    TARGET_GROUP_INFO_LIST = "TargetGroupInfoList"
    TARGET_GROUP_PAIR_INFO_LIST = "TargetGroupPairInfoList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "elb_info_list": "ElbInfoList",
        "target_group_info_list": "TargetGroupInfoList",
        "target_group_pair_info_list": "TargetGroupPairInfoList",
    }

    elb_info_list: Optional[list[ELBInfo]] = None
    target_group_info_list: Optional[list[TargetGroupInfo]] = None
    target_group_pair_info_list: Optional[list[TargetGroupPairInfo]] = None


@dataclass
class OnPremisesTagSet(PropertyType):
    ON_PREMISES_TAG_SET_LIST = "OnPremisesTagSetList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_premises_tag_set_list": "OnPremisesTagSetList",
    }

    on_premises_tag_set_list: Optional[list[OnPremisesTagSetListObject]] = None


@dataclass
class OnPremisesTagSetListObject(PropertyType):
    ON_PREMISES_TAG_GROUP = "OnPremisesTagGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_premises_tag_group": "OnPremisesTagGroup",
    }

    on_premises_tag_group: Optional[list[TagFilter]] = None


@dataclass
class RevisionLocation(PropertyType):
    GIT_HUB_LOCATION = "GitHubLocation"
    REVISION_TYPE = "RevisionType"
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "git_hub_location": "GitHubLocation",
        "revision_type": "RevisionType",
        "s3_location": "S3Location",
    }

    git_hub_location: Optional[GitHubLocation] = None
    revision_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_location: Optional[S3Location] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    BUNDLE_TYPE = "BundleType"
    E_TAG = "ETag"
    KEY = "Key"
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "bundle_type": "BundleType",
        "e_tag": "ETag",
        "key": "Key",
        "version": "Version",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bundle_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    e_tag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagFilter(PropertyType):
    KEY = "Key"
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key": "Key",
        "type_": "Type",
        "value": "Value",
    }

    key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, TagFilterType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupInfo(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupPairInfo(PropertyType):
    PROD_TRAFFIC_ROUTE = "ProdTrafficRoute"
    TARGET_GROUPS = "TargetGroups"
    TEST_TRAFFIC_ROUTE = "TestTrafficRoute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prod_traffic_route": "ProdTrafficRoute",
        "target_groups": "TargetGroups",
        "test_traffic_route": "TestTrafficRoute",
    }

    prod_traffic_route: Optional[TrafficRoute] = None
    target_groups: Optional[list[TargetGroupInfo]] = None
    test_traffic_route: Optional[TrafficRoute] = None


@dataclass
class TrafficRoute(PropertyType):
    LISTENER_ARNS = "ListenerArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "listener_arns": "ListenerArns",
    }

    listener_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class TriggerConfig(PropertyType):
    TRIGGER_EVENTS = "TriggerEvents"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_TARGET_ARN = "TriggerTargetArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "trigger_events": "TriggerEvents",
        "trigger_name": "TriggerName",
        "trigger_target_arn": "TriggerTargetArn",
    }

    trigger_events: Optional[Union[list[str], Ref]] = None
    trigger_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

