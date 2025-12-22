"""ADConnectorDomainMembersSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDomainMembersSGIngress:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '10.0.0.0/8'


@cloudformation_dataclass
class ADConnectorDomainMembersSGIngress1:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '172.16.0.0/12'


@cloudformation_dataclass
class ADConnectorDomainMembersSGIngress2:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '192.168.0.0/16'


@cloudformation_dataclass
class ADConnectorDomainMembersSGEgress:
    resource: Egress
    description = 'Allow All Outbound Communications'
    ip_protocol = '-1'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class ADConnectorDomainMembersSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${DomainNetBiosName}-DomainMembersSG-ADConnector')


@cloudformation_dataclass
class ADConnectorDomainMembersSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = Sub('${DomainNetBiosName} Domain Members SG via AD Connector')
    vpc_id = ref(VPCID)
    security_group_ingress = [ADConnectorDomainMembersSGIngress, ADConnectorDomainMembersSGIngress1, ADConnectorDomainMembersSGIngress2]
    security_group_egress = [ADConnectorDomainMembersSGEgress]
    tags = [ADConnectorDomainMembersSGAssociationParameter]
    condition = 'DomainMembersSGCondition'
