"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import VPCFlowLogsCloudWatchKMSKey, VPCFlowLogsCloudWatchKMSKeyConditionCondition, VPCFlowLogsLogFormat, VPCFlowLogsLogGroupRetention, VPCFlowLogsMaxAggregationInterval, VPCFlowLogsTrafficType, VPCID
from .outputs import VPCFlowLogsLogGroupOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template enables VPC Flow Logs to CloudWatch.',
        parameters=[VPCFlowLogsCloudWatchKMSKey, VPCFlowLogsLogFormat, VPCFlowLogsLogGroupRetention, VPCFlowLogsMaxAggregationInterval, VPCFlowLogsTrafficType, VPCID],
        outputs=[VPCFlowLogsLogGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
