"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudwatch
from cloudformation_dataclasses.intrinsics import Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .monitoring import CloudWatchDashboard as CloudWatchDashboard
from .outputs import DashboardArnOutput as DashboardArnOutput
from .params import LogGroupName as LogGroupName
from .params import NatGatewayID as NatGatewayID
from .params import NatGatewayPrivateIP as NatGatewayPrivateIP
from .params import VpcCidr as VpcCidr

__all__: list[str] = ['CloudWatchDashboard', 'DashboardArnOutput', 'LogGroupName', 'NatGatewayID', 'NatGatewayPrivateIP', 'Output', 'Parameter', 'STRING', 'Sub', 'Template', 'VpcCidr', 'cloudformation_dataclass', 'cloudwatch', 'get_att', 'ref', 'setup_resources']
