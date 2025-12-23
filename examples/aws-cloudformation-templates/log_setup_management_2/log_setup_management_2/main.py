"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='A central event bus rule and log group to collect CloudFormation logs from all target accounts',
        parameters=[OUID, OrgID, CentralEventBusName, CentralEventLogName, KmsKeyId, StackSetRegions],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
