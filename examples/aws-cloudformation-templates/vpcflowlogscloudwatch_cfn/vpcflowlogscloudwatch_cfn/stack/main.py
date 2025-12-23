"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    retention_in_days = ref(VPCFlowLogsLogGroupRetention)
    kms_key_id = If("VPCFlowLogsCloudWatchKMSKeyCondition", ref(VPCFlowLogsCloudWatchKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class VPCFlowLogsRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['vpc-flow-logs.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class VPCFlowLogsRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [VPCFlowLogsRoleAllowStatement0]


@cloudformation_dataclass
class VPCFlowLogsRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CloudWatchLogs'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogGroups',
        'logs:DescribeLogStreams',
    ]
    resource_arn = get_att(VPCFlowLogsLogGroup, "Arn")


@cloudformation_dataclass
class VPCFlowLogsRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [VPCFlowLogsRoleAllowStatement0_1]


@cloudformation_dataclass
class VPCFlowLogsRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = VPCFlowLogsRolePolicies0PolicyDocument


@cloudformation_dataclass
class VPCFlowLogsRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    description = 'Rights to Publish VPC Flow Logs to CloudWatch Logs'
    assume_role_policy_document = VPCFlowLogsRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [VPCFlowLogsRolePolicy]


@cloudformation_dataclass
class VPCFlowLogsToCloudWatchAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'VPC Flow Logs CloudWatch'


@cloudformation_dataclass
class VPCFlowLogsToCloudWatch:
    """AWS::EC2::FlowLog resource."""

    resource: ec2.FlowLog
    log_destination_type = 'cloud-watch-logs'
    log_group_name = ref(VPCFlowLogsLogGroup)
    deliver_logs_permission_arn = get_att(VPCFlowLogsRole, "Arn")
    log_format = ref(VPCFlowLogsLogFormat)
    max_aggregation_interval = ref(VPCFlowLogsMaxAggregationInterval)
    resource_id = ref(VPCID)
    resource_type = 'VPC'
    traffic_type = ref(VPCFlowLogsTrafficType)
    tags = [VPCFlowLogsToCloudWatchAssociationParameter]
