# Efsaccesspoint

Migrated from [EFSAccessPoint.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m efsaccesspoint
```

### Validate Template

```bash
python -m efsaccesspoint --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EFSFileSystem` | AWS::EFS::FileSystem |
| `EFSMountTarget1` | AWS::EFS::MountTarget |
| `EFSMountTarget2` | AWS::EFS::MountTarget |
| `EFSMountTarget3` | AWS::EFS::MountTarget |
| `EFSAccessPoint` | AWS::EFS::AccessPoint |
