"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ResourceFunctionOutput:
    resource: Output
    value = get_att(ResourceFunction, "Arn")
    export_name = 'StackMetricsMacroFunction'
