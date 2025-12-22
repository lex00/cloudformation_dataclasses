"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import DockerImage
from .outputs import AppBuildArnOutput, AppBuildOutput, AppDeployOutput, AppDeploydArnOutput, CodeBuildRoleArnOutput, CodeBuildRoleOutput, CodeCommitArnOutput, CodeCommitNameOutput, PipelineS3BucketArnOutput, PipelineS3BucketOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""Deploys the prequisites for creating required code pipelines this includes 
""",
        parameters=[DockerImage],
        outputs=[CodeCommitNameOutput, CodeCommitArnOutput, PipelineS3BucketOutput, PipelineS3BucketArnOutput, CodeBuildRoleOutput, CodeBuildRoleArnOutput, AppDeployOutput, AppDeploydArnOutput, AppBuildOutput, AppBuildArnOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
