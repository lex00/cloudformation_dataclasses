"""ADConnectorDomainMembersSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDomainMembersSGEgress:
    resource: ec2.security_group.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '10.0.0.0/8'


@cloudformation_dataclass
class ADConnectorDomainMembersSGEgress1:
    resource: ec2.security_group.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '172.16.0.0/12'


@cloudformation_dataclass
class ADConnectorDomainMembersSGEgress2:
    resource: ec2.security_group.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '192.168.0.0/16'


@cloudformation_dataclass
class ADConnectorDomainMembersSGEgress3:
    resource: ec2.security_group.Egress
    description = 'Allow All Outbound Communications'
    ip_protocol = '-1'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class ADConnectorDomainMembersSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${DomainNetBiosName}-DomainMembersSG-ADConnector')


@cloudformation_dataclass
class ADConnectorDomainMembersSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = Sub('${DomainNetBiosName} Domain Members SG via AD Connector')
    vpc_id = ref(VPCID)
    security_group_ingress = [ADConnectorDomainMembersSGEgress, ADConnectorDomainMembersSGEgress1, ADConnectorDomainMembersSGEgress2]
    security_group_egress = [ADConnectorDomainMembersSGEgress3]
    tags = [ADConnectorDomainMembersSGAssociationParameter]
    condition = 'DomainMembersSGCondition'
