# Vpc

Imported from `Product.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m vpc
```

### Validate Template

```bash
python -m vpc --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ServiceCatalogCloudFormationProduct` | AWS::ServiceCatalog::CloudFormationProduct |
| `ServiceCatalogPortfolioProductAssociation` | AWS::ServiceCatalog::PortfolioProductAssociation |
| `ServiceCatalogCustomTagOptionsAssociation` | AWS::ServiceCatalog::TagOptionAssociation |
