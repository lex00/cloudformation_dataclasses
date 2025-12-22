"""NeptuneDBClusterParameterGroup - AWS::Neptune::DBClusterParameterGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBClusterParameterGroup:
    """AWS::Neptune::DBClusterParameterGroup resource."""

    resource: DBClusterParameterGroup
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
