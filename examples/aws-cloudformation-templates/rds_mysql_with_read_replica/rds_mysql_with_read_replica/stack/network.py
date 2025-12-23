"""Network resources: DBEC2SecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBEC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Open database for access'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'SourceSecurityGroupName': ref(EC2SecurityGroup),
    }]
    condition = 'IsEC2VPC'
