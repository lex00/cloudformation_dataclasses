"""Compute resources: ControlPlane, ControlPlaneSecurityGroupIngress, LaunchTemplate, ManagedNodeGroup."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class ControlPlaneResourcesVpcConfig:
    resource: eks.cluster.ResourcesVpcConfig
    security_group_ids = [ref(ControlPlaneSecurityGroup)]
    subnet_ids = [ref(PublicSubnet1), ref(PublicSubnet2), ref(PublicSubnet3), ref(PrivateSubnet1), ref(PrivateSubnet2), ref(PrivateSubnet3)]


@cloudformation_dataclass
class ControlPlane:
    """AWS::EKS::Cluster resource."""

    resource: eks.Cluster
    name = Sub('${AWS::StackName}-cluster')
    resources_vpc_config = ControlPlaneResourcesVpcConfig
    role_arn = get_att(EKSClusterRole, "Arn")
    version = ref(EKSClusterVersion)


@cloudformation_dataclass
class ControlPlaneSecurityGroupIngress:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(ControlPlaneSecurityGroup)
    ip_protocol = IpProtocol.ALL
    source_security_group_id = get_att(ControlPlaneSecurityGroup, "GroupId")
    source_security_group_owner_id = AWS_ACCOUNT_ID


@cloudformation_dataclass
class LaunchTemplateEbs:
    resource: ec2.launch_template.Ebs
    iops = 3000
    throughput = 125
    volume_size = 80
    volume_type = 'gp3'


@cloudformation_dataclass
class LaunchTemplateBlockDeviceMapping:
    resource: ec2.launch_template.BlockDeviceMapping
    device_name = '/dev/xvda'
    ebs = LaunchTemplateEbs


@cloudformation_dataclass
class LaunchTemplateMetadataOptions:
    resource: ec2.launch_template.MetadataOptions
    http_put_response_hop_limit = 2
    http_tokens = 'optional'


@cloudformation_dataclass
class LaunchTemplateTagSpecification:
    resource: ec2.launch_template.TagSpecification
    resource_type = 'instance'
    tags = [{
        AssociationParameter.key: 'Name',
        AssociationParameter.value: Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-name',
        AssociationParameter.value: Sub('ng-${AWS::StackName}'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-type',
        AssociationParameter.value: 'managed',
    }]


@cloudformation_dataclass
class LaunchTemplateTagSpecification1:
    resource: ec2.launch_template.TagSpecification
    resource_type = 'volume'
    tags = [{
        AssociationParameter.key: 'Name',
        AssociationParameter.value: Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-name',
        AssociationParameter.value: Sub('ng-${AWS::StackName}'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-type',
        AssociationParameter.value: 'managed',
    }]


@cloudformation_dataclass
class LaunchTemplateTagSpecification2:
    resource: ec2.launch_template.TagSpecification
    resource_type = 'network-interface'
    tags = [{
        AssociationParameter.key: 'Name',
        AssociationParameter.value: Sub('ekshandson-ng-${AWS::StackName}-Node'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-name',
        AssociationParameter.value: Sub('ng-${AWS::StackName}'),
    }, {
        AssociationParameter.key: 'alpha.eksctl.io/nodegroup-type',
        AssociationParameter.value: 'managed',
    }]


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: ec2.launch_template.LaunchTemplateData
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    metadata_options = LaunchTemplateMetadataOptions
    security_group_ids = [ref(ControlPlaneSecurityGroup)]
    tag_specifications = [LaunchTemplateTagSpecification, LaunchTemplateTagSpecification1, LaunchTemplateTagSpecification2]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateLaunchTemplateData
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')


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
