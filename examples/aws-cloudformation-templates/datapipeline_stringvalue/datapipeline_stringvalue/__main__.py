"""Allow running as: python -m datapipeline_stringvalue."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="A CloudFormation template which shows how to provide multiple values to one StringValue when creating a DataPipeline definition, This template is entirely based on the example provided in the DataPipeline documentation here: http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-emrconfiguration.html - Written by Nishant Casey")
