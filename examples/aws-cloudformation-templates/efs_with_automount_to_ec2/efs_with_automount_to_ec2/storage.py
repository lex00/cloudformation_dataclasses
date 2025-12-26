"""Storage resources: EFSFileSystem, EFSMountTarget1, EFSMountTarget2, EFSMountTarget3, EFSMountTarget4."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystem:
    """AWS::EFS::FileSystem resource."""

    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'


@cloudformation_dataclass
class EFSMountTarget1:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(0, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget2:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(1, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget3:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(2, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget4:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(3, ref(Subnets))
