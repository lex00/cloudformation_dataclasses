"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation
from cloudformation_dataclasses.intrinsics import Join, Sub

from .infra import VPCPeeringRequesterSetupStack as VPCPeeringRequesterSetupStack
from .infra import VPCPeeringUpdatesStack as VPCPeeringUpdatesStack
from .params import NumberOfRouteTables as NumberOfRouteTables
from .params import NumberOfSecurityGroups as NumberOfSecurityGroups
from .params import PeerName as PeerName
from .params import PeerOwnerId as PeerOwnerId
from .params import PeerRoleARN as PeerRoleARN
from .params import PeerVPCCIDR as PeerVPCCIDR
from .params import PeerVPCID as PeerVPCID
from .params import RouteTableIds as RouteTableIds
from .params import SecurityGroupIds as SecurityGroupIds
from .params import TemplatesS3BucketName as TemplatesS3BucketName
from .params import TemplatesS3BucketRegion as TemplatesS3BucketRegion
from .params import TemplatesS3KeyPrefix as TemplatesS3KeyPrefix
from .params import VPCID as VPCID

__all__: list[str] = ['Join', 'NumberOfRouteTables', 'NumberOfSecurityGroups', 'Parameter', 'ParameterType', 'PeerName', 'PeerOwnerId', 'PeerRoleARN', 'PeerVPCCIDR', 'PeerVPCID', 'RouteTableIds', 'STRING', 'SecurityGroupIds', 'Sub', 'Template', 'TemplatesS3BucketName', 'TemplatesS3BucketRegion', 'TemplatesS3KeyPrefix', 'VPCID', 'VPCPeeringRequesterSetupStack', 'VPCPeeringUpdatesStack', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
