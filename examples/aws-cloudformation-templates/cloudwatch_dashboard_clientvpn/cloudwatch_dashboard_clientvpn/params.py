"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Folder:
    """(Optional) Folder to store the queries in."""

    resource: Parameter
    type = STRING
    description = '(Optional) Folder to store the queries in.'
    default = 'aws-client-vpn'
    allowed_pattern = '^[a-zA-Z0-9/-]*$'
    constraint_description = 'Folder name must contain only alphanumeric characters. Slashes (/) are folder separators.'


@cloudformation_dataclass
class ClientVPNLogGroup:
    """Name of the Client VPN CloudWatch Log Group"""

    resource: Parameter
    type = STRING
    description = 'Name of the Client VPN CloudWatch Log Group'
    default = 'aws/aws-client-vpn/prod'
