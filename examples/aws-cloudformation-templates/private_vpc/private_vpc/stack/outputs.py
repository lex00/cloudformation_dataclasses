"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ClusterNameOutput:
    """The name of the ECS cluster"""

    resource: Output
    value = ref(ECSCluster)
    description = 'The name of the ECS cluster'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ClusterName',
])


@cloudformation_dataclass
class InternalUrlOutput:
    """The url of the internal load balancer"""

    resource: Output
    value = Join('', [
    'http://',
    get_att(PrivateLoadBalancer, "DNSName"),
])
    description = 'The url of the internal load balancer'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'InternalUrl',
])


@cloudformation_dataclass
class ExternalUrlOutput:
    """The url of the external load balancer"""

    resource: Output
    value = Join('', [
    'http://',
    get_att(PublicLoadBalancer, "DNSName"),
])
    description = 'The url of the external load balancer'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ExternalUrl',
])


@cloudformation_dataclass
class ECSRoleOutput:
    """The ARN of the ECS role"""

    resource: Output
    value = get_att(ECSRole, "Arn")
    description = 'The ARN of the ECS role'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ECSRole',
])


@cloudformation_dataclass
class ECSTaskExecutionRoleOutput:
    """The ARN of the ECS role"""

    resource: Output
    value = get_att(ECSTaskExecutionRole, "Arn")
    description = 'The ARN of the ECS role'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ECSTaskExecutionRole',
])


@cloudformation_dataclass
class PublicListenerOutput:
    """The ARN of the public load balancer's Listener"""

    resource: Output
    value = ref(PublicLoadBalancerListener)
    description = "The ARN of the public load balancer's Listener"
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicListener',
])


@cloudformation_dataclass
class PrivateListenerOutput:
    """The ARN of the private load balancer's Listener"""

    resource: Output
    value = ref(PrivateLoadBalancerListener)
    description = "The ARN of the private load balancer's Listener"
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PrivateListener',
])


@cloudformation_dataclass
class VPCIdOutput:
    """The ID of the VPC that this stack is deployed in"""

    resource: Output
    value = ref(VPC)
    description = 'The ID of the VPC that this stack is deployed in'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'VPCId',
])


@cloudformation_dataclass
class PublicSubnetOneOutput:
    """Public subnet one"""

    resource: Output
    value = ref(PublicSubnetOne)
    description = 'Public subnet one'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetOne',
])


@cloudformation_dataclass
class PublicSubnetTwoOutput:
    """Public subnet two"""

    resource: Output
    value = ref(PublicSubnetTwo)
    description = 'Public subnet two'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetTwo',
])


@cloudformation_dataclass
class PrivateSubnetOneOutput:
    """Private subnet one"""

    resource: Output
    value = ref(PrivateSubnetOne)
    description = 'Private subnet one'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PrivateSubnetOne',
])


@cloudformation_dataclass
class PrivateSubnetTwoOutput:
    """Private subnet two"""

    resource: Output
    value = ref(PrivateSubnetTwo)
    description = 'Private subnet two'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PrivateSubnetTwo',
])


@cloudformation_dataclass
class FargateContainerSecurityGroupOutput:
    """A security group used to allow Fargate containers to receive traffic"""

    resource: Output
    value = ref(FargateContainerSecurityGroup)
    description = 'A security group used to allow Fargate containers to receive traffic'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'FargateContainerSecurityGroup',
])
