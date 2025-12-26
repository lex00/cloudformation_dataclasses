"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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
from cloudformation_dataclasses.aws import codepipeline, events, iam
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_REGION,
    ImportValue,
    Join,
    Sub,
)
from .params import *  # noqa: F403, F401

from .main import EventRole as EventRole
from .main import EventRoleAllowStatement0 as EventRoleAllowStatement0
from .main import EventRoleAllowStatement0_1 as EventRoleAllowStatement0_1
from .main import EventRoleAssumeRolePolicyDocument as EventRoleAssumeRolePolicyDocument
from .main import EventRolePolicies0PolicyDocument as EventRolePolicies0PolicyDocument
from .main import EventRolePolicy as EventRolePolicy
from .main import Pipeline as Pipeline
from .main import PipelineActionDeclaration as PipelineActionDeclaration
from .main import PipelineActionDeclaration1 as PipelineActionDeclaration1
from .main import PipelineActionDeclaration2 as PipelineActionDeclaration2
from .main import PipelineActionDeclaration3 as PipelineActionDeclaration3
from .main import PipelineActionTypeId as PipelineActionTypeId
from .main import PipelineActionTypeId1 as PipelineActionTypeId1
from .main import PipelineActionTypeId2 as PipelineActionTypeId2
from .main import PipelineActionTypeId3 as PipelineActionTypeId3
from .main import PipelineArtifactStore as PipelineArtifactStore
from .main import PipelineInputArtifact as PipelineInputArtifact
from .main import PipelineInputArtifact1 as PipelineInputArtifact1
from .main import PipelineInputArtifact2 as PipelineInputArtifact2
from .main import PipelineOutputArtifact as PipelineOutputArtifact
from .main import PipelineOutputArtifact1 as PipelineOutputArtifact1
from .main import PipelineRole as PipelineRole
from .main import PipelineRoleAllowStatement0 as PipelineRoleAllowStatement0
from .main import PipelineRoleAllowStatement0_1 as PipelineRoleAllowStatement0_1
from .main import PipelineRoleAllowStatement0_2 as PipelineRoleAllowStatement0_2
from .main import PipelineRoleAllowStatement0_3 as PipelineRoleAllowStatement0_3
from .main import PipelineRoleAllowStatement1 as PipelineRoleAllowStatement1
from .main import PipelineRoleAssumeRolePolicyDocument as PipelineRoleAssumeRolePolicyDocument
from .main import PipelineRolePolicies0PolicyDocument as PipelineRolePolicies0PolicyDocument
from .main import PipelineRolePolicies1PolicyDocument as PipelineRolePolicies1PolicyDocument
from .main import PipelineRolePolicies2PolicyDocument as PipelineRolePolicies2PolicyDocument
from .main import PipelineRolePolicy as PipelineRolePolicy
from .main import PipelineRolePolicy1 as PipelineRolePolicy1
from .main import PipelineRolePolicy2 as PipelineRolePolicy2
from .main import PipelineStageDeclaration as PipelineStageDeclaration
from .main import PipelineStageDeclaration1 as PipelineStageDeclaration1
from .main import PipelineStageDeclaration2 as PipelineStageDeclaration2
from .messaging import EventRule as EventRule
from .messaging import EventRuleTarget as EventRuleTarget
from .params import CodeBuildStack as CodeBuildStack

__all__: list[str] = ['AWS_ACCOUNT_ID', 'AWS_REGION', 'CodeBuildStack', 'EventRole', 'EventRoleAllowStatement0', 'EventRoleAllowStatement0_1', 'EventRoleAssumeRolePolicyDocument', 'EventRolePolicies0PolicyDocument', 'EventRolePolicy', 'EventRule', 'EventRuleTarget', 'ImportValue', 'Join', 'Parameter', 'Pipeline', 'PipelineActionDeclaration', 'PipelineActionDeclaration1', 'PipelineActionDeclaration2', 'PipelineActionDeclaration3', 'PipelineActionTypeId', 'PipelineActionTypeId1', 'PipelineActionTypeId2', 'PipelineActionTypeId3', 'PipelineArtifactStore', 'PipelineInputArtifact', 'PipelineInputArtifact1', 'PipelineInputArtifact2', 'PipelineOutputArtifact', 'PipelineOutputArtifact1', 'PipelineRole', 'PipelineRoleAllowStatement0', 'PipelineRoleAllowStatement0_1', 'PipelineRoleAllowStatement0_2', 'PipelineRoleAllowStatement0_3', 'PipelineRoleAllowStatement1', 'PipelineRoleAssumeRolePolicyDocument', 'PipelineRolePolicies0PolicyDocument', 'PipelineRolePolicies1PolicyDocument', 'PipelineRolePolicies2PolicyDocument', 'PipelineRolePolicy', 'PipelineRolePolicy1', 'PipelineRolePolicy2', 'PipelineStageDeclaration', 'PipelineStageDeclaration1', 'PipelineStageDeclaration2', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'codepipeline', 'events', 'get_att', 'iam', 'ref', 'setup_resources']
