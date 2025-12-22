"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AppName, BackupRetentionPeriod, CreateSnsSubscriptionCondition, CreateSnsTopicCondition, DBClusterIdentifier, DBInstanceClass, EnableAuditLogUploadCondition, Env, GremlinRequestsPerSecThreshold, HighCpuAlarmThreshold, IAMAuthEnabled, LowMemoryAlarmThreshold, MajorVersionUpgrade, MinorVersionUpgrade, NeptuneDBClusterPreferredBackupWindow, NeptuneDBClusterPreferredMaintenanceWindow, NeptuneDBInstancePreferredMaintenanceWindow, NeptuneDBSubnetGroupName, NeptuneQueryTimeout, NeptuneSNSTopicArn, Owner, Port, SNSEmailSubscription, SparqlRequestsPerSecThreshold, Storage, StorageEncrypted, Tier, UploadAuditLogs, User, VPCStack, Version
from .outputs import NeptuneEndpointAddressOutput, NeptuneEndpointPortOutput, NeptuneReadEndpointAddressOutput, NeptuneSnsTopicOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation template to automatically provision AWS Neptune Graph Database through optimized CI/CD method with AWS CloudWatch and AWS SNS.',
        parameters=[Env, AppName, User, Owner, Tier, Version, Storage, VPCStack, DBInstanceClass, DBClusterIdentifier, Port, NeptuneQueryTimeout, StorageEncrypted, NeptuneDBSubnetGroupName, NeptuneSNSTopicArn, SNSEmailSubscription, HighCpuAlarmThreshold, LowMemoryAlarmThreshold, GremlinRequestsPerSecThreshold, SparqlRequestsPerSecThreshold, UploadAuditLogs, BackupRetentionPeriod, NeptuneDBClusterPreferredMaintenanceWindow, NeptuneDBInstancePreferredMaintenanceWindow, NeptuneDBClusterPreferredBackupWindow, MajorVersionUpgrade, MinorVersionUpgrade, IAMAuthEnabled],
        outputs=[NeptuneEndpointAddressOutput, NeptuneReadEndpointAddressOutput, NeptuneSnsTopicOutput, NeptuneEndpointPortOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
