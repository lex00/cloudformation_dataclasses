from __future__ import annotations

"""ControlPlaneSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ControlPlaneSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Communication between the control plane and worker nodegroups'
    vpc_id: Ref[VPC] = ref()
    group_name = Sub('${AWS::StackName}-eks-control-plane-sg')
