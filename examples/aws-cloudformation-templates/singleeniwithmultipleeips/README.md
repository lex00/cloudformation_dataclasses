# Singleeniwithmultipleeips

Migrated from [SingleENIwithMultipleEIPs.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m singleeniwithmultipleeips
```

### Validate Template

```bash
python -m singleeniwithmultipleeips --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EIP1` | AWS::EC2::EIP |
| `EIP2` | AWS::EC2::EIP |
| `Association1` | AWS::EC2::EIPAssociation |
| `Association2` | AWS::EC2::EIPAssociation |
| `ENI` | AWS::EC2::NetworkInterface |
