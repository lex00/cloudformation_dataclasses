"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DBName:
    """The database name"""

    resource: Parameter
    type = STRING
    description = 'The database name'
    default = 'MyDatabase'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 64
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'


@cloudformation_dataclass
class DBUser:
    """The database admin account username"""

    resource: Parameter
    type = STRING
    description = 'The database admin account username'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 16
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'
    no_echo = True


@cloudformation_dataclass
class DBAllocatedStorage:
    """The size of the database (Gb)"""

    resource: Parameter
    type = NUMBER
    description = 'The size of the database (Gb)'
    default = '5'
    min_value = 5
    max_value = 1024
    constraint_description = 'must be between 5 and 1024Gb.'


@cloudformation_dataclass
class DBInstanceClass:
    """The database instance type"""

    resource: Parameter
    type = STRING
    description = 'The database instance type'
    default = 'db.t3.medium'
    constraint_description = 'must select a valid database instance type.'


@cloudformation_dataclass
class EC2SecurityGroup:
    """The EC2 security group that contains instances that need access to the database"""

    resource: Parameter
    type = STRING
    description = 'The EC2 security group that contains instances that need access to the database'
    default = 'default'
    allowed_pattern = '[a-zA-Z0-9\\-]+'
    constraint_description = 'must be a valid security group name.'


@cloudformation_dataclass
class MultiAZ:
    """Multi-AZ master database"""

    resource: Parameter
    type = STRING
    description = 'Multi-AZ master database'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]
    constraint_description = 'must be true or false.'


@cloudformation_dataclass
class EnableReadReplica:
    """Enable the ReadReplica"""

    resource: Parameter
    type = STRING
    description = 'Enable the ReadReplica'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]
    constraint_description = 'must be true or false.'


@cloudformation_dataclass
class IsEC2VPCCondition:
    resource: TemplateCondition
    logical_id = 'IsEC2VPC'
    expression = Or(conditions=[Equals(AWS_REGION, 'eu-central-1'), Equals(AWS_REGION, 'cn-north-1')])


@cloudformation_dataclass
class EnableReadReplicaCondition:
    resource: TemplateCondition
    logical_id = 'EnableReadReplica'
    expression = Equals(ref(EnableReadReplica), 'true')
