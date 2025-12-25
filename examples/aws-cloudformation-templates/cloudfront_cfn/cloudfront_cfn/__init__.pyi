"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
    DenyStatement,
    Output,
    Parameter,
    ParameterType,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    cloudfront,
    ec2,
    elasticloadbalancingv2,
    iam,
    kms,
    lambda_,
    s3,
)
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .main import ALBExternalAccessSG as ALBExternalAccessSG
from .main import ALBExternalAccessSGAssociationParameter as ALBExternalAccessSGAssociationParameter
from .main import ALBExternalAccessSGAssociationParameter1 as ALBExternalAccessSGAssociationParameter1
from .main import CloudFrontDistribution as CloudFrontDistribution
from .main import CloudFrontDistributionCookies as CloudFrontDistributionCookies
from .main import CloudFrontDistributionCustomOriginConfig as CloudFrontDistributionCustomOriginConfig
from .main import CloudFrontDistributionDefaultCacheBehavior as CloudFrontDistributionDefaultCacheBehavior
from .main import CloudFrontDistributionDistributionConfig as CloudFrontDistributionDistributionConfig
from .main import CloudFrontDistributionForwardedValues as CloudFrontDistributionForwardedValues
from .main import CloudFrontDistributionLambdaFunctionAssociation as CloudFrontDistributionLambdaFunctionAssociation
from .main import CloudFrontDistributionLogging as CloudFrontDistributionLogging
from .main import CloudFrontDistributionOrigin as CloudFrontDistributionOrigin
from .main import CloudFrontDistributionViewerCertificate as CloudFrontDistributionViewerCertificate
from .main import EC2Instance as EC2Instance
from .main import EC2InstanceAssociationParameter as EC2InstanceAssociationParameter
from .main import EC2InstanceAssociationParameter1 as EC2InstanceAssociationParameter1
from .main import EC2InstanceBlockDeviceMapping as EC2InstanceBlockDeviceMapping
from .main import EC2InstanceEbs as EC2InstanceEbs
from .main import EC2InstanceSG as EC2InstanceSG
from .main import EC2InstanceSGAssociationParameter as EC2InstanceSGAssociationParameter
from .main import EC2InstanceSGAssociationParameter1 as EC2InstanceSGAssociationParameter1
from .main import HTTPSTcpIn as HTTPSTcpIn
from .main import HTTPTcpIn as HTTPTcpIn
from .main import LambdaEdgeFunction as LambdaEdgeFunction
from .main import LambdaEdgeFunctionCode as LambdaEdgeFunctionCode
from .main import LambdaEdgeVersion as LambdaEdgeVersion
from .main import OriginALB as OriginALB
from .main import OriginALBHttpsListener as OriginALBHttpsListener
from .main import OriginALBHttpsListenerAction as OriginALBHttpsListenerAction
from .main import OriginALBHttpsListenerCertificate as OriginALBHttpsListenerCertificate
from .main import OriginALBHttpsListenerRule as OriginALBHttpsListenerRule
from .main import OriginALBHttpsListenerRuleAction as OriginALBHttpsListenerRuleAction
from .main import OriginALBHttpsListenerRuleRuleCondition as OriginALBHttpsListenerRuleRuleCondition
from .main import OriginALBLoadBalancerAttribute as OriginALBLoadBalancerAttribute
from .main import OriginALBLoadBalancerAttribute1 as OriginALBLoadBalancerAttribute1
from .main import OriginALBLoadBalancerAttribute2 as OriginALBLoadBalancerAttribute2
from .main import OriginALBLoadBalancerAttribute3 as OriginALBLoadBalancerAttribute3
from .main import OriginALBLoadBalancerAttribute4 as OriginALBLoadBalancerAttribute4
from .main import OriginALBTG as OriginALBTG
from .main import OriginALBTGLoadBalancerAttribute as OriginALBTGLoadBalancerAttribute
from .main import OriginALBTGLoadBalancerAttribute1 as OriginALBTGLoadBalancerAttribute1
from .main import OriginALBTGLoadBalancerAttribute2 as OriginALBTGLoadBalancerAttribute2
from .main import OriginALBTGTargetDescription as OriginALBTGTargetDescription
from .main import Tcp8080In as Tcp8080In
from .main import Tcp8080Out as Tcp8080Out
from .outputs import ALBExternalAccessSGIDOutput as ALBExternalAccessSGIDOutput
from .outputs import AdministratorAccessIAMRoleOutput as AdministratorAccessIAMRoleOutput
from .outputs import AlternateDomainNamesOutput as AlternateDomainNamesOutput
from .outputs import CloudFrontEndpointOutput as CloudFrontEndpointOutput
from .outputs import EC2InstanceDNSOutput as EC2InstanceDNSOutput
from .outputs import EC2InstanceIDOutput as EC2InstanceIDOutput
from .outputs import EC2InstanceIPOutput as EC2InstanceIPOutput
from .outputs import EC2InstanceSGIDOutput as EC2InstanceSGIDOutput
from .outputs import LambdaEdgeFunctionARNOutput as LambdaEdgeFunctionARNOutput
from .outputs import LambdaEdgeFunctionOutput as LambdaEdgeFunctionOutput
from .outputs import LambdaEdgeVersionOutput as LambdaEdgeVersionOutput
from .outputs import LoggingBucketKMSKeyOutput as LoggingBucketKMSKeyOutput
from .outputs import LoggingBucketOutput as LoggingBucketOutput
from .outputs import OriginALBOutput as OriginALBOutput
from .params import ACMCertificateIdentifier as ACMCertificateIdentifier
from .params import ALBAttributeDeletionProtection as ALBAttributeDeletionProtection
from .params import ALBAttributeIdleTimeOut as ALBAttributeIdleTimeOut
from .params import ALBAttributeRoutingHttp2 as ALBAttributeRoutingHttp2
from .params import ALBScheme as ALBScheme
from .params import ALBTargetGroupAttributeDeregistration as ALBTargetGroupAttributeDeregistration
from .params import ALBTargetGroupHealthCheckIntervalSeconds as ALBTargetGroupHealthCheckIntervalSeconds
from .params import ALBTargetGroupHealthCheckTimeoutSeconds as ALBTargetGroupHealthCheckTimeoutSeconds
from .params import ALBTargetGroupHealthyThresholdCount as ALBTargetGroupHealthyThresholdCount
from .params import ALBTargetGroupUnhealthyThresholdCount as ALBTargetGroupUnhealthyThresholdCount
from .params import ALBType as ALBType
from .params import AlternateDomainNames as AlternateDomainNames
from .params import AppName as AppName
from .params import BootVolSize as BootVolSize
from .params import BootVolType as BootVolType
from .params import Compress as Compress
from .params import DefaultTTL as DefaultTTL
from .params import EC2ImageId as EC2ImageId
from .params import EC2InstanceType as EC2InstanceType
from .params import Environment as Environment
from .params import ForwardCookies as ForwardCookies
from .params import HealthCheckPath as HealthCheckPath
from .params import HealthCheckProtocol as HealthCheckProtocol
from .params import IPV6Enabled as IPV6Enabled
from .params import KeyPairName as KeyPairName
from .params import LambdaEventType as LambdaEventType
from .params import LoggingBucketVersioning as LoggingBucketVersioning
from .params import MaxTTL as MaxTTL
from .params import MinTTL as MinTTL
from .params import MinimumProtocolVersion as MinimumProtocolVersion
from .params import OriginALBTGPort as OriginALBTGPort
from .params import OriginKeepaliveTimeout as OriginKeepaliveTimeout
from .params import OriginProtocolPolicy as OriginProtocolPolicy
from .params import OriginReadTimeout as OriginReadTimeout
from .params import PriceClass as PriceClass
from .params import PublicSubnetId1 as PublicSubnetId1
from .params import PublicSubnetId2 as PublicSubnetId2
from .params import QueryString as QueryString
from .params import SslSupportMethod as SslSupportMethod
from .params import ViewerProtocolPolicy as ViewerProtocolPolicy
from .params import VpcId as VpcId
from .security import AdministratorAccessIAMRole as AdministratorAccessIAMRole
from .security import AdministratorAccessIAMRoleAllowStatement0 as AdministratorAccessIAMRoleAllowStatement0
from .security import AdministratorAccessIAMRoleAssumeRolePolicyDocument as AdministratorAccessIAMRoleAssumeRolePolicyDocument
from .security import LambdaEdgeIAMRole as LambdaEdgeIAMRole
from .security import LambdaEdgeIAMRoleAllowStatement0 as LambdaEdgeIAMRoleAllowStatement0
from .security import LambdaEdgeIAMRoleAllowStatement0_1 as LambdaEdgeIAMRoleAllowStatement0_1
from .security import LambdaEdgeIAMRoleAssumeRolePolicyDocument as LambdaEdgeIAMRoleAssumeRolePolicyDocument
from .security import LambdaEdgeIAMRolePolicies0PolicyDocument as LambdaEdgeIAMRolePolicies0PolicyDocument
from .security import LambdaEdgeIAMRolePolicy as LambdaEdgeIAMRolePolicy
from .security import LoggingBucketKMSKey as LoggingBucketKMSKey
from .security import LoggingBucketKMSKeyAlias as LoggingBucketKMSKeyAlias
from .security import LoggingBucketKMSKeyAllowStatement0 as LoggingBucketKMSKeyAllowStatement0
from .security import LoggingBucketKMSKeyAllowStatement1 as LoggingBucketKMSKeyAllowStatement1
from .security import LoggingBucketKMSKeyKeyPolicy as LoggingBucketKMSKeyKeyPolicy
from .storage import LoggingBucket as LoggingBucket
from .storage import LoggingBucketBucketEncryption as LoggingBucketBucketEncryption
from .storage import LoggingBucketDeleteMarkerReplication as LoggingBucketDeleteMarkerReplication
from .storage import LoggingBucketOwnershipControls as LoggingBucketOwnershipControls
from .storage import LoggingBucketOwnershipControlsRule as LoggingBucketOwnershipControlsRule
from .storage import LoggingBucketPolicy as LoggingBucketPolicy
from .storage import LoggingBucketPolicyAllowStatement0 as LoggingBucketPolicyAllowStatement0
from .storage import LoggingBucketPolicyDenyStatement1 as LoggingBucketPolicyDenyStatement1
from .storage import LoggingBucketPolicyPolicyDocument as LoggingBucketPolicyPolicyDocument
from .storage import LoggingBucketPublicAccessBlockConfiguration as LoggingBucketPublicAccessBlockConfiguration
from .storage import LoggingBucketServerSideEncryptionByDefault as LoggingBucketServerSideEncryptionByDefault
from .storage import LoggingBucketServerSideEncryptionRule as LoggingBucketServerSideEncryptionRule

