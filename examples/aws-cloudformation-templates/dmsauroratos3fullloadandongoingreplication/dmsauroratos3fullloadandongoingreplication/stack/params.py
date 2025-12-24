"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ClientIP:
    """The IP address range that can be used to connect to the RDS instances from your local machine. It must be a valid IP CIDR range of the form x.x.x.x/x. Pls get your address using checkip.amazonaws.com or whatsmyip.org"""

    resource: Parameter
    type = STRING
    description = 'The IP address range that can be used to connect to the RDS instances from your local machine. It must be a valid IP CIDR range of the form x.x.x.x/x. Pls get your address using checkip.amazonaws.com or whatsmyip.org'
    default = '0.0.0.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'It must be a valid IP CIDR range of the form x.x.x.x/x. Suggest to enable access to your IP address only. Pls get your address using checkip.amazonaws.com or whatsmyip.org.'


@cloudformation_dataclass
class ExistsDMSVPCRole:
    """If the dms-vpc-role exists in your account, please enter Y, else enter N"""

    resource: Parameter
    type = STRING
    description = 'If the dms-vpc-role exists in your account, please enter Y, else enter N'
    default = 'N'
    allowed_pattern = '[YN]'
    min_length = 1
    max_length = 1
    constraint_description = 'Permitted value is Y or N.'


@cloudformation_dataclass
class ExistsDMSCloudwatchRole:
    """If the dms-cloudwatch-logs-role exists in your account, please enter Y, else enter N"""

    resource: Parameter
    type = STRING
    description = 'If the dms-cloudwatch-logs-role exists in your account, please enter Y, else enter N'
    default = 'N'
    allowed_pattern = '[YN]'
    min_length = 1
    max_length = 1
    constraint_description = 'Permitted value is Y or N.'


@cloudformation_dataclass
class SnapshotIdentifier:
    """The ARN of the Aurora DB Cluster Snapshot used to populate the Aurora DB Cluster that will be used as the source for the DMS task."""

    resource: Parameter
    type = STRING
    description = 'The ARN of the Aurora DB Cluster Snapshot used to populate the Aurora DB Cluster that will be used as the source for the DMS task.'
    default = 'arn:aws:rds:us-east-1:01234567890123:cluster-snapshot:dms-sampledb-snapshot'


@cloudformation_dataclass
class NotExistsDMSVPCRoleCondition:
    resource: Condition
    expression = Equals(ref(ExistsDMSVPCRole), 'N')


@cloudformation_dataclass
class NotExistsDMSCloudwatchRoleCondition:
    resource: Condition
    expression = Equals(ref(ExistsDMSCloudwatchRole), 'N')
