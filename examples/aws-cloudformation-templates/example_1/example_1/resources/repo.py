"""Repo - AWS::CodeCommit::Repository resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Repo:
    """AWS::CodeCommit::Repository resource."""

    # Unknown resource type: AWS::CodeCommit::Repository
    resource: CloudFormationResource
    repository_name = 'my-repo'
