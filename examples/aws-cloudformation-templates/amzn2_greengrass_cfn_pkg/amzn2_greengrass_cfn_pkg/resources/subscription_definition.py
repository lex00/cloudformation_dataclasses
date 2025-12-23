"""SubscriptionDefinition - AWS::Greengrass::SubscriptionDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubscriptionDefinition:
    """AWS::Greengrass::SubscriptionDefinition resource."""

    resource: greengrass.SubscriptionDefinition
    initial_version = {
        'Subscriptions': [
            {
                'Id': 'Subscription1',
                'Source': 'cloud',
                'Subject': Join('/', [
    ref(CoreName),
    'in',
]),
                'Target': ref(GGSampleFunctionVersion),
            },
            {
                'Id': 'Subscription2',
                'Source': ref(GGSampleFunctionVersion),
                'Subject': Join('/', [
    ref(CoreName),
    'out',
]),
                'Target': 'cloud',
            },
            {
                'Id': 'Subscription3',
                'Source': ref(GGSampleFunctionVersion),
                'Subject': Join('/', [
    ref(CoreName),
    'telem',
]),
                'Target': 'cloud',
            },
        ],
    }
    name = 'SubscriptionDefinition'
