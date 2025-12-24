"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CertificateArn:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class VPCId:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class PublicSubnet1:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class PublicSubnet2:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class DestinationSecurityGroupId:
    resource: Parameter
    type = STRING
