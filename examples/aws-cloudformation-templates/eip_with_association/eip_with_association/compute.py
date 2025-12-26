"""Compute resources: EC2Instance, IPAssoc."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    user_data = Base64(Join('', [
    'IPAddress=',
    ref(IPAddress),
]))
    instance_type = ref(InstanceType)
    subnet_id = Select(0, ref(Subnets))
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)


@cloudformation_dataclass
class IPAssoc:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    instance_id = ref(EC2Instance)
    allocation_id = get_att(IPAddress, "AllocationId")
