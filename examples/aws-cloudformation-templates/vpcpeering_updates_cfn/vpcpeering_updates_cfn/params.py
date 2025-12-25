"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NumberOfRouteTables:
    """Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter."""

    resource: Parameter
    type = STRING
    description = 'Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


@cloudformation_dataclass
class NumberOfSecurityGroups:
    """Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter."""

    resource: Parameter
    type = STRING
    description = 'Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


@cloudformation_dataclass
class PeerName:
    """Name of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


@cloudformation_dataclass
class PeerVPCCIDR:
    """CIDR of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'CIDR of the VPC Peer'
    allowed_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(1[6-9]|2[0-8]))$'
    constraint_description = 'CIDR block parameter must be in the form x.x.x.x/16-28'


@cloudformation_dataclass
class RouteTableIds:
    """Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    resource: Parameter
    type = STRING
    description = 'Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'
    allowed_pattern = '^(rtb-[0-9a-f]{17})$|^((rtb-[0-9a-f]{17}(,|, ))*rtb-[0-9a-f]{17})$'
    constraint_description = 'Must have a prefix of "rtb-". Followed by 17 characters (numbers, letters "a-f"). Additional route tables can be provided, separated by a "comma".'


@cloudformation_dataclass
class SecurityGroupIds:
    """Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID
    description = 'Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'


@cloudformation_dataclass
class VPCPeeringConnectionId:
    """ID of the VPC Peering Connection"""

    resource: Parameter
    type = STRING
    description = 'ID of the VPC Peering Connection'
    allowed_pattern = '^pcx-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "pcx-". Followed by 17 characters (numbers, letters "a-f")'


@cloudformation_dataclass
class _2RouteTableConditionCondition:
    resource: TemplateCondition
    logical_id = '2RouteTableCondition'
    expression = Or(conditions=[Equals(ref(NumberOfRouteTables), 2), Condition("3RouteTableCondition"), Condition("4RouteTableCondition"), Condition("5RouteTableCondition"), Condition("6RouteTableCondition")])


@cloudformation_dataclass
class _3RouteTableConditionCondition:
    resource: TemplateCondition
    logical_id = '3RouteTableCondition'
    expression = Or(conditions=[Equals(ref(NumberOfRouteTables), 3), Condition("4RouteTableCondition"), Condition("5RouteTableCondition"), Condition("6RouteTableCondition")])


@cloudformation_dataclass
class _4RouteTableConditionCondition:
    resource: TemplateCondition
    logical_id = '4RouteTableCondition'
    expression = Or(conditions=[Equals(ref(NumberOfRouteTables), 4), Condition("5RouteTableCondition"), Condition("6RouteTableCondition")])


@cloudformation_dataclass
class _5RouteTableConditionCondition:
    resource: TemplateCondition
    logical_id = '5RouteTableCondition'
    expression = Or(conditions=[Equals(ref(NumberOfRouteTables), 5), Condition("6RouteTableCondition")])


@cloudformation_dataclass
class _6RouteTableConditionCondition:
    resource: TemplateCondition
    logical_id = '6RouteTableCondition'
    expression = Equals(ref(NumberOfRouteTables), 6)


@cloudformation_dataclass
class _2SecurityGroupConditionCondition:
    resource: TemplateCondition
    logical_id = '2SecurityGroupCondition'
    expression = Or(conditions=[Equals(ref(NumberOfSecurityGroups), 2), Condition("3SecurityGroupCondition"), Condition("4SecurityGroupCondition"), Condition("5SecurityGroupCondition"), Condition("6SecurityGroupCondition")])


@cloudformation_dataclass
class _3SecurityGroupConditionCondition:
    resource: TemplateCondition
    logical_id = '3SecurityGroupCondition'
    expression = Or(conditions=[Equals(ref(NumberOfSecurityGroups), 3), Condition("4SecurityGroupCondition"), Condition("5SecurityGroupCondition"), Condition("6SecurityGroupCondition")])


@cloudformation_dataclass
class _4SecurityGroupConditionCondition:
    resource: TemplateCondition
    logical_id = '4SecurityGroupCondition'
    expression = Or(conditions=[Equals(ref(NumberOfSecurityGroups), 4), Condition("5SecurityGroupCondition"), Condition("6SecurityGroupCondition")])


@cloudformation_dataclass
class _5SecurityGroupConditionCondition:
    resource: TemplateCondition
    logical_id = '5SecurityGroupCondition'
    expression = Or(conditions=[Equals(ref(NumberOfSecurityGroups), 5), Condition("6SecurityGroupCondition")])


@cloudformation_dataclass
class _6SecurityGroupConditionCondition:
    resource: TemplateCondition
    logical_id = '6SecurityGroupCondition'
    expression = Equals(ref(NumberOfSecurityGroups), 6)
