"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CertificateURLOutput:
    """Go to this URL to check certificate issued or not (also find domain verification details)"""

    resource: Output
    value = Sub('https://${AWS::Region}.console.aws.amazon.com/acm/home?region=${AWS::Region}#/certificates/${CertificateId}', {
    'CertificateId': Select(1, Split('/', ref(ASCPrivateLinkCertificate))),
})
    description = 'Go to this URL to check certificate issued or not (also find domain verification details)'


@cloudformation_dataclass
class VPCEndpointServiceURLOutput:
    """Go to this URL to check VPC Endpoint Service attributes (also find privateDNS domain verification details)"""

    resource: Output
    value = Sub('https://${AWS::Region}.console.aws.amazon.com/vpc/home?region=${AWS::Region}#VpcEndpointServiceDetails:EndpointServiceId=${ASCPrivateLinkVPCES}')
    description = 'Go to this URL to check VPC Endpoint Service attributes (also find privateDNS domain verification details)'


@cloudformation_dataclass
class TargetGroupURLOutput:
    """Go to this URL to check target group health check status (to see if got connectivity to SAP)"""

    resource: Output
    value = Sub('https://${AWS::Region}.console.aws.amazon.com/ec2/home?region=${AWS::Region}#TargetGroup:targetGroupArn=${ASCPrivateLinkTargetGroup}')
    description = 'Go to this URL to check target group health check status (to see if got connectivity to SAP)'
