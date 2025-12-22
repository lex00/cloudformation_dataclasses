from __future__ import annotations

"""NeptuneDBInstance - AWS::Neptune::DBInstance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBInstance:
    """AWS::Neptune::DBInstance resource."""

    resource: DBInstance
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
