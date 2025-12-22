from __future__ import annotations

"""EFSSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSSecurityGroupIngress:
    resource: Ingress
    from_port = '2049'
    ip_protocol = 'tcp'
    to_port = '2049'
    source_security_group_id = get_att(InstanceSecurityGroup, "GroupId")


@cloudformation_dataclass
class EFSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [EFSSecurityGroupIngress]
    vpc_id = ref(VPC)
