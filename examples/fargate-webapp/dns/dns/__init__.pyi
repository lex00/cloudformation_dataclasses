"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import ARN, ARN_EQUALS, ARN_LIKE, AWS_ACCOUNT_ID, AWS_NOTIFICATION_ARNS, AWS_NO_VALUE, AWS_PARTITION, AWS_REGION, AWS_STACK_ID, AWS_STACK_NAME, AWS_URL_SUFFIX, BOOL, Base64, Cidr, CloudFormationResource, Condition, ConditionOperator, DenyStatement, FindInMap, GetAZs, GetAtt, IP_ADDRESS, If, ImportValue, IpProtocol, Join, Mapping, NUMBER, Output, Parameter, ParameterType, PolicyDocument, PolicyStatement, Ref, ResourceRegistry, STRING, STRING_EQUALS, STRING_LIKE, STRING_NOT_EQUALS, STRING_NOT_LIKE, Select, Split, Sub, Tag, Template, Transform, cloudformation_dataclass, get_att, ref, registry, setup_resources
from cloudformation_dataclasses.aws import certificatemanager, route53
from cloudformation_dataclasses.aws.certificatemanager import certificate

from .stack.params import DomainNameParam as DomainNameParam
from .stack.dns import Certificate as Certificate
from .stack.dns import CertificateDomainValidation as CertificateDomainValidation
from .stack.dns import HostedZone as HostedZone

__all__: list[str] = ['ARN', 'ARN_EQUALS', 'ARN_LIKE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'BOOL', 'Base64', 'Certificate', 'CertificateDomainValidation', 'Cidr', 'CloudFormationResource', 'Condition', 'ConditionOperator', 'DenyStatement', 'DomainNameParam', 'FindInMap', 'GetAZs', 'GetAtt', 'HostedZone', 'IP_ADDRESS', 'If', 'ImportValue', 'IpProtocol', 'Join', 'Mapping', 'NUMBER', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'Ref', 'ResourceRegistry', 'STRING', 'STRING_EQUALS', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_LIKE', 'Select', 'Split', 'Sub', 'Tag', 'Template', 'Transform', 'certificate', 'certificatemanager', 'cloudformation_dataclass', 'get_att', 'ref', 'registry', 'route53', 'setup_resources']
