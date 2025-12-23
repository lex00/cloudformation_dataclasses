"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template uses a custom resource Lambda to apply a Name tag to the VPC peering connection on the Accepter Account.',
        parameters=[LambdaFunctionName, LambdaLogLevel, LambdaLogsCloudWatchKMSKey, LambdaLogsLogGroupRetention, PeerName, VPCPeeringConnectionId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
