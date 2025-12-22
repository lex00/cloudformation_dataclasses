"""PrivateSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSGIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    source_security_group_id = ref(BastionSG)


@cloudformation_dataclass
class PrivateSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'PrivateSG'


@cloudformation_dataclass
class PrivateSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGIngress]
    vpc_id = ref(VPC)
    tags = [PrivateSGAssociationParameter]
