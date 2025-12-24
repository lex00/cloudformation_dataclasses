"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""This template has resources that will be installed into all managed accounts
in the OU. For the purposes of the sample it's not important what exactly we
are creating here. To demonstrate the consolidated logging, errors can be
introduced into this template, such as choosing a bucket name that already
exists. This template uses a Rain module, which can be packaged with `rain
pkg -x common-resources.yaml`.
""",
        parameters=[AppName],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
