from __future__ import annotations

"""Ec2Volume - AWS::EC2::Volume resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Ec2VolumeAssociationParameter:
    resource: AssociationParameter
    key = ref(Ec2VolumeTagKey)
    value = 'Ec2VolumeTagValue'


@cloudformation_dataclass
class Ec2Volume:
    """AWS::EC2::Volume resource."""

    resource: Volume
    auto_enable_io = ref(Ec2VolumeAutoEnableIO)
    size = '5'
    availability_zone = Select(0, GetAZs())
    tags = [Ec2VolumeAssociationParameter]
