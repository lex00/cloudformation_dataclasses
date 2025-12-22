"""Tcp8080In - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Tcp8080In:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EC2InstanceSG)
    to_port = '8080'
    ip_protocol = 'tcp'
    from_port = '8080'
    source_security_group_id = ref(ALBExternalAccessSG)
