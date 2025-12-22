"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import CronOrRate, CronRateCondition, CronSchedule, DesiredCapacity, InstanceType, KeyName, LatestAmiId, MaxSize, RateSchedule, SchedulerTasksCount, SubnetId, VpcId
from .outputs import ECSALBOutput, EcsClusterOutput, EcsServiceOutput, EcsTaskDefOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Amazon ECS Time and Event-Based Task Scheduling with CloudFormation. This will let you run tasks on a regular, scheduled basis and in response to CloudWatch Events. It easier to launch and stop container services that you need to run only at certain times. For example a backup/cleanup task.',
        parameters=[KeyName, VpcId, SubnetId, DesiredCapacity, MaxSize, SchedulerTasksCount, CronOrRate, CronSchedule, RateSchedule, InstanceType, LatestAmiId],
        outputs=[EcsServiceOutput, EcsClusterOutput, EcsTaskDefOutput, ECSALBOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
