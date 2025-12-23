"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='A CloudFormation template which shows how to provide multiple values to one StringValue when creating a DataPipeline definition, This template is entirely based on the example provided in the DataPipeline documentation here: http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emrconfiguration.html - Written by Nishant Casey',
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
