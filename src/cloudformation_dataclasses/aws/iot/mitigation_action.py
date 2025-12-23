"""PropertyTypes for AWS::IoT::MitigationAction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActionParams(PropertyType):
    UPDATE_DEVICE_CERTIFICATE_PARAMS = "UpdateDeviceCertificateParams"
    ADD_THINGS_TO_THING_GROUP_PARAMS = "AddThingsToThingGroupParams"
    PUBLISH_FINDING_TO_SNS_PARAMS = "PublishFindingToSnsParams"
    ENABLE_IO_T_LOGGING_PARAMS = "EnableIoTLoggingParams"
    REPLACE_DEFAULT_POLICY_VERSION_PARAMS = "ReplaceDefaultPolicyVersionParams"
    UPDATE_CA_CERTIFICATE_PARAMS = "UpdateCACertificateParams"

    _property_mappings: ClassVar[dict[str, str]] = {
        "update_device_certificate_params": "UpdateDeviceCertificateParams",
        "add_things_to_thing_group_params": "AddThingsToThingGroupParams",
        "publish_finding_to_sns_params": "PublishFindingToSnsParams",
        "enable_io_t_logging_params": "EnableIoTLoggingParams",
        "replace_default_policy_version_params": "ReplaceDefaultPolicyVersionParams",
        "update_ca_certificate_params": "UpdateCACertificateParams",
    }

    update_device_certificate_params: Optional[UpdateDeviceCertificateParams] = None
    add_things_to_thing_group_params: Optional[AddThingsToThingGroupParams] = None
    publish_finding_to_sns_params: Optional[PublishFindingToSnsParams] = None
    enable_io_t_logging_params: Optional[EnableIoTLoggingParams] = None
    replace_default_policy_version_params: Optional[ReplaceDefaultPolicyVersionParams] = None
    update_ca_certificate_params: Optional[UpdateCACertificateParams] = None


@dataclass
class AddThingsToThingGroupParams(PropertyType):
    OVERRIDE_DYNAMIC_GROUPS = "OverrideDynamicGroups"
    THING_GROUP_NAMES = "ThingGroupNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "override_dynamic_groups": "OverrideDynamicGroups",
        "thing_group_names": "ThingGroupNames",
    }

    override_dynamic_groups: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    thing_group_names: Optional[Union[list[str], Ref]] = None


@dataclass
class EnableIoTLoggingParams(PropertyType):
    ROLE_ARN_FOR_LOGGING = "RoleArnForLogging"
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn_for_logging": "RoleArnForLogging",
        "log_level": "LogLevel",
    }

    role_arn_for_logging: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PublishFindingToSnsParams(PropertyType):
    TOPIC_ARN = "TopicArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicArn",
    }

    topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplaceDefaultPolicyVersionParams(PropertyType):
    TEMPLATE_NAME = "TemplateName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_name": "TemplateName",
    }

    template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateCACertificateParams(PropertyType):
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateDeviceCertificateParams(PropertyType):
    ACTION = "Action"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None

