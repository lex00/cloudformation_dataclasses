"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DashboardArnOutput:
    """ARN of the created CloudWatch Dashboard"""

    resource: Output
    value = ref(CloudWatchDashboard)
    description = 'ARN of the created CloudWatch Dashboard'
