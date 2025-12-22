"""VPCPeeringRequesterSetupStack - AWS::CloudFormation::Stack resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCPeeringRequesterSetupStack:
    """AWS::CloudFormation::Stack resource."""

    resource: cloudformation.Stack
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Requester-Setup.cfn.yaml', {
    'S3Bucket': ref(TemplatesS3BucketName),
    'S3KeyPrefix': ref(TemplatesS3KeyPrefix),
    'S3Region': ref(TemplatesS3BucketRegion),
})
    parameters = {
        'PeerName': ref(PeerName),
        'PeerOwnerId': ref(PeerOwnerId),
        'PeerRoleARN': ref(PeerRoleARN),
        'PeerVPCID': ref(PeerVPCID),
        'VPCID': ref(VPCID),
    }
