from __future__ import annotations

"""ControlPlaneSecurityGroupIngress - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ControlPlaneSecurityGroupIngress:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id: Ref[ControlPlaneSecurityGroup] = ref()
    ip_protocol = '-1'
    source_security_group_id: GetAtt[ControlPlaneSecurityGroup] = get_att("GroupId")
    source_security_group_owner_id = AWS_ACCOUNT_ID
