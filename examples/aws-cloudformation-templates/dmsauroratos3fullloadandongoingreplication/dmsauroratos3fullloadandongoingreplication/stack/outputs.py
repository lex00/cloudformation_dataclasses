"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StackNameOutput:
    resource: Output
    value = AWS_STACK_NAME


@cloudformation_dataclass
class RegionNameOutput:
    resource: Output
    value = AWS_REGION


@cloudformation_dataclass
class S3BucketNameOutput:
    resource: Output
    value = ref(S3Bucket)


@cloudformation_dataclass
class AuroraEndpointOutput:
    resource: Output
    value = get_att(AuroraCluster, "Endpoint.Address")
