from __future__ import annotations

"""DirectorySettingsResource - Custom::DirectorySettingsResource resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectorySettingsResource:
    """Custom::DirectorySettingsResource resource."""

    # Unknown resource type: Custom::DirectorySettingsResource
    resource: CloudFormationResource
    service_token = get_att(DirectorySettingsLambdaFunction, "Arn")
    directory_id = ref(DirectoryID)
    create_directory_alias = ref(CreateDirectoryAlias)
    enable_directory_sso = ref(EnableDirectorySSO)
    directory_alias = ref(DirectoryAlias)
    directory_monitoring_topic_name = get_att(DirectoryMonitoringTopic, "TopicName")
