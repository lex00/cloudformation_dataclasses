"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsLogGroupOutput:
    """CloudWatch Log Group where VPC Flow Log data will be published"""

    resource: Output
    value = ref("VPCFlowLogsLogGroup")
    description = 'CloudWatch Log Group where VPC Flow Log data will be published'
