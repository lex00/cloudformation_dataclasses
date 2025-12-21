"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import DBAllocatedStorage, DBInstanceClass, DBName, DBUser, EC2SecurityGroup, EnableReadReplica, EnableReadReplicaCondition, IsEC2VPCCondition, MultiAZ
from .outputs import DBCredentialSecretNameArnOutput, EC2PlatformOutput, JDBCConnectionStringOutput, ReplicaJDBCConnectionStringOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template RDS_MySQL_With_Read_Replica: Sample template showing how to create a highly-available, RDS DBInstance with a read replica. **WARNING** This template creates an Amazon Relational Database Service database instance and Amazon CloudWatch alarms. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[DBName, DBUser, DBAllocatedStorage, DBInstanceClass, EC2SecurityGroup, MultiAZ, EnableReadReplica],
        outputs=[DBCredentialSecretNameArnOutput, EC2PlatformOutput, JDBCConnectionStringOutput, ReplicaJDBCConnectionStringOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
