"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ConfigRuleForVolumeTagsArnOutput:
    resource: Output
    value = get_att(ConfigRuleForVolumeTags, "Arn")


@cloudformation_dataclass
class ConfigRuleForVolumeTagsConfigRuleIdOutput:
    resource: Output
    value = get_att(ConfigRuleForVolumeTags, "ConfigRuleId")


@cloudformation_dataclass
class ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput:
    resource: Output
    value = get_att(ConfigRuleForVolumeAutoEnableIO, "Compliance.Type")
