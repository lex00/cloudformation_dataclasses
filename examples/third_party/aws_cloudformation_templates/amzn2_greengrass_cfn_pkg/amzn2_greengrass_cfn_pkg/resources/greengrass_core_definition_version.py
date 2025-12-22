from __future__ import annotations

"""GreengrassCoreDefinitionVersion - AWS::Greengrass::CoreDefinitionVersion resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassCoreDefinitionVersionCore:
    resource: Core
    certificate_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'cert',
    get_att(IoTThing, "certificateId"),
]),
])
    id = Join('_', [
    ref(CoreName),
    'Core',
])
    sync_shadow = 'false'
    thing_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'thing',
    Join('_', [
    ref(CoreName),
    'Core',
]),
]),
])


@cloudformation_dataclass
class GreengrassCoreDefinitionVersion:
    """AWS::Greengrass::CoreDefinitionVersion resource."""

    resource: CoreDefinitionVersion
    core_definition_id = ref(GreengrassCoreDefinition)
    cores = [GreengrassCoreDefinitionVersionCore]
