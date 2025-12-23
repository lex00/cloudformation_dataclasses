# PrivateVpc

Imported from `EMRCLusterGangliaWithSparkOrS3backedHbase.yaml`.

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
uv run python -m private_vpc
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EMRCluster` | AWS::EMR::Cluster |
| `EMRClusterServiceRole` | AWS::IAM::Role |
| `EMRClusterinstanceProfileRole` | AWS::IAM::Role |
| `EMRClusterinstanceProfile` | AWS::IAM::InstanceProfile |
