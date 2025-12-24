"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AutoScalingGroupOutput:
    """AutoScaling Group Name"""

    resource: Output
    value = ref(AutoScalingGroup)
    description = 'AutoScaling Group Name'
    export_name = Sub('${AWS::StackName}-AutoScalingGroup')


@cloudformation_dataclass
class StackNameOutput:
    """Stack Name"""

    resource: Output
    value = AWS_STACK_NAME
    description = 'Stack Name'


@cloudformation_dataclass
class URLOutput:
    """The URL of the website"""

    resource: Output
    value = Join('', [
    'http://',
    get_att(ElasticLoadBalancer, "DNSName"),
])
    description = 'The URL of the website'
