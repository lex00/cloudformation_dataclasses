from __future__ import annotations

"""GreengrassGroup - AWS::Greengrass::Group resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassGroupGroupVersion:
    resource: GroupVersion
    core_definition_version_arn: Ref[GreengrassCoreDefinitionVersion] = ref()
    function_definition_version_arn: GetAtt[FunctionDefinition] = get_att("LatestVersionArn")
    subscription_definition_version_arn: GetAtt[SubscriptionDefinition] = get_att("LatestVersionArn")


@cloudformation_dataclass
class GreengrassGroup:
    """AWS::Greengrass::Group resource."""

    resource: Group
    initial_version = GreengrassGroupGroupVersion
    name = ref(CoreName)
    role_arn: GetAtt[GreengrassResourceRole] = get_att("Arn")
