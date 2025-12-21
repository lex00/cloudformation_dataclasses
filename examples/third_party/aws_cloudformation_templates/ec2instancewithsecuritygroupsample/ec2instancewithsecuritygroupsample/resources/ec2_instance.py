from __future__ import annotations

"""EC2Instance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: Instance
    instance_type = ref(InstanceType)
    subnet_id = Select(0, ref(Subnets))
    security_group_ids = [get_att("InstanceSecurityGroup", "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
