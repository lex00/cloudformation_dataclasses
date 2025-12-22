from __future__ import annotations

"""EFSAccessPoint - AWS::EFS::AccessPoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSAccessPointAccessPointTag:
    resource: AccessPointTag
    key = 'Name'
    value = ref(AccessPointName)


@cloudformation_dataclass
class EFSAccessPoint:
    """AWS::EFS::AccessPoint resource."""

    resource: AccessPoint
    file_system_id = ref(EFSFileSystem)
    access_point_tags = [EFSAccessPointAccessPointTag]
