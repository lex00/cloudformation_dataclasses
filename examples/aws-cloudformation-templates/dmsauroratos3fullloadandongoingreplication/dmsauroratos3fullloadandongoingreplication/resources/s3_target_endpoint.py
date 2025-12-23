"""S3TargetEndpoint - AWS::DMS::Endpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3TargetEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'target'
    engine_name = 'S3'
    extra_connection_attributes = 'addColumnName=true'
    s3_settings = {
        'BucketName': ref(S3Bucket),
        'ServiceAccessRoleArn': get_att(S3TargetDMSRole, "Arn"),
    }
    depends_on = ["DMSReplicationInstance", "S3Bucket", "S3TargetDMSRole"]