__all__: list[str] = ['ACMCertificateIdentifier', 'ALBAttributeDeletionProtection', 'ALBAttributeIdleTimeOut', 'ALBAttributeRoutingHttp2', 'ALBExternalAccessSG', 'ALBExternalAccessSGAssociationParameter', 'ALBExternalAccessSGAssociationParameter1', 'ALBExternalAccessSGIDOutput', 'ALBScheme', 'ALBTargetGroupAttributeDeregistration', 'ALBTargetGroupHealthCheckIntervalSeconds', 'ALBTargetGroupHealthCheckTimeoutSeconds', 'ALBTargetGroupHealthyThresholdCount', 'ALBTargetGroupUnhealthyThresholdCount', 'ALBType', 'AdministratorAccessIAMRole', 'AdministratorAccessIAMRoleAllowStatement0', 'AdministratorAccessIAMRoleAssumeRolePolicyDocument', 'AdministratorAccessIAMRoleOutput', 'AlternateDomainNames', 'AlternateDomainNamesOutput', 'AppName', 'BOOL', 'BootVolSize', 'BootVolType', 'CloudFrontDistribution', 'CloudFrontDistributionCookies', 'CloudFrontDistributionCustomOriginConfig', 'CloudFrontDistributionDefaultCacheBehavior', 'CloudFrontDistributionDistributionConfig', 'CloudFrontDistributionForwardedValues', 'CloudFrontDistributionLambdaFunctionAssociation', 'CloudFrontDistributionLogging', 'CloudFrontDistributionOrigin', 'CloudFrontDistributionViewerCertificate', 'CloudFrontEndpointOutput', 'Compress', 'DefaultTTL', 'DenyStatement', 'EC2ImageId', 'EC2Instance', 'EC2InstanceAssociationParameter', 'EC2InstanceAssociationParameter1', 'EC2InstanceBlockDeviceMapping', 'EC2InstanceDNSOutput', 'EC2InstanceEbs', 'EC2InstanceIDOutput', 'EC2InstanceIPOutput', 'EC2InstanceSG', 'EC2InstanceSGAssociationParameter', 'EC2InstanceSGAssociationParameter1', 'EC2InstanceSGIDOutput', 'EC2InstanceType', 'Environment', 'ForwardCookies', 'HTTPSTcpIn', 'HTTPTcpIn', 'HealthCheckPath', 'HealthCheckProtocol', 'IPV6Enabled', 'KeyPairName', 'LambdaEdgeFunction', 'LambdaEdgeFunctionARNOutput', 'LambdaEdgeFunctionCode', 'LambdaEdgeFunctionOutput', 'LambdaEdgeIAMRole', 'LambdaEdgeIAMRoleAllowStatement0', 'LambdaEdgeIAMRoleAllowStatement0_1', 'LambdaEdgeIAMRoleAssumeRolePolicyDocument', 'LambdaEdgeIAMRolePolicies0PolicyDocument', 'LambdaEdgeIAMRolePolicy', 'LambdaEdgeVersion', 'LambdaEdgeVersionOutput', 'LambdaEventType', 'LoggingBucket', 'LoggingBucketBucketEncryption', 'LoggingBucketDeleteMarkerReplication', 'LoggingBucketKMSKey', 'LoggingBucketKMSKeyAlias', 'LoggingBucketKMSKeyAllowStatement0', 'LoggingBucketKMSKeyAllowStatement1', 'LoggingBucketKMSKeyKeyPolicy', 'LoggingBucketKMSKeyOutput', 'LoggingBucketOutput', 'LoggingBucketOwnershipControls', 'LoggingBucketOwnershipControlsRule', 'LoggingBucketPolicy', 'LoggingBucketPolicyAllowStatement0', 'LoggingBucketPolicyDenyStatement1', 'LoggingBucketPolicyPolicyDocument', 'LoggingBucketPublicAccessBlockConfiguration', 'LoggingBucketServerSideEncryptionByDefault', 'LoggingBucketServerSideEncryptionRule', 'LoggingBucketVersioning', 'MaxTTL', 'MinTTL', 'MinimumProtocolVersion', 'OriginALB', 'OriginALBHttpsListener', 'OriginALBHttpsListenerAction', 'OriginALBHttpsListenerCertificate', 'OriginALBHttpsListenerRule', 'OriginALBHttpsListenerRuleAction', 'OriginALBHttpsListenerRuleRuleCondition', 'OriginALBLoadBalancerAttribute', 'OriginALBLoadBalancerAttribute1', 'OriginALBLoadBalancerAttribute2', 'OriginALBLoadBalancerAttribute3', 'OriginALBLoadBalancerAttribute4', 'OriginALBOutput', 'OriginALBTG', 'OriginALBTGLoadBalancerAttribute', 'OriginALBTGLoadBalancerAttribute1', 'OriginALBTGLoadBalancerAttribute2', 'OriginALBTGPort', 'OriginALBTGTargetDescription', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy', 'OriginReadTimeout', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'PriceClass', 'PublicSubnetId1', 'PublicSubnetId2', 'QueryString', 'STRING', 'ServerSideEncryption', 'SslSupportMethod', 'Sub', 'Tcp8080In', 'Tcp8080Out', 'Template', 'ViewerProtocolPolicy', 'VpcId', 'cloudformation_dataclass', 'cloudfront', 'ec2', 'elasticloadbalancingv2', 'get_att', 'iam', 'kms', 'lambda_', 'ref', 's3', 'setup_resources']
