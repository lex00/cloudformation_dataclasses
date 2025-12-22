"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AppRunnerOutput:
    """URL of the deployed App Runner Service"""

    resource: Output
    value = Join('', [
    'https://',
    get_att("AppRunner", "ServiceUrl"),
])
    description = 'URL of the deployed App Runner Service'
