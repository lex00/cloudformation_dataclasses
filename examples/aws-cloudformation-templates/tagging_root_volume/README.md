# TaggingRootVolume

Migrated from [Tagging_Root_volume.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m tagging_root_volume
```

### Validate Template

```bash
python -m tagging_root_volume --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `WindowsInstance` | AWS::EC2::Instance |
| `LinuxInstance` | AWS::EC2::Instance |
| `InstanceRole` | AWS::IAM::Role |
| `InstanceProfile` | AWS::IAM::InstanceProfile |
