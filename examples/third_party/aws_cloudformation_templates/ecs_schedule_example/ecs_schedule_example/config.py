"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the ECS instances."""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the ECS instances.'


@cloudformation_dataclass
class VpcId:
    """Select a VPC that allows instances to access the Internet."""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'Select a VPC that allows instances to access the Internet.'


@cloudformation_dataclass
class SubnetId:
    """Select at two subnets in your selected VPC."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'Select at two subnets in your selected VPC.'


@cloudformation_dataclass
class DesiredCapacity:
    """Number of instances to launch in your ECS cluster."""

    resource: Parameter
    type = NUMBER
    description = 'Number of instances to launch in your ECS cluster.'
    default = 1


@cloudformation_dataclass
class MaxSize:
    """Maximum number of instances that can be launched in your ECS cluster."""

    resource: Parameter
    type = NUMBER
    description = 'Maximum number of instances that can be launched in your ECS cluster.'
    default = 1


@cloudformation_dataclass
class SchedulerTasksCount:
    """Maximum number of Tasks that you want to the Scheduler to run"""

    resource: Parameter
    type = NUMBER
    description = 'Maximum number of Tasks that you want to the Scheduler to run'
    default = 1


@cloudformation_dataclass
class CronOrRate:
    """Choose to use a cron expression or a rate expression you want to use."""

    resource: Parameter
    type = STRING
    description = 'Choose to use a cron expression or a rate expression you want to use.'
    default = 'cron'
    allowed_values = [
    'cron',
    'rate',
]


@cloudformation_dataclass
class CronSchedule:
    """This defines the Schedule at which to run the. Cron Expressions - http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions"""

    resource: Parameter
    type = STRING
    description = 'This defines the Schedule at which to run the. Cron Expressions - http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions'
    default = 'cron(00 11 ? * * *)'


@cloudformation_dataclass
class RateSchedule:
    """This defines the Schedule at which to run the. Rate Expressions - http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#RateExpressions"""

    resource: Parameter
    type = STRING
    description = 'This defines the Schedule at which to run the. Rate Expressions - http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#RateExpressions'
    default = 'rate(1 day)'


@cloudformation_dataclass
class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 't2.micro'
    allowed_values = [
    't2.micro',
    't2.small',
    't2.medium',
    't2.large',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'c4.large',
    'c4.xlarge',
    'c4.2xlarge',
    'c4.4xlarge',
    'c4.8xlarge',
    'c3.large',
    'c3.xlarge',
    'c3.2xlarge',
    'c3.4xlarge',
    'c3.8xlarge',
    'r3.large',
    'r3.xlarge',
    'r3.2xlarge',
    'r3.4xlarge',
    'r3.8xlarge',
    'i2.xlarge',
    'i2.2xlarge',
    'i2.4xlarge',
    'i2.8xlarge',
]
    constraint_description = 'Please choose a valid instance type.'


@cloudformation_dataclass
class LatestAmiId:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id'


@cloudformation_dataclass
class CronRateCondition:
    resource: Condition
    expression = Equals(ref(CronOrRate), 'cron')
