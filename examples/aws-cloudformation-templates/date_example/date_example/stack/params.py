"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Date:
    """Date for this test (ISO 8601 format)"""

    resource: Parameter
    type = STRING
    description = 'Date for this test (ISO 8601 format)'
    default = ''
    allowed_pattern = '^$|^\\d{4}(-\\d\\d(-\\d\\d(T\\d\\d:\\d\\d(:\\d\\d)?(\\.\\d+)?(([+-]\\d\\d:\\d\\d)|Z)?)?)?)?$'


@cloudformation_dataclass
class Date2:
    """Second date for test to use (ISO 8601 format)"""

    resource: Parameter
    type = STRING
    description = 'Second date for test to use (ISO 8601 format)'
    default = ''
    allowed_pattern = '^$|^\\d{4}(-\\d\\d(-\\d\\d(T\\d\\d:\\d\\d(:\\d\\d)?(\\.\\d+)?(([+-]\\d\\d:\\d\\d)|Z)?)?)?)?$'


@cloudformation_dataclass
class Days:
    """Days"""

    resource: Parameter
    type = NUMBER
    description = 'Days'
    default = 1
