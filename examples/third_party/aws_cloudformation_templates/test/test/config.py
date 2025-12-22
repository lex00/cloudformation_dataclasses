"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class BucketMapMapping:
    resource: Mapping
    map_data = {
        'Monthly': {
            'ResourceName': 'MyThirtyDayBucket',
            'Retention': 30,
        },
        'Yearly': {
            'Retention': 365,
        },
    }
