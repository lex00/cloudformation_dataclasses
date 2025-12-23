"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystem:
    """AWS::EFS::FileSystem resource."""

    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'


@cloudformation_dataclass
class ELBSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'ToPort': '80',
    }, {
        'CidrIp': '0.0.0.0/0',
        'FromPort': '443',
        'IpProtocol': 'tcp',
        'ToPort': '443',
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '22',
        'IpProtocol': 'tcp',
        'ToPort': '22',
    }, {
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'SourceSecurityGroupId': get_att(ELBSecurityGroup, "GroupId"),
        'ToPort': '80',
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class EFSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [{
        'FromPort': '2049',
        'IpProtocol': 'tcp',
        'ToPort': '2049',
        'SourceSecurityGroupId': get_att(InstanceSecurityGroup, "GroupId"),
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class EFSMountTarget1:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(0, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget2:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(1, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget3:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(2, ref(Subnets))


@cloudformation_dataclass
class EFSMountTarget4:
    """AWS::EFS::MountTarget resource."""

    resource: efs.MountTarget
    file_system_id = ref(EFSFileSystem)
    security_groups = [get_att(EFSSecurityGroup, "GroupId")]
    subnet_id = Select(3, ref(Subnets))


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class IAMAssumeInstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [IAMAssumeInstanceRoleAllowStatement0]


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['ec2:DescribeTags']
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRoleAllowStatement2:
    resource: PolicyStatement
    action = 'logs:*'
    resource_arn = '*'


@cloudformation_dataclass
class IAMAssumeInstanceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [IAMAssumeInstanceRoleAllowStatement0_1, IAMAssumeInstanceRoleAllowStatement1, IAMAssumeInstanceRoleAllowStatement2]


@cloudformation_dataclass
class IAMAssumeInstanceRolePolicy:
    resource: iam.user.Policy
    policy_document = IAMAssumeInstanceRolePolicies0PolicyDocument
    policy_name = Join('-', [
    'IAM',
    'EC2',
    'Policy',
])


@cloudformation_dataclass
class IAMAssumeInstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = IAMAssumeInstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [IAMAssumeInstanceRolePolicy]
    role_name = Join('-', [
    'IAM',
    'EC2',
    'Role',
])


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    instance_profile_name = Join('-', [
    'IAM',
    'InstanceProfile',
])
    path = '/'
    roles = [ref(IAMAssumeInstanceRole)]


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    iam_instance_profile = ref(InstanceProfile)
    image_id = FindInMap("EC2RegionMap", AWS_REGION, '64')
    instance_type = ref(InstanceType)
    key_name = ref(KeyName)
    security_groups = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash -x
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
apt-get update
apt-get install -y curl nfs-common
EC2_REGION=${AWS::Region}
DIR_TGT=/mnt/efs/
EFS_FILE_SYSTEM_ID=${EFSFileSystem}
mkdir -p $DIR_TGT
DIR_SRC=$EFS_FILE_SYSTEM_ID.efs.$EC2_REGION.amazonaws.com
mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 $DIR_SRC:/ $DIR_TGT"""))


@cloudformation_dataclass
class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.load_balancer.HealthCheck
    healthy_threshold = '3'
    interval = '30'
    target = Join('', [
    'HTTP:',
    '80',
    '/',
])
    timeout = '5'
    unhealthy_threshold = '5'


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    instance_port = '80'
    load_balancer_port = '80'
    protocol = 'HTTP'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    security_groups = [ref(ELBSecurityGroup)]
    subnets = ref(Subnets)
    cross_zone = 'true'
    health_check = ElasticLoadBalancerHealthCheck
    listeners = [ElasticLoadBalancerListeners]


@cloudformation_dataclass
class AutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    launch_configuration_name = ref(LaunchConfig)
    load_balancer_names = [ref(ElasticLoadBalancer)]
    max_size = '3'
    min_size = '1'
    vpc_zone_identifier = ref(Subnets)


@cloudformation_dataclass
class ScaleUpPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(AutoScalingGroup)
    cooldown = '60'
    scaling_adjustment = '1'


@cloudformation_dataclass
class CPUAlarmHighDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(AutoScalingGroup)


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_actions = [ref(ScaleUpPolicy)]
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    comparison_operator = 'GreaterThanThreshold'
    dimensions = [CPUAlarmHighDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '90'


@cloudformation_dataclass
class ScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(AutoScalingGroup)
    cooldown = '60'
    scaling_adjustment = '-1'


@cloudformation_dataclass
class CPUAlarmLowDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(AutoScalingGroup)


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_actions = [ref(ScaleDownPolicy)]
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    comparison_operator = 'LessThanThreshold'
    dimensions = [CPUAlarmLowDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '70'
