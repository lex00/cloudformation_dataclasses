from __future__ import annotations

"""IPAssoc - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IPAssoc:
    """AWS::EC2::EIPAssociation resource."""

    resource: EIPAssociation
    instance_id: Ref[EC2Instance] = ref()
    allocation_id: GetAtt[IPAddress] = get_att("AllocationId")
