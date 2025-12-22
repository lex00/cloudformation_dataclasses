"""EFSFileSystem - AWS::EFS::FileSystem resource."""

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
