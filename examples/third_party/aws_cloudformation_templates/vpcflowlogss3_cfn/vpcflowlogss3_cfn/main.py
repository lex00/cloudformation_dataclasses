"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import S3AccessLogsBucketName, S3AccessLogsConditionCondition, VPCFlowLogsBucketKMSKey, VPCFlowLogsBucketKMSKeyConditionCondition, VPCFlowLogsBucketKeyEnabled, VPCFlowLogsBucketName, VPCFlowLogsLogFormat, VPCFlowLogsMaxAggregationInterval, VPCFlowLogsNewBucketConditionCondition, VPCFlowLogsTrafficType, VPCID
from .outputs import VPCFlowLogsBucketOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template enables VPC Flow Logs to S3. An option is provided to create an Amazon S3 bucket with encryption to host the flow logs.',
        parameters=[S3AccessLogsBucketName, VPCFlowLogsBucketKeyEnabled, VPCFlowLogsBucketKMSKey, VPCFlowLogsBucketName, VPCFlowLogsLogFormat, VPCFlowLogsMaxAggregationInterval, VPCFlowLogsTrafficType, VPCID],
        outputs=[VPCFlowLogsBucketOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
