"""Security resources: ExecutionRoleBuilderMacroTestRole."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ExecutionRoleBuilderMacroTestRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    type_ = 'Lambda'
    name = 'ExecutionRoleForAppA'
    path = '/boundedexecroles/'
    permissions_boundary = ref(PermissionBoundaryArn)
    permissions = [{
        'ReadOnly': 'arn:aws:s3:::mygreatbucket1',
    }, {
        'ReadWrite': 'arn:aws:dynamodb:us-west-2:123456789012:table/table1',
    }, {
        'ReadOnly': 'arn:aws:ssm:us-west-2:123456789012:parameter/dev/myapp1/*',
    }, {
        'ReadOnly': 'arn:aws:kms:us-west-2:123456789012:key/a8f4be2b-5fcd-zzzz-yyyy-xxxxxxxxxxxx',
    }]
