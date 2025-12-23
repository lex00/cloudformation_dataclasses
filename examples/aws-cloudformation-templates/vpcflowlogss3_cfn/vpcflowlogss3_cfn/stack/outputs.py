"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsBucketOutput:
    """S3 bucket name where VPC Flow Log data will be published"""

    resource: Output
    value = If("VPCFlowLogsNewBucketCondition", ref(VPCFlowLogsBucket), ref(VPCFlowLogsBucketName))
    description = 'S3 bucket name where VPC Flow Log data will be published'
