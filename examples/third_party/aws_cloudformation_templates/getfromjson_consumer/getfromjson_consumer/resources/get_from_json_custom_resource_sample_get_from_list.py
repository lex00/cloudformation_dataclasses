from __future__ import annotations

"""GetFromJsonCustomResourceSampleGetFromList - Custom::GetFromJson resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GetFromJsonCustomResourceSampleGetFromList:
    """Custom::GetFromJson resource."""

    # Unknown resource type: Custom::GetFromJson
    resource: CloudFormationResource
    service_timeout = 1
    service_token = ImportValue('Custom-GetFromJson')
    json_data = ref(GetFromListJsonData)
    search = ref(GetFromListJsonDataQuery)
