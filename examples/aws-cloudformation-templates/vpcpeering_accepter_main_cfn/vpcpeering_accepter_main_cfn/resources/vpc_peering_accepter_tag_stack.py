"""VPCPeeringAccepterTagStack - AWS::CloudFormation::Stack resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCPeeringAccepterTagStack:
    """AWS::CloudFormation::Stack resource."""

    resource: cloudformation.Stack
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Accepter-Tag.cfn.yaml', {
    'S3Bucket': ref(TemplatesS3BucketName),
    'S3KeyPrefix': ref(TemplatesS3KeyPrefix),
    'S3Region': ref(TemplatesS3BucketRegion),
})
    parameters = {
        'LambdaFunctionName': ref(LambdaFunctionName),
        'LambdaLogLevel': ref(LambdaLogLevel),
        'LambdaLogsCloudWatchKMSKey': ref(LambdaLogsCloudWatchKMSKey),
        'LambdaLogsLogGroupRetention': ref(LambdaLogsLogGroupRetention),
        'LambdaRoleName': ref(LambdaRoleName),
        'PeerName': ref(PeerName),
        'VPCPeeringConnectionId': ref(VPCPeeringConnectionId),
    }
