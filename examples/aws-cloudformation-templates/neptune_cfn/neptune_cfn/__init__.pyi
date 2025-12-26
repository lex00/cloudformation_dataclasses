"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
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
    cloudwatch,
    ec2,
    iam,
    neptune,
    sns,
)
from cloudformation_dataclasses.intrinsics import (
    Equals,
    If,
    ImportValue,
    Not,
    Sub,
)

from .database import NeptuneDBCluster as NeptuneDBCluster
from .database import NeptuneDBClusterParameterGroup as NeptuneDBClusterParameterGroup
from .database import NeptuneDBInstance as NeptuneDBInstance
from .database import NeptuneDBParameterGroup as NeptuneDBParameterGroup
from .database import NeptuneDBSubnetGroup as NeptuneDBSubnetGroup
from .messaging import NeptuneAlarmSubscription as NeptuneAlarmSubscription
from .messaging import NeptuneAlarmTopic as NeptuneAlarmTopic
from .monitoring import NeptunePrimaryCpuAlarm as NeptunePrimaryCpuAlarm
from .monitoring import NeptunePrimaryCpuAlarmDimension as NeptunePrimaryCpuAlarmDimension
from .monitoring import NeptunePrimaryGremlinRequestsPerSecAlarm as NeptunePrimaryGremlinRequestsPerSecAlarm
from .monitoring import NeptunePrimaryGremlinRequestsPerSecAlarmDimension as NeptunePrimaryGremlinRequestsPerSecAlarmDimension
from .monitoring import NeptunePrimaryMemoryAlarm as NeptunePrimaryMemoryAlarm
from .monitoring import NeptunePrimaryMemoryAlarmDimension as NeptunePrimaryMemoryAlarmDimension
from .monitoring import NeptunePrimarySparqlRequestsPerSecAlarm as NeptunePrimarySparqlRequestsPerSecAlarm
from .monitoring import NeptunePrimarySparqlRequestsPerSecAlarmDimension as NeptunePrimarySparqlRequestsPerSecAlarmDimension
from .network import NeptuneDBSG as NeptuneDBSG
from .network import NeptuneDBSGAssociationParameter as NeptuneDBSGAssociationParameter
from .outputs import NeptuneEndpointAddressOutput as NeptuneEndpointAddressOutput
from .outputs import NeptuneEndpointPortOutput as NeptuneEndpointPortOutput
from .outputs import NeptuneReadEndpointAddressOutput as NeptuneReadEndpointAddressOutput
from .outputs import NeptuneSnsTopicOutput as NeptuneSnsTopicOutput
from .params import AppName as AppName
from .params import BackupRetentionPeriod as BackupRetentionPeriod
from .params import CreateSnsSubscriptionCondition as CreateSnsSubscriptionCondition
from .params import CreateSnsTopicCondition as CreateSnsTopicCondition
from .params import DBClusterIdentifier as DBClusterIdentifier
from .params import DBInstanceClass as DBInstanceClass
from .params import EnableAuditLogUploadCondition as EnableAuditLogUploadCondition
from .params import Env as Env
from .params import GremlinRequestsPerSecThreshold as GremlinRequestsPerSecThreshold
from .params import HighCpuAlarmThreshold as HighCpuAlarmThreshold
from .params import IAMAuthEnabled as IAMAuthEnabled
from .params import LowMemoryAlarmThreshold as LowMemoryAlarmThreshold
from .params import MajorVersionUpgrade as MajorVersionUpgrade
from .params import MinorVersionUpgrade as MinorVersionUpgrade
from .params import NeptuneDBClusterPreferredBackupWindow as NeptuneDBClusterPreferredBackupWindow
from .params import NeptuneDBClusterPreferredMaintenanceWindow as NeptuneDBClusterPreferredMaintenanceWindow
from .params import NeptuneDBInstancePreferredMaintenanceWindow as NeptuneDBInstancePreferredMaintenanceWindow
from .params import NeptuneDBSubnetGroupName as NeptuneDBSubnetGroupName
from .params import NeptuneQueryTimeout as NeptuneQueryTimeout
from .params import NeptuneSNSTopicArn as NeptuneSNSTopicArn
from .params import Owner as Owner
from .params import Port as Port
from .params import SNSEmailSubscription as SNSEmailSubscription
from .params import SparqlRequestsPerSecThreshold as SparqlRequestsPerSecThreshold
from .params import Storage as Storage
from .params import StorageEncrypted as StorageEncrypted
from .params import Tier as Tier
from .params import UploadAuditLogs as UploadAuditLogs
from .params import User as User
from .params import VPCStack as VPCStack
from .params import Version as Version
from .security import NeptuneCloudWatchPolicy as NeptuneCloudWatchPolicy
from .security import NeptuneCloudWatchPolicyAllowStatement0 as NeptuneCloudWatchPolicyAllowStatement0
from .security import NeptuneCloudWatchPolicyAllowStatement1 as NeptuneCloudWatchPolicyAllowStatement1
from .security import NeptuneCloudWatchPolicyPolicyDocument as NeptuneCloudWatchPolicyPolicyDocument
from .security import NeptuneRole as NeptuneRole
from .security import NeptuneRoleAllowStatement0 as NeptuneRoleAllowStatement0
from .security import NeptuneRoleAssumeRolePolicyDocument as NeptuneRoleAssumeRolePolicyDocument
from .security import NeptuneS3Policy as NeptuneS3Policy
from .security import NeptuneS3PolicyAllowStatement0 as NeptuneS3PolicyAllowStatement0
from .security import NeptuneS3PolicyPolicyDocument as NeptuneS3PolicyPolicyDocument

