"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import quicksight, s3
from .params import *  # noqa: F403, F401

from .storage import Bucket as Bucket
from .storage import Object1 as Object1
from .storage import Object2 as Object2
from .storage import Object3 as Object3
from .storage import Object3ManifestFileLocation as Object3ManifestFileLocation
from .storage import Object3ManifestFileLocation1 as Object3ManifestFileLocation1
from .storage import Object4 as Object4
from .storage import Object4ManifestFileLocation as Object4ManifestFileLocation

__all__: list[str] = ['Bucket', 'CloudFormationResource', 'Object1', 'Object2', 'Object3', 'Object3ManifestFileLocation', 'Object3ManifestFileLocation1', 'Object4', 'Object4ManifestFileLocation', 'Template', 'cloudformation_dataclass', 'get_att', 'quicksight', 'ref', 's3', 'setup_resources']
