"""MyRDSParamGroup - AWS::RDS::DBParameterGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyRDSParamGroup:
    """AWS::RDS::DBParameterGroup resource."""

    resource: rds.DBParameterGroup
    family = 'MySQL8.0'
    description = 'CloudFormation Sample Database Parameter Group'
    parameters = {
        'autocommit': '1',
        'general_log': '1',
    }
