"""Compliant S3 Bucket example.

A secure bucket that passes default security scanning checks.
Includes replication and access logging.

Source: https://github.com/awslabs/aws-cloudformation-templates/blob/main/S3/compliant-bucket.yaml
"""

from .main import build_template

__all__ = ["build_template"]
