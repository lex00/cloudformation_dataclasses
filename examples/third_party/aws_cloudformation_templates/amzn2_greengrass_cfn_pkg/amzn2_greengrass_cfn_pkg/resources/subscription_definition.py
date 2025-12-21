from __future__ import annotations

"""SubscriptionDefinition - AWS::Greengrass::SubscriptionDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubscriptionDefinitionSubscription:
    resource: Subscription
    id = 'Subscription1'
    source = 'cloud'
    subject = Join('/', [
    ref(CoreName),
    'in',
])
    target: Ref[GGSampleFunctionVersion] = ref()


@cloudformation_dataclass
class SubscriptionDefinitionSubscription1:
    resource: Subscription
    id = 'Subscription2'
    source: Ref[GGSampleFunctionVersion] = ref()
    subject = Join('/', [
    ref(CoreName),
    'out',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscription2:
    resource: Subscription
    id = 'Subscription3'
    source: Ref[GGSampleFunctionVersion] = ref()
    subject = Join('/', [
    ref(CoreName),
    'telem',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscriptionDefinitionVersion:
    resource: SubscriptionDefinitionVersion
    subscriptions = [SubscriptionDefinitionSubscription, SubscriptionDefinitionSubscription1, SubscriptionDefinitionSubscription2]


@cloudformation_dataclass
class SubscriptionDefinition:
    """AWS::Greengrass::SubscriptionDefinition resource."""

    resource: greengrass.SubscriptionDefinition
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion
    name = 'SubscriptionDefinition'
