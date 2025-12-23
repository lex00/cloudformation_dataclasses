"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""Sample template showing how to create an Amazon RDS Database Instance with a
DBParameterGroup. **WARNING** This template creates an Amazon Relational
Database Service database instance. You will be billed for the AWS
resources used if you create a stack from this template.
""",
        parameters=[DBName, DBUser],
        outputs=[JDBCConnectionStringOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
