"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class WebsiteURLOutput:
    """URL for newly created KWOS deploy stack"""

    resource: Output
    value = Join('', [
    'http://',
    get_att(KWOSInstance, "PublicDnsName"),
])
    description = 'URL for newly created KWOS deploy stack'


@cloudformation_dataclass
class InstanceIdOutput:
    """Instance Id of newly created instance"""

    resource: Output
    value = ref(KWOSInstance)
    description = 'Instance Id of newly created instance'
