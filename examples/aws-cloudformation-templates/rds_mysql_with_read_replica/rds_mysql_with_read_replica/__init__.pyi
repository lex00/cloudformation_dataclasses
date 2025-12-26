"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, rds, secretsmanager
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    AWS_REGION,
    Equals,
    If,
    Join,
    Or,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .database import MainDB as MainDB
from .database import MainDBTagFormat as MainDBTagFormat
from .database import ReplicaDB as ReplicaDB
from .database import ReplicaDBTagFormat as ReplicaDBTagFormat
from .network import DBEC2SecurityGroup as DBEC2SecurityGroup
from .network import DBEC2SecurityGroupIngress as DBEC2SecurityGroupIngress
from .outputs import DBCredentialSecretNameArnOutput as DBCredentialSecretNameArnOutput
from .outputs import EC2PlatformOutput as EC2PlatformOutput
from .outputs import JDBCConnectionStringOutput as JDBCConnectionStringOutput
from .outputs import ReplicaJDBCConnectionStringOutput as ReplicaJDBCConnectionStringOutput
from .params import DBAllocatedStorage as DBAllocatedStorage
from .params import DBInstanceClass as DBInstanceClass
from .params import DBName as DBName
from .params import DBUser as DBUser
from .params import EC2SecurityGroup as EC2SecurityGroup
from .params import EnableReadReplica as EnableReadReplica
from .params import EnableReadReplicaCondition as EnableReadReplicaCondition
from .params import IsEC2VPCCondition as IsEC2VPCCondition
from .params import MultiAZ as MultiAZ
from .security import DBCredential as DBCredential
from .security import DBCredentialGenerateSecretString as DBCredentialGenerateSecretString

__all__: list[str] = ['AWS_NO_VALUE', 'AWS_REGION', 'DBAllocatedStorage', 'DBCredential', 'DBCredentialGenerateSecretString', 'DBCredentialSecretNameArnOutput', 'DBEC2SecurityGroup', 'DBEC2SecurityGroupIngress', 'DBInstanceClass', 'DBName', 'DBUser', 'EC2PlatformOutput', 'EC2SecurityGroup', 'EnableReadReplica', 'EnableReadReplicaCondition', 'Equals', 'If', 'IsEC2VPCCondition', 'JDBCConnectionStringOutput', 'Join', 'MainDB', 'MainDBTagFormat', 'MultiAZ', 'NUMBER', 'Or', 'Output', 'Parameter', 'ReplicaDB', 'ReplicaDBTagFormat', 'ReplicaJDBCConnectionStringOutput', 'STRING', 'Sub', 'Template', 'TemplateCondition', 'cloudformation_dataclass', 'ec2', 'get_att', 'rds', 'ref', 'secretsmanager', 'setup_resources']
