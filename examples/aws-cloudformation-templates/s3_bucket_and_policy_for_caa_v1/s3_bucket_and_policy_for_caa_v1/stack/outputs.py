"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketOutput:
    """S3 Bucket Name"""

    resource: Output
    value = ref(Bucket)
    description = 'S3 Bucket Name'


@cloudformation_dataclass
class BucketPolicyOutput:
    """S3 Bucket Policy Name"""

    resource: Output
    value = ref(BucketPolicy)
    description = 'S3 Bucket Policy Name'
