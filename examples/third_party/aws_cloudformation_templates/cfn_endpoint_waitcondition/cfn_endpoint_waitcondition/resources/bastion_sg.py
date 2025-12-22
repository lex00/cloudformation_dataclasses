from __future__ import annotations

"""BastionSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BastionSGIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class BastionSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'BastionSG'


@cloudformation_dataclass
class BastionSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Inbound Bastion Traffic'
    security_group_ingress = [BastionSGIngress]
    vpc_id = ref(VPC)
    tags = [BastionSGAssociationParameter]
