"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Tags:
    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    default = 'Env=Prod,Application=MyApp,BU=ModernisationTeam'
