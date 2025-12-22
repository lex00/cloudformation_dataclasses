from __future__ import annotations

"""ConfigTopicPolicy - AWS::SNS::TopicPolicy resource."""

from .. import *  # noqa: F403


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

    resource: TopicPolicy
    policy_document = ConfigTopicPolicyPolicyDocument
    topics = [ref(ConfigTopic)]
