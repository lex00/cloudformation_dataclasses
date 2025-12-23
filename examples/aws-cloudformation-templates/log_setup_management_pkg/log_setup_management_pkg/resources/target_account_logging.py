"""TargetAccountLogging - AWS::CloudFormation::StackSet resource."""

from .. import *  # noqa: F403


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
