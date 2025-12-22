from __future__ import annotations

"""VPCPeeringUpdatesStack - AWS::CloudFormation::Stack resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCPeeringUpdatesStack:
    """AWS::CloudFormation::Stack resource."""

    resource: Stack
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Updates.cfn.yaml', {
    'S3Bucket': ref(TemplatesS3BucketName),
    'S3KeyPrefix': ref(TemplatesS3KeyPrefix),
    'S3Region': ref(TemplatesS3BucketRegion),
})
    parameters = {
        'NumberOfRouteTables': ref(NumberOfRouteTables),
        'NumberOfSecurityGroups': ref(NumberOfSecurityGroups),
        'PeerName': ref(PeerName),
        'PeerVPCCIDR': ref(PeerVPCCIDR),
        'RouteTableIds': ref(RouteTableIds),
        'SecurityGroupIds': Join(',', ref(SecurityGroupIds)),
        'VPCPeeringConnectionId': get_att(VPCPeeringRequesterSetupStack, "Outputs.VPCPeeringConnectionId"),
    }
