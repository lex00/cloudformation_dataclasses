"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import BucketName, PublisherAccountID
from .outputs import BucketOutput, BucketPolicyOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template: Sample template which will create an s3 bucket with a bucket policy to enable cross account acccess. The template requires you to provide an AWS account ID to provide cross account access to, and a globally unique name for an s3 bucket.',
        parameters=[BucketName, PublisherAccountID],
        outputs=[BucketOutput, BucketPolicyOutput],
    )


if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
