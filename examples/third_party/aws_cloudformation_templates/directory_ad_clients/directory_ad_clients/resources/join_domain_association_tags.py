"""JoinDomainAssociationTags - AWS::SSM::Association resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JoinDomainAssociationTagsInstanceAssociationOutputLocation:
    resource: InstanceAssociationOutputLocation
    s3_location = If("SSMLogsBucketCondition", {
    S3OutputLocation.output_s3_bucket_name: ref(SSMLogsBucketName),
    S3OutputLocation.output_s3_key_prefix: Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


@cloudformation_dataclass
class JoinDomainAssociationTagsTarget:
    resource: Target
    key = 'tag:DomainJoin'
    values = [ref(DirectoryName)]


@cloudformation_dataclass
class JoinDomainAssociationTags:
    """AWS::SSM::Association resource."""

    resource: Association
    association_name = Sub('JoinDomain-Association-viaTags-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationTagsInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationTagsTarget]
    parameters = {
        'directoryId': [ref(DirectoryID)],
        'directoryName': [ref(DirectoryName)],
        'dnsIpAddresses': If("DomainDNSServersCondition", [
    If("DomainDNSServer1Condition", ref(DomainDNSServer1), AWS_NO_VALUE),
    If("DomainDNSServer2Condition", ref(DomainDNSServer2), AWS_NO_VALUE),
    If("DomainDNSServer3Condition", ref(DomainDNSServer3), AWS_NO_VALUE),
    If("DomainDNSServer4Condition", ref(DomainDNSServer4), AWS_NO_VALUE),
], AWS_NO_VALUE),
    }
