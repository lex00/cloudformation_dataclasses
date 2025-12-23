"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template enables VPC Flow Logs to CloudWatch, S3, or both.',
        parameters=[CreateVPCFlowLogsToCloudWatch, CreateVPCFlowLogsToS3, S3AccessLogsBucketName, TemplatesS3BucketName, TemplatesS3BucketRegion, VPCFlowLogsBucketKeyEnabled, VPCFlowLogsBucketKMSKey, VPCFlowLogsBucketName, VPCFlowLogsCloudWatchKMSKey, VPCFlowLogsLogFormat, VPCFlowLogsLogGroupRetention, VPCFlowLogsMaxAggregationInterval, VPCFlowLogsTrafficType, VPCID],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
