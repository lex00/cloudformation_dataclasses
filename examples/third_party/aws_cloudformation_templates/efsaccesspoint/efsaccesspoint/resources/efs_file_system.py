from __future__ import annotations

"""EFSFileSystem - AWS::EFS::FileSystem resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystemElasticFileSystemTag:
    resource: ElasticFileSystemTag
    key = 'Name'
    value = ref(EFSFileSystemName)


@cloudformation_dataclass
class EFSFileSystem:
    """AWS::EFS::FileSystem resource."""

    resource: FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
    file_system_tags = [EFSFileSystemElasticFileSystemTag]
