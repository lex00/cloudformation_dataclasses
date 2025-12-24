"""Cicd resources: Repo."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Repo:
    """AWS::CodeCommit::Repository resource."""

    resource: codecommit.Repository
    repository_name = 'my-repo'
