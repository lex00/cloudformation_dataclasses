from __future__ import annotations

"""EFSMountTarget2 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget2:
    """AWS::EFS::MountTarget resource."""

    resource: MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup2)]
    subnet_id = ref(Subnet2)
