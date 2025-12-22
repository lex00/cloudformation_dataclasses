"""SubscriptionDefinition - AWS::Greengrass::SubscriptionDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubscriptionDefinitionSubscription:
    resource: greengrass.Subscription
    id = 'Subscription1'
    source = 'cloud'
    subject = Join('/', [
    ref(CoreName),
    'in',
])
    target = ref(GGSampleFunctionVersion)


@cloudformation_dataclass
class SubscriptionDefinitionSubscription1:
    resource: greengrass.Subscription
    id = 'Subscription2'
    source = ref(GGSampleFunctionVersion)
    subject = Join('/', [
    ref(CoreName),
    'out',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscription2:
    resource: greengrass.Subscription
    id = 'Subscription3'
    source = ref(GGSampleFunctionVersion)
    subject = Join('/', [
    ref(CoreName),
    'telem',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscriptionDefinitionVersion:
    resource: greengrass.SubscriptionDefinitionVersion
    subscriptions = [SubscriptionDefinitionSubscription, SubscriptionDefinitionSubscription1, SubscriptionDefinitionSubscription2]


@cloudformation_dataclass
class SubscriptionDefinition:
    """AWS::Greengrass::SubscriptionDefinition resource."""

    resource: greengrass.SubscriptionDefinition
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion
    name = 'SubscriptionDefinition'
