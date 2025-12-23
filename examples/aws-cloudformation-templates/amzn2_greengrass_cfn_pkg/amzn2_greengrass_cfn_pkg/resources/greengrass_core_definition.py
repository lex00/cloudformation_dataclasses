"""GreengrassCoreDefinition - AWS::Greengrass::CoreDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassCoreDefinition:
    """AWS::Greengrass::CoreDefinition resource."""

    resource: CoreDefinition
    name = Join('_', [
    ref(CoreName),
    'Core',
])
