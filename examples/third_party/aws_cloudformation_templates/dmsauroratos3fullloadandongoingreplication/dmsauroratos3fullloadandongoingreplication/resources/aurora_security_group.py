"""AuroraSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AuroraSecurityGroupIngress:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '3306'
    to_port = '3306'
    cidr_ip = ref(ClientIP)


@cloudformation_dataclass
class AuroraSecurityGroupIngress1:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '3306'
    to_port = '3306'
    cidr_ip = '10.0.0.0/24'


@cloudformation_dataclass
class AuroraSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Security group for Aurora SampleDB DB Instance'
    group_name = 'Aurora SampleDB Security Group'
    vpc_id = ref(VPC)
    security_group_ingress = [AuroraSecurityGroupIngress, AuroraSecurityGroupIngress1]
