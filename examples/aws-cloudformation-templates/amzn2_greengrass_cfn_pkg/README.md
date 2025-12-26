# Amzn2GreengrassCfnPkg

Imported from `RDS_with_DBParameterGroup.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m amzn2_greengrass_cfn_pkg
```

### Validate Template

```bash
python -m amzn2_greengrass_cfn_pkg --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `MyDB` | AWS::RDS::DBInstance |
| `MyRDSParamGroup` | AWS::RDS::DBParameterGroup |
