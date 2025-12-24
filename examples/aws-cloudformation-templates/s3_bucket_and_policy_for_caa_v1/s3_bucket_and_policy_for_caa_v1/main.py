"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template: Sample template which will create an s3 bucket with a bucket policy to enable cross account acccess. The template requires you to provide an AWS account ID to provide cross account access to, and a globally unique name for an s3 bucket.',
        parameters=[BucketName, PublisherAccountID],
        outputs=[BucketOutput, BucketPolicyOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
