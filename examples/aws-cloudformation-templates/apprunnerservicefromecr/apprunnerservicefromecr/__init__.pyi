"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Output,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import apprunner, iam
from cloudformation_dataclasses.intrinsics import AWS_STACK_NAME, Join

from .main import AppRunner as AppRunner
from .main import AppRunnerAuthenticationConfiguration as AppRunnerAuthenticationConfiguration
from .main import AppRunnerImageConfiguration as AppRunnerImageConfiguration
from .main import AppRunnerImageRepository as AppRunnerImageRepository
from .main import AppRunnerSourceConfiguration as AppRunnerSourceConfiguration
from .outputs import AppRunnerOutput as AppRunnerOutput
from .params import ECRURL as ECRURL
from .params import TCPPORT as TCPPORT
from .security import AppRunnerRole as AppRunnerRole
from .security import AppRunnerRoleAllowStatement0 as AppRunnerRoleAllowStatement0
from .security import AppRunnerRoleAllowStatement0_1 as AppRunnerRoleAllowStatement0_1
from .security import AppRunnerRoleAssumeRolePolicyDocument as AppRunnerRoleAssumeRolePolicyDocument
from .security import AppRunnerRolePolicies0PolicyDocument as AppRunnerRolePolicies0PolicyDocument
from .security import AppRunnerRolePolicy as AppRunnerRolePolicy

__all__: list[str] = ['AWS_STACK_NAME', 'AppRunner', 'AppRunnerAuthenticationConfiguration', 'AppRunnerImageConfiguration', 'AppRunnerImageRepository', 'AppRunnerOutput', 'AppRunnerRole', 'AppRunnerRoleAllowStatement0', 'AppRunnerRoleAllowStatement0_1', 'AppRunnerRoleAssumeRolePolicyDocument', 'AppRunnerRolePolicies0PolicyDocument', 'AppRunnerRolePolicy', 'AppRunnerSourceConfiguration', 'ECRURL', 'Join', 'NUMBER', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'TCPPORT', 'Template', 'apprunner', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 'setup_resources']
