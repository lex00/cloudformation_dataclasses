"""Allow running as: python -m lambda_iot_topicrule."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="lambda_iot_topicrule CloudFormation template")
