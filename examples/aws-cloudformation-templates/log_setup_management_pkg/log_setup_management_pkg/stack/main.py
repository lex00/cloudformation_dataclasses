"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = Sub('${CentralEventBusName}-DLQ')


@cloudformation_dataclass
class CentralEventBus:
    """AWS::Events::EventBus resource."""

    resource: events.EventBus
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = ref(CentralEventBusName)
    dead_letter_config = {
        'Arn': get_att(DeadLetterQueue, "Arn"),
    }


@cloudformation_dataclass
class CentralEventBusPolicy:
    """AWS::Events::EventBusPolicy resource."""

    resource: events.EventBusPolicy
    event_bus_name = ref(CentralEventBus)
    statement_id = 'CentralEventBusPolicyStatement'
    statement = {
        'Effect': 'Allow',
        'Principal': '*',
        'Action': 'events:PutEvents',
        'Resource': Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/${CentralEventBusName}'),
        'Condition': {
            'StringEquals': {
                'aws:PrincipalOrgID': ref(OrgID),
            },
        },
    }


@cloudformation_dataclass
class CentralEventLogKeyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'AWS': [Sub('arn:aws:iam::${AWS::AccountId}:role/Admin')],
    }
    action = [
        'kms:Create*',
        'kms:Describe*',
        'kms:Enable*',
        'kms:List*',
        'kms:Put*',
        'kms:Update*',
        'kms:Revoke*',
        'kms:Disable*',
        'kms:Get*',
        'kms:Delete*',
        'kms:ScheduleKeyDeletion',
        'kms:CancelKeyDeletion',
        'kms:GenerateDataKey',
        'kms:TagResource',
        'kms:UntagResource',
    ]
    resource_arn = Sub('arn:aws:kms:${AWS::Region}:${AWS::AccountId}:key/*')


@cloudformation_dataclass
class CentralEventLogKeyAllowStatement1:
    resource: PolicyStatement
    sid = 'Allow CloudWatch Logs to use the key'
    principal = {
        'Service': 'logs.amazonaws.com',
    }
    action = [
        'kms:Encrypt*',
        'kms:Decrypt*',
        'kms:ReEncrypt*',
        'kms:GenerateDataKey*',
        'kms:Describe*',
    ]
    resource_arn = Sub('arn:aws:kms:${AWS::Region}:${AWS::AccountId}:key/*')


@cloudformation_dataclass
class CentralEventLogKeyKeyPolicy:
    resource: PolicyDocument
    statement = [CentralEventLogKeyAllowStatement0, CentralEventLogKeyAllowStatement1]


@cloudformation_dataclass
class CentralEventLogKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    description = 'KMS key for log group'
    key_policy = CentralEventLogKeyKeyPolicy


@cloudformation_dataclass
class CentralEventLog:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_class = 'STANDARD'
    log_group_name = ref(CentralEventLogName)
    kms_key_id = get_att(CentralEventLogKey, "Arn")
    depends_on = ["CentralEventBus"]


@cloudformation_dataclass
class CentralEventLogQuery:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = 'CentralCloudFormationEventLogs'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` | sort @timestamp desc'
    log_group_names = [ref(CentralEventLogName)]


@cloudformation_dataclass
class CentralEventLogQueryReason:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = 'CentralCloudFormationFailures'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` as status, `detail.status-details.status-reason` as reason | sort @timestamp desc | filter status like "FAILED" | filter reason not like "canceled" | filter resource not like "AWS::CloudFormation::Stack" '
    log_group_names = [ref(CentralEventLogName)]


@cloudformation_dataclass
class CentralEventLogPolicy:
    """AWS::Logs::ResourcePolicy resource."""

    resource: logs.ResourcePolicy
    policy_name = 'CentralEventLogResourcePolicy'
    policy_document = Sub("""{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "delivery.logs.amazonaws.com",
          "events.amazonaws.com"
        ]
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:CreateLogStream"
      ],
      "Resource": "${CentralEventLog.Arn}"
    }
  ]
}
""")


@cloudformation_dataclass
class CentralEventRule:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    name = 'CloudFormationLogs'
    event_bus_name = ref(CentralEventBusName)
    state = 'ENABLED'
    event_pattern = {
        'source': [{
            'prefix': '',
        }],
    }
    targets = [{
        'Arn': get_att(CentralEventLog, "Arn"),
        'Id': 'CloudFormationLogsToCentralGroup',
        'DeadLetterConfig': {
            'Arn': get_att(DeadLetterQueue, "Arn"),
        },
    }]
    depends_on = ["CentralEventLog"]


@cloudformation_dataclass
class TargetAccountLogging:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = """AWSTemplateFormatVersion: '2010-09-09'

Description: EventBridge Rule to send CloudFormation events to a central EventBus

Parameters:

  CentralEventBusArn:
    Type: String

Resources:

  CloudFormationEventRule:
    Type: AWS::Events::Rule
    Metadata:
      Comment: Send all cloudformation events to the central event bus
    Properties:
      Name: CloudFormationEventRule
      EventBusName: !Sub arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default
      EventPattern:
        source:
          - aws.cloudformation
      State: ENABLED
      Targets:
        - Arn: !Ref CentralEventBusArn 
          RoleArn: !GetAtt EventBridgeRole.Arn
          Id: CentralEventBus
          DeadLetterConfig:
            Arn: !GetAtt DeadLetterQueue.Arn

  DeadLetterQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: CloudFormation-Logs-DLQ

  DeadLetterQueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      PolicyDocument:
        Version: "2012-10-17"
        Id: AllowEventBridgeToWriteLogs
        Statement:
          - Sid: AllowEventBridgeToWriteLogs
            Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: sqs:SendMessage
            Resource: !GetAtt DeadLetterQueue.Arn
            Condition:
              ArnLike:
                aws:SourceArn: !Sub "arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/CloudFormationEventRule"
      Queues:
        - !Ref DeadLetterQueue

  EventBridgeRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: 'sts:AssumeRole'

  EventBridgeRolePolicy:
    Type: AWS::IAM::RolePolicy
    Metadata: 
      Comment: Allow CloudFormation events to be written to the default event bus in the target account
    Properties:
      PolicyName: EventBridgeRolePolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action: 'events:PutEvents'
            Resource: !Ref CentralEventBusArn 
      RoleName: !Ref EventBridgeRole"""
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [{
        'DeploymentTargets': {
            'OrganizationalUnitIds': [ref(OUID)],
        },
        'Regions': [
            'us-east-1',
            'us-west-2',
        ],
    }]
    parameters = [{
        'ParameterKey': 'CentralEventBusArn',
        'ParameterValue': get_att(CentralEventBus, "Arn"),
    }]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = {
        'FailureToleranceCount': 0,
        'MaxConcurrentCount': 2,
        'RegionConcurrencyType': 'PARALLEL',
    }
    auto_deployment = {
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True,
    }
    stack_set_name = 'log-setup'
    depends_on = ["CentralEventRule", "CentralEventLog", "CentralEventLogPolicy"]
