"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Repo:
    """AWS::CodeCommit::Repository resource."""

    # Unknown resource type: AWS::CodeCommit::Repository
    resource: CloudFormationResource
    repository_name = 'my-repo'


@cloudformation_dataclass
class AddReadme:
    """Boto3::CodeCommit.put_file resource."""

    # Unknown resource type: Boto3::CodeCommit.put_file
    resource: CloudFormationResource
    repository_name = get_att(Repo, "Name")
    branch_name = 'master'
    file_content = 'Hello, world'
    file_path = 'README.md'
    commit_message = 'Add another README.md'
    name = 'CloudFormation'
