"""RDS stack - PostgreSQL database with Secrets Manager."""

from cloudformation_dataclasses.core import (
    IpProtocol,
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.aws import ec2, rds, secretsmanager
from cloudformation_dataclasses.aws.secretsmanager import secret
from cloudformation_dataclasses.intrinsics.functions import Sub

from .stack import *  # noqa: F403, F401

__all__ = [
    "IpProtocol",
    "Output",
    "Parameter",
    "ParameterType",
    "STRING",
    "Sub",
    "Template",
    "cloudformation_dataclass",
    "ec2",
    "get_att",
    "rds",
    "ref",
    "secret",
    "secretsmanager",
]
