# Efsaccesspoint

Migrated from [EFSAccessPoint.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m efsaccesspoint
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
