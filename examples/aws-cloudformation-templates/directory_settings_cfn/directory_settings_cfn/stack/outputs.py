"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryAliasUrlOutput:
    """Directory Alias"""

    resource: Output
    value = get_att(DirectorySettingsResource, "AliasUrl")
    description = 'Directory Alias'
