"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GetFromJsonCustomResourceSampleGetFromListValueOutput:
    resource: Output
    value = get_att(GetFromJsonCustomResourceSampleGetFromList, "Data")


@cloudformation_dataclass
class GetFromJsonCustomResourceSampleGetFromMapValueOutput:
    resource: Output
    value = get_att(GetFromJsonCustomResourceSampleGetFromMap, "Data")
