"""Security resources: TestResourceHandlerRole, TestResourceHandlerPolicy, SiteCloudFrontLogsReplicationRole, SiteContentReplicationRole, SiteWebACL, SiteContentReplicationPolicy, SiteCloudFrontLogsReplicationPolicy, CognitoUserPool, CognitoDomain, CognitoClient, JwtResourceHandlerRole."""

from .. import *  # noqa: F403


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
    depends_on = ["SiteDistribution"]


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
