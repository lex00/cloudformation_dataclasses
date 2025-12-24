"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Example of cross-account, same-region, S3 replication (v2) using server-side encryption with a customer-managed KMS key.  Create a symmetric KMS key with an alias, and a source S3 bucket with default encryption and versioning enabled. Create an IAM role, used by a replication rule, to provide access to the source and destination buckets and KMS keys.',
        parameters=[AccountIdDestination],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
