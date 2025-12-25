"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DeliveryChannelExists:
    """Do you have an exisiting AWS Config delivery channel?"""

    resource: Parameter
    type = STRING
    description = 'Do you have an exisiting AWS Config delivery channel?'
    default = 'false'
    allowed_values = [
    'false',
    'true',
]


@cloudformation_dataclass
class Ec2VolumeAutoEnableIO:
    resource: Parameter
    type = STRING
    default = 'false'
    allowed_values = [
    'false',
    'true',
]


@cloudformation_dataclass
class Ec2VolumeTagKey:
    resource: Parameter
    type = STRING
    default = 'CostCenter'


@cloudformation_dataclass
class CreateDeliveryChannelCondition:
    resource: TemplateCondition
    logical_id = 'CreateDeliveryChannel'
    expression = Equals(ref(DeliveryChannelExists), 'false')
