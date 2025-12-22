"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class OUID:
    resource: Parameter
    type = STRING
    default = 'ou-qxtx-vv0thlla'
