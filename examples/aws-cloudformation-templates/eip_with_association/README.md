# EipWithAssociation

Migrated from [EIP_With_Association.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m eip_with_association
```

### Validate Template

```bash
python -m eip_with_association --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EC2Instance` | AWS::EC2::Instance |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `IPAddress` | AWS::EC2::EIP |
| `IPAssoc` | AWS::EC2::EIPAssociation |
