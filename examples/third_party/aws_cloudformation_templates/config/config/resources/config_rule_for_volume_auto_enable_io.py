from __future__ import annotations

"""ConfigRuleForVolumeAutoEnableIO - AWS::Config::ConfigRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOScope:
    resource: Scope
    compliance_resource_id: Ref[Ec2Volume] = ref()
    compliance_resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSourceDetail:
    resource: SourceDetail
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOSource:
    resource: Source
    owner = 'CUSTOM_LAMBDA'
    source_details = [ConfigRuleForVolumeAutoEnableIOSourceDetail]
    source_identifier: GetAtt[VolumeAutoEnableIOComplianceCheck] = get_att("Arn")


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIO:
    """AWS::Config::ConfigRule resource."""

    resource: ConfigRule
    config_rule_name = 'ConfigRuleForVolumeAutoEnableIO'
    scope = ConfigRuleForVolumeAutoEnableIOScope
    source = ConfigRuleForVolumeAutoEnableIOSource
    depends_on = ["ConfigPermissionToCallLambda", "ConfigRecorder"]
