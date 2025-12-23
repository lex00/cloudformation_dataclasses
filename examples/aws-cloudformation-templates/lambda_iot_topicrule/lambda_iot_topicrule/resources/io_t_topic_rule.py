"""IoTTopicRule - AWS::IoT::TopicRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTTopicRuleLambdaAction:
    resource: iot.topic_rule.LambdaAction
    function_arn = get_att(MyLambda, "Arn")


@cloudformation_dataclass
class IoTTopicRuleAction:
    resource: iot.topic_rule.Action
    lambda_ = IoTTopicRuleLambdaAction


@cloudformation_dataclass
class IoTTopicRuleTopicRulePayload:
    resource: iot.topic_rule.TopicRulePayload
    actions = [IoTTopicRuleAction]
    aws_iot_sql_version = '2016-03-23'
    sql = " SELECT * FROM 'topic_2'"
    rule_disabled = False


@cloudformation_dataclass
class IoTTopicRule:
    """AWS::IoT::TopicRule resource."""

    resource: iot.TopicRule
    rule_name = ref(MyLambda)
    topic_rule_payload = IoTTopicRuleTopicRulePayload
