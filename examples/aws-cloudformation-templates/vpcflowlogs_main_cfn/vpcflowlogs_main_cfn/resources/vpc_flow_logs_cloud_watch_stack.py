"""VPCFlowLogsCloudWatchStack - AWS::CloudFormation::Stack resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsCloudWatchStack:
    """AWS::CloudFormation::Stack resource."""

    resource: cloudformation.Stack
    template_url = Sub('https://${TemplatesS3BucketName}.s3.${TemplatesS3BucketRegion}.${AWS::URLSuffix}/templates/VPCFlowLogsCloudWatch.cfn.yaml')
    parameters = {
        'VPCFlowLogsCloudWatchKMSKey': ref(VPCFlowLogsCloudWatchKMSKey),
        'VPCFlowLogsLogFormat': ref(VPCFlowLogsLogFormat),
        'VPCFlowLogsLogGroupRetention': ref(VPCFlowLogsLogGroupRetention),
        'VPCFlowLogsMaxAggregationInterval': ref(VPCFlowLogsMaxAggregationInterval),
        'VPCFlowLogsTrafficType': ref(VPCFlowLogsTrafficType),
        'VPCID': ref(VPCID),
    }
    condition = 'VPCFlowLogsToCloudWatchCondition'
