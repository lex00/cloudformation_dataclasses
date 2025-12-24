"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteURLOutput:
    resource: Output
    value = Sub('https://${SiteDistribution.DomainName}')


@cloudformation_dataclass
class RedirectURIOutput:
    resource: Output
    value = Sub('https://${SiteDistribution.DomainName}/index.html')


@cloudformation_dataclass
class AppNameOutput:
    resource: Output
    value = ref(AppName)


@cloudformation_dataclass
class RestApiInvokeURLOutput:
    resource: Output
    value = Sub('https://${RestApi}.execute-api.${AWS::Region}.amazonaws.com/${RestApiStage}')


@cloudformation_dataclass
class AppClientIdOutput:
    resource: Output
    value = ref(CognitoClient)


@cloudformation_dataclass
class CognitoDomainPrefixOutput:
    resource: Output
    value = ref(AppName)
