"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import ClientIP, ExistsDMSCloudwatchRole, ExistsDMSVPCRole, NotExistsDMSCloudwatchRoleCondition, NotExistsDMSVPCRoleCondition, SnapshotIdentifier
from .outputs import AuroraEndpointOutput, RegionNameOutput, S3BucketNameOutput, StackNameOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This CloudFormation sample template DMSAuroraToS3FullLoadAndOngoingReplication creates an Aurora RDS instance and DMS instance in a VPC, and an S3 bucket. The Aurora RDS instance is configured as the DMS Source Endpoint and the S3 bucket is configured as the DMS Target Endpoint. A DMS task is created and configured to migrate existing data and replicate ongoing changes from the source endpoint to the target endpoint. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[ClientIP, ExistsDMSVPCRole, ExistsDMSCloudwatchRole, SnapshotIdentifier],
        outputs=[StackNameOutput, RegionNameOutput, S3BucketNameOutput, AuroraEndpointOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
