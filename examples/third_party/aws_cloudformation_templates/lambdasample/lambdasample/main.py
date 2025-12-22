"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import EnvName, LambdaHandlerPath
from .outputs import LambdaFunctionARNOutput, LambdaFunctionNameOutput, LambdaRoleARNOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Template for Lambda Sample.',
        parameters=[EnvName, LambdaHandlerPath],
        outputs=[LambdaRoleARNOutput, LambdaFunctionNameOutput, LambdaFunctionARNOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
