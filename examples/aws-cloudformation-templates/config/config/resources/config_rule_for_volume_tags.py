"""ConfigRuleForVolumeTags - AWS::Config::ConfigRule resource."""

from .. import *  # noqa: F403


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

    resource: ConfigRule
    input_parameters = {
        'tag1Key': 'CostCenter',
    }
    scope = ConfigRuleForVolumeTagsScope
    source = ConfigRuleForVolumeTagsSource
    depends_on = ["ConfigRecorder"]
