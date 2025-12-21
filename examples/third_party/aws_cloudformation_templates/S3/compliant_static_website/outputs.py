"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class SiteURLOutput:
    resource: Output
    value = Sub('https://${Distribution.DomainName}')
