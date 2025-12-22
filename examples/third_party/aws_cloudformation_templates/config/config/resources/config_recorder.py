"""ConfigRecorder - AWS::Config::ConfigurationRecorder resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigRecorderExclusionByResourceTypes:
    resource: config.configuration_recorder.ExclusionByResourceTypes
    resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRecorder:
    """AWS::Config::ConfigurationRecorder resource."""

    resource: ConfigurationRecorder
    name = 'default'
    recording_group = ConfigRecorderExclusionByResourceTypes
    role_arn = get_att(ConfigRole, "Arn")
