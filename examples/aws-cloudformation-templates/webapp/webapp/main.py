"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.s3 import BucketVersioningStatus


@cloudformation_dataclass
class TestResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class TestResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerRoleAllowStatement0]


@cloudformation_dataclass
class TestResourceHandlerRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = TestResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']


@cloudformation_dataclass
class TestResourceHandlerPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        'dynamodb:BatchGetItem',
        'dynamodb:GetItem',
        'dynamodb:Query',
        'dynamodb:Scan',
        'dynamodb:BatchWriteItem',
        'dynamodb:PutItem',
        'dynamodb:UpdateItem',
    ]
    resource_arn = [get_att(TestTable, "Arn")]


@cloudformation_dataclass
class TestResourceHandlerPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerPolicyAllowStatement0]


@cloudformation_dataclass
class TestResourceHandlerPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = TestResourceHandlerPolicyPolicyDocument
    policy_name = 'handler-policy'
    role_name = ref(TestResourceHandlerRole)


@cloudformation_dataclass
class SiteOriginAccessControlOriginAccessControlConfig:
    resource: cloudfront.origin_access_control.OriginAccessControlConfig
    name = Join('', [
    ref(AppName),
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


@cloudformation_dataclass
class SiteOriginAccessControl:
    """AWS::CloudFront::OriginAccessControl resource."""

    resource: cloudfront.OriginAccessControl
    origin_access_control_config = SiteOriginAccessControlOriginAccessControlConfig


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = SiteCloudFrontLogsLogBucketDefaultRetention


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteCloudFrontLogsLogBucketObjectLockRule


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationRoleAllowStatement0]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(SiteCloudFrontLogsLogBucket)


@cloudformation_dataclass
class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(SiteCloudFrontLogsReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(SiteCloudFrontLogsReplicationRole, "Arn")
    rules = [SiteCloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControlsRule:
    resource: s3.bucket.OwnershipControlsRule
    object_ownership = 'BucketOwnerPreferred'


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControls:
    resource: s3.bucket.OwnershipControls
    rules = [SiteCloudFrontLogsBucketOwnershipControlsRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketDeleteMarkerReplication
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteContentLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = SiteContentLogBucketDefaultRetention


@cloudformation_dataclass
class SiteContentLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteContentLogBucketObjectLockRule


@cloudformation_dataclass
class SiteContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteContentLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteContentReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class SiteContentReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicationRoleAllowStatement0]


@cloudformation_dataclass
class SiteContentReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = SiteContentReplicationRoleAssumeRolePolicyDocument
    path = '/'


@cloudformation_dataclass
class SiteContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteContentReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(SiteContentLogBucket)


@cloudformation_dataclass
class SiteContentBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(SiteContentReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteContentBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = SiteContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteContentBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(SiteContentReplicationRole, "Arn")
    rules = [SiteContentBucketReplicationRule]


@cloudformation_dataclass
class SiteContentBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteContentBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteWebACLAllowAction:
    resource: wafv2.web_acl.AllowAction


@cloudformation_dataclass
class SiteWebACLDefaultAction:
    resource: wafv2.web_acl.DefaultAction
    allow = SiteWebACLAllowAction


@cloudformation_dataclass
class SiteWebACLVisibilityConfig:
    resource: wafv2.web_acl.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForWebACLWithAMR'


@cloudformation_dataclass
class SiteWebACLOverrideAction:
    resource: wafv2.web_acl.OverrideAction
    none = {}


@cloudformation_dataclass
class SiteWebACLVisibilityConfig1:
    resource: wafv2.web_acl.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForAMRCRS'


@cloudformation_dataclass
class SiteWebACLExcludedRule:
    resource: wafv2.web_acl.ExcludedRule
    name = 'NoUserAgent_HEADER'


@cloudformation_dataclass
class SiteWebACLManagedRuleGroupStatement:
    resource: wafv2.web_acl.ManagedRuleGroupStatement
    vendor_name = 'AWS'
    name = 'AWSManagedRulesCommonRuleSet'
    excluded_rules = [SiteWebACLExcludedRule]


@cloudformation_dataclass
class SiteWebACLStatement:
    resource: wafv2.web_acl.Statement
    managed_rule_group_statement = SiteWebACLManagedRuleGroupStatement


@cloudformation_dataclass
class SiteWebACLRule:
    resource: wafv2.web_acl.Rule
    name = 'AWS-AWSManagedRulesCommonRuleSet'
    priority = 0
    override_action = SiteWebACLOverrideAction
    visibility_config = SiteWebACLVisibilityConfig1
    statement = SiteWebACLStatement


@cloudformation_dataclass
class SiteWebACL:
    """AWS::WAFv2::WebACL resource."""

    resource: wafv2.WebACL
    name = Sub('${AppName}-WebACLWithAMR')
    scope = 'CLOUDFRONT'
    description = 'Web ACL with AWS Managed Rules'
    default_action = SiteWebACLDefaultAction
    visibility_config = SiteWebACLVisibilityConfig
    tags = [{
        'Key': 'Name',
        'Value': ref(AppName),
    }]
    rules = [SiteWebACLRule]


@cloudformation_dataclass
class SiteDistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    cache_policy_id = '658327ea-f89d-4fab-a63d-7e88639e58f6'
    compress = True
    target_origin_id = Sub('${AppName}-origin-1')
    viewer_protocol_policy = 'redirect-to-https'


@cloudformation_dataclass
class SiteDistributionLogging:
    resource: cloudfront.distribution.Logging
    bucket = get_att(SiteCloudFrontLogsBucket, "RegionalDomainName")


@cloudformation_dataclass
class SiteDistributionS3OriginConfig:
    resource: cloudfront.distribution.S3OriginConfig
    origin_access_identity = ''


@cloudformation_dataclass
class SiteDistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = get_att(SiteContentBucket, "RegionalDomainName")
    id = Sub('${AppName}-origin-1')
    origin_access_control_id = get_att(SiteOriginAccessControl, "Id")
    s3_origin_config = SiteDistributionS3OriginConfig


@cloudformation_dataclass
class SiteDistributionViewerCertificate:
    resource: cloudfront.distribution.ViewerCertificate
    cloud_front_default_certificate = True


@cloudformation_dataclass
class SiteDistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    default_cache_behavior = SiteDistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = SiteDistributionLogging
    origins = [SiteDistributionOrigin]
    viewer_certificate = SiteDistributionViewerCertificate
    web_acl_id = get_att(SiteWebACL, "Arn")


@cloudformation_dataclass
class SiteDistribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    distribution_config = SiteDistributionDistributionConfig


@cloudformation_dataclass
class SiteContentReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class SiteContentReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteContentReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteContentReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicationPolicyAllowStatement0, SiteContentReplicationPolicyAllowStatement1, SiteContentReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class SiteContentReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = SiteContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(SiteContentReplicationRole)


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentLogBucketAccessPolicyDenyStatement0, SiteContentLogBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentLogBucket)
    policy_document = SiteContentLogBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')
    condition = {
        STRING_EQUALS: {
            'AWS:SourceArn': Sub('arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SiteDistribution.Id}'),
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement2:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


@cloudformation_dataclass
class SiteContentBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentBucket)
    policy_document = SiteContentBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicaBucketAccessPolicyDenyStatement0, SiteContentReplicaBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentReplicaBucket)
    policy_document = SiteContentReplicaBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationPolicyAllowStatement0, SiteCloudFrontLogsReplicationPolicyAllowStatement1, SiteCloudFrontLogsReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = SiteCloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(SiteCloudFrontLogsReplicationRole)


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsLogBucket)
    policy_document = SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsBucket)
    policy_document = SiteCloudFrontLogsBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsReplicaBucket)
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class CognitoUserPoolAdminCreateUserConfig:
    resource: cognito.user_pool.AdminCreateUserConfig
    allow_admin_create_user_only = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute:
    resource: cognito.user_pool.SchemaAttribute
    name = 'email'
    required = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute1:
    resource: cognito.user_pool.SchemaAttribute
    name = 'given_name'
    required = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute2:
    resource: cognito.user_pool.SchemaAttribute
    name = 'family_name'
    required = True


