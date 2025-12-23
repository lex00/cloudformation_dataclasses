"""PropertyTypes for AWS::MediaConnect::FlowOutput."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DestinationConfiguration(PropertyType):
    DESTINATION_IP = "DestinationIp"
    DESTINATION_PORT = "DestinationPort"
    INTERFACE = "Interface"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_ip": "DestinationIp",
        "destination_port": "DestinationPort",
        "interface": "Interface",
    }

    destination_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interface: Optional[Interface] = None


@dataclass
class EncodingParameters(PropertyType):
    ENCODER_PROFILE = "EncoderProfile"
    COMPRESSION_FACTOR = "CompressionFactor"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encoder_profile": "EncoderProfile",
        "compression_factor": "CompressionFactor",
    }

    encoder_profile: Optional[Union[str, EncoderProfile, Ref, GetAtt, Sub]] = None
    compression_factor: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Encryption(PropertyType):
    SECRET_ARN = "SecretArn"
    KEY_TYPE = "KeyType"
    ALGORITHM = "Algorithm"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "key_type": "KeyType",
        "algorithm": "Algorithm",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FlowTransitEncryption(PropertyType):
    ENCRYPTION_KEY_TYPE = "EncryptionKeyType"
    ENCRYPTION_KEY_CONFIGURATION = "EncryptionKeyConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_type": "EncryptionKeyType",
        "encryption_key_configuration": "EncryptionKeyConfiguration",
    }

    encryption_key_type: Optional[Union[str, FlowTransitEncryptionKeyType, Ref, GetAtt, Sub]] = None
    encryption_key_configuration: Optional[FlowTransitEncryptionKeyConfiguration] = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    SECRETS_MANAGER = "SecretsManager"
    AUTOMATIC = "Automatic"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_manager": "SecretsManager",
        "automatic": "Automatic",
    }

    secrets_manager: Optional[SecretsManagerEncryptionKeyConfiguration] = None
    automatic: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Interface(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaStreamOutputConfiguration(PropertyType):
    ENCODING_PARAMETERS = "EncodingParameters"
    MEDIA_STREAM_NAME = "MediaStreamName"
    ENCODING_NAME = "EncodingName"
    DESTINATION_CONFIGURATIONS = "DestinationConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encoding_parameters": "EncodingParameters",
        "media_stream_name": "MediaStreamName",
        "encoding_name": "EncodingName",
        "destination_configurations": "DestinationConfigurations",
    }

    encoding_parameters: Optional[EncodingParameters] = None
    media_stream_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encoding_name: Optional[Union[str, EncodingName, Ref, GetAtt, Sub]] = None
    destination_configurations: Optional[list[DestinationConfiguration]] = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    SECRET_ARN = "SecretArn"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    VPC_INTERFACE_NAME = "VpcInterfaceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_interface_name": "VpcInterfaceName",
    }

    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

