"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NeptuneEndpointAddressOutput:
    """Neptune DB endpoint address"""

    resource: Output
    value = get_att(NeptuneDBCluster, "Endpoint")
    description = 'Neptune DB endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-address')


@cloudformation_dataclass
class NeptuneReadEndpointAddressOutput:
    """Neptune DB read-only endpoint address"""

    resource: Output
    value = get_att(NeptuneDBCluster, "ReadEndpoint")
    description = 'Neptune DB read-only endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-read-endpoint-address')


@cloudformation_dataclass
class NeptuneSnsTopicOutput:
    """Neptune SNS Topic for alarms"""

    resource: Output
    value = If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))
    description = 'Neptune SNS Topic for alarms'
    export_name = Sub('${Env}-${AppName}-neptune-sns-topic')


@cloudformation_dataclass
class NeptuneEndpointPortOutput:
    """Endpoint port"""

    resource: Output
    value = get_att(NeptuneDBCluster, "Port")
    description = 'Endpoint port'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-port')
