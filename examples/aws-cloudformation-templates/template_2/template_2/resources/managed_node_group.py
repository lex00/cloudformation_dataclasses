"""ManagedNodeGroup - AWS::EKS::Nodegroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ManagedNodeGroupSsoIdentity:
    resource: eks.capability.SsoIdentity
    id = ref(LaunchTemplate)


@cloudformation_dataclass
class ManagedNodeGroupScalingConfig:
    resource: eks.nodegroup.ScalingConfig
    desired_size = 2
    max_size = 2
    min_size = 2


@cloudformation_dataclass
class ManagedNodeGroup:
    """AWS::EKS::Nodegroup resource."""

    resource: eks.Nodegroup
    ami_type = 'AL2_x86_64'
    cluster_name = ref(ControlPlane)
    instance_types = [ref(NodeGroupInstanceTypes)]
    labels = {
        'alpha.eksctl.io/cluster-name': ref(ControlPlane),
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
    }
    launch_template = ManagedNodeGroupSsoIdentity
    node_role = get_att(NodeInstanceRole, "Arn")
    nodegroup_name = Sub('ng-${AWS::StackName}')
    scaling_config = ManagedNodeGroupScalingConfig
    subnets = [ref(PrivateSubnet1), ref(PrivateSubnet2), ref(PrivateSubnet3)]
    tags = {
        'alpha.eksctl.io/nodegroup-name': Sub('ng-${AWS::StackName}'),
        'alpha.eksctl.io/nodegroup-type': 'managed',
    }