__all__: list[str] = ['AppName', 'BackupRetentionPeriod', 'CreateSnsSubscriptionCondition', 'CreateSnsTopicCondition', 'DBClusterIdentifier', 'DBInstanceClass', 'EnableAuditLogUploadCondition', 'Env', 'Equals', 'GremlinRequestsPerSecThreshold', 'HighCpuAlarmThreshold', 'IAMAuthEnabled', 'If', 'ImportValue', 'LowMemoryAlarmThreshold', 'MajorVersionUpgrade', 'MinorVersionUpgrade', 'NUMBER', 'NeptuneAlarmSubscription', 'NeptuneAlarmTopic', 'NeptuneCloudWatchPolicy', 'NeptuneCloudWatchPolicyAllowStatement0', 'NeptuneCloudWatchPolicyAllowStatement1', 'NeptuneCloudWatchPolicyPolicyDocument', 'NeptuneDBCluster', 'NeptuneDBClusterParameterGroup', 'NeptuneDBClusterPreferredBackupWindow', 'NeptuneDBClusterPreferredMaintenanceWindow', 'NeptuneDBInstance', 'NeptuneDBInstancePreferredMaintenanceWindow', 'NeptuneDBParameterGroup', 'NeptuneDBSG', 'NeptuneDBSGAssociationParameter', 'NeptuneDBSubnetGroup', 'NeptuneDBSubnetGroupName', 'NeptuneEndpointAddressOutput', 'NeptuneEndpointPortOutput', 'NeptunePrimaryCpuAlarm', 'NeptunePrimaryCpuAlarmDimension', 'NeptunePrimaryGremlinRequestsPerSecAlarm', 'NeptunePrimaryGremlinRequestsPerSecAlarmDimension', 'NeptunePrimaryMemoryAlarm', 'NeptunePrimaryMemoryAlarmDimension', 'NeptunePrimarySparqlRequestsPerSecAlarm', 'NeptunePrimarySparqlRequestsPerSecAlarmDimension', 'NeptuneQueryTimeout', 'NeptuneReadEndpointAddressOutput', 'NeptuneRole', 'NeptuneRoleAllowStatement0', 'NeptuneRoleAssumeRolePolicyDocument', 'NeptuneS3Policy', 'NeptuneS3PolicyAllowStatement0', 'NeptuneS3PolicyPolicyDocument', 'NeptuneSNSTopicArn', 'NeptuneSnsTopicOutput', 'Not', 'Output', 'Owner', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'Port', 'SNSEmailSubscription', 'STRING', 'SparqlRequestsPerSecThreshold', 'Storage', 'StorageEncrypted', 'Sub', 'Template', 'TemplateCondition', 'Tier', 'UploadAuditLogs', 'User', 'VPCStack', 'Version', 'cloudformation_dataclass', 'cloudwatch', 'ec2', 'get_att', 'iam', 'neptune', 'ref', 'setup_resources', 'sns']
