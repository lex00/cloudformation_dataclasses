"""NeptuneDBCluster - AWS::Neptune::DBCluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBCluster:
    """AWS::Neptune::DBCluster resource."""

    resource: DBCluster
    backup_retention_period = ref(BackupRetentionPeriod)
    db_cluster_identifier = ref(DBClusterIdentifier)
    db_cluster_parameter_group_name = ref(NeptuneDBClusterParameterGroup)
    db_subnet_group_name = ref(NeptuneDBSubnetGroup)
    iam_auth_enabled = ref(IAMAuthEnabled)
    db_port = ref(Port)
    preferred_backup_window = ref(NeptuneDBClusterPreferredBackupWindow)
    preferred_maintenance_window = ref(NeptuneDBClusterPreferredMaintenanceWindow)
    storage_encrypted = ref(StorageEncrypted)
    vpc_security_group_ids = [ref(NeptuneDBSG)]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Cluster'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]
    depends_on = ["NeptuneDBSG"]
