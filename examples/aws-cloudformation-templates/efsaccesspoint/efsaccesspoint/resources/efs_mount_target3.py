"""EFSMountTarget3 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget3:
    """AWS::EFS::MountTarget resource."""

    resource: MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup3)]
    subnet_id = ref(Subnet3)
