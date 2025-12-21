"""Deployment context - inferred from template patterns.

Detected naming pattern: ${AppName}-${AWS::Region}-${AWS::AccountId}

Customize this context for your deployment environment.
"""

from . import *  # noqa: F403
from .config import AppName


@cloudformation_dataclass
class TemplateContext:
    """
    Deployment context for this template.

    Uses AppName parameter as project_name prefix.
    Naming pattern: ${AppName}-${AWS::Region}-${AWS::AccountId}
    """

    context: DeploymentContext
    project_name = ref(AppName)  # From AppName parameter


# Instantiate for use in resources
ctx = TemplateContext()
