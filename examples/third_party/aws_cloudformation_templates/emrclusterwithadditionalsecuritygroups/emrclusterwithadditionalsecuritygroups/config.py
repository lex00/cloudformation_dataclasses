"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterName:
    """Name of the cluster"""

    resource: Parameter
    type = STRING
    description = 'Name of the cluster'
    default = 'emrcluster'


@cloudformation_dataclass
class KeyName:
    """Must be an existing Keyname"""

    resource: Parameter
    type = STRING
    description = 'Must be an existing Keyname'


@cloudformation_dataclass
class MasterInstanceType:
    """Instance type to be used for the master instance."""

    resource: Parameter
    type = STRING
    description = 'Instance type to be used for the master instance.'
    default = 'm3.xlarge'


@cloudformation_dataclass
class CoreInstanceType:
    """Instance type to be used for core instances."""

    resource: Parameter
    type = STRING
    description = 'Instance type to be used for core instances.'
    default = 'm3.xlarge'


@cloudformation_dataclass
class NumberOfCoreInstances:
    """Must be a valid number"""

    resource: Parameter
    type = NUMBER
    description = 'Must be a valid number'
    default = 2


@cloudformation_dataclass
class SubnetID:
    """Must be a valid public subnet ID"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid public subnet ID'


@cloudformation_dataclass
class AdditionalCoreNodeSecurityGroups:
    """Comma-delimited list of additional security groups for core and task nodes"""

    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    description = 'Comma-delimited list of additional security groups for core and task nodes'


@cloudformation_dataclass
class AdditionalPrimaryNodeSecurityGroups:
    """Comma-delimited list of additional security groups for primary nodes"""

    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    description = 'Comma-delimited list of additional security groups for primary nodes'


@cloudformation_dataclass
class LogUri:
    """Must be a valid S3 URL"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid S3 URL'
    default = 's3://emrclusterlogbucket/'


@cloudformation_dataclass
class S3DataUri:
    """Must be a valid S3 bucket URL"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid S3 bucket URL'
    default = 's3://emrclusterdatabucket/'


@cloudformation_dataclass
class ReleaseLabel:
    """Must be a valid EMR release version"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid EMR release version'
    default = 'emr-5.7.0'


@cloudformation_dataclass
class Applications:
    """Please select which application will be installed on the cluster. This would be either Ganglia and spark, or Ganglia and s3 backed Hbase"""

    resource: Parameter
    type = STRING
    description = 'Please select which application will be installed on the cluster. This would be either Ganglia and spark, or Ganglia and s3 backed Hbase'
    allowed_values = [
    'Spark',
    'Hbase',
]


@cloudformation_dataclass
class SparkCondition:
    resource: Condition
    expression = Equals(ref(Applications), 'Spark')


@cloudformation_dataclass
class HbaseCondition:
    resource: Condition
    expression = Equals(ref(Applications), 'Hbase')
