"""Compute resources: EC2Instance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    subnet_id = Select(0, ref(Subnets))
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
