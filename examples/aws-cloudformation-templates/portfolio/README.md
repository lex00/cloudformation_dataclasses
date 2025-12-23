# Portfolio

Migrated from [Portfolio.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m portfolio
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ServiceCatalogPortfolio` | AWS::ServiceCatalog::Portfolio |
| `ServiceCatalogProductTagOptionsDept` | AWS::ServiceCatalog::TagOption |
| `ServiceCatalogProductTagOptionsEnv` | AWS::ServiceCatalog::TagOption |
| `ServiceCatalogProductTagOptionsUser` | AWS::ServiceCatalog::TagOption |
| `ServiceCatalogProductTagOptionsOwner` | AWS::ServiceCatalog::TagOption |
| `ServiceCatalogPortfolioShare` | AWS::ServiceCatalog::PortfolioShare |
