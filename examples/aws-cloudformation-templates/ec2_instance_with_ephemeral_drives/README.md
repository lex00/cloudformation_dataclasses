# Ec2InstanceWithEphemeralDrives

Migrated from [EC2_Instance_With_Ephemeral_Drives.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m ec2_instance_with_ephemeral_drives
```

### Validate Template

```bash
python -m ec2_instance_with_ephemeral_drives --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EC2Instance` | AWS::EC2::Instance |
| `EC2SecurityGroup` | AWS::EC2::SecurityGroup |
