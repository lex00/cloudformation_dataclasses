"""VPCFlowLogsS3Stack - AWS::CloudFormation::Stack resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsS3Stack:
    """AWS::CloudFormation::Stack resource."""

    resource: cloudformation.Stack
    template_url = Sub('https://${TemplatesS3BucketName}.s3.${TemplatesS3BucketRegion}.${AWS::URLSuffix}/templates/VPCFlowLogsS3.cfn.yaml')
    parameters = {
        'S3AccessLogsBucketName': ref(S3AccessLogsBucketName),
        'VPCFlowLogsBucketKeyEnabled': ref(VPCFlowLogsBucketKeyEnabled),
        'VPCFlowLogsBucketKMSKey': ref(VPCFlowLogsBucketKMSKey),
        'VPCFlowLogsBucketName': ref(VPCFlowLogsBucketName),
        'VPCFlowLogsLogFormat': ref(VPCFlowLogsLogFormat),
        'VPCFlowLogsMaxAggregationInterval': ref(VPCFlowLogsMaxAggregationInterval),
        'VPCFlowLogsTrafficType': ref(VPCFlowLogsTrafficType),
        'VPCID': ref(VPCID),
    }
    condition = 'VPCFlowLogsToS3Condition'
