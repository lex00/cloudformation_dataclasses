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
from cloudformation_dataclasses.aws import cloudwatch, logs
from cloudformation_dataclasses.intrinsics import Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .monitoring import ADSAMLAuthDistinctUsers as ADSAMLAuthDistinctUsers
from .monitoring import ADSAMLAuthDistinctUsersConnectionDuration as ADSAMLAuthDistinctUsersConnectionDuration
from .monitoring import ADSAMLAuthTotalUsageReport as ADSAMLAuthTotalUsageReport
from .monitoring import ADSAMLAuthUsersConnectionDuration as ADSAMLAuthUsersConnectionDuration
from .monitoring import Dashboard as Dashboard
from .monitoring import MixAuthDistinctUsers as MixAuthDistinctUsers
from .monitoring import MixAuthDistinctUsersConnectionDuration as MixAuthDistinctUsersConnectionDuration
from .monitoring import MixAuthTotalUsageReport as MixAuthTotalUsageReport
from .monitoring import MixAuthUsersConnectionDuration as MixAuthUsersConnectionDuration
from .monitoring import MutualAuthDistinctUsers as MutualAuthDistinctUsers
from .monitoring import MutualAuthDistinctUsersConnectionDuration as MutualAuthDistinctUsersConnectionDuration
from .monitoring import MutualAuthTotalUsageReport as MutualAuthTotalUsageReport
from .monitoring import MutualAuthUsersConnectionDuration as MutualAuthUsersConnectionDuration
from .monitoring import TotalUsagePerClientVPNEndpoint as TotalUsagePerClientVPNEndpoint
from .outputs import DashboardUrlOutput as DashboardUrlOutput
from .outputs import LogInsightsUrlOutput as LogInsightsUrlOutput
from .params import ClientVPNLogGroup as ClientVPNLogGroup
from .params import Folder as Folder

__all__: list[str] = ['ADSAMLAuthDistinctUsers', 'ADSAMLAuthDistinctUsersConnectionDuration', 'ADSAMLAuthTotalUsageReport', 'ADSAMLAuthUsersConnectionDuration', 'ClientVPNLogGroup', 'Dashboard', 'DashboardUrlOutput', 'Folder', 'LogInsightsUrlOutput', 'MixAuthDistinctUsers', 'MixAuthDistinctUsersConnectionDuration', 'MixAuthTotalUsageReport', 'MixAuthUsersConnectionDuration', 'MutualAuthDistinctUsers', 'MutualAuthDistinctUsersConnectionDuration', 'MutualAuthTotalUsageReport', 'MutualAuthUsersConnectionDuration', 'Output', 'Parameter', 'STRING', 'Sub', 'Template', 'TotalUsagePerClientVPNEndpoint', 'cloudformation_dataclass', 'cloudwatch', 'get_att', 'logs', 'ref', 'setup_resources']
