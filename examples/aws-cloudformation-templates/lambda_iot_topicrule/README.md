# LambdaIotTopicrule

Imported from `RDS_Snapshot_On_Delete.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m lambda_iot_topicrule
```

### Validate Template

```bash
python -m lambda_iot_topicrule --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `MyDB` | AWS::RDS::DBInstance |
