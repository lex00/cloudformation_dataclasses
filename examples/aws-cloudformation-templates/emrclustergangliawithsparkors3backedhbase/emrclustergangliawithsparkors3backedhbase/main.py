"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Best Practice EMR Cluster for Spark or S3 backed Hbase',
        parameters=[EMRClusterName, KeyName, MasterInstanceType, CoreInstanceType, NumberOfCoreInstances, SubnetID, LogUri, S3DataUri, ReleaseLabel, Applications],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
