# Vpcflowlogss3Cfn

Migrated from [VPCFlowLogsS3.cfn.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Run Tests

```bash
uv run pytest tests/ -v
```

### Generate Template

```bash
uv run python -m vpcflowlogss3_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPCFlowLogstoS3` | AWS::EC2::FlowLog |
| `VPCFlowLogsBucket` | AWS::S3::Bucket |
| `VPCFlowLogsBucketPolicy` | AWS::S3::BucketPolicy |
