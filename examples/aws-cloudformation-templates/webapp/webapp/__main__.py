"""Allow running as: python -m webapp."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Creates a web application with a static website using S3 and CloudFront, an API Gateway REST API, and a DynamoDB table, with Cognito authentication. Apache-2.0 License. Adapt this template to your needs and thoruoughly test it before introducing it in a production environment. **WARNING** This template will create resources in your account that may incur billing charges.")
