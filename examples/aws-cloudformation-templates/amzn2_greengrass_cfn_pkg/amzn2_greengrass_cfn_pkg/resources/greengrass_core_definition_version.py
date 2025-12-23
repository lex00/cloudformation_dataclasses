"""GreengrassCoreDefinitionVersion - AWS::Greengrass::CoreDefinitionVersion resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassCoreDefinitionVersion:
    """AWS::Greengrass::CoreDefinitionVersion resource."""

    resource: greengrass.CoreDefinitionVersion
    core_definition_id = ref(GreengrassCoreDefinition)
    cores = [{
        'CertificateArn': Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'cert',
    get_att(IoTThing, "certificateId"),
]),
]),
        'Id': Join('_', [
    ref(CoreName),
    'Core',
]),
        'SyncShadow': 'false',
        'ThingArn': Join(':', [
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
]),
    }]
