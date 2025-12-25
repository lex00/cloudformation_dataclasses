"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    dms,
    ec2,
    iam,
    rds,
    s3,
)
from cloudformation_dataclasses.aws.dms import ReplicationInstance, ReplicationSubnetGroup, ReplicationTask
from cloudformation_dataclasses.aws.ec2 import Subnet, SubnetRouteTableAssociation, VPCGatewayAttachment
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_ID,
    AWS_STACK_NAME,
    Equals,
    GetAZs,
    Select,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .database import AuroraCluster as AuroraCluster
from .database import AuroraDB as AuroraDB
from .database import AuroraDBSubnetGroup as AuroraDBSubnetGroup
from .database import AuroraDBTagFormat as AuroraDBTagFormat
from .main import AuroraSourceEndpoint as AuroraSourceEndpoint
from .main import DMSReplicationInstance as DMSReplicationInstance
from .main import DMSReplicationSubnetGroup as DMSReplicationSubnetGroup
from .main import DMSReplicationTask as DMSReplicationTask
from .main import S3TargetEndpoint as S3TargetEndpoint
from .main import S3TargetEndpointRedshiftSettings as S3TargetEndpointRedshiftSettings
from .network import AttachGateway as AttachGateway
from .network import AuroraSecurityGroup as AuroraSecurityGroup
from .network import AuroraSecurityGroupEgress as AuroraSecurityGroupEgress
from .network import AuroraSecurityGroupEgress1 as AuroraSecurityGroupEgress1
from .network import DBSubnet1 as DBSubnet1
from .network import DBSubnet1AssociationParameter as DBSubnet1AssociationParameter
from .network import DBSubnet2 as DBSubnet2
from .network import DBSubnet2AssociationParameter as DBSubnet2AssociationParameter
from .network import DMSSecurityGroup as DMSSecurityGroup
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import Route as Route
from .network import RouteTable as RouteTable
from .network import RouteTableAssociationParameter as RouteTableAssociationParameter
from .network import SubnetRouteTableAssociation as SubnetRouteTableAssociation
from .network import SubnetRouteTableAssociation1 as SubnetRouteTableAssociation1
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .network import VPCAssociationParameter1 as VPCAssociationParameter1
from .outputs import AuroraEndpointOutput as AuroraEndpointOutput
from .outputs import RegionNameOutput as RegionNameOutput
from .outputs import S3BucketNameOutput as S3BucketNameOutput
from .outputs import StackNameOutput as StackNameOutput
from .params import ClientIP as ClientIP
from .params import ExistsDMSCloudwatchRole as ExistsDMSCloudwatchRole
from .params import ExistsDMSVPCRole as ExistsDMSVPCRole
from .params import NotExistsDMSCloudwatchRoleCondition as NotExistsDMSCloudwatchRoleCondition
from .params import NotExistsDMSVPCRoleCondition as NotExistsDMSVPCRoleCondition
from .params import SnapshotIdentifier as SnapshotIdentifier
from .security import DMSCloudwatchRole as DMSCloudwatchRole
from .security import DMSCloudwatchRoleAllowStatement0 as DMSCloudwatchRoleAllowStatement0
from .security import DMSCloudwatchRoleAssumeRolePolicyDocument as DMSCloudwatchRoleAssumeRolePolicyDocument
from .security import DMSVpcRole as DMSVpcRole
from .security import DMSVpcRoleAllowStatement0 as DMSVpcRoleAllowStatement0
from .security import DMSVpcRoleAssumeRolePolicyDocument as DMSVpcRoleAssumeRolePolicyDocument
from .security import S3TargetDMSRole as S3TargetDMSRole
from .security import S3TargetDMSRoleAllowStatement0 as S3TargetDMSRoleAllowStatement0
from .security import S3TargetDMSRoleAllowStatement0_1 as S3TargetDMSRoleAllowStatement0_1
from .security import S3TargetDMSRoleAllowStatement1 as S3TargetDMSRoleAllowStatement1
from .security import S3TargetDMSRoleAssumeRolePolicyDocument as S3TargetDMSRoleAssumeRolePolicyDocument
from .security import S3TargetDMSRolePolicies0PolicyDocument as S3TargetDMSRolePolicies0PolicyDocument
from .security import S3TargetDMSRolePolicy as S3TargetDMSRolePolicy
from .storage import S3Bucket as S3Bucket
from .storage import S3BucketBucketEncryption as S3BucketBucketEncryption
from .storage import S3BucketPublicAccessBlockConfiguration as S3BucketPublicAccessBlockConfiguration
from .storage import S3BucketServerSideEncryptionByDefault as S3BucketServerSideEncryptionByDefault
from .storage import S3BucketServerSideEncryptionRule as S3BucketServerSideEncryptionRule

__all__: list[str] = ['AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AttachGateway', 'AuroraCluster', 'AuroraDB', 'AuroraDBSubnetGroup', 'AuroraDBTagFormat', 'AuroraEndpointOutput', 'AuroraSecurityGroup', 'AuroraSecurityGroupEgress', 'AuroraSecurityGroupEgress1', 'AuroraSourceEndpoint', 'ClientIP', 'DBSubnet1', 'DBSubnet1AssociationParameter', 'DBSubnet2', 'DBSubnet2AssociationParameter', 'DMSCloudwatchRole', 'DMSCloudwatchRoleAllowStatement0', 'DMSCloudwatchRoleAssumeRolePolicyDocument', 'DMSReplicationInstance', 'DMSReplicationSubnetGroup', 'DMSReplicationTask', 'DMSSecurityGroup', 'DMSVpcRole', 'DMSVpcRoleAllowStatement0', 'DMSVpcRoleAssumeRolePolicyDocument', 'Equals', 'ExistsDMSCloudwatchRole', 'ExistsDMSVPCRole', 'GetAZs', 'InternetGateway', 'InternetGatewayAssociationParameter', 'NotExistsDMSCloudwatchRoleCondition', 'NotExistsDMSVPCRoleCondition', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'RegionNameOutput', 'ReplicationInstance', 'ReplicationSubnetGroup', 'ReplicationTask', 'Route', 'RouteTable', 'RouteTableAssociationParameter', 'S3Bucket', 'S3BucketBucketEncryption', 'S3BucketNameOutput', 'S3BucketPublicAccessBlockConfiguration', 'S3BucketServerSideEncryptionByDefault', 'S3BucketServerSideEncryptionRule', 'S3TargetDMSRole', 'S3TargetDMSRoleAllowStatement0', 'S3TargetDMSRoleAllowStatement0_1', 'S3TargetDMSRoleAllowStatement1', 'S3TargetDMSRoleAssumeRolePolicyDocument', 'S3TargetDMSRolePolicies0PolicyDocument', 'S3TargetDMSRolePolicy', 'S3TargetEndpoint', 'S3TargetEndpointRedshiftSettings', 'STRING', 'Select', 'ServerSideEncryption', 'SnapshotIdentifier', 'StackNameOutput', 'Sub', 'Subnet', 'SubnetRouteTableAssociation', 'SubnetRouteTableAssociation1', 'Template', 'TemplateCondition', 'VPC', 'VPCAssociationParameter', 'VPCAssociationParameter1', 'VPCGatewayAttachment', 'cloudformation_dataclass', 'dms', 'ec2', 'get_att', 'iam', 'rds', 'ref', 's3', 'setup_resources']
