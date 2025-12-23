"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PipelineRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['codepipeline.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class PipelineRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0]


@cloudformation_dataclass
class PipelineRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'codecommit:GetBranch',
        'codecommit:GetCommit',
        'codecommit:UploadArchive',
        'codecommit:GetUploadArchiveStatus',
    ]
    resource_arn = [ImportValue(Sub('${CodeBuildStack}-CodeCommitArn'))]


@cloudformation_dataclass
class PipelineRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_1]


@cloudformation_dataclass
class PipelineRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CanAccessCodeCommit'
    policy_document = PipelineRolePolicies0PolicyDocument


@cloudformation_dataclass
class PipelineRoleAllowStatement0_2:
    resource: PolicyStatement
    action = 's3:ListBucket'
    resource_arn = '*'


@cloudformation_dataclass
class PipelineRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObject',
        's3:GetObjectVersion',
        's3:GetBucketVersioning',
        's3:PutObject',
        's3:GetBucketPolicy',
        's3:GetObjectAcl',
        's3:PutObjectAcl',
        's3:DeleteObject',
    ]
    resource_arn = [
        ImportValue(Sub('${CodeBuildStack}-PipelineS3BucketArn')),
        Sub('${filename}/*', {
    'filename': ImportValue(Sub('${CodeBuildStack}-PipelineS3BucketArn')),
}),
    ]


@cloudformation_dataclass
class PipelineRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_2, PipelineRoleAllowStatement1]


@cloudformation_dataclass
class PipelineRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'CanAccessS3'
    policy_document = PipelineRolePolicies1PolicyDocument


@cloudformation_dataclass
class PipelineRoleAllowStatement0_3:
    resource: PolicyStatement
    action = [
        'codebuild:BatchGetBuilds',
        'codebuild:StartBuild',
    ]
    resource_arn = [
        ImportValue(Sub('${CodeBuildStack}-AppBuildArn')),
        ImportValue(Sub('${CodeBuildStack}-AppDeployArn')),
    ]


@cloudformation_dataclass
class PipelineRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_3]


@cloudformation_dataclass
class PipelineRolePolicy2:
    resource: iam.user.Policy
    policy_name = 'CanStartCodeBuild'
    policy_document = PipelineRolePolicies2PolicyDocument


@cloudformation_dataclass
class PipelineRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = PipelineRoleAssumeRolePolicyDocument
    policies = [PipelineRolePolicy, PipelineRolePolicy1, PipelineRolePolicy2]


@cloudformation_dataclass
class PipelineArtifactStore:
    resource: codepipeline.pipeline.ArtifactStore
    type_ = 'S3'
    location = ImportValue(Sub('${CodeBuildStack}-PipelineS3Bucket'))


@cloudformation_dataclass
class PipelineActionTypeId:
    resource: codepipeline.pipeline.ActionTypeId
    category = 'Source'
    owner = 'AWS'
    provider = 'CodeCommit'
    version = 1


@cloudformation_dataclass
class PipelineOutputArtifact:
    resource: codepipeline.pipeline.OutputArtifact
    name = 'Source'


@cloudformation_dataclass
class PipelineActionDeclaration:
    resource: codepipeline.pipeline.ActionDeclaration
    name = 'Source'
    action_type_id = PipelineActionTypeId
    configuration = {
        'RepositoryName': ImportValue(Sub('${CodeBuildStack}-CodeCommitName')),
        'BranchName': 'main',
        'PollForSourceChanges': False,
    }
    output_artifacts = [PipelineOutputArtifact]


@cloudformation_dataclass
class PipelineStageDeclaration:
    resource: codepipeline.pipeline.StageDeclaration
    name = 'Source'
    actions = [PipelineActionDeclaration]


@cloudformation_dataclass
class PipelineActionTypeId1:
    resource: codepipeline.pipeline.ActionTypeId
    category = 'Build'
    owner = 'AWS'
    provider = 'CodeBuild'
    version = 1


@cloudformation_dataclass
class PipelineInputArtifact:
    resource: codepipeline.pipeline.InputArtifact
    name = 'Source'


@cloudformation_dataclass
class PipelineOutputArtifact1:
    resource: codepipeline.pipeline.OutputArtifact
    name = 'FullZip'


