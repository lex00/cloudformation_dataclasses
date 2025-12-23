"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FileSystemIdOutput:
    """ID of the created EFS File System"""

    resource: Output
    value = ref(EFSFileSystem)
    description = 'ID of the created EFS File System'
