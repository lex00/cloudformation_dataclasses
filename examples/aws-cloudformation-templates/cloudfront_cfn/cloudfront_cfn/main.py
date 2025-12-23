"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import ACMCertificateIdentifier, ALBAttributeDeletionProtection, ALBAttributeIdleTimeOut, ALBAttributeRoutingHttp2, ALBScheme, ALBTargetGroupAttributeDeregistration, ALBTargetGroupHealthCheckIntervalSeconds, ALBTargetGroupHealthCheckTimeoutSeconds, ALBTargetGroupHealthyThresholdCount, ALBTargetGroupUnhealthyThresholdCount, ALBType, AlternateDomainNames, AppName, BootVolSize, BootVolType, Compress, DefaultTTL, EC2ImageId, EC2InstanceType, Environment, ForwardCookies, HealthCheckPath, HealthCheckProtocol, IPV6Enabled, KeyPairName, LambdaEventType, LoggingBucketVersioning, MaxTTL, MinTTL, MinimumProtocolVersion, OriginALBTGPort, OriginKeepaliveTimeout, OriginProtocolPolicy, OriginReadTimeout, PriceClass, PublicSubnetId1, PublicSubnetId2, QueryString, SslSupportMethod, ViewerProtocolPolicy, VpcId
from .outputs import ALBExternalAccessSGIDOutput, AdministratorAccessIAMRoleOutput, AlternateDomainNamesOutput, CloudFrontEndpointOutput, EC2InstanceDNSOutput, EC2InstanceIDOutput, EC2InstanceIPOutput, EC2InstanceSGIDOutput, LambdaEdgeFunctionARNOutput, LambdaEdgeFunctionOutput, LambdaEdgeVersionOutput, LoggingBucketKMSKeyOutput, LoggingBucketOutput, OriginALBOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='CI/CD optimized AWS CloudFormation Sample Template for AWS CloudFront Distribution with Custom Origin with an example of using the AWS Application Load Balancer (ALB) and a basic Amazon EC2 Instance. AWS CloudFront Distribution is associated with Lambda@Edge for Security Headers inspection. In addition, AWS CloudFormation Template will provision an Examples of necessary IAM, S3, KMS and Security Groups resources. ### Before deployment please make sure that all parameters are reviewed and updated according the specific use case. ### **WARNING** This template creates one Amazon EC2 instance and an Application Load Balancer, KMS Keys, S3 bucket, CloudFront Distribution resources. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[Environment, VpcId, PublicSubnetId1, PublicSubnetId2, AppName, AlternateDomainNames, ACMCertificateIdentifier, LambdaEventType, IPV6Enabled, EC2ImageId, EC2InstanceType, KeyPairName, BootVolSize, BootVolType, ALBType, OriginALBTGPort, OriginProtocolPolicy, Compress, DefaultTTL, MaxTTL, MinTTL, QueryString, ForwardCookies, ViewerProtocolPolicy, PriceClass, SslSupportMethod, MinimumProtocolVersion, OriginKeepaliveTimeout, OriginReadTimeout, ALBScheme, ALBTargetGroupHealthCheckIntervalSeconds, ALBTargetGroupHealthCheckTimeoutSeconds, ALBTargetGroupHealthyThresholdCount, ALBTargetGroupUnhealthyThresholdCount, ALBAttributeIdleTimeOut, ALBAttributeDeletionProtection, ALBAttributeRoutingHttp2, ALBTargetGroupAttributeDeregistration, HealthCheckProtocol, HealthCheckPath, LoggingBucketVersioning],
        outputs=[AdministratorAccessIAMRoleOutput, LoggingBucketOutput, LoggingBucketKMSKeyOutput, OriginALBOutput, ALBExternalAccessSGIDOutput, EC2InstanceSGIDOutput, EC2InstanceDNSOutput, EC2InstanceIPOutput, EC2InstanceIDOutput, CloudFrontEndpointOutput, AlternateDomainNamesOutput, LambdaEdgeFunctionOutput, LambdaEdgeFunctionARNOutput, LambdaEdgeVersionOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
