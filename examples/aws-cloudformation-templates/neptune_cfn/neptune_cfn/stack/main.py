"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'SG of Neptune DB'
    vpc_id = ImportValue(Sub('${VPCStack}-VPCID'))
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-neptune-sg'),
    }]


@cloudformation_dataclass
class NeptuneDBClusterParameterGroup:
    """AWS::Neptune::DBClusterParameterGroup resource."""

    resource: neptune.DBClusterParameterGroup
    description = Sub('CloudFormation managed Neptune DB Cluster Parameter Group - ${Env}-${AppName}-cluster-parameter-group')
    parameters = {
        'neptune_enable_audit_log': If("EnableAuditLogUpload", 1, 0),
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-neptune-cluster-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-cluster-parameter-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


@cloudformation_dataclass
class NeptuneDBSubnetGroup:
    """AWS::Neptune::DBSubnetGroup resource."""

    resource: neptune.DBSubnetGroup
    db_subnet_group_description = Sub('CloudFormation managed Neptune DB Subnet Group - ${Env}-${AppName}-subnet-group')
    db_subnet_group_name = ref(NeptuneDBSubnetGroupName)
    subnet_ids = [ImportValue(Sub('${VPCStack}-PrivateSubnet1')), ImportValue(Sub('${VPCStack}-PrivateSubnet2'))]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-subnet-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


@cloudformation_dataclass
class NeptuneDBCluster:
    """AWS::Neptune::DBCluster resource."""

    resource: neptune.DBCluster
    backup_retention_period = ref(BackupRetentionPeriod)
    db_cluster_identifier = ref(DBClusterIdentifier)
    db_cluster_parameter_group_name = ref(NeptuneDBClusterParameterGroup)
    db_subnet_group_name = ref(NeptuneDBSubnetGroup)
    iam_auth_enabled = ref(IAMAuthEnabled)
    db_port = ref(Port)
    preferred_backup_window = ref(NeptuneDBClusterPreferredBackupWindow)
    preferred_maintenance_window = ref(NeptuneDBClusterPreferredMaintenanceWindow)
    storage_encrypted = ref(StorageEncrypted)
    vpc_security_group_ids = [ref(NeptuneDBSG)]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Cluster'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]
    depends_on = ["NeptuneDBSG"]


@cloudformation_dataclass
class NeptuneDBParameterGroup:
    """AWS::Neptune::DBParameterGroup resource."""

    resource: neptune.DBParameterGroup
    description = Sub('CloudFormation managed Neptune DB Parameter Group - ${Env}-${AppName}-parameter-group')
    parameters = {
        'neptune_query_timeout': ref(NeptuneQueryTimeout),
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-parameter-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


@cloudformation_dataclass
class NeptuneDBInstance:
    """AWS::Neptune::DBInstance resource."""

    resource: neptune.DBInstance
    allow_major_version_upgrade = ref(MajorVersionUpgrade)
    auto_minor_version_upgrade = ref(MinorVersionUpgrade)
    db_cluster_identifier = ref(NeptuneDBCluster)
    db_instance_class = ref(DBInstanceClass)
    db_parameter_group_name = ref(NeptuneDBParameterGroup)
    db_subnet_group_name = ref(NeptuneDBSubnetGroup)
    preferred_maintenance_window = ref(NeptuneDBInstancePreferredMaintenanceWindow)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Instance'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


@cloudformation_dataclass
class NeptuneAlarmTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic
    display_name = Sub('${AWS::StackName} alarm topic')
    condition = 'CreateSnsTopic'


@cloudformation_dataclass
class NeptuneAlarmSubscription:
    """AWS::SNS::Subscription resource."""

    resource: sns.Subscription
    endpoint = ref(SNSEmailSubscription)
    protocol = 'email'
    topic_arn = If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))
    condition = 'CreateSnsSubscription'


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'EnableLogGroups'
    action = [
        'logs:CreateLogGroup',
        'logs:PutRetentionPolicy',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'EnableLogStreams'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogStreams',
        'logs:GetLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*:log-stream:*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneCloudWatchPolicyAllowStatement0, NeptuneCloudWatchPolicyAllowStatement1]


@cloudformation_dataclass
class NeptuneCloudWatchPolicy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: iam.ManagedPolicy
    description = 'Default policy for CloudWatch logs'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-cw-policy-${AWS::Region}')
    policy_document = NeptuneCloudWatchPolicyPolicyDocument


@cloudformation_dataclass
class NeptuneS3PolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowNeptuneAccessToS3'
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::*')]


@cloudformation_dataclass
class NeptuneS3PolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneS3PolicyAllowStatement0]


@cloudformation_dataclass
class NeptuneS3Policy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: iam.ManagedPolicy
    description = 'Neptune default policy for S3 access for data load'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-s3-policy-${AWS::Region}')
    policy_document = NeptuneS3PolicyPolicyDocument


@cloudformation_dataclass
class NeptuneRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': [
            'monitoring.rds.amazonaws.com',
            'rds.amazonaws.com',
        ],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class NeptuneRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneRoleAllowStatement0]


@cloudformation_dataclass
class NeptuneRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${Env}-${AppName}-neptune-iam-role-${AWS::Region}')
    assume_role_policy_document = NeptuneRoleAssumeRolePolicyDocument
    managed_policy_arns = [ref(NeptuneCloudWatchPolicy), ref(NeptuneS3Policy)]
    condition = 'EnableAuditLogUpload'


@cloudformation_dataclass
class NeptunePrimaryCpuAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryCpuAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB CPU over ${HighCpuAlarmThreshold}%')
    namespace = 'AWS/Neptune'
    metric_name = 'CPUUtilization'
    unit = 'Percent'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(HighCpuAlarmThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryCpuAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB memory under ${LowMemoryAlarmThreshold} bytes')
    namespace = 'AWS/Neptune'
    metric_name = 'FreeableMemory'
    unit = 'Bytes'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(LowMemoryAlarmThreshold)
    comparison_operator = 'LessThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryMemoryAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]


@cloudformation_dataclass
class NeptunePrimaryGremlinRequestsPerSecAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = 'gremlin-cluster'


@cloudformation_dataclass
class NeptunePrimaryGremlinRequestsPerSecAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB Gremlin Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'GremlinRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(GremlinRequestsPerSecThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryGremlinRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB Sparql Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'SparqlRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(SparqlRequestsPerSecThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimarySparqlRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