@cloudformation_dataclass
class CognitoUserPool:
    """AWS::Cognito::UserPool resource."""

    resource: cognito.UserPool
    user_pool_name = ref(AppName)
    admin_create_user_config = CognitoUserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    schema = [CognitoUserPoolSchemaAttribute, CognitoUserPoolSchemaAttribute1, CognitoUserPoolSchemaAttribute2]
    depends_on = [SiteDistribution]


@cloudformation_dataclass
class CognitoDomain:
    """AWS::Cognito::UserPoolDomain resource."""

    resource: cognito.UserPoolDomain
    domain = ref(AppName)
    user_pool_id = ref(CognitoUserPool)


@cloudformation_dataclass
class CognitoClient:
    """AWS::Cognito::UserPoolClient resource."""

    resource: cognito.UserPoolClient
    client_name = ref(AppName)
    generate_secret = False
    user_pool_id = ref(CognitoUserPool)
    callback_ur_ls = [Sub('https://${SiteDistribution.DomainName}/index.html')]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']


@cloudformation_dataclass
class TestResourceHandlerContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaCodeS3Bucket)
    s3_key = ref(LambdaCodeS3Key)


@cloudformation_dataclass
class TestResourceHandlerEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'TABLE_NAME': ref(TestTable),
    }


@cloudformation_dataclass
class TestResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-test-handler')
    runtime = 'provided.al2023'
    code = TestResourceHandlerContent
    role = get_att(TestResourceHandlerRole, "Arn")
    environment = TestResourceHandlerEnvironment


