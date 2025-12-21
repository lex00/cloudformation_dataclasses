from __future__ import annotations

"""ConfigTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigTopic:
    """AWS::SNS::Topic resource."""

    resource: Topic
