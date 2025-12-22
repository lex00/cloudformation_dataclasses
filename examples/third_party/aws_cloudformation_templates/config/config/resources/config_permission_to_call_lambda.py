"""ConfigPermissionToCallLambda - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigPermissionToCallLambda:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    function_name = get_att(VolumeAutoEnableIOComplianceCheck, "Arn")
    action = 'lambda:InvokeFunction'
    principal = 'config.amazonaws.com'
