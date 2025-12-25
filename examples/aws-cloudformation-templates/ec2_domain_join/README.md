# Ec2DomainJoin

Migrated from [EC2-Domain-Join.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m ec2_domain_join
```

### Validate Template

```bash
python -m ec2_domain_join --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `myssmdocument` | AWS::SSM::Document |
| `myEC2InstanceSSM` | AWS::EC2::Instance |
| `myInstanceProfile` | AWS::IAM::InstanceProfile |
| `myEC2SSMRole` | AWS::IAM::Role |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
