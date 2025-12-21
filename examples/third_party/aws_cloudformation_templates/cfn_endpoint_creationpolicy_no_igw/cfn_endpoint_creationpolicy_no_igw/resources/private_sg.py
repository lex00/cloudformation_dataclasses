from __future__ import annotations

"""PrivateSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSGIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = ref(VpcCIDR)


@cloudformation_dataclass
class PrivateSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'PrivateSG'


@cloudformation_dataclass
class PrivateSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGIngress]
    vpc_id: Ref[VPC] = ref()
    tags = [PrivateSGAssociationParameter]
