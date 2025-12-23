"""BastionSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BastionSGEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class BastionSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'BastionSG'


@cloudformation_dataclass
class BastionSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Inbound Bastion Traffic'
    security_group_ingress = [BastionSGEgress]
    vpc_id = ref(VPC)
    tags = [BastionSGAssociationParameter]
