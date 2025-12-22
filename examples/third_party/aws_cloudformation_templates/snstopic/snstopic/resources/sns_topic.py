"""SNSTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SNSTopic:
    """AWS::SNS::Topic resource."""

    resource: Topic
