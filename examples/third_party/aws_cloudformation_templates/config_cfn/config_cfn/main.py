"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import CreateDeliveryChannelCondition, DeliveryChannelExists, Ec2VolumeAutoEnableIO, Ec2VolumeTagKey
from .outputs import ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput, ConfigRuleForVolumeTagsArnOutput, ConfigRuleForVolumeTagsConfigRuleIdOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template Config: This template demonstrates the usage of AWS Config resources. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[DeliveryChannelExists, Ec2VolumeAutoEnableIO, Ec2VolumeTagKey],
        outputs=[ConfigRuleForVolumeTagsArnOutput, ConfigRuleForVolumeTagsConfigRuleIdOutput, ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
