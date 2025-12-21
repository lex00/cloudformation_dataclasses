"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CodeCommitNameOutput:
    """The code commit repository name"""

    resource: Output
    value = get_att("CodeCommitRepo", "Name")
    description = 'The code commit repository name'
    export_name = Sub('${AWS::StackName}-CodeCommitName')


@cloudformation_dataclass
class CodeCommitArnOutput:
    """The code commit repository arn"""

    resource: Output
    value = get_att("CodeCommitRepo", "Arn")
    description = 'The code commit repository arn'
    export_name = Sub('${AWS::StackName}-CodeCommitArn')


@cloudformation_dataclass
class PipelineS3BucketOutput:
    """The s3 bucket used by the deployment codepipelines"""

    resource: Output
    value = ref("PipelineS3Bucket")
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3Bucket')


@cloudformation_dataclass
class PipelineS3BucketArnOutput:
    """The s3 bucket used by the deployment codepipelines"""

    resource: Output
    value = get_att("PipelineS3Bucket", "Arn")
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3BucketArn')


@cloudformation_dataclass
class CodeBuildRoleOutput:
    """IAM Role ARN associated with CodeBuild projects"""

    resource: Output
    value = ref("CodeBuildRole")
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRole')


@cloudformation_dataclass
class CodeBuildRoleArnOutput:
    """IAM Role ARN associated with CodeBuild projects"""

    resource: Output
    value = get_att("CodeBuildRole", "Arn")
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRoleArn')


@cloudformation_dataclass
class AppDeployOutput:
    resource: Output
    value = ref("AppDeploy")
    export_name = Sub('${AWS::StackName}-AppDeploy')


@cloudformation_dataclass
class AppDeploydArnOutput:
    resource: Output
    value = get_att("AppDeploy", "Arn")
    export_name = Sub('${AWS::StackName}-AppDeployArn')


@cloudformation_dataclass
class AppBuildOutput:
    resource: Output
    value = ref("AppBuild")
    export_name = Sub('${AWS::StackName}-AppBuild')


@cloudformation_dataclass
class AppBuildArnOutput:
    resource: Output
    value = get_att("AppBuild", "Arn")
    export_name = Sub('${AWS::StackName}-AppBuildArn')
