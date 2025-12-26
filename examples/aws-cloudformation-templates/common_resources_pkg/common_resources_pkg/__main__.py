"""Allow running as: python -m common_resources_pkg."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template has resources that will be installed into all managed accounts\nin the OU. For the purposes of the sample it's not important what exactly we\nare creating here. To demonstrate the consolidated logging, errors can be\nintroduced into this template, such as choosing a bucket name that already\nexists. This template uses a Rain module, which can be packaged with `rain\npkg -x common-resources.yaml`.\n")
