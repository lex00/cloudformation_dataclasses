from __future__ import annotations

"""FargateContainerSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FargateContainerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Access to the Fargate containers'
    vpc_id: Ref[VPC] = ref()
