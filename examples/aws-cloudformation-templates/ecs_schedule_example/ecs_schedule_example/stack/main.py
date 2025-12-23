"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: ecs.Cluster


@cloudformation_dataclass
class EcsSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'ECS Security Group'
    vpc_id = ref(VpcId)


@cloudformation_dataclass
class EcsSecurityGroupHTTPinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class EcsSecurityGroupSSHinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = '192.168.1.0/0'


@cloudformation_dataclass
class EcsSecurityGroupALBports:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '31000'
    to_port = '61000'
    source_security_group_id = ref(EcsSecurityGroup)


@cloudformation_dataclass
class LogsKmsKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    description = 'ECS Logs Encryption Key'
    enable_key_rotation = True


@cloudformation_dataclass
class CloudwatchLogsGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Join('-', [
    'ECSLogGroup',
    AWS_STACK_NAME,
])
    retention_in_days = 14
    kms_key_id = ref(LogsKmsKey)


@cloudformation_dataclass
class TaskDefinitionLogConfiguration:
    resource: ecs.task_definition.LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': ref(CloudwatchLogsGroup),
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


@cloudformation_dataclass
class TaskDefinitionMountPoint:
    resource: ecs.task_definition.MountPoint
    container_path = '/usr/local/apache2/htdocs'
    source_volume = 'my-vol'


@cloudformation_dataclass
class TaskDefinitionPortMapping:
    resource: ecs.task_definition.PortMapping
    container_port = 80


@cloudformation_dataclass
class TaskDefinitionContainerDefinition:
    resource: ecs.task_definition.ContainerDefinition
    name = 'simple-app'
    cpu = '10'
    essential = 'true'
    image = 'httpd:2.4'
    memory = '300'
    log_configuration = TaskDefinitionLogConfiguration
    mount_points = [TaskDefinitionMountPoint]
    port_mappings = [TaskDefinitionPortMapping]


@cloudformation_dataclass
class TaskDefinitionLogConfiguration1:
    resource: ecs.task_definition.LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': ref(CloudwatchLogsGroup),
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


@cloudformation_dataclass
class TaskDefinitionVolumeFrom:
    resource: ecs.task_definition.VolumeFrom
    source_container = 'simple-app'


@cloudformation_dataclass
class TaskDefinitionContainerDefinition1:
    resource: ecs.task_definition.ContainerDefinition
    name = 'busybox'
    cpu = 10
    command = ['/bin/sh -c "while true; do echo \'<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>\' > top; /bin/date > date ; echo \'</div></body></html>\' > bottom; cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done"']
    entry_point = ['sh', '-c']
    essential = False
    image = 'busybox'
    memory = 200
    log_configuration = TaskDefinitionLogConfiguration1
    volumes_from = [TaskDefinitionVolumeFrom]


@cloudformation_dataclass
class TaskDefinitionSecret:
    resource: ecs.service.Secret
    name = 'my-vol'


@cloudformation_dataclass
class TaskDefinition:
    """AWS::ECS::TaskDefinition resource."""

    resource: ecs.TaskDefinition
    family = Join('', [
    AWS_STACK_NAME,
    '-ecs-demo-app',
])
    container_definitions = [TaskDefinitionContainerDefinition, TaskDefinitionContainerDefinition1]
    volumes = [TaskDefinitionSecret]


@cloudformation_dataclass
class ECSALBLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class ECSALB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    name = 'ECSALB'
    scheme = 'internet-facing'
    load_balancer_attributes = [ECSALBLoadBalancerAttribute]
    subnets = ref(SubnetId)
    security_groups = [ref(EcsSecurityGroup)]


@cloudformation_dataclass
class ECSTG:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 10
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = 'ECSTG'
    port = 80
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ref(VpcId)
    depends_on = ["ECSALB"]


@cloudformation_dataclass
class ALBListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class ALBListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [ALBListenerAction]
    load_balancer_arn = ref(ECSALB)
    port = '80'
    protocol = 'HTTP'
    depends_on = ["ECSServiceRole"]


@cloudformation_dataclass
class ECSALBListenerRuleAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class ECSALBListenerRuleRuleCondition:
    resource: elasticloadbalancingv2.listener_rule.RuleCondition
    field = 'path-pattern'
    values = ['/']


@cloudformation_dataclass
class ECSALBListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: elasticloadbalancingv2.ListenerRule
    actions = [ECSALBListenerRuleAction]
    conditions = [ECSALBListenerRuleRuleCondition]
    listener_arn = ref(ALBListener)
    priority = 1
    depends_on = ["ALBListener"]


@cloudformation_dataclass
class EC2RoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EC2RoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0]


@cloudformation_dataclass
class EC2RoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecs:CreateCluster',
        'ecs:DeregisterContainerInstance',
        'ecs:DiscoverPollEndpoint',
        'ecs:Poll',
        'ecs:RegisterContainerInstance',
        'ecs:StartTelemetrySession',
        'ecs:Submit*',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class EC2RolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0_1]


