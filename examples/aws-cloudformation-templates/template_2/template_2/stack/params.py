"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCCidrBlock:
    resource: Parameter
    type = STRING
    default = '10.0.0.0/16'


@cloudformation_dataclass
class PublicCidrBlock1:
    resource: Parameter
    type = STRING
    default = '10.0.1.0/24'


@cloudformation_dataclass
class PublicCidrBlock2:
    resource: Parameter
    type = STRING
    default = '10.0.2.0/24'


@cloudformation_dataclass
class PublicCidrBlock3:
    resource: Parameter
    type = STRING
    default = '10.0.3.0/24'


@cloudformation_dataclass
class PrivateCidrBlock1:
    resource: Parameter
    type = STRING
    default = '10.0.4.0/24'


@cloudformation_dataclass
class PrivateCidrBlock2:
    resource: Parameter
    type = STRING
    default = '10.0.5.0/24'


@cloudformation_dataclass
class PrivateCidrBlock3:
    resource: Parameter
    type = STRING
    default = '10.0.6.0/24'


@cloudformation_dataclass
class EKSClusterVersion:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class NodeGroupInstanceTypes:
    resource: Parameter
    type = STRING
    default = 't3.medium'


@cloudformation_dataclass
class ServicePrincipalPartitionMapMapping:
    resource: Mapping
    map_data = {
        'aws': {
            'EC2': 'ec2.amazonaws.com',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
        'aws-cn': {
            'EC2': 'ec2.amazonaws.com.cn',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
        'aws-us-gov': {
            'EC2': 'ec2.amazonaws.com',
            'EKS': 'eks.amazonaws.com',
            'EKSFargatePods': 'eks-fargate-pods.amazonaws.com',
        },
    }
