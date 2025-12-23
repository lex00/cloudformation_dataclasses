"""Pipeline - AWS::CodePipeline::Pipeline resource."""

from .. import *  # noqa: F403


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