@cloudformation_dataclass
class EC2RolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = EC2RolePolicies0PolicyDocument


@cloudformation_dataclass
class EC2Role:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EC2RoleAssumeRolePolicyDocument
    path = '/'
    policies = [EC2RolePolicy]


@cloudformation_dataclass
class EC2InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(EC2Role)]


@cloudformation_dataclass
class ContainerInstances:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    image_id = ref(LatestAmiId)
    security_groups = [ref(EcsSecurityGroup)]
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(EC2InstanceProfile)
    key_name = ref(KeyName)
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
    --resource ECSAutoScalingGroup \
    --region ${AWS::Region}
"""))


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = ref(SubnetId)
    launch_configuration_name = ref(ContainerInstances)
    min_size = '1'
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)


@cloudformation_dataclass
class ECSServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0]


@cloudformation_dataclass
class ECSServiceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
        'ec2:Describe*',
        'ec2:AuthorizeSecurityGroupIngress',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSServiceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSServiceRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSServiceRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSServiceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSServiceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSServiceRolePolicy]


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: ecs.task_set.LoadBalancer
    container_name = 'simple-app'
    container_port = '80'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class Service:
    """AWS::ECS::Service resource."""

    resource: ecs.Service
    cluster = ref(ECSCluster)
    desired_count = '1'
    load_balancers = [ServiceLoadBalancer]
    role = ref(ECSServiceRole)
    task_definition = ref(TaskDefinition)
    depends_on = ["ALBListener"]


@cloudformation_dataclass
class ECSEventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSEventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0]


@cloudformation_dataclass
class ECSEventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['ecs:RunTask']
    resource_arn = '*'


@cloudformation_dataclass
class ECSEventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSEventRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSEventRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSEventRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSEventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSEventRolePolicy]


@cloudformation_dataclass
class ECSScheduledTask:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", ref(CronSchedule), ref(RateSchedule))
    state = 'ENABLED'
    targets = [{
        'Arn': get_att(ECSCluster, "Arn"),
        'Id': 'Target1',
        'RoleArn': get_att(ECSEventRole, "Arn"),
        'EcsParameters': {
            'TaskCount': ref(SchedulerTasksCount),
            'TaskDefinitionArn': ref(TaskDefinition),
        },
    }]
    depends_on = ["ECSEventRole"]


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['application-autoscaling.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AutoscalingRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0]


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'application-autoscaling:*',
        'cloudwatch:DescribeAlarms',
        'cloudwatch:PutMetricAlarm',
        'ecs:DescribeServices',
        'ecs:UpdateService',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class AutoscalingRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0_1]


@cloudformation_dataclass
class AutoscalingRolePolicy:
    resource: iam.user.Policy
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


@cloudformation_dataclass
class AutoscalingRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]


@cloudformation_dataclass
class ServiceScalingTarget:
    """AWS::ApplicationAutoScaling::ScalableTarget resource."""

    resource: applicationautoscaling.ScalableTarget
    max_capacity = 2
    min_capacity = 1
    resource_id = Join('', [
    'service/',
    ref(ECSCluster),
    '/',
    get_att(Service, "Name"),
])
    role_arn = get_att(AutoscalingRole, "Arn")
    scalable_dimension = 'ecs:service:DesiredCount'
    service_namespace = 'ecs'
    depends_on = ["Service"]


@cloudformation_dataclass
class ServiceScalingPolicyStepAdjustment:
    resource: applicationautoscaling.scaling_policy.StepAdjustment
    metric_interval_lower_bound = 0
    scaling_adjustment = 200


@cloudformation_dataclass
class ServiceScalingPolicyStepScalingPolicyConfiguration:
    resource: applicationautoscaling.scaling_policy.StepScalingPolicyConfiguration
    adjustment_type = 'PercentChangeInCapacity'
    cooldown = 60
    metric_aggregation_type = 'Average'
    step_adjustments = [ServiceScalingPolicyStepAdjustment]


@cloudformation_dataclass
class ServiceScalingPolicy:
    """AWS::ApplicationAutoScaling::ScalingPolicy resource."""

    resource: applicationautoscaling.ScalingPolicy
    policy_name = 'AStepPolicy'
    policy_type = 'StepScaling'
    scaling_target_id = ref(ServiceScalingTarget)
    step_scaling_policy_configuration = ServiceScalingPolicyStepScalingPolicyConfiguration


@cloudformation_dataclass
class ALB500sAlarmScaleUpDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'ECSService'
    value = ref(Service)


@cloudformation_dataclass
class ALB500sAlarmScaleUp:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    evaluation_periods = '1'
    statistic = 'Average'
    threshold = '10'
    alarm_description = 'Alarm if our ALB generates too many HTTP 500s.'
    period = '60'
    alarm_actions = [ref(ServiceScalingPolicy)]
    namespace = 'AWS/ApplicationELB'
    dimensions = [ALB500sAlarmScaleUpDimension]
    comparison_operator = 'GreaterThanThreshold'
    metric_name = 'HTTPCode_ELB_5XX_Count'
