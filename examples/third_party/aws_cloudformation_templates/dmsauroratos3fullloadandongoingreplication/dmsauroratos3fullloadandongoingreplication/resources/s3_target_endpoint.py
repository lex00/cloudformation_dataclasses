from __future__ import annotations

"""S3TargetEndpoint - AWS::DMS::Endpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3TargetEndpointS3Settings:
    resource: S3Settings
    bucket_name: Ref[S3Bucket] = ref()
    service_access_role_arn: GetAtt[S3TargetDMSRole] = get_att("Arn")


@cloudformation_dataclass
class S3TargetEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: Endpoint
    endpoint_type = 'target'
    engine_name = 'S3'
    extra_connection_attributes = 'addColumnName=true'
    s3_settings = S3TargetEndpointS3Settings
    depends_on = ["DMSReplicationInstance", "S3Bucket", "S3TargetDMSRole"]
