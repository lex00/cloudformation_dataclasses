"""IoTPolicy - AWS::IoT::Policy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTPolicyAllowStatement0:
    resource: PolicyStatement
    action = 'iot:Connect'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:client/*')]


@cloudformation_dataclass
class IoTPolicyAllowStatement1:
    resource: PolicyStatement
    action = 'iot:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/${AWS::StackName}'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_1'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_2'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/sdk/*'),
    ]


@cloudformation_dataclass
class IoTPolicyAllowStatement2:
    resource: PolicyStatement
    action = 'iot:Subscribe'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topicfilter/*')]


@cloudformation_dataclass
class IoTPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [IoTPolicyAllowStatement0, IoTPolicyAllowStatement1, IoTPolicyAllowStatement2]


@cloudformation_dataclass
class IoTPolicy:
    """AWS::IoT::Policy resource."""

    resource: Policy
    policy_document = IoTPolicyPolicyDocument
