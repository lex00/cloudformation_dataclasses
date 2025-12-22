from __future__ import annotations

"""IoTTopicRule - AWS::IoT::TopicRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTTopicRuleLambdaAction:
    resource: LambdaAction
    function_arn: GetAtt[MyLambda] = get_att("Arn")


@cloudformation_dataclass
class IoTTopicRuleAction:
    resource: Action
    lambda_ = IoTTopicRuleLambdaAction


@cloudformation_dataclass
class IoTTopicRuleTopicRulePayload:
    resource: TopicRulePayload
    actions = [IoTTopicRuleAction]
    aws_iot_sql_version = '2016-03-23'
    sql = " SELECT * FROM 'topic_2'"
    rule_disabled = False


@cloudformation_dataclass
class IoTTopicRule:
    """AWS::IoT::TopicRule resource."""

    resource: TopicRule
    rule_name: Ref[MyLambda] = ref()
    topic_rule_payload = IoTTopicRuleTopicRulePayload
