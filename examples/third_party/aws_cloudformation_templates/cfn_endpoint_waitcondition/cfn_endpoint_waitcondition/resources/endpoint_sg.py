"""EndpointSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EndpointSGIngress:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class EndpointSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'EndpointSG'


@cloudformation_dataclass
class EndpointSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Traffic into CloudFormation Endpoint'
    security_group_ingress = [EndpointSGIngress]
    vpc_id = ref(VPC)
    tags = [EndpointSGAssociationParameter]
