from __future__ import annotations

"""AWSManagedADDomainMembersSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADDomainMembersSGIngress:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '10.0.0.0/8'


@cloudformation_dataclass
class AWSManagedADDomainMembersSGIngress1:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '172.16.0.0/12'


@cloudformation_dataclass
class AWSManagedADDomainMembersSGIngress2:
    resource: Ingress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '192.168.0.0/16'


@cloudformation_dataclass
class AWSManagedADDomainMembersSGEgress:
    resource: Egress
    description = 'Allow All Outbound Communications'
    ip_protocol = '-1'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class AWSManagedADDomainMembersSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWSManagedADDomainNetBiosName}-DomainMembersSG-AWSManagedAD')


@cloudformation_dataclass
class AWSManagedADDomainMembersSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = Sub('${AWSManagedADDomainNetBiosName} Domain Members SG via AWS Managed Microsoft AD')
    vpc_id = ref(VPCID)
    security_group_ingress = [AWSManagedADDomainMembersSGIngress, AWSManagedADDomainMembersSGIngress1, AWSManagedADDomainMembersSGIngress2]
    security_group_egress = [AWSManagedADDomainMembersSGEgress]
    tags = [AWSManagedADDomainMembersSGAssociationParameter]
    condition = 'DomainMembersSGCondition'
