"""NeptuneDBSubnetGroup - AWS::Neptune::DBSubnetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBSubnetGroup:
    """AWS::Neptune::DBSubnetGroup resource."""

    resource: DBSubnetGroup
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
