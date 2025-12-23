"""EFSAccessPoint - AWS::EFS::AccessPoint resource."""

from .. import *  # noqa: F403


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
