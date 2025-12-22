"""ConfigRuleForVolumeAutoEnableIO - AWS::Config::ConfigRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOScope:
    resource: config.Scope
    compliance_resource_id = ref(Ec2Volume)
    compliance_resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSourceDetail:
    resource: config.SourceDetail
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSource:
    resource: config.Source
    owner = 'CUSTOM_LAMBDA'
    source_details = [ConfigRuleForVolumeAutoEnableIOSourceDetail]
    source_identifier = get_att(VolumeAutoEnableIOComplianceCheck, "Arn")


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIO:
    """AWS::Config::ConfigRule resource."""

    resource: ConfigRule
    config_rule_name = 'ConfigRuleForVolumeAutoEnableIO'
    scope = ConfigRuleForVolumeAutoEnableIOScope
    source = ConfigRuleForVolumeAutoEnableIOSource
    depends_on = ["ConfigPermissionToCallLambda", "ConfigRecorder"]
