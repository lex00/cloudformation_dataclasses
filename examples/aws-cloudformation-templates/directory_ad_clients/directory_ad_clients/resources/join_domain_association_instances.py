"""JoinDomainAssociationInstances - AWS::SSM::Association resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JoinDomainAssociationInstancesInstanceAssociationOutputLocation:
    resource: ssm.association.InstanceAssociationOutputLocation
    s3_location = If("SSMLogsBucketCondition", {
    S3OutputLocation.output_s3_bucket_name: ref(SSMLogsBucketName),
    S3OutputLocation.output_s3_key_prefix: Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


@cloudformation_dataclass
class JoinDomainAssociationInstancesTarget:
    resource: ssm.maintenance_window_task.Target
    key = 'InstanceIds'
    values = [ref(DomainMember2WithSsmAssociationInstance), ref(DomainMember4LinuxWithSsmAssociationInstance)]


@cloudformation_dataclass
class JoinDomainAssociationInstances:
    """AWS::SSM::Association resource."""

    resource: ssm.Association
    association_name = Sub('JoinDomain-Association-viaInstances-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationInstancesInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationInstancesTarget]
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
