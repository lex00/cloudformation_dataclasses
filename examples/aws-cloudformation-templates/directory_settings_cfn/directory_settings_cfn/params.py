"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CreateDirectoryConsoleDelegatedAccessRoles:
    """Create sample IAM ROLES that can be used to delegate users/groups access to certain areas of the AWS Management Console. User/Group assignment to these IAM roles has to be done manually via Directory Services -> Directory -> Application Management Tab."""

    resource: Parameter
    type = STRING
    description = 'Create sample IAM ROLES that can be used to delegate users/groups access to certain areas of the AWS Management Console. User/Group assignment to these IAM roles has to be done manually via Directory Services -> Directory -> Application Management Tab.'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class CreateDirectoryAlias:
    """Create an alias for the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com. NOTE, after an alias has been created, it cannot be deleted or reused. Hence if a different alias already exists, then you must use the existing alias (also shown in CloudFormation error)."""

    resource: Parameter
    type = STRING
    description = 'Create an alias for the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com. NOTE, after an alias has been created, it cannot be deleted or reused. Hence if a different alias already exists, then you must use the existing alias (also shown in CloudFormation error).'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class DirectoryAlias:
    """(Optional) Specifies an alias to be assigned to the directory, such as http://<alias>.awsapps.com. Note, after alias is created it cannot be deleted or reused. Note, will only be set, if `CreateDirectoryAlias` parameter, has a value of `Yes`."""

    resource: Parameter
    type = STRING
    description = '(Optional) Specifies an alias to be assigned to the directory, such as http://<alias>.awsapps.com. Note, after alias is created it cannot be deleted or reused. Note, will only be set, if `CreateDirectoryAlias` parameter, has a value of `Yes`.'
    allowed_pattern = '^$|^(?!d-)([\\da-zA-Z]+)([-]*[\\da-zA-Z])*$'
    max_length = 62


@cloudformation_dataclass
class DirectoryID:
    """Directory ID that will have settings updated"""

    resource: Parameter
    type = STRING
    description = 'Directory ID that will have settings updated'
    allowed_pattern = '^d-[0-9a-f]{10}$'


@cloudformation_dataclass
class DirectoryMonitoringEmail:
    """Email for SNS Topic to monitor directory changes."""

    resource: Parameter
    type = STRING
    description = 'Email for SNS Topic to monitor directory changes.'
    allowed_pattern = '^[\\w%+.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,63}$'


@cloudformation_dataclass
class DirectoryMonitoringSNSTopicKMSKey:
    """(Optional) KMS Key ID to use for encrypting the directory monitoring SNS topic messages. If empty, encryption is enabled with SNS managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ID to use for encrypting the directory monitoring SNS topic messages. If empty, encryption is enabled with SNS managing the server-side encryption keys.'
    allowed_pattern = '^$|^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$'
    constraint_description = 'Key ID example: 1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class EnableDirectorySSO:
    """Enable single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If true, "DirectoryAlias" must also be true, & "DirectoryAlias" parameter input required."""

    resource: Parameter
    type = STRING
    description = 'Enable single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If true, "DirectoryAlias" must also be true, & "DirectoryAlias" parameter input required.'
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class LambdaFunctionName:
    """Lambda Function Name for Custom Resource"""

    resource: Parameter
    type = STRING
    description = 'Lambda Function Name for Custom Resource'
    default = 'CR-DirectorySettings'
    allowed_pattern = '^[\\w-]{1,64}$'
    constraint_description = 'Max 64 alphanumeric characters. Also special characters supported [_, -]'


@cloudformation_dataclass
class LambdaLogLevel:
    """Lambda logging level"""

    resource: Parameter
    type = STRING
    description = 'Lambda logging level'
    default = 'INFO'
    allowed_values = [
    'INFO',
    'DEBUG',
]


@cloudformation_dataclass
class LambdaLogsLogGroupRetention:
    """Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs"""

    resource: Parameter
    type = STRING
    description = 'Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs'
    default = 14
    allowed_values = [
    1,
    3,
    5,
    7,
    14,
    30,
    60,
    90,
    120,
    150,
    180,
    365,
    400,
    545,
    731,
    1827,
    3653,
]


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class LambdaS3BucketName:
    """Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = 'Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Lambda S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class LambdaZipFileName:
    """Amazon S3 key of the deployment package."""

    resource: Parameter
    type = STRING
    description = 'Amazon S3 key of the deployment package.'
    default = 'directory_settings_custom_resource.zip'
    min_length = 1
    max_length = 1024


@cloudformation_dataclass
class Subnets:
    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID


@cloudformation_dataclass
class SecurityGroups:
    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID


@cloudformation_dataclass
class DirectoryConsoleDelegatedAccessRolesConditionCondition:
    resource: TemplateCondition
    logical_id = 'DirectoryConsoleDelegatedAccessRolesCondition'
    expression = Equals(ref(CreateDirectoryConsoleDelegatedAccessRoles), True)


@cloudformation_dataclass
class DirectoryMonitoringSNSTopicKMSKeyConditionCondition:
    resource: TemplateCondition
    logical_id = 'DirectoryMonitoringSNSTopicKMSKeyCondition'
    expression = Not(Equals(ref(DirectoryMonitoringSNSTopicKMSKey), ''))


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKeyConditionCondition:
    resource: TemplateCondition
    logical_id = 'LambdaLogsCloudWatchKMSKeyCondition'
    expression = Not(Equals(ref(LambdaLogsCloudWatchKMSKey), ''))
