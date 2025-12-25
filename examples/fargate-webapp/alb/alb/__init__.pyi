"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import ARN, ARN_EQUALS, ARN_LIKE, AWS_ACCOUNT_ID, AWS_NOTIFICATION_ARNS, AWS_NO_VALUE, AWS_PARTITION, AWS_REGION, AWS_STACK_ID, AWS_STACK_NAME, AWS_URL_SUFFIX, BOOL, Base64, Cidr, CloudFormationResource, Condition, ConditionOperator, DenyStatement, FindInMap, GetAZs, GetAtt, IP_ADDRESS, If, ImportValue, IpProtocol, Join, Mapping, NUMBER, Output, Parameter, ParameterType, PolicyDocument, PolicyStatement, Ref, ResourceRegistry, STRING, STRING_EQUALS, STRING_LIKE, STRING_NOT_EQUALS, STRING_NOT_LIKE, Select, Split, Sub, Tag, Template, Transform, cloudformation_dataclass, get_att, ref, registry, setup_resources
from cloudformation_dataclasses.aws import ec2, elasticloadbalancingv2, route53
from cloudformation_dataclasses.aws.ec2 import security_group
from cloudformation_dataclasses.aws.elasticloadbalancingv2 import listener

from .stack.params import CertificateArnParam as CertificateArnParam
from .stack.params import DomainNameParam as DomainNameParam
from .stack.params import HostedZoneIdParam as HostedZoneIdParam
from .stack.params import PublicSubnetIdsParam as PublicSubnetIdsParam
from .stack.params import VpcIdParam as VpcIdParam
from .stack.alb import AlbSecurityGroup as AlbSecurityGroup
from .stack.alb import ApplicationLoadBalancer as ApplicationLoadBalancer
from .stack.alb import DnsRecord as DnsRecord
from .stack.alb import DnsRecordAliasTarget as DnsRecordAliasTarget
from .stack.alb import HttpIngress as HttpIngress
from .stack.alb import HttpListener as HttpListener
from .stack.alb import HttpRedirectAction as HttpRedirectAction
from .stack.alb import HttpToHttpsRedirectConfig as HttpToHttpsRedirectConfig
from .stack.alb import HttpsForwardAction as HttpsForwardAction
from .stack.alb import HttpsIngress as HttpsIngress
from .stack.alb import HttpsListener as HttpsListener
from .stack.alb import HttpsListenerCertificate as HttpsListenerCertificate
from .stack.alb import TargetGroup as TargetGroup
from .stack.network import AlbSecurityGroup as AlbSecurityGroup
from .stack.network import ApplicationLoadBalancer as ApplicationLoadBalancer
from .stack.network import DnsRecord as DnsRecord
from .stack.network import DnsRecordAliasTarget as DnsRecordAliasTarget
from .stack.network import HttpIngress as HttpIngress
from .stack.network import HttpListener as HttpListener
from .stack.network import HttpRedirectAction as HttpRedirectAction
from .stack.network import HttpToHttpsRedirectConfig as HttpToHttpsRedirectConfig
from .stack.network import HttpsForwardAction as HttpsForwardAction
from .stack.network import HttpsIngress as HttpsIngress
from .stack.network import HttpsListener as HttpsListener
from .stack.network import HttpsListenerCertificate as HttpsListenerCertificate
from .stack.network import TargetGroup as TargetGroup

__all__: list[str] = ['ARN', 'ARN_EQUALS', 'ARN_LIKE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'AlbSecurityGroup', 'ApplicationLoadBalancer', 'BOOL', 'Base64', 'CertificateArnParam', 'Cidr', 'CloudFormationResource', 'Condition', 'ConditionOperator', 'DenyStatement', 'DnsRecord', 'DnsRecordAliasTarget', 'DomainNameParam', 'FindInMap', 'GetAZs', 'GetAtt', 'HostedZoneIdParam', 'HttpIngress', 'HttpListener', 'HttpRedirectAction', 'HttpToHttpsRedirectConfig', 'HttpsForwardAction', 'HttpsIngress', 'HttpsListener', 'HttpsListenerCertificate', 'IP_ADDRESS', 'If', 'ImportValue', 'IpProtocol', 'Join', 'Mapping', 'NUMBER', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'PublicSubnetIdsParam', 'Ref', 'ResourceRegistry', 'STRING', 'STRING_EQUALS', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_LIKE', 'Select', 'Split', 'Sub', 'Tag', 'TargetGroup', 'Template', 'Transform', 'VpcIdParam', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancingv2', 'get_att', 'listener', 'ref', 'registry', 'route53', 'security_group', 'setup_resources']
