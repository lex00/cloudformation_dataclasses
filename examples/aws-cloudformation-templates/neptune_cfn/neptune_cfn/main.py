"""Template builder."""

from . import *  # noqa: F403, F401


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
