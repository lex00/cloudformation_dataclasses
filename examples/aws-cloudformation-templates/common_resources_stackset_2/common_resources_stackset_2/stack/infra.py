"""Infra resources: StackSet."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StackSetDeploymentTargets:
    resource: cloudformation.stack_set.DeploymentTargets
    organizational_unit_ids = [ref(OUID)]


@cloudformation_dataclass
class StackSetStackInstances:
    resource: cloudformation.stack_set.StackInstances
    deployment_targets = StackSetDeploymentTargets
    regions = ref(StackSetRegions)


@cloudformation_dataclass
class StackSetParameter:
    resource: cloudformation.stack_set.Parameter
    parameter_key = 'AppName'
    parameter_value = 'stackset-logging-sample'


@cloudformation_dataclass
class StackSetParameter1:
    resource: cloudformation.stack_set.Parameter
    parameter_key = 'KmsKeyId'
    parameter_value = ref(KmsKeyId)


@cloudformation_dataclass
class StackSetOperationPreferences:
    resource: cloudformation.stack_set.OperationPreferences
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


@cloudformation_dataclass
class StackSetAutoDeployment:
    resource: cloudformation.stack_set.AutoDeployment
    enabled = True
    retain_stacks_on_account_removal = True


@cloudformation_dataclass
class StackSet:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = """AWSTemplateFormatVersion: "2010-09-09"
Description: |
  This template has resources that will be installed into all managed accounts
  in the OU. For the purposes of the sample it's not important what exactly we
  are creating here. To demonstrate the consolidated logging, errors can be
  introduced into this template, such as choosing a bucket name that already
  exists.

Parameters:
  AppName:
    Description: This name will be used as part of resource names
    Type: String
    Default: stacksets-sample
  KmsKeyId:
    Type: String
    Description: 'The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID'
    Default: alias/aws/sqs

Resources:
  TestQ:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: test-events17
      KmsMasterKeyId: !Ref KmsKeyId

  StorageLogBucket:
    Type: AWS::S3::Bucket
    Metadata:
      Comment: This bucket records access logs for the main bucket
      checkov:
        skip:
          - comment: This is the log bucket
            id: CKV_AWS_18
      guard:
        SuppressedRules:
          - S3_BUCKET_LOGGING_ENABLED
          - S3_BUCKET_REPLICATION_ENABLED
      Rain:
        Content: RAIN_NO_CONTENT
        EmptyOnDelete: false
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      BucketName: !Sub ${AppName}-logs-${AWS::Region}-${AWS::AccountId}
      ObjectLockConfiguration:
        ObjectLockEnabled: Enabled
        Rule:
          DefaultRetention:
            Mode: COMPLIANCE
            Years: 1
      ObjectLockEnabled: true
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      VersioningConfiguration:
        Status: Enabled

  StorageBucket:
    Type: AWS::S3::Bucket
    Metadata:
      guard:
        SuppressedRules:
          - S3_BUCKET_DEFAULT_LOCK_ENABLED
      Rain:
        Content: RAIN_NO_CONTENT
        EmptyOnDelete: false
        DistributionLogicalId: NONE
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      BucketName: !Sub ${AppName}-${AWS::Region}-${AWS::AccountId}
      LoggingConfiguration:
        DestinationBucketName: !Ref StorageLogBucket
      ObjectLockEnabled: false
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      ReplicationConfiguration:
        Role: !GetAtt StorageReplicationRole.Arn
        Rules:
          - Destination:
              Bucket: !GetAtt StorageReplicaBucket.Arn
            Status: Enabled
      VersioningConfiguration:
        Status: Enabled

  StorageReplicaBucket:
    Type: AWS::S3::Bucket
    Metadata:
      Comment: This bucket is used as a target for replicas from the main bucket
      checkov:
        skip:
          - comment: This is the replica bucket
            id: CKV_AWS_18
      guard:
        SuppressedRules:
          - S3_BUCKET_DEFAULT_LOCK_ENABLED
          - S3_BUCKET_REPLICATION_ENABLED
          - S3_BUCKET_LOGGING_ENABLED
      Rain:
        Content: RAIN_NO_CONTENT
        EmptyOnDelete: false
    Properties:
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      BucketName: !Sub ${AppName}-replicas-${AWS::Region}-${AWS::AccountId}
      ObjectLockEnabled: false
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      VersioningConfiguration:
        Status: Enabled

  StorageReplicationPolicy:
    Type: AWS::IAM::RolePolicy
    Properties:
      PolicyDocument:
        Statement:
          - Action:
              - s3:GetReplicationConfiguration
              - s3:ListBucket
            Effect: Allow
            Resource: !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}
          - Action:
              - s3:GetObjectVersionForReplication
              - s3:GetObjectVersionAcl
              - s3:GetObjectVersionTagging
            Effect: Allow
            Resource: !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*
          - Action:
              - s3:ReplicateObject
              - s3:ReplicateDelete
              - s3:ReplicationTags
            Effect: Allow
            Resource: !Sub arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*
        Version: "2012-10-17"
      PolicyName: bucket-replication-policy
      RoleName: !Ref StorageReplicationRole

  StorageReplicationRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action:
              - sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - s3.amazonaws.com
        Version: "2012-10-17"
      Path: /

  StorageLogBucketAccessPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Sub ${AppName}-logs-${AWS::Region}-${AWS::AccountId}
      PolicyDocument:
        Statement:
          - Action: s3:*
            Condition:
              Bool:
                aws:SecureTransport: false
            Effect: Deny
            Principal:
              AWS: '*'
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*
          - Action: s3:PutObject
            Condition:
              ArnLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
            Effect: Allow
            Principal:
              Service: logging.s3.amazonaws.com
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*
        Version: "2012-10-17"

  StorageBucketAccessPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Sub ${AppName}-${AWS::Region}-${AWS::AccountId}
      PolicyDocument:
        Statement:
          - Action: s3:*
            Condition:
              Bool:
                aws:SecureTransport: false
            Effect: Deny
            Principal:
              AWS: '*'
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*
          - Action: s3:PutObject
            Condition:
              ArnLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
            Effect: Allow
            Principal:
              Service: logging.s3.amazonaws.com
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*
        Version: "2012-10-17"

  StorageReplicaBucketAccessPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Sub ${AppName}-replicas-${AWS::Region}-${AWS::AccountId}
      PolicyDocument:
        Statement:
          - Action: s3:*
            Condition:
              Bool:
                aws:SecureTransport: false
            Effect: Deny
            Principal:
              AWS: '*'
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*
          - Action: s3:PutObject
            Condition:
              ArnLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
            Effect: Allow
            Principal:
              Service: logging.s3.amazonaws.com
            Resource:
              - !Sub arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*
        Version: "2012-10-17"
"""
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [StackSetStackInstances]
    parameters = [StackSetParameter, StackSetParameter1]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging'
    operation_preferences = StackSetOperationPreferences
    auto_deployment = StackSetAutoDeployment
    stack_set_name = 'common-resources'
