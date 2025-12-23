"""Network resources: ADConnectorDomainMembersSG."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDomainMembersSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = Sub('${DomainNetBiosName} Domain Members SG via AD Connector')
    vpc_id = ref(VPCID)
    security_group_ingress = [{
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '10.0.0.0/8',
    }, {
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '172.16.0.0/12',
    }, {
        'IpProtocol': '-1',
        'Description': 'LAB - Allow All Private IP Communications',
        'CidrIp': '192.168.0.0/16',
    }]
    security_group_egress = [{
        'Description': 'Allow All Outbound Communications',
        'IpProtocol': '-1',
        'CidrIp': '0.0.0.0/0',
    }]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${DomainNetBiosName}-DomainMembersSG-ADConnector'),
    }]
    condition = 'DomainMembersSGCondition'
