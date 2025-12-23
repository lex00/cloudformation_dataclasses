"""Infra resources: StackSet."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StackSet:
    """AWS::CloudFormation::StackSet resource."""

    resource: cloudformation.StackSet
    template_body = """Description: |
  This template has resources that will be installed into all managed accounts
  in the OU. For the purposes of the sample it's not important what exactly we
  are creating here. To demonstrate the consolidated logging, errors can be
  introduced into this template, such as choosing a bucket name that already
  exists. This template uses a Rain module, which can be packaged with `rain
  pkg -x common-resources.yaml`.

Parameters:
  AppName:
    Type: String
    Description: This name will be used as part of resource names
    Default: stacksets-sample

Resources:
  TestQ:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: test-events17

  StorageLogBucket:
    Type: AWS::S3::Bucket
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

  StorageBucket:
    Type: AWS::S3::Bucket
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
    Metadata:
      guard:
        SuppressedRules:
          - S3_BUCKET_DEFAULT_LOCK_ENABLED

  StorageReplicaBucket:
    Type: AWS::S3::Bucket
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

  StorageLogBucketPolicyPolicy:
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

  StorageBucketPolicyPolicy:
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

  StorageReplicaBucketPolicyPolicy:
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



#  BadBucket:
#    Type: AWS::S3::Bucket
#    Metadata:
#      guard:
#        SuppressedRules:
#          - S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED
#          - S3_BUCKET_DEFAULT_LOCK_ENABLED
#          - S3_BUCKET_VERSIONING_ENABLED
#          - S3_BUCKET_REPLICATION_ENABLED
#          - S3_BUCKET_PUBLIC_WRITE_PROHIBITED
#          - S3_BUCKET_PUBLIC_READ_PROHIBITED
#          - S3_BUCKET_LOGGING_ENABLED
#      Comment:
#        This bucket is purposefully using an existing name, to cause a deployment failure
#    Properties:
#      BucketName: rain-artifacts-646934191481-us-east-1"""
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
        'ParameterKey': 'AppName',
        'ParameterValue': 'stackset-logging-sample',
    }]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging'
    operation_preferences = {
        'FailureToleranceCount': 0,
        'MaxConcurrentCount': 2,
        'RegionConcurrencyType': 'PARALLEL',
    }
    auto_deployment = {
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True,
    }
    stack_set_name = 'common-resources'