@cloudformation_dataclass
class RestApi:
    """AWS::ApiGateway::RestApi resource."""

    resource: apigateway.RestApi
    name = ref(AppName)


@cloudformation_dataclass
class TestResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = ref(RestApi)


@cloudformation_dataclass
class TestResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TestResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')


@cloudformation_dataclass
class TestResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TestResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')


@cloudformation_dataclass
class TestResourceOptionsIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = ref(TestResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration


@cloudformation_dataclass
class RestApiAuthorizer:
    """AWS::ApiGateway::Authorizer resource."""

    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [get_att(CognitoUserPool, "Arn")]
    rest_api_id = ref(RestApi)
    type_ = 'COGNITO_USER_POOLS'


@cloudformation_dataclass
class TestResourceGetIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'GET'
    resource_id = ref(TestResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id = ref(RestApiAuthorizer)
    integration = TestResourceGetIntegration


@cloudformation_dataclass
class JwtResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class JwtResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [JwtResourceHandlerRoleAllowStatement0]


@cloudformation_dataclass
class JwtResourceHandlerRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = JwtResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']


@cloudformation_dataclass
class JwtResourceHandlerContent:
    resource: lambda_.layer_version.Content
    s3_bucket = 'rain-artifacts-207567786752-us-east-1'
    s3_key = '15d7c92b571beed29cf6c012a96022482eee1df1b477ad528ddc03a4be52c076'


@cloudformation_dataclass
class JwtResourceHandlerEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'COGNITO_REGION': 'us-east-1',
        'COGNITO_POOL_ID': ref(CognitoUserPool),
        'COGNITO_REDIRECT_URI': Sub('https://${SiteDistribution.DomainName}/index.html'),
        'COGNITO_DOMAIN_PREFIX': ref(AppName),
        'COGNITO_APP_CLIENT_ID': ref(CognitoClient),
    }


@cloudformation_dataclass
class JwtResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-jwt-handler')
    runtime = 'provided.al2023'
    code = JwtResourceHandlerContent
    role = get_att(JwtResourceHandlerRole, "Arn")
    environment = JwtResourceHandlerEnvironment


@cloudformation_dataclass
class JwtResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = ref(RestApi)


@cloudformation_dataclass
class JwtResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(JwtResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')


@cloudformation_dataclass
class JwtResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(JwtResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')


@cloudformation_dataclass
class JwtResourceOptionsIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class JwtResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = ref(JwtResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    integration = JwtResourceOptionsIntegration


@cloudformation_dataclass
class JwtResourceGetIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class JwtResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'GET'
    resource_id = ref(JwtResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration


@cloudformation_dataclass
class RestApiDeployment:
    """AWS::ApiGateway::Deployment resource."""

    resource: apigateway.Deployment
    rest_api_id = ref(RestApi)
    depends_on = [TestResourceGet, TestResourceOptions, JwtResourceGet, JwtResourceOptions]


@cloudformation_dataclass
class RestApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: apigateway.Stage
    rest_api_id = ref(RestApi)
    deployment_id = ref(RestApiDeployment)
    stage_name = 'prod'
