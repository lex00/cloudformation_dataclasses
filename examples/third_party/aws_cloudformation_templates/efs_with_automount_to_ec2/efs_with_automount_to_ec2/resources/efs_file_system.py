from __future__ import annotations

"""EFSFileSystem - AWS::EFS::FileSystem resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystem:
    """AWS::EFS::FileSystem resource."""

    resource: FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
