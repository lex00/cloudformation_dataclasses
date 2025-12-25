"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: ecs.Cluster


@cloudformation_dataclass
class EcsSecurityGroupHTTPinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = IpProtocol.TCP
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class EcsSecurityGroupSSHinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = IpProtocol.TCP
    from_port = '22'
    to_port = '22'
    cidr_ip = '192.168.1.0/0'


@cloudformation_dataclass
class EcsSecurityGroupALBports:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = IpProtocol.TCP
    from_port = '31000'
    to_port = '61000'
    source_security_group_id = ref(EcsSecurityGroup)


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
