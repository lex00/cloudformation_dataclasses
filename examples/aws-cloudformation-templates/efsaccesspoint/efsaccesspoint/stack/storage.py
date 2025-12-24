"""Storage resources: EFSFileSystem, EFSMountTarget1, EFSMountTarget2, EFSMountTarget3, EFSAccessPoint."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystemAccessPointTag:
    resource: efs.access_point.AccessPointTag
    key = 'Name'
    value = ref(EFSFileSystemName)


@cloudformation_dataclass
class EFSFileSystem:
    """AWS::EFS::FileSystem resource."""

    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
    file_system_tags = [EFSFileSystemAccessPointTag]


@cloudformation_dataclass
class EFSMountTarget1:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup1)]
    subnet_id = ref(Subnet1)


@cloudformation_dataclass
class EFSMountTarget2:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup2)]
    subnet_id = ref(Subnet2)


@cloudformation_dataclass
class EFSMountTarget3:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [ref(SecurityGroup3)]
    subnet_id = ref(Subnet3)


@cloudformation_dataclass
class EFSAccessPointAccessPointTag:
    resource: efs.access_point.AccessPointTag
    key = 'Name'
    value = ref(AccessPointName)


@cloudformation_dataclass
class EFSAccessPoint:
    """AWS::EFS::AccessPoint resource."""

    resource: efs.AccessPoint
    file_system_id = ref(EFSFileSystem)
    access_point_tags = [EFSAccessPointAccessPointTag]
