"""Fargate resources - ECS cluster, task definition, and service."""

from .. import *  # noqa: F403, F401


@cloudformation_dataclass
class TaskSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 80
    to_port = 80
    source_security_group_id = ref(AlbSecurityGroupIdParam)

@cloudformation_dataclass
class TaskSecurityGroup:
    """Security group for Fargate tasks."""

    resource: ec2.SecurityGroup
    group_description = "Security group for Fargate tasks"
    vpc_id = ref(VpcIdParam)
    security_group_ingress = [TaskSecurityGroupIngress]
