"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import CreateDirectoryAlias, CreateDirectoryConsoleDelegatedAccessRoles, DirectoryAlias, DirectoryConsoleDelegatedAccessRolesConditionCondition, DirectoryID, DirectoryMonitoringEmail, DirectoryMonitoringSNSTopicKMSKey, DirectoryMonitoringSNSTopicKMSKeyConditionCondition, EnableDirectorySSO, LambdaFunctionName, LambdaLogLevel, LambdaLogsCloudWatchKMSKey, LambdaLogsCloudWatchKMSKeyConditionCondition, LambdaLogsLogGroupRetention, LambdaS3BucketName, LambdaZipFileName, SecurityGroups, Subnets
from .outputs import DirectoryAliasUrlOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This templates updates the settings for an AD Connector or AWS Managed AD directory. Tasks accomplied, (1) enables directory monitoring (2) option to create a custom access url (alias) (3) option to enable SSO via directory services. Note, deleting the directory, will only remove directory monitoring, directory SSO or alias settings will not be touched.',
        parameters=[CreateDirectoryConsoleDelegatedAccessRoles, CreateDirectoryAlias, DirectoryAlias, DirectoryID, DirectoryMonitoringEmail, DirectoryMonitoringSNSTopicKMSKey, EnableDirectorySSO, LambdaFunctionName, LambdaLogLevel, LambdaLogsLogGroupRetention, LambdaLogsCloudWatchKMSKey, LambdaS3BucketName, LambdaZipFileName, Subnets, SecurityGroups],
        outputs=[DirectoryAliasUrlOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
