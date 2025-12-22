"""NeptuneDBParameterGroup - AWS::Neptune::DBParameterGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBParameterGroup:
    """AWS::Neptune::DBParameterGroup resource."""

    resource: DBParameterGroup
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
