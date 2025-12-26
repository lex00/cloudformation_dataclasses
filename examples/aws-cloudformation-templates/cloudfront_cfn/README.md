# CloudfrontCfn

Imported from `ubuntu20.04_cfn-hup.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cloudfront_cfn
```

### Validate Template

```bash
python -m cloudfront_cfn --validate
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
