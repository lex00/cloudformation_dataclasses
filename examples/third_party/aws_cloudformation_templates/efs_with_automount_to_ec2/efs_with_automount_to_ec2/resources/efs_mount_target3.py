from __future__ import annotations

"""EFSMountTarget3 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget3:
    """AWS::EFS::MountTarget resource."""

    resource: MountTarget
    file_system_id: Ref[EFSFileSystem] = ref()
    security_groups = [get_att("EFSSecurityGroup", "GroupId")]
    subnet_id = Select(2, ref(Subnets))
