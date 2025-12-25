"""Allow running as: python -m portfolio."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="CI/CD optimized AWS CloudFormation Sample Template for AWS Service Catalog Portfolio creation. ### Before deployment please make sure that all parameters are reviewed and updated according the specific use case. ### **WARNING** This template creates AWS Service Catalog Portfolio, please make sure you review billing costs for AWS Service Catalog.")
