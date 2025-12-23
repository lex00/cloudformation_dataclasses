"""CodeCommitRepo - AWS::CodeCommit::Repository resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CodeCommitRepo:
    """AWS::CodeCommit::Repository resource."""

    resource: codecommit.Repository
    repository_name = Sub('${AWS::StackName}-repo')
    repository_description = Sub('This is a repository for the ${AWS::StackName} project.')
