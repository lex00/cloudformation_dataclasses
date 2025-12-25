"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import codecommit
from .params import *  # noqa: F403, F401

from .cicd import Repo as Repo
from .main import AddReadme as AddReadme

__all__: list[str] = ['AddReadme', 'CloudFormationResource', 'Repo', 'Template', 'cloudformation_dataclass', 'codecommit', 'get_att', 'ref', 'setup_resources']
