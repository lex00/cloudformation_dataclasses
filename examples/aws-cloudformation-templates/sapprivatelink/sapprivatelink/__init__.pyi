"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    NUMBER,
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
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    certificatemanager,
    ec2,
    elasticloadbalancingv2,
    iam,
    lambda_,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    AWS_REGION,
    Equals,
    If,
    Select,
    Split,
    Sub,
)

from .main import ASCPrivateLinkCertificate as ASCPrivateLinkCertificate
from .main import ASCPrivateLinkCertificateDomainValidationOption as ASCPrivateLinkCertificateDomainValidationOption
from .main import ASCPrivateLinkEnablePrivateDNS as ASCPrivateLinkEnablePrivateDNS
from .main import ASCPrivateLinkLambdaFunction as ASCPrivateLinkLambdaFunction
from .main import ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig as ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig
from .main import ASCPrivateLinkLambdaFunctionCode as ASCPrivateLinkLambdaFunctionCode
from .main import ASCPrivateLinkListener as ASCPrivateLinkListener
from .main import ASCPrivateLinkListenerAction as ASCPrivateLinkListenerAction
from .main import ASCPrivateLinkListenerCertificate as ASCPrivateLinkListenerCertificate
from .main import ASCPrivateLinkNLB as ASCPrivateLinkNLB
from .main import ASCPrivateLinkNLBLoadBalancerAttribute as ASCPrivateLinkNLBLoadBalancerAttribute
from .main import ASCPrivateLinkTargetGroup as ASCPrivateLinkTargetGroup
from .main import ASCPrivateLinkTargetGroupTargetDescription as ASCPrivateLinkTargetGroupTargetDescription
from .main import ASCPrivateLinkVPCES as ASCPrivateLinkVPCES
from .main import ASCPrivateLinkVPCESPermission as ASCPrivateLinkVPCESPermission
from .outputs import CertificateURLOutput as CertificateURLOutput
from .outputs import TargetGroupURLOutput as TargetGroupURLOutput
from .outputs import VPCEndpointServiceURLOutput as VPCEndpointServiceURLOutput
from .params import DomainName as DomainName
from .params import HealthCheckPath as HealthCheckPath
from .params import HostedZone as HostedZone
from .params import IP as IP
from .params import InVpc as InVpc
from .params import IpInVpcCondition as IpInVpcCondition
from .params import Port as Port
from .params import Protocol as Protocol
from .params import SapUseHttpsCondition as SapUseHttpsCondition
from .params import SecurityGroups as SecurityGroups
from .params import Subnets as Subnets
from .params import VpcId as VpcId
from .security import ASCPrivateLinkLambdaRole as ASCPrivateLinkLambdaRole
from .security import ASCPrivateLinkLambdaRoleAllowStatement0 as ASCPrivateLinkLambdaRoleAllowStatement0
from .security import ASCPrivateLinkLambdaRoleAllowStatement0_1 as ASCPrivateLinkLambdaRoleAllowStatement0_1
from .security import ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument as ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument
from .security import ASCPrivateLinkLambdaRolePolicies0PolicyDocument as ASCPrivateLinkLambdaRolePolicies0PolicyDocument
from .security import ASCPrivateLinkLambdaRolePolicy as ASCPrivateLinkLambdaRolePolicy

__all__: list[str] = ['ASCPrivateLinkCertificate', 'ASCPrivateLinkCertificateDomainValidationOption', 'ASCPrivateLinkEnablePrivateDNS', 'ASCPrivateLinkLambdaFunction', 'ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig', 'ASCPrivateLinkLambdaFunctionCode', 'ASCPrivateLinkLambdaRole', 'ASCPrivateLinkLambdaRoleAllowStatement0', 'ASCPrivateLinkLambdaRoleAllowStatement0_1', 'ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument', 'ASCPrivateLinkLambdaRolePolicies0PolicyDocument', 'ASCPrivateLinkLambdaRolePolicy', 'ASCPrivateLinkListener', 'ASCPrivateLinkListenerAction', 'ASCPrivateLinkListenerCertificate', 'ASCPrivateLinkNLB', 'ASCPrivateLinkNLBLoadBalancerAttribute', 'ASCPrivateLinkTargetGroup', 'ASCPrivateLinkTargetGroupTargetDescription', 'ASCPrivateLinkVPCES', 'ASCPrivateLinkVPCESPermission', 'AWS_NO_VALUE', 'AWS_REGION', 'CertificateURLOutput', 'CloudFormationResource', 'DomainName', 'Equals', 'HealthCheckPath', 'HostedZone', 'IP', 'If', 'InVpc', 'IpInVpcCondition', 'NUMBER', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'Port', 'Protocol', 'STRING', 'SapUseHttpsCondition', 'SecurityGroups', 'Select', 'Split', 'Sub', 'Subnets', 'TargetGroupURLOutput', 'Template', 'TemplateCondition', 'VPCEndpointServiceURLOutput', 'VpcId', 'certificatemanager', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancingv2', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
