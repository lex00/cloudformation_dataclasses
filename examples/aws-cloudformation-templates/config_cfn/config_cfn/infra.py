"""Infra resources: ConfigRecorder, DeliveryChannel, ConfigRuleForVolumeTags, ConfigRuleForVolumeAutoEnableIO."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ConfigRecorderExclusionByResourceTypes:
    resource: config.configuration_recorder.ExclusionByResourceTypes
    resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRecorder:
    """AWS::Config::ConfigurationRecorder resource."""

    resource: config.ConfigurationRecorder
    name = 'default'
    recording_group = ConfigRecorderExclusionByResourceTypes
    role_arn = get_att(ConfigRole, "Arn")


@cloudformation_dataclass
class DeliveryChannelConfigSnapshotDeliveryProperties:
    resource: config.delivery_channel.ConfigSnapshotDeliveryProperties
    delivery_frequency = 'Six_Hours'


@cloudformation_dataclass
class DeliveryChannel:
    """AWS::Config::DeliveryChannel resource."""

    resource: config.DeliveryChannel
    config_snapshot_delivery_properties = DeliveryChannelConfigSnapshotDeliveryProperties
    s3_bucket_name = ref(ConfigBucket)
    sns_topic_arn = ref(ConfigTopic)
    condition = 'CreateDeliveryChannel'


@cloudformation_dataclass
class ConfigRuleForVolumeTagsScope:
    resource: config.config_rule.Scope
    compliance_resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRuleForVolumeTagsSource:
    resource: config.config_rule.Source
    owner = 'AWS'
    source_identifier = 'REQUIRED_TAGS'


@cloudformation_dataclass
class ConfigRuleForVolumeTags:
    """AWS::Config::ConfigRule resource."""

    resource: config.ConfigRule
    input_parameters = {
        'tag1Key': 'CostCenter',
    }
    scope = ConfigRuleForVolumeTagsScope
    source = ConfigRuleForVolumeTagsSource
    depends_on = ["ConfigRecorder"]


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOScope:
    resource: config.config_rule.Scope
    compliance_resource_id = ref(Ec2Volume)
    compliance_resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSourceDetail:
    resource: config.config_rule.SourceDetail
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSource:
    resource: config.config_rule.Source
    owner = 'CUSTOM_LAMBDA'
    source_details = [ConfigRuleForVolumeAutoEnableIOSourceDetail]
    source_identifier = get_att(VolumeAutoEnableIOComplianceCheck, "Arn")


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIO:
    """AWS::Config::ConfigRule resource."""

    resource: config.ConfigRule
    config_rule_name = 'ConfigRuleForVolumeAutoEnableIO'
    scope = ConfigRuleForVolumeAutoEnableIOScope
    source = ConfigRuleForVolumeAutoEnableIOSource
    depends_on = ["ConfigPermissionToCallLambda", "ConfigRecorder"]
