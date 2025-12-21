from __future__ import annotations

"""MacroFunction - AWS::Serverless::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.12'
    code_uri = 'lambda'
    handler = 'index.handler'
