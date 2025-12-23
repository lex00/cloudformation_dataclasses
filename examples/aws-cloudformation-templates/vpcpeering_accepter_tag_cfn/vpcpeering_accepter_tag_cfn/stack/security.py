"""Security resources: TagVpcPeeringConnectionsLambdaRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}:log-stream:*')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1, TagVpcPeeringConnectionsLambdaRoleAllowStatement1]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'Tagging'
    action = [
        'ec2:CreateTags',
        'ec2:DeleteTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:vpc-peering-connection/*')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'TagVpcPeeringConnections'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = 'Rights to Tag VPC Peering Connection'
    assume_role_policy_document = TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [TagVpcPeeringConnectionsLambdaRolePolicy, TagVpcPeeringConnectionsLambdaRolePolicy1]
