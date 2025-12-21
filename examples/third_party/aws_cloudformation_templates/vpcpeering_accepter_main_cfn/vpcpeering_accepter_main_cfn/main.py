"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import LambdaFunctionName, LambdaLogLevel, LambdaLogsCloudWatchKMSKey, LambdaLogsLogGroupRetention, LambdaRoleName, NumberOfRouteTables, NumberOfSecurityGroups, PeerName, PeerVPCCIDR, RouteTableIds, SecurityGroupIds, TemplatesS3BucketName, TemplatesS3BucketRegion, TemplatesS3KeyPrefix, VPCPeeringConnectionId


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template accomplishes the following tasks: (1) applies a name tag to the specified VPC peering connection. (2) updates the specified route tables and security groups to allow communications via the VPC peering connection. Note, this is for the VPC Peering Accepter account.',
        parameters=[LambdaFunctionName, LambdaLogLevel, LambdaLogsCloudWatchKMSKey, LambdaLogsLogGroupRetention, LambdaRoleName, NumberOfRouteTables, NumberOfSecurityGroups, PeerName, PeerVPCCIDR, RouteTableIds, SecurityGroupIds, TemplatesS3BucketName, TemplatesS3BucketRegion, TemplatesS3KeyPrefix, VPCPeeringConnectionId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
