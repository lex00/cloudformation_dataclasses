"""IPAssoc - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IPAssoc:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    instance_id = ref(EC2Instance)
    allocation_id = get_att(IPAddress, "AllocationId")
