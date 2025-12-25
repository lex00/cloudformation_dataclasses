"""Allow running as: python -m amzn2_greengrass_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Create Greengrass resources and group, with supporting AWS services. See https://aws.amazon.com/blogs/iot/automating-aws-iot-greengrass-setup-with-aws-cloudformation/ for further details.")
