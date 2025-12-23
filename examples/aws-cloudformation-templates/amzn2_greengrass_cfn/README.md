# Amzn2GreengrassCfn

Imported from `cloudfront-nocache.yml`.

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
uv run python -m amzn2_greengrass_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CachePolicy` | AWS::CloudFront::CachePolicy |
| `Distribution` | AWS::CloudFront::Distribution |