@cloudformation_dataclass
class PipelineActionDeclaration1:
    resource: codepipeline.pipeline.ActionDeclaration
    name = 'App-Build'
    action_type_id = PipelineActionTypeId1
    configuration = {
        'ProjectName': ImportValue(Sub('${CodeBuildStack}-AppBuild')),
    }
    input_artifacts = [PipelineInputArtifact]
    output_artifacts = [PipelineOutputArtifact1]
    run_order = 1


@cloudformation_dataclass
class PipelineStageDeclaration1:
    resource: codepipeline.pipeline.StageDeclaration
    name = 'Build-AppBuild'
    actions = [PipelineActionDeclaration1]


@cloudformation_dataclass
class PipelineActionTypeId2:
    resource: codepipeline.pipeline.ActionTypeId
    category = 'Approval'
    owner = 'AWS'
    provider = 'Manual'
    version = 1


@cloudformation_dataclass
class PipelineActionDeclaration2:
    resource: codepipeline.pipeline.ActionDeclaration
    name = 'Approval'
    action_type_id = PipelineActionTypeId2
    configuration = {
        'CustomData': 'Review the build output and approve to deploy',
    }
    run_order = 2


@cloudformation_dataclass
class PipelineActionTypeId3:
    resource: codepipeline.pipeline.ActionTypeId
    category = 'Build'
    owner = 'AWS'
    provider = 'CodeBuild'
    version = 1


@cloudformation_dataclass
class PipelineInputArtifact1:
    resource: codepipeline.pipeline.InputArtifact
    name = 'Source'


@cloudformation_dataclass
class PipelineInputArtifact2:
    resource: codepipeline.pipeline.InputArtifact
    name = 'FullZip'


@cloudformation_dataclass
class PipelineActionDeclaration3:
    resource: codepipeline.pipeline.ActionDeclaration
    name = 'App-Deploy'
    action_type_id = PipelineActionTypeId3
    configuration = {
        'ProjectName': ImportValue(Sub('${CodeBuildStack}-AppDeploy')),
        'PrimarySource': 'Source',
        'EnvironmentVariables': '[{"name":"ENVIRONMENT","value":"SampleEnv","type":"PLAINTEXT"}]',
    }
    input_artifacts = [PipelineInputArtifact1, PipelineInputArtifact2]
    run_order = 3


@cloudformation_dataclass
class PipelineStageDeclaration2:
    resource: codepipeline.pipeline.StageDeclaration
    name = 'Deploy-App'
    actions = [PipelineActionDeclaration2, PipelineActionDeclaration3]


@cloudformation_dataclass
class Pipeline:
    """AWS::CodePipeline::Pipeline resource."""

    resource: codepipeline.Pipeline
    name = Sub('${AWS::StackName}-Code-Pipeline')
    artifact_store = PipelineArtifactStore
    restart_execution_on_update = False
    role_arn = get_att(PipelineRole, "Arn")
    stages = [PipelineStageDeclaration, PipelineStageDeclaration1, PipelineStageDeclaration2]


@cloudformation_dataclass
class EventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class EventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0]


@cloudformation_dataclass
class EventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'codepipeline:StartPipelineExecution'
    resource_arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    ref(Pipeline),
])


@cloudformation_dataclass
class EventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0_1]


@cloudformation_dataclass
class EventRolePolicy:
    resource: iam.user.Policy
    policy_name = 'eb-pipeline-execution'
    policy_document = EventRolePolicies0PolicyDocument


@cloudformation_dataclass
class EventRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [EventRolePolicy]


@cloudformation_dataclass
class EventRuleTarget:
    resource: events.rule.Target
    arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    ref(Pipeline),
])
    role_arn = get_att(EventRole, "Arn")
    id = 'codepipeline-Pipeline'


@cloudformation_dataclass
class EventRule:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    event_pattern = {
        'source': ['aws.codecommit'],
        'detail-type': ['CodeCommit Repository State Change'],
        'resources': [ImportValue(Sub('${CodeBuildStack}-CodeCommitArn'))],
        'detail': {
            'event': [
                'referenceCreated',
                'referenceUpdated',
            ],
            'referenceType': ['branch'],
            'referenceName': ['main'],
        },
    }
    targets = [EventRuleTarget]
