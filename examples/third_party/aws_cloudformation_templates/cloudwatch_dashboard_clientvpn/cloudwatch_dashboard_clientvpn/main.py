"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import ClientVPNLogGroup, Folder
from .outputs import DashboardUrlOutput, LogInsightsUrlOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""This CloudFormation template creates a set of CloudWatch Logs Insights queries and a corresponding dashboard  for comprehensive AWS Client VPN usage reporting. It provides detailed insights into VPN usage patterns,  connection durations, data transfer volumes, and user activities across different authentication methods  (AD/SAML, Mutual Auth, and Mixed Auth).
""",
        parameters=[Folder, ClientVPNLogGroup],
        outputs=[LogInsightsUrlOutput, DashboardUrlOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
