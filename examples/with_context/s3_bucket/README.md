# S3Bucket

Imported from `s3_bucket_with_policy.yaml`.

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
uv run python -m s3_bucket
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `MyData` | AWS::S3::Bucket |
| `MyDataPolicy` | AWS::S3::BucketPolicy |
