"""Compute resources: ControlPlane, ControlPlaneSecurityGroupIngress, LaunchTemplate, ManagedNodeGroup."""

from .. import *  # noqa: F403


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
    ip_protocol = '-1'
    source_security_group_id = get_att(ControlPlaneSecurityGroup, "GroupId")
    source_security_group_owner_id = AWS_ACCOUNT_ID


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = {
        'BlockDeviceMappings': [{
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'Iops': 3000,
                'Throughput': 125,
                'VolumeSize': 80,
                'VolumeType': 'gp3',
            },
        }],
        'MetadataOptions': {
            'HttpPutResponseHopLimit': 2,
            'HttpTokens': 'optional',
        },
        'SecurityGroupIds': [ref(ControlPlaneSecurityGroup)],
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'network-interface',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
        ],
    }
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
