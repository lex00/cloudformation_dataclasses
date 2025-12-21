"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AdministratorAccessIAMRoleOutput:
    """Administrator Access IAM Role"""

    resource: Output
    value = ref("AdministratorAccessIAMRole")
    description = 'Administrator Access IAM Role'
    export_name = Sub('${AppName}-iam-${Environment}-administrator-access-role')


@cloudformation_dataclass
class LoggingBucketOutput:
    """Name of S3 Logging bucket"""

    resource: Output
    value = ref("LoggingBucket")
    description = 'Name of S3 Logging bucket'
    export_name = ref("LoggingBucket")


@cloudformation_dataclass
class LoggingBucketKMSKeyOutput:
    """Logging Bucket KMS Key"""

    resource: Output
    value = ref("LoggingBucketKMSKey")
    description = 'Logging Bucket KMS Key'
    export_name = Sub('${AppName}-${Environment}-s3-logging-kms')


@cloudformation_dataclass
class OriginALBOutput:
    """The URL of the Origin ALB"""

    resource: Output
    value = get_att("OriginALB", "DNSName")
    description = 'The URL of the Origin ALB'
    export_name = Sub('${AppName}-${Environment}-origin-alb-dns')


@cloudformation_dataclass
class ALBExternalAccessSGIDOutput:
    """ALB External Access Security Group ID"""

    resource: Output
    value = ref("ALBExternalAccessSG")
    description = 'ALB External Access Security Group ID'
    export_name = Sub('${AppName}-${Environment}-alb-external-access-ingrees-sg')


@cloudformation_dataclass
class EC2InstanceSGIDOutput:
    """EC2 Instance Security Group ID"""

    resource: Output
    value = ref("EC2InstanceSG")
    description = 'EC2 Instance Security Group ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-sg')


@cloudformation_dataclass
class EC2InstanceDNSOutput:
    """EC2 Instance DNS Name"""

    resource: Output
    value = get_att("EC2Instance", "PrivateDnsName")
    description = 'EC2 Instance DNS Name'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-dns')


@cloudformation_dataclass
class EC2InstanceIPOutput:
    """EC2 Instance IP Address"""

    resource: Output
    value = get_att("EC2Instance", "PrivateIp")
    description = 'EC2 Instance IP Address'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-ip-address')


@cloudformation_dataclass
class EC2InstanceIDOutput:
    """EC2 Instance Instance ID"""

    resource: Output
    value = ref("EC2Instance")
    description = 'EC2 Instance Instance ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-id')


@cloudformation_dataclass
class CloudFrontEndpointOutput:
    """Endpoint for Cloudfront Distribution"""

    resource: Output
    value = ref("CloudFrontDistribution")
    description = 'Endpoint for Cloudfront Distribution'
    export_name = Sub('${AppName}-${Environment}-cloudfront-distribution')


@cloudformation_dataclass
class AlternateDomainNamesOutput:
    """Alternate Domain Names (CNAME)"""

    resource: Output
    value = ref(AlternateDomainNames)
    description = 'Alternate Domain Names (CNAME)'


@cloudformation_dataclass
class LambdaEdgeFunctionOutput:
    """The Name of the Lambda@Edge Function"""

    resource: Output
    value = 'LambdaEdgeFunction'
    description = 'The Name of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-3')


@cloudformation_dataclass
class LambdaEdgeFunctionARNOutput:
    """The ARN of the Lambda@Edge Function"""

    resource: Output
    value = get_att("LambdaEdgeFunction", "Arn")
    description = 'The ARN of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-arn-3')


@cloudformation_dataclass
class LambdaEdgeVersionOutput:
    """Lambda@Edge Version Function"""

    resource: Output
    value = get_att("LambdaEdgeVersion", "Version")
    description = 'Lambda@Edge Version Function'
