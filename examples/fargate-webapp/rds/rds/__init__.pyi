"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    IpProtocol,
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.aws import ec2, rds, secretsmanager
from cloudformation_dataclasses.aws.secretsmanager import secret
from cloudformation_dataclasses.intrinsics.functions import Sub

from .stack.params import DatabaseNameParam as DatabaseNameParam
from .stack.params import PrivateSubnetIdsParam as PrivateSubnetIdsParam
from .stack.params import VpcCidrParam as VpcCidrParam
from .stack.params import VpcIdParam as VpcIdParam
from .stack.rds import DbSecret as DbSecret
from .stack.rds import DbSecretGenerateString as DbSecretGenerateString
from .stack.rds import DbSecurityGroup as DbSecurityGroup
from .stack.rds import DbSecurityGroupIngress as DbSecurityGroupIngress
from .stack.rds import DbSubnetGroup as DbSubnetGroup
from .stack.rds import PostgresInstance as PostgresInstance
from .stack.rds import SecretTargetAttachment as SecretTargetAttachment

__all__: list[str] = ['DatabaseNameParam', 'DbSecret', 'DbSecretGenerateString', 'DbSecurityGroup', 'DbSecurityGroupIngress', 'DbSubnetGroup', 'IpProtocol', 'Output', 'Parameter', 'ParameterType', 'PostgresInstance', 'PrivateSubnetIdsParam', 'STRING', 'SecretTargetAttachment', 'Sub', 'Template', 'VpcCidrParam', 'VpcIdParam', 'cloudformation_dataclass', 'ec2', 'get_att', 'rds', 'ref', 'secret', 'secretsmanager']
