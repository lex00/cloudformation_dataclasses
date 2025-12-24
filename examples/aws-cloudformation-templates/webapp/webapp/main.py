"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Creates a web application with a static website using S3 and CloudFront, an API Gateway REST API, and a DynamoDB table, with Cognito authentication. Apache-2.0 License. Adapt this template to your needs and thoruoughly test it before introducing it in a production environment. **WARNING** This template will create resources in your account that may incur billing charges.',
        parameters=[AppName, LambdaCodeS3Bucket, LambdaCodeS3Key],
        outputs=[SiteURLOutput, RedirectURIOutput, AppNameOutput, RestApiInvokeURLOutput, AppClientIdOutput, CognitoDomainPrefixOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
