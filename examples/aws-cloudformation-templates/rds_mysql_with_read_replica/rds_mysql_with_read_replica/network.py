"""Network resources: DBEC2SecurityGroup."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class DBEC2SecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = '3306'
    to_port = '3306'
    source_security_group_name = ref(EC2SecurityGroup)


@cloudformation_dataclass
class DBEC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Open database for access'
    security_group_ingress = [DBEC2SecurityGroupIngress]
    condition = 'IsEC2VPC'
