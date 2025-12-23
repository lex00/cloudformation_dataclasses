"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NotificationTopicSubscription:
    resource: sns.topic.Subscription
    endpoint = ref(OperatorEMail)
    protocol = 'email'


@cloudformation_dataclass
class NotificationTopic:
    """AWS::SNS::Topic resource."""

    # Unknown resource type: AWS::SNS::Topic
    resource: CloudFormationResource
    display_name = Sub('${AWS::StackName}-NotificationTopic')
    subscription = [NotificationTopicSubscription]
    kms_master_key_id = ref(KmsKeyArn)


@cloudformation_dataclass
class LaunchTemplateEbs:
    resource: ec2.launch_template.Ebs
    volume_size = 32


@cloudformation_dataclass
class LaunchTemplateBlockDeviceMapping:
    resource: ec2.launch_template.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = LaunchTemplateEbs


@cloudformation_dataclass
class LaunchTemplateTagSpecification:
    resource: ec2.launch_template.TagSpecification
    resource_type = 'instance'
    tags = [{
        AssociationParameter.key: 'Name',
        AssociationParameter.value: Sub('${AWS::StackName}-Instance'),
    }]


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: ec2.launch_template.LaunchTemplateData
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    security_group_ids = ref(SecurityGroups)
    key_name = ref(KeyName)
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
"""))
    tag_specifications = [LaunchTemplateTagSpecification]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
    launch_template_data = LaunchTemplateLaunchTemplateData


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = 'HTTP'
    target_type = 'instance'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.auto_scaling_group.LaunchTemplateSpecification
    launch_template_id = ref(LaunchTemplate)
    version = get_att(LaunchTemplate, "LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroupNotificationConfiguration:
    resource: autoscaling.auto_scaling_group.NotificationConfiguration
    topic_arn = ref(NotificationTopic)
    notification_types = ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR']


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = ref(AZs)
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref(TargetGroup)]
    notification_configurations = [WebServerGroupNotificationConfiguration]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)


@cloudformation_dataclass
class WebServerScaleUpPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = 1


@cloudformation_dataclass
class WebServerScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = -1


@cloudformation_dataclass
class CPUAlarmHighDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(WebServerGroup)


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 90
    alarm_actions = [ref(WebServerScaleUpPolicy)]
    dimensions = [CPUAlarmHighDimension]
    comparison_operator = 'GreaterThanThreshold'


@cloudformation_dataclass
class CPUAlarmLowDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(WebServerGroup)


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 70
    alarm_actions = [ref(WebServerScaleDownPolicy)]
    dimensions = [CPUAlarmLowDimension]
    comparison_operator = 'LessThanThreshold'


@cloudformation_dataclass
class LoadBalancerSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [LoadBalancerSecurityGroupEgress]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    security_groups = [ref(LoadBalancerSecurityGroup)]
    subnets = ref(Subnets)
    type_ = 'application'


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: elasticloadbalancingv2.listener_certificate.Certificate
    certificate_arn = ref(CertificateArn)


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = ref(ElasticLoadBalancer)
    port = 443
    protocol = 'HTTPS'
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [LoadBalancerListenerCertificate]


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = 'tcp'
    from_port = 80
    to_port = 80
    source_security_group_id = ref(LoadBalancerSecurityGroup)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
