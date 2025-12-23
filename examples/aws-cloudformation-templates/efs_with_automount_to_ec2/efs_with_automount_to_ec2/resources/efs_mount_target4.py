"""EFSMountTarget4 - AWS::EFS::MountTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSMountTarget4:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(3, ref(Subnets))
