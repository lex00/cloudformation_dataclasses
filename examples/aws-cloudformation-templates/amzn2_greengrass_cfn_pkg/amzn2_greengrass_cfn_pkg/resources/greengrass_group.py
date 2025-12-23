"""GreengrassGroup - AWS::Greengrass::Group resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassGroup:
    """AWS::Greengrass::Group resource."""

    resource: greengrass.Group
    initial_version = {
        'CoreDefinitionVersionArn': ref(GreengrassCoreDefinitionVersion),
        'FunctionDefinitionVersionArn': get_att(FunctionDefinition, "LatestVersionArn"),
        'SubscriptionDefinitionVersionArn': get_att(SubscriptionDefinition, "LatestVersionArn"),
    }
    name = ref(CoreName)
    role_arn = get_att(GreengrassResourceRole, "Arn")
