# AWS CloudFormation Template Examples

This directory contains CloudFormation template examples implemented using the `cloudformation-dataclasses` library. These examples are inspired by [AWS's official CloudFormation template examples](https://github.com/awslabs/aws-cloudformation-templates).

## Structure

Each subdirectory corresponds to an AWS service:

```
aws_cloudformation_templates/
├── DynamoDB/
│   ├── simple_table.py      # DynamoDB table with provisioned throughput
│   └── tests/
└── ...
```

## Running Examples

Generate a CloudFormation template from any example:

```bash
# From the project root
cd examples/aws_cloudformation_templates/DynamoDB
python simple_table.py
```

## Running Tests

```bash
# Run all example tests
uv run pytest examples/aws_cloudformation_templates/

# Run tests for a specific service
uv run pytest examples/aws_cloudformation_templates/DynamoDB/tests/
```

## Adding New Examples

1. Create a new directory for the AWS service (if needed)
2. Add your example module with a `build_template()` function
3. Add tests in a `tests/` subdirectory
4. Export from `__init__.py`
