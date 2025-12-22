"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = """#!PyPlate
output = []
for tag in params['Tags']:
   key, value = tag.split('=')
   output.append({"Key": key, "Value": value})"""
