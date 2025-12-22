"""GreengrassGroup - AWS::Greengrass::Group resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassGroupGroupVersion:
    resource: greengrass.group.GroupVersion
    core_definition_version_arn = ref(GreengrassCoreDefinitionVersion)
    function_definition_version_arn = get_att(FunctionDefinition, "LatestVersionArn")
    subscription_definition_version_arn = get_att(SubscriptionDefinition, "LatestVersionArn")


@cloudformation_dataclass
class GreengrassGroup:
    """AWS::Greengrass::Group resource."""

    resource: greengrass.Group
    initial_version = GreengrassGroupGroupVersion
    name = ref(CoreName)
    role_arn = get_att(GreengrassResourceRole, "Arn")
