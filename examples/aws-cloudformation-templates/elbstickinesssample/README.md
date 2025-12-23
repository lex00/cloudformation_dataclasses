# Elbstickinesssample

Migrated from [ELBStickinessSample.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m elbstickinesssample
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancing::LoadBalancer |
| `EC2Instance1` | AWS::EC2::Instance |
| `EC2Instance2` | AWS::EC2::Instance |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
