"""Allow running as: python -m sqsfifoqueue."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Best Practice SQS FIFO Queue, only available in us-east-1, us-east-2, us-west-2, eu-west-1, ap-northeast-1, ap-southeast-2 at time of template creation.")
