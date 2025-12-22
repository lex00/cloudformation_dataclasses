from __future__ import annotations

"""EFSMountTarget1 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget1:
    """AWS::EFS::MountTarget resource."""

    resource: MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup1)]
    subnet_id = ref(Subnet1)
