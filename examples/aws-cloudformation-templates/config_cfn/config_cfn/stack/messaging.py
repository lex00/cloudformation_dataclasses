"""Messaging resources: ConfigTopic, ConfigTopicPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic


@cloudformation_dataclass
class ConfigTopicPolicyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'config.amazonaws.com',
    }
    action = 'SNS:Publish'
    resource_arn = '*'


@cloudformation_dataclass
class ConfigTopicPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ConfigTopicPolicyAllowStatement0]


@cloudformation_dataclass
class ConfigTopicPolicy:
    """AWS::SNS::TopicPolicy resource."""

    resource: sns.TopicPolicy
    policy_document = ConfigTopicPolicyPolicyDocument
    topics = [ref(ConfigTopic)]
