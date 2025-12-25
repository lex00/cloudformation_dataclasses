"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class PermissionBoundaryArn:
    """ARN for the Permission Boundary Policy"""

    resource: Parameter
    type = STRING
    description = 'ARN for the Permission Boundary Policy'
