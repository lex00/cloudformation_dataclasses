"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template RDS_Snapshot_On_Delete: Sample template showing how to create an RDS DBInstance that is snapshotted on stack deletion. **WARNING** This template creates an Amazon RDS database instance. When the stack is deleted a database snapshot will be left in your account. You will be billed for the AWS resources used if you create a stack from this template.',
        outputs=[JDBCConnectionStringOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
