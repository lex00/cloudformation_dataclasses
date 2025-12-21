from __future__ import annotations

"""BastionInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BastionInstanceAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'Bastion'


@cloudformation_dataclass
class BastionInstance:
    """AWS::EC2::Instance resource."""

    resource: Instance
    key_name = ref(KeyName)
    instance_type = 't2.micro'
    security_group_ids = [ref("BastionSG")]
    subnet_id: Ref[PublicSubnet1] = ref()
    image_id = ref(LinuxAMI)
    iam_instance_profile: Ref[BastionProfile] = ref()
    tags = [BastionInstanceAssociationParameter]
