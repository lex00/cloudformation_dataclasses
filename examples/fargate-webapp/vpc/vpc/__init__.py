"""VPC stack - network foundation for Fargate webapp."""

from cloudformation_dataclasses.core import (
    Output,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import GetAZs, Join, Select

from . import stack
from .stack import *  # noqa: F403, F401

__all__ = [
    "GetAZs",
    "Join",
    "Output",
    "Select",
    "Template",
    "cloudformation_dataclass",
    "ec2",
    "get_att",
    "ref",
    *stack.__all__,
]
