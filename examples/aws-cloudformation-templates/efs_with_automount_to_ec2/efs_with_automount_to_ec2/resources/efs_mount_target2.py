"""EFSMountTarget2 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget2:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(1, ref(Subnets))
