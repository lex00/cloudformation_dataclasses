"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Create an Amazon Data Firehose stream with server-side encryption set using AWS Managed keys and destination error logging enabled to a created Amazon CloudWatch log group and log stream.',
        parameters=[DestinationBucketName, LogStreamName, LogGroupName, CloudWatchLogsKMSKey, CloudWatchLogGroupRetention, DeliveryStreamName],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
