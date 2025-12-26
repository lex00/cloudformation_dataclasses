"""Database resources: NeptuneDBClusterParameterGroup, NeptuneDBSubnetGroup, NeptuneDBCluster, NeptuneDBParameterGroup, NeptuneDBInstance."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBClusterParameterGroup:
    """AWS::Neptune::DBClusterParameterGroup resource."""

    resource: neptune.DBClusterParameterGroup
    description = Sub('CloudFormation managed Neptune DB Cluster Parameter Group - ${Env}-${AppName}-cluster-parameter-group')
    parameters = {
        'neptune_enable_audit_log': If("EnableAuditLogUpload", 1, 0),
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-neptune-cluster-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-cluster-parameter-group'),
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


@cloudformation_dataclass
class NeptuneDBSubnetGroup:
    """AWS::Neptune::DBSubnetGroup resource."""

    resource: neptune.DBSubnetGroup
    db_subnet_group_description = Sub('CloudFormation managed Neptune DB Subnet Group - ${Env}-${AppName}-subnet-group')
    db_subnet_group_name = ref(NeptuneDBSubnetGroupName)
    subnet_ids = [ImportValue(Sub('${VPCStack}-PrivateSubnet1')), ImportValue(Sub('${VPCStack}-PrivateSubnet2'))]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-subnet-group'),
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


@cloudformation_dataclass
class NeptuneDBCluster:
    """AWS::Neptune::DBCluster resource."""

    resource: neptune.DBCluster
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
    depends_on = [NeptuneDBSG]


@cloudformation_dataclass
class NeptuneDBParameterGroup:
    """AWS::Neptune::DBParameterGroup resource."""

    resource: neptune.DBParameterGroup
    description = Sub('CloudFormation managed Neptune DB Parameter Group - ${Env}-${AppName}-parameter-group')
    parameters = {
        'neptune_query_timeout': ref(NeptuneQueryTimeout),
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-parameter-group'),
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


@cloudformation_dataclass
class NeptuneDBInstance:
    """AWS::Neptune::DBInstance resource."""

    resource: neptune.DBInstance
    allow_major_version_upgrade = ref(MajorVersionUpgrade)
    auto_minor_version_upgrade = ref(MinorVersionUpgrade)
    db_cluster_identifier = ref(NeptuneDBCluster)
    db_instance_class = ref(DBInstanceClass)
    db_parameter_group_name = ref(NeptuneDBParameterGroup)
    db_subnet_group_name = ref(NeptuneDBSubnetGroup)
    preferred_maintenance_window = ref(NeptuneDBInstancePreferredMaintenanceWindow)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Instance'),
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
