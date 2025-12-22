"""HTTPSTcpIn - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class HTTPSTcpIn:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id = ref(ALBExternalAccessSG)
    to_port = 443
    ip_protocol = 'tcp'
    from_port = 443
    cidr_ip = '0.0.0.0/0'
