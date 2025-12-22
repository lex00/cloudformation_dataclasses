from __future__ import annotations

"""ConfigRecorder - AWS::Config::ConfigurationRecorder resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigRecorderRecordingGroup:
    resource: RecordingGroup
    resource_types = ['AWS::EC2::Volume']


@cloudformation_dataclass
class ConfigRecorder:
    """AWS::Config::ConfigurationRecorder resource."""

    resource: ConfigurationRecorder
    name = 'default'
    recording_group = ConfigRecorderRecordingGroup
    role_arn: GetAtt[ConfigRole] = get_att("Arn")
