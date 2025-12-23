"""ControlPlaneSecurityGroupIngress - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ControlPlaneSecurityGroupIngress:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(ControlPlaneSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = get_att(ControlPlaneSecurityGroup, "GroupId")
    source_security_group_owner_id = AWS_ACCOUNT_ID
