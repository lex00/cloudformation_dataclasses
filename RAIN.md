# Rain Integration

## Overview

[Rain](https://github.com/aws-cloudformation/rain) is AWS's official CLI tool for CloudFormation development. It provides faster deployments, better UX, and additional features beyond the standard AWS CLI.

This document describes how `cloudformation_dataclasses` works with Rain and potential future integrations.

---

## Current Compatibility

Rain works with any valid CloudFormation template. Our generated output is fully compatible:

```python
from my_stack import MyTemplate

template = MyTemplate().resource

# JSON output - works with rain
template.to_json()

# YAML output - works with rain (requires pyyaml)
template.to_yaml()
```

### Basic Workflow

```bash
# Generate template
python my_stack.py > template.yaml

# Deploy with Rain
rain deploy template.yaml my-stack-name

# Or use Rain's other commands
rain diff template.yaml my-stack-name
rain logs my-stack-name
rain rm my-stack-name
```

---

## Rain Features

### Rain Directives

Rain supports special YAML tags for packaging and asset management:

| Directive | Purpose | Example |
|-----------|---------|---------|
| `!Rain::Embed` | Embed file contents as string | Lambda inline code |
| `!Rain::Include` | Parse and insert YAML/JSON file | Shared config |
| `!Rain::Env` | Insert environment variable | Build-time config |
| `!Rain::S3` | Upload to S3, insert URI | Lambda zip, static assets |
| `!Rain::S3Http` | Upload to S3, insert HTTP URL | Public assets |
| `!Rain::Module` | Import Rain module (experimental) | Reusable components |

### Rain Config Files

Rain accepts a config file for parameters and tags:

```yaml
# rain-config.yaml
Parameters:
  Environment: prod
  InstanceType: t3.medium
Tags:
  Team: Platform
  CostCenter: Engineering
```

```bash
rain deploy template.yaml my-stack --config rain-config.yaml
```

### Rain Deploy Options

Key flags for deployment:

- `--config` - YAML/JSON file with parameters and tags
- `--profile` - AWS CLI profile
- `--region` - Target AWS region
- `--yes` - Skip confirmation prompts
- `--detach` - Start deployment without waiting
- `--termination-protection` - Enable stack protection
- `--role-arn` - IAM role for CloudFormation to assume

---

## Future Integration Ideas

### 1. Rain Config Generation (Low Effort)

Generate Rain config files from `DeploymentContext`:

```python
# Potential API
ctx = MyDeploymentContext(stage="prod", region="us-east-1")
ctx.to_rain_config("rain-config.yaml")

# Or from Template
template.to_rain_config("rain-config.yaml",
    parameters={"Environment": "prod"},
    tags={"Team": "Platform"}
)
```

**Output:**
```yaml
Parameters:
  Environment: prod
Tags:
  Team: Platform
  Stage: prod
  Region: us-east-1
```

### 2. Rain Directive Classes (Medium Effort)

Python classes that serialize to Rain directives for asset management.

#### Basic Directives

```python
from cloudformation_dataclasses.rain import Embed, Include, Env, S3, S3Http

# Embed file contents as inline string
Embed("path/to/file.py")
# -> !Rain::Embed path/to/file.py

# Include and parse YAML/JSON file
Include("path/to/config.yaml")
# -> !Rain::Include path/to/config.yaml

# Insert environment variable value
Env("MY_VAR")
# -> !Rain::Env MY_VAR

# Upload to S3, return s3:// URI
S3("path/to/assets/")
# -> !Rain::S3 path/to/assets/

# Upload to S3, return https:// URL
S3Http("path/to/public/")
# -> !Rain::S3Http path/to/public/
```

#### S3 Asset Class for Lambda Bundles

The `S3` directive supports advanced options for Lambda deployments:

```python
@dataclass
class S3:
    """Rain S3 upload directive with build support."""
    path: str                           # Local file or directory
    zip: bool = False                   # Zip before upload (auto for dirs)
    run: Optional[str] = None           # Build script to run first
    bucket_property: str = "S3Bucket"   # Property name for bucket
    key_property: str = "S3Key"         # Property name for key
    format: str = "Uri"                 # "Uri" or "Http"
```

**Lambda with build script:**

```python
@cloudformation_dataclass
class MyLambda:
    resource: Function
    runtime = "python3.12"
    handler = "handler.main"
    code = S3(
        path="./lambda-src/",
        zip=True,
        run="./scripts/build-lambda.sh",  # Runs before upload
        bucket_property="S3Bucket",
        key_property="S3Key",
    )
```

**Generated YAML:**

```yaml
Resources:
  MyLambda:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: python3.12
      Handler: handler.main
      Code: !Rain::S3
        Path: ./lambda-src/
        Zip: true
        Run: ./scripts/build-lambda.sh
        BucketProperty: S3Bucket
        KeyProperty: S3Key
```

**After `rain deploy`**, Rain:
1. Executes `./scripts/build-lambda.sh`
2. Zips the `./lambda-src/` directory
3. Uploads to `rain-artifacts-{account}-{region}` bucket
4. Transforms template to:

```yaml
Resources:
  MyLambda:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: python3.12
      Handler: handler.main
      Code:
        S3Bucket: rain-artifacts-123456789012-us-east-1
        S3Key: abc123def456...
```

#### Simple Lambda Examples

**Inline code (small functions):**

```python
@cloudformation_dataclass
class SimpleHandler:
    resource: Function
    runtime = "python3.12"
    handler = "index.handler"
    code = Code(zip_file=Embed("./src/handler.py"))
```

**Directory bundle (typical Lambda):**

```python
@cloudformation_dataclass
class ApiHandler:
    resource: Function
    runtime = "python3.12"
    handler = "app.handler"
    code = S3("./api-lambda/", zip=True)
```

**With npm/pip build:**

```python
@cloudformation_dataclass
class NodeFunction:
    resource: Function
    runtime = "nodejs20.x"
    handler = "dist/index.handler"
    code = S3(
        path="./node-lambda/dist/",
        zip=True,
        run="cd node-lambda && npm ci && npm run build",
    )
```

#### CodeDeploy & Other Services

The same pattern works for any service needing S3 assets:

```python
# CodeDeploy revision
@cloudformation_dataclass
class AppDeployment:
    resource: DeploymentGroup
    revision = S3("./deploy-bundle/", zip=True)

# CloudFormation nested stack
@cloudformation_dataclass
class NestedStack:
    resource: Stack
    template_url = S3Http("./nested/template.yaml")

# API Gateway OpenAPI spec
@cloudformation_dataclass
class RestApi:
    resource: Api
    body = Include("./openapi/spec.yaml")

# Step Functions definition
@cloudformation_dataclass
class StateMachine:
    resource: StateMachine
    definition_string = Embed("./stepfunctions/workflow.asl.json")
```

#### Implementation Design

```python
# cloudformation_dataclasses/rain/directives.py

@dataclass
class S3:
    """Rain S3 upload directive."""
    path: str
    zip: bool = False
    run: Optional[str] = None
    bucket_property: Optional[str] = None
    key_property: Optional[str] = None
    format: str = "Uri"  # "Uri" or "Http"

    def to_yaml_tag(self) -> tuple[str, Any]:
        """Return YAML tag and value for custom representer."""
        if self.run or self.bucket_property or self.key_property:
            # Complex form with properties
            value = {"Path": self.path}
            if self.zip:
                value["Zip"] = True
            if self.run:
                value["Run"] = self.run
            if self.bucket_property:
                value["BucketProperty"] = self.bucket_property
            if self.key_property:
                value["KeyProperty"] = self.key_property
            return ("!Rain::S3", value)
        else:
            # Simple form - just path
            return ("!Rain::S3", self.path)


@dataclass
class Embed:
    """Rain file embed directive."""
    path: str

    def to_yaml_tag(self) -> tuple[str, str]:
        return ("!Rain::Embed", self.path)


@dataclass
class S3Http:
    """Rain S3 upload with HTTP URL."""
    path: str

    def to_yaml_tag(self) -> tuple[str, str]:
        return ("!Rain::S3Http", self.path)
```

#### YAML Output with Custom Tags

To generate proper Rain YAML with custom tags:

```python
import yaml

def rain_representer(dumper, data):
    """Custom YAML representer for Rain directives."""
    tag, value = data.to_yaml_tag()
    if isinstance(value, dict):
        return dumper.represent_mapping(tag, value)
    return dumper.represent_scalar(tag, value)

# Register representers
yaml.add_representer(S3, rain_representer)
yaml.add_representer(Embed, rain_representer)
yaml.add_representer(S3Http, rain_representer)
```

### 3. CLI Helper (Medium Effort)

Wrapper command for common Rain operations:

```bash
# Deploy directly from Python module
python -m cloudformation_dataclasses.rain deploy my_stack.py --stack-name prod-vpc

# Generate template and config, then deploy
python -m cloudformation_dataclasses.rain deploy my_stack.py \
    --stack-name prod-vpc \
    --config rain-config.yaml \
    --profile prod
```

### 4. Rain Module Generation (Higher Effort)

Generate Rain-compatible modules from wrapper classes:

```python
@cloudformation_dataclass
class VPCModule:
    """Reusable VPC module for Rain."""
    resource: RainModule  # Special marker

    # Module parameters
    parameters = [VPCCidr, EnableNat]

    # Module resources
    resources = [MainVPC, PublicSubnet, PrivateSubnet, NatGateway]

    # Module outputs
    outputs = [VPCIdOutput, SubnetIdsOutput]
```

---

## Comparison: Rain vs AWS CLI

| Feature | AWS CLI | Rain |
|---------|---------|------|
| Deploy speed | Slower | Faster (parallel uploads) |
| Progress display | Basic | Rich terminal UI |
| Diff before deploy | Manual | Built-in `rain diff` |
| Log streaming | Separate command | Built-in `rain logs` |
| Template packaging | `aws cloudformation package` | Automatic |
| Asset upload | Manual S3 | `!Rain::S3` directives |
| Config files | None | `--config` flag |

---

## Resources

- [Rain GitHub Repository](https://github.com/aws-cloudformation/rain)
- [Rain Documentation](https://aws-cloudformation.github.io/rain/)
- [Rain Deploy Command](https://aws-cloudformation.github.io/rain/rain_deploy.html)
- [Rain Pkg Command](https://aws-cloudformation.github.io/rain/rain_pkg.html)

---

## Status

**Current**: Full compatibility - Rain works with our JSON/YAML output

**Planned**: None currently scheduled

**Potential future work**:
1. `to_rain_config()` method for generating config files
2. Rain directive classes (`Embed`, `S3`, etc.)
3. CLI helper for deploy workflow
4. Rain module generation (see below)

---

## Rain Module Workflow

Rain modules are reusable CloudFormation components with their own Parameters, Resources, and Outputs. Here's how developers could define Python dataclasses that render as Rain modules.

### What the Developer Writes

```python
from cloudformation_dataclasses import cloudformation_dataclass
from cloudformation_dataclasses.rain import RainModule, IfParam

@cloudformation_dataclass
class SecureVPC:
    """Reusable VPC module with optional NAT Gateway."""
    resource: RainModule  # Marker indicating this generates a Rain module

    # Module parameters (become Rain module parameters)
    class Parameters:
        vpc_cidr: str = "10.0.0.0/16"
        enable_nat: bool = False

    # Resources - can use IfParam for conditional inclusion
    vpc = MainVPC(cidr_block=Ref("VpcCidr"))
    public_subnet = PublicSubnet(vpc_id=vpc.ref())
    private_subnet = PrivateSubnet(vpc_id=vpc.ref())

    # Conditional resource - only created if EnableNat parameter is true
    nat_gateway = IfParam("EnableNat", NatGateway(subnet_id=public_subnet.ref()))

    # Module outputs
    class Outputs:
        vpc_id = vpc.ref()
        public_subnet_id = public_subnet.ref()
        private_subnet_id = private_subnet.ref()
```

### What Gets Generated

```yaml
# secure_vpc.yaml - Rain module format
Rain:
  Metadata:
    Name: SecureVPC
    Description: Reusable VPC module with optional NAT Gateway.

Parameters:
  VpcCidr:
    Type: String
    Default: "10.0.0.0/16"
  EnableNat:
    Type: String
    AllowedValues: ["true", "false"]
    Default: "false"

Resources:
  MainVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidr

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MainVPC
      # ... other properties

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MainVPC
      # ... other properties

  NatGateway:
    Type: AWS::EC2::NatGateway
    Rain:
      IfParam: EnableNat  # Rain-specific conditional
    Properties:
      SubnetId: !Ref PublicSubnet

Outputs:
  VpcId:
    Value: !Ref MainVPC
  PublicSubnetId:
    Value: !Ref PublicSubnet
  PrivateSubnetId:
    Value: !Ref PrivateSubnet
```

### Using Modules in Parent Templates

```python
from cloudformation_dataclasses.rain import RainModuleRef

@cloudformation_dataclass
class ProductionInfra:
    resource: Template

    # Reference the SecureVPC module
    vpc = RainModuleRef(
        module_path="./modules/secure_vpc.yaml",
        properties={
            "VpcCidr": "10.1.0.0/16",
            "EnableNat": "true"
        }
    )

    # Use module outputs
    app_server = EC2Instance(
        subnet_id=vpc.get_output("PrivateSubnetId")
    )
```

**Parent template output:**

```yaml
Resources:
  Vpc:
    Type: !Rain::Module ./modules/secure_vpc.yaml
    Properties:
      VpcCidr: "10.1.0.0/16"
      EnableNat: "true"

  AppServer:
    Type: AWS::EC2::Instance
    Properties:
      SubnetId: !GetAtt Vpc.PrivateSubnetId
```

### Implementation Requirements

To support Rain modules, we would need:

| Component | Purpose |
|-----------|---------|
| `RainModule` marker | Signals that a class should serialize to Rain module format |
| `RainMetadata` class | Holds module name and description for Rain metadata block |
| `IfParam` / `IfNotParam` | Rain-specific conditional resource inclusion |
| `RainModuleRef` | Reference to external Rain module in parent templates |
| `to_rain_module()` | New serialization method generating Rain module YAML |
| Custom YAML representer | Outputs Rain-specific tags (`!Rain::Module`, etc.) |

### Complexity Assessment

| Feature | Effort | Value |
|---------|--------|-------|
| Basic module generation | Medium | High - enables component reuse |
| IfParam conditionals | Low | High - cleaner than CloudFormation Conditions |
| Module references | Medium | High - composable infrastructure |
| Module parameters | Low | Medium - straightforward mapping |
| Full Rain metadata | Low | Low - nice to have |

---

## Python Dataclasses vs Rain Module Syntax

### Side-by-Side Comparison

**Rain Module (Native YAML):**

```yaml
# vpc-module.yaml
Rain:
  Metadata:
    Name: SecureVPC

Parameters:
  VpcCidr:
    Type: String
    Default: "10.0.0.0/16"
  EnableNat:
    Type: String
    AllowedValues: ["true", "false"]
    Default: "false"

Resources:
  MainVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidr
      EnableDnsSupport: true

  NatGateway:
    Type: AWS::EC2::NatGateway
    Rain:
      IfParam: EnableNat
    Properties:
      SubnetId: !Ref PublicSubnet

Outputs:
  VpcId:
    Value: !Ref MainVPC
```

**Python Dataclasses (Current):**

```python
# vpc_module.py
@cloudformation_dataclass
class VpcCidr:
    resource: Parameter
    type_ = STRING
    default = "10.0.0.0/16"

@cloudformation_dataclass
class EnableNat:
    resource: Parameter
    type_ = STRING
    allowed_values = ["true", "false"]
    default = "false"

@cloudformation_dataclass
class MainVPC:
    resource: VPC
    cidr_block = ref(VpcCidr)
    enable_dns_support = True

@cloudformation_dataclass
class NatGateway:
    resource: NatGateway
    subnet_id = ref(PublicSubnet)
    condition = "NatEnabled"  # CF condition, not Rain's IfParam

@cloudformation_dataclass
class VpcIdOutput:
    resource: Output
    value = ref(MainVPC)

@cloudformation_dataclass
class VPCModule:
    resource: Template
    parameters = [VpcCidr, EnableNat]
    conditions = {"NatEnabled": Equals(ref(EnableNat), "true")}
    resources = [MainVPC, NatGateway]
    outputs = [VpcIdOutput]
```

### Feature Comparison

| Aspect | Rain YAML | Python Dataclasses |
|--------|-----------|-------------------|
| **Lines of code** | ~35 | ~45 |
| **Type safety** | None | Full (IDE autocomplete, type hints) |
| **Refactoring** | Find/replace | IDE rename, go-to-definition |
| **Reuse** | Copy/paste or `!Rain::Module` | Python imports, inheritance |
| **Conditionals** | `Rain: IfParam` (simple) | CF Conditions (verbose) |
| **Testing** | Linting only | Unit tests, property tests |
| **Composition** | Module references | Class composition, factories |
| **Learning curve** | Low (YAML) | Medium (Python + library) |

### Where Each Shines

**Rain modules work best for:**
- Small, self-contained components
- Teams comfortable with YAML
- Simple conditional resources (`IfParam` is elegant)

**Python dataclasses work best for:**
- Large, complex infrastructure
- Teams with Python experience
- Reusable patterns across many stacks
- When you need programmatic generation
- IDE support (autocomplete, type checking, refactoring)
- Testable infrastructure

### Potential Hybrid Approach

The ideal might be Python for authoring with Rain module output:

```python
# Write in Python with full IDE support
@cloudformation_dataclass
class SecureVPC:
    resource: RainModule  # Marker for Rain output

    nat = IfParam("EnableNat", NatGateway(...))  # Rain-style conditional

# Generate Rain module YAML
template.to_rain_module("secure_vpc.yaml")
```

This would give Python's authoring benefits while outputting Rain's cleaner module format with `IfParam` instead of verbose CF Conditions.

---

## Unified Conditionals Design

A key insight is that we can design a single Python API that outputs either CloudFormation Conditions or Rain's `IfParam` syntax depending on the target format.

### The Problem

CloudFormation conditionals are verbose:

```python
# Current approach - requires explicit Condition definition
@cloudformation_dataclass
class VPCModule:
    resource: Template
    conditions = {"NatEnabled": Equals(ref(EnableNat), "true")}
    resources = [NatGateway]  # NatGateway has condition="NatEnabled"
```

Rain's approach is cleaner but Rain-specific:
```yaml
NatGateway:
  Rain:
    IfParam: EnableNat
```

### Proposed API

A unified conditional that works for both output formats:

```python
from cloudformation_dataclasses.conditionals import IfParam, IfNotParam, If

# Simple parameter-based conditional (maps to Rain's IfParam)
nat_gateway = IfParam("EnableNat", NatGateway(subnet_id=ref(PublicSubnet)))

# Negated parameter conditional (maps to Rain's IfNotParam)
no_nat_warning = IfNotParam("EnableNat", CloudWatchAlarm(...))

# Value comparison
prod_resources = IfParam("Environment", HighMemoryInstance(...), equals="prod")

# Complex condition (CF only - no Rain equivalent)
complex_resource = If(
    And(
        Equals(ref(Environment), "prod"),
        Equals(ref(Region), "us-east-1")
    ),
    resource
)
```

### How It Works

```python
@dataclass
class IfParam:
    """Conditional resource based on a parameter value."""
    param_name: str
    resource: CloudFormationResource
    equals: str = "true"  # Default for boolean params

    @property
    def condition_name(self) -> str:
        """Auto-generate CF condition name."""
        return f"{self.param_name}Enabled"

    def to_cf_condition(self) -> tuple[str, dict]:
        """Generate CF Condition definition."""
        return (
            self.condition_name,
            Equals(Ref(self.param_name), self.equals).to_dict()
        )

    def to_rain_metadata(self) -> dict:
        """Generate Rain resource metadata."""
        return {"Rain": {"IfParam": self.param_name}}
```

### Output Comparison

**Same Python code:**
```python
@cloudformation_dataclass
class VPCModule:
    resource: Template
    nat = IfParam("EnableNat", NatGateway(subnet_id=ref(PublicSubnet)))
```

**CF Output (`to_json()`):**
```json
{
  "Conditions": {
    "EnableNatEnabled": {"Fn::Equals": [{"Ref": "EnableNat"}, "true"]}
  },
  "Resources": {
    "NatGateway": {
      "Type": "AWS::EC2::NatGateway",
      "Condition": "EnableNatEnabled",
      "Properties": {"SubnetId": {"Ref": "PublicSubnet"}}
    }
  }
}
```

**Rain Output (`to_rain_module()`):**
```yaml
Resources:
  NatGateway:
    Type: AWS::EC2::NatGateway
    Rain:
      IfParam: EnableNat
    Properties:
      SubnetId: !Ref PublicSubnet
```

### Template Serialization Logic

```python
class Template:
    def to_dict(self) -> dict:
        """Standard CF output - expands IfParam to Conditions."""
        conditions = {}
        resources = {}

        for item in self.resources:
            if isinstance(item, IfParam):
                # Extract and add condition
                cond_name, cond_def = item.to_cf_condition()
                conditions[cond_name] = cond_def

                # Add resource with condition reference
                resource = item.resource
                resource.condition = cond_name
                resources[resource.logical_id] = resource.to_dict()
            else:
                resources[item.logical_id] = item.to_dict()

        result = {"Resources": resources}
        if conditions:
            result["Conditions"] = conditions
        return result

    def to_rain_module(self) -> str:
        """Rain module output - uses Rain metadata."""
        resources = {}

        for item in self.resources:
            if isinstance(item, IfParam):
                resource_dict = item.resource.to_dict()
                resource_dict.update(item.to_rain_metadata())
                resources[item.resource.logical_id] = resource_dict
            else:
                resources[item.logical_id] = item.to_dict()

        return yaml.dump({"Resources": resources})
```

### Extended Conditionals

```python
# Boolean parameter (true/false string) - default
IfParam("EnableNat", resource)
# CF: Equals(Ref("EnableNat"), "true")
# Rain: IfParam: EnableNat

# Specific value comparison
IfParam("Environment", resource, equals="prod")
# CF: Equals(Ref("Environment"), "prod")
# Rain: Not directly supported, falls back to CF Condition

# Negation
IfNotParam("EnableNat", resource)
# CF: Not(Equals(Ref("EnableNat"), "true"))
# Rain: IfNotParam: EnableNat

# Complex conditions (CF only)
If(And(condition1, condition2), resource)
# CF: Full Condition support
# Rain: Falls back to CF Condition (no Rain equivalent)
```

### Implementation Complexity

| Component | Effort | Notes |
|-----------|--------|-------|
| `IfParam` / `IfNotParam` classes | Low | Simple dataclasses |
| Template condition extraction | Medium | Walk resources, collect conditions |
| Rain metadata injection | Low | Add dict to resource output |
| `to_rain_module()` method | Medium | YAML with custom tags |
| Complex `If` with conditions | Medium | Already have condition functions |

### Key Insight

`IfParam("EnableNat", resource)` is **syntactic sugar** that means different things in different contexts:

- **CF context**: Generates a Condition + sets `resource.condition`
- **Rain context**: Adds `Rain: {IfParam: EnableNat}` metadata

The Python API stays the same; only the output format changes. This gives developers a clean, unified way to express conditionals while supporting both deployment targets.

---

## Rain Adoption & Market Context

### Rain's Current Status

Rain is a niche but actively maintained tool within the CloudFormation ecosystem:

| Metric | Value |
|--------|-------|
| GitHub Stars | ~932 |
| Forks | 87 |
| Contributors | 54+ |
| Releases | 77 (latest v1.24.1, Nov 2025) |

From the [Rain maintainer](https://github.com/aws-cloudformation/rain/discussions/179):

> "I'm the primary maintainer of rain. I'm a Solutions Architect at AWS specializing in Infrastructure as Code. Rain's growth has been entirely organic, with no marketing support."

### IaC Tool Comparison

| Tool | GitHub Stars | Focus |
|------|-------------|-------|
| **Terraform** | ~43,000 | Multi-cloud IaC |
| **Pulumi** | ~22,000 | Multi-cloud with programming languages |
| **AWS CDK** | ~11,500 | AWS with programming languages |
| **Rain** | ~932 | CloudFormation workflow enhancement |

Rain is significantly smaller than the major IaC tools because it's **not a replacement for CloudFormation** - it's a developer experience enhancement for existing CF users.

### Why Rain Has Limited Adoption

1. **Narrow scope** - Only enhances CF, doesn't replace it
2. **No marketing** - Organic growth only
3. **CDK competition** - Teams wanting "better CF" often jump to CDK instead
4. **Terraform dominance** - Multi-cloud shops skip CF entirely

### Market Landscape

| Tool | Released | Best For |
|------|----------|----------|
| **CloudFormation** | 2011 | AWS-native, YAML/JSON preferred |
| **Terraform** | 2014 | Multi-cloud, declarative HCL |
| **CDK** | 2019 | AWS + programming languages |
| **Rain** | 2020 | CF power users wanting better DX |

**Market reality:**
- Terraform dominates enterprise multi-cloud (~40-50% of IaC market)
- CDK is growing fast for AWS-focused teams
- Raw CloudFormation is still widely used but often seen as legacy
- Rain is a "power user" tool with small but dedicated following

### Implications for cloudformation_dataclasses

Rain integration makes sense because:

1. **Complementary tools** - Both target CF power users who want better DX
2. **Similar philosophy** - Enhance CF rather than replace it
3. **Low adoption barrier** - Rain users are already CF-invested
4. **Module system** - Rain modules offer reusable components that align with our wrapper pattern

However, the realistic user base for Rain-specific features is small (~1,000 GitHub stars suggests low thousands of active users globally).

**Recommendation:** Support Rain output as an optional enhancement, not a core feature. Focus on standard CF compatibility first.

### Sources

- [AWS CloudFormation Rain GitHub](https://github.com/aws-cloudformation/rain)
- [Rain User Feedback Discussion](https://github.com/aws-cloudformation/rain/discussions/179)
- [CDK vs Terraform vs CloudFormation Comparison](https://www.pluralsight.com/resources/blog/cloud/cloudformation-terraform-or-cdk-guide-to-iac-on-aws)
- [AWS CloudFormation 2024 Year in Review](https://aws.amazon.com/blogs/devops/aws-cloudformation-2024-year-in-review/)

---

## Adopting Dataclasses in an Existing Rain Project

Existing Rain projects can incrementally adopt `cloudformation_dataclasses` without disrupting their current workflow. The key is that Python-generated YAML is just YAML - Rain doesn't care how it was created.

### Typical Rain Project Structure

```
infrastructure/
├── modules/                    # Rain modules (YAML)
│   ├── vpc.yaml               # !Rain::Module components
│   ├── database.yaml
│   └── lambda-api.yaml
├── stacks/                    # Parent templates
│   ├── dev.yaml
│   ├── staging.yaml
│   └── prod.yaml
├── configs/                   # Rain config files
│   ├── dev.yaml
│   └── prod.yaml
└── deploy.sh                  # Deployment script
```

### Goal: Add Python Without Disrupting

An existing Rain user wants to:
1. Keep existing Rain modules working
2. Import select modules to Python for enhancement
3. Have both YAML and Python-generated output coexist
4. Maintain their `rain deploy` workflow

### Strategy: Side-by-Side Generation

```
infrastructure/
├── modules/                    # Existing Rain modules (untouched)
│   ├── vpc.yaml
│   ├── database.yaml
│   └── lambda-api.yaml
├── python/                     # NEW: Python source
│   ├── __init__.py
│   ├── monitoring.py           # New module in Python
│   └── imported/               # Imported from YAML
│       └── vpc.py              # Imported, now editable
├── generated/                  # NEW: Python → YAML output
│   └── monitoring.yaml         # Generated from python/
├── stacks/
│   ├── dev.yaml               # Can reference both modules/ and generated/
│   └── prod.yaml
└── Makefile                   # Build + deploy
```

### Import a Rain Module to Python

```bash
# Import existing Rain module, preserving Rain-specific features
cfn-import modules/vpc.yaml -o python/imported/vpc.py --preserve-rain

# The importer recognizes Rain metadata and conditionals:
# - Rain: Metadata → docstring + metadata dict
# - IfParam/IfNotParam → preserved as comments or future IfParam class
```

**Input (`modules/vpc.yaml`):**
```yaml
Rain:
  Metadata:
    Name: SecureVPC
    Description: VPC with optional NAT

Parameters:
  VpcCidr:
    Type: String
    Default: "10.0.0.0/16"
  EnableNat:
    Type: String
    Default: "false"

Resources:
  MainVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCidr

  NatGateway:
    Type: AWS::EC2::NatGateway
    Rain:
      IfParam: EnableNat
    Properties:
      SubnetId: !Ref PublicSubnet
```

**Output (`python/imported/vpc.py`):**
```python
"""
SecureVPC - VPC with optional NAT

Imported from: modules/vpc.yaml
Rain module: True
"""

from cloudformation_dataclasses import cloudformation_dataclass, ref
from cloudformation_dataclasses.aws.ec2 import VPC, NatGateway, Subnet
from cloudformation_dataclasses.core import Template, Parameter

# Original Rain metadata preserved
RAIN_METADATA = {
    "Name": "SecureVPC",
    "Description": "VPC with optional NAT",
}


@cloudformation_dataclass
class VpcCidr:
    resource: Parameter
    type_ = "String"
    default = "10.0.0.0/16"


@cloudformation_dataclass
class EnableNat:
    resource: Parameter
    type_ = "String"
    default = "false"


@cloudformation_dataclass
class MainVPC:
    resource: VPC
    cidr_block = ref(VpcCidr)


@cloudformation_dataclass
class NatGatewayResource:
    """
    NOTE: Original had Rain IfParam conditional.
    To preserve Rain behavior, output as Rain module with:
        template.to_rain_module()

    For standard CF output, use Condition instead:
        condition = "NatEnabled"
    """
    resource: NatGateway
    subnet_id = ref(PublicSubnet)
    # Rain: IfParam: EnableNat  (preserved in to_rain_module() output)
    _rain_if_param = "EnableNat"  # Metadata for Rain output


@cloudformation_dataclass
class SecureVPCModule:
    resource: Template
    description = "VPC with optional NAT"
    parameters = [VpcCidr, EnableNat]
    resources = [MainVPC, PublicSubnet, PrivateSubnet, NatGatewayResource]


def build_module():
    return SecureVPCModule().resource


if __name__ == "__main__":
    template = build_module()
    # Output as Rain module (preserves IfParam)
    print(template.to_rain_module())
```

### Generate YAML That Works with Rain

```bash
# Generate Rain-compatible YAML
python python/imported/vpc.py > generated/vpc.yaml

# Or use a build script
make generate
```

**Makefile:**
```makefile
PYTHON_MODULES := $(wildcard python/*.py python/imported/*.py)
GENERATED := $(patsubst python/%.py,generated/%.yaml,$(PYTHON_MODULES))

generate: $(GENERATED)

generated/%.yaml: python/%.py
	@mkdir -p $(dir $@)
	python $< > $@

deploy-dev: generate
	rain deploy stacks/dev.yaml dev-stack --config configs/dev.yaml

deploy-prod: generate
	rain deploy stacks/prod.yaml prod-stack --config configs/prod.yaml
```

### Reference Both Module Types in Parent Templates

Parent templates can mix original Rain modules with Python-generated ones:

```yaml
# stacks/prod.yaml
Resources:
  # Original Rain module (unchanged)
  Database:
    Type: !Rain::Module ../modules/database.yaml
    Properties:
      InstanceClass: db.r5.xlarge

  # Python-generated module (same syntax!)
  VPC:
    Type: !Rain::Module ../generated/vpc.yaml
    Properties:
      VpcCidr: "10.1.0.0/16"
      EnableNat: "true"

  # New Python-generated module
  Monitoring:
    Type: !Rain::Module ../generated/monitoring.yaml
    Properties:
      AlertEmail: ops@example.com
```

Rain doesn't care whether the YAML was hand-written or generated - it's all just YAML.

### Preserving Rain Directives

When importing templates with Rain directives, the importer preserves them:

**Input:**
```yaml
Resources:
  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        ZipFile: !Rain::Embed ./src/handler.py
```

**Output (`--preserve-rain`):**
```python
from cloudformation_dataclasses.rain import Embed

@cloudformation_dataclass
class MyFunction:
    resource: Function
    code = Code(zip_file=Embed("./src/handler.py"))
```

**Generated YAML:**
```yaml
Resources:
  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        ZipFile: !Rain::Embed ./src/handler.py
```

### Workflow Comparison

| Step | Before (Pure Rain) | After (Hybrid) |
|------|-------------------|----------------|
| Edit module | Edit YAML directly | Edit Python or YAML |
| Validate | `rain fmt`, `rain ls` | Python type checker + rain commands |
| Generate | N/A | `make generate` |
| Deploy | `rain deploy` | `rain deploy` (unchanged) |
| View diff | `rain diff` | `rain diff` (unchanged) |
| Rollback | `rain rm` | `rain rm` (unchanged) |

### Migration Phases

**Phase 1: Observe**
- Keep all existing Rain modules
- Install cloudformation_dataclasses
- Import one simple module as a test

**Phase 2: Parallel Development**
- New modules written in Python
- Generated YAML placed in `generated/`
- Existing modules stay in `modules/`
- Both referenced from parent templates

**Phase 3: Gradual Import**
- Import complex modules that need refactoring
- Enhance with Python features (loops, conditionals, reuse)
- Keep simple modules as YAML

**Phase 4: Full Python (Optional)**
- All modules in Python
- YAML becomes build artifact
- Rain workflow unchanged (still deploy YAML)

### Import Options for Rain Modules

```bash
# Basic import
cfn-import modules/vpc.yaml -o python/vpc.py

# Preserve Rain-specific features for round-trip
cfn-import modules/vpc.yaml -o python/vpc.py --preserve-rain

# Import as standard CF (convert IfParam to Conditions)
cfn-import modules/vpc.yaml -o python/vpc.py --mode standard

# Import multiple modules
cfn-import modules/ -o python/imported/ --recursive --preserve-rain
```

### Output Modes

| Flag | Rain Metadata | IfParam/IfNotParam | Directives |
|------|--------------|-------------------|------------|
| `--preserve-rain` | Kept as dict | Preserved for `to_rain_module()` | `Embed()`, `S3()` classes |
| `--mode standard` | Converted to docstring | Converted to CF Conditions | Expanded inline |
| (default) | Best effort | Preserved with comments | Preserved |

### Key Benefits

1. **Zero disruption** - Rain workflow stays exactly the same
2. **Incremental adoption** - Import one module at a time
3. **Best of both worlds** - Python authoring, Rain deployment
4. **Reversible** - Generated YAML is valid Rain input
5. **No lock-in** - Can always go back to hand-written YAML

---

## Nested Stacks with Rain

CloudFormation nested stacks allow breaking large templates into smaller, reusable components. Rain's `!Rain::S3Http` directive makes nested stacks much easier by automatically uploading child templates to S3.

### The Problem with Native CloudFormation

Without Rain, nested stacks require manual S3 management:

```yaml
# Native CF - you must upload child template yourself
Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/my-bucket/stacks/vpc.yaml  # Manual upload!
      Parameters:
        Environment: !Ref Environment
```

### Rain's Solution: S3Http Auto-Upload

Rain's `!Rain::S3Http` directive automatically uploads local files to S3 during deployment:

```yaml
# With Rain - automatic upload
Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Rain::S3Http ./stacks/vpc.yaml  # Uploaded automatically
      Parameters:
        Environment: !Ref Environment
```

### Python Dataclasses + Rain = Nested Stack Support

Since `cloudformation_dataclasses` can generate templates with Rain directives, you get full nested stack support:

```python
from cloudformation_dataclasses import cloudformation_dataclass, ref
from cloudformation_dataclasses.aws.cloudformation import Stack
from cloudformation_dataclasses.rain import S3Http

# Child template reference using Rain's S3Http directive
@cloudformation_dataclass
class VPCStack:
    """Nested VPC infrastructure stack."""
    resource: Stack
    template_url = S3Http("./stacks/vpc.yaml")
    parameters = {
        "Environment": ref(Environment),
        "VpcCidr": "10.0.0.0/16",
    }

@cloudformation_dataclass
class DatabaseStack:
    """Nested database stack."""
    resource: Stack
    template_url = S3Http("./stacks/database.yaml")
    parameters = {
        "Environment": ref(Environment),
        "VpcId": get_att(VPCStack, "Outputs.VpcId"),
        "SubnetIds": get_att(VPCStack, "Outputs.PrivateSubnetIds"),
    }

@cloudformation_dataclass
class ApplicationStack:
    """Nested application stack."""
    resource: Stack
    template_url = S3Http("./stacks/app.yaml")
    parameters = {
        "Environment": ref(Environment),
        "VpcId": get_att(VPCStack, "Outputs.VpcId"),
        "DatabaseEndpoint": get_att(DatabaseStack, "Outputs.Endpoint"),
    }
    depends_on = [DatabaseStack.__name__]

@cloudformation_dataclass
class ParentInfrastructure:
    """Parent stack orchestrating all nested stacks."""
    resource: Template
    description = "Multi-tier application infrastructure"
    parameters = [Environment]
    resources = [VPCStack, DatabaseStack, ApplicationStack]
    outputs = [
        VpcIdOutput,
        DatabaseEndpointOutput,
        ApplicationUrlOutput,
    ]
```

**Generated YAML:**

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Multi-tier application infrastructure

Parameters:
  Environment:
    Type: String
    AllowedValues: [dev, staging, prod]

Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Rain::S3Http ./stacks/vpc.yaml
      Parameters:
        Environment: !Ref Environment
        VpcCidr: "10.0.0.0/16"

  DatabaseStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Rain::S3Http ./stacks/database.yaml
      Parameters:
        Environment: !Ref Environment
        VpcId: !GetAtt VPCStack.Outputs.VpcId
        SubnetIds: !GetAtt VPCStack.Outputs.PrivateSubnetIds

  ApplicationStack:
    Type: AWS::CloudFormation::Stack
    DependsOn: DatabaseStack
    Properties:
      TemplateURL: !Rain::S3Http ./stacks/app.yaml
      Parameters:
        Environment: !Ref Environment
        VpcId: !GetAtt VPCStack.Outputs.VpcId
        DatabaseEndpoint: !GetAtt DatabaseStack.Outputs.Endpoint

Outputs:
  VpcId:
    Value: !GetAtt VPCStack.Outputs.VpcId
  DatabaseEndpoint:
    Value: !GetAtt DatabaseStack.Outputs.Endpoint
  ApplicationUrl:
    Value: !GetAtt ApplicationStack.Outputs.Url
```

### Full Python Generation: Child and Parent Templates

For maximum type safety, generate both parent and child templates from Python:

```
infrastructure/
├── python/
│   ├── parent.py              # Orchestration stack
│   ├── stacks/
│   │   ├── vpc.py             # VPC child template
│   │   ├── database.py        # Database child template
│   │   └── app.py             # Application child template
├── generated/
│   ├── parent.yaml            # Generated parent
│   └── stacks/
│       ├── vpc.yaml           # Generated child (referenced by parent)
│       ├── database.yaml
│       └── app.yaml
└── Makefile
```

**Makefile:**

```makefile
all: generate

generate:
	python python/stacks/vpc.py > generated/stacks/vpc.yaml
	python python/stacks/database.py > generated/stacks/database.yaml
	python python/stacks/app.py > generated/stacks/app.yaml
	python python/parent.py > generated/parent.yaml

deploy-dev: generate
	cd generated && rain deploy parent.yaml dev-infrastructure --config ../configs/dev.yaml

deploy-prod: generate
	cd generated && rain deploy parent.yaml prod-infrastructure --config ../configs/prod.yaml
```

**Build flow:**

1. Generate all child templates from Python
2. Generate parent template (references child paths)
3. `rain deploy` uploads all templates via `!Rain::S3Http`
4. CloudFormation creates nested stack hierarchy

### Cross-Stack References

Access outputs from nested stacks using `!GetAtt`:

```python
# In Python
database_endpoint = get_att(DatabaseStack, "Outputs.Endpoint")

# In generated YAML
# DatabaseEndpoint: !GetAtt DatabaseStack.Outputs.Endpoint
```

### Shared Components Across Stacks

Define reusable components once, use in multiple child templates:

```python
# python/shared/security_groups.py
@cloudformation_dataclass
class WebServerSecurityGroup:
    """Reusable web server security group."""
    resource: SecurityGroup
    group_description = "Allow HTTP/HTTPS traffic"
    security_group_ingress = [
        SecurityGroupIngress(ip_protocol="tcp", from_port=80, to_port=80, cidr_ip="0.0.0.0/0"),
        SecurityGroupIngress(ip_protocol="tcp", from_port=443, to_port=443, cidr_ip="0.0.0.0/0"),
    ]

# python/stacks/app.py
from shared.security_groups import WebServerSecurityGroup

@cloudformation_dataclass
class AppTemplate:
    resource: Template
    resources = [
        WebServerSecurityGroup,  # Imported from shared module
        AppServer,
        LoadBalancer,
    ]
```

### Nested Stack Outputs

Export values from child stacks for use elsewhere:

```python
# In child stack (vpc.py)
@cloudformation_dataclass
class VpcIdOutput:
    resource: Output
    value = ref(MainVPC)
    export = Export(name=sub("${AWS::StackName}-VpcId"))

@cloudformation_dataclass
class PrivateSubnetIdsOutput:
    resource: Output
    value = join(",", [ref(PrivateSubnet1), ref(PrivateSubnet2)])
    export = Export(name=sub("${AWS::StackName}-PrivateSubnetIds"))

# In parent stack
vpc_id = get_att(VPCStack, "Outputs.VpcId")
```

### Nested vs Rain Modules

| Feature | Nested Stacks | Rain Modules |
|---------|--------------|--------------|
| **Scope** | Full CloudFormation templates | Reusable components |
| **State** | Separate stack with own resources | Expanded into parent |
| **Updates** | Can update child independently | Requires parent redeploy |
| **Outputs** | Cross-stack via `!GetAtt` | Inline in parent |
| **Drift** | Separate drift detection | Part of parent |
| **Limits** | 500 resources per nested stack | Combined into parent limit |
| **Rollback** | Per-stack rollback | Full template rollback |

**When to use nested stacks:**
- Large infrastructure with 100+ resources
- Components that update independently
- Separate IAM permissions per component
- Need to stay under CloudFormation limits

**When to use Rain modules:**
- Smaller reusable patterns
- Always deployed together
- Simpler cross-component references
- Fewer moving parts

### S3Http Directive Implementation

```python
@dataclass
class S3Http:
    """Rain S3 upload directive returning HTTPS URL."""
    path: str

    def to_yaml_tag(self) -> tuple[str, str]:
        return ("!Rain::S3Http", self.path)

    def to_dict(self) -> dict[str, Any]:
        """For JSON output, cannot use Rain directive."""
        raise ValueError(
            "S3Http requires YAML output with Rain. "
            "Use template.to_rain_yaml() or manually upload to S3."
        )
```

### Complete Example: Three-Tier Architecture

```python
# python/parent.py
from cloudformation_dataclasses import cloudformation_dataclass, ref, get_att, sub
from cloudformation_dataclasses.aws.cloudformation import Stack
from cloudformation_dataclasses.core import Template, Parameter, Output
from cloudformation_dataclasses.rain import S3Http

@cloudformation_dataclass
class Environment:
    resource: Parameter
    type_ = "String"
    allowed_values = ["dev", "staging", "prod"]
    default = "dev"

@cloudformation_dataclass
class NetworkStack:
    resource: Stack
    template_url = S3Http("./stacks/network.yaml")
    parameters = {"Environment": ref(Environment)}

@cloudformation_dataclass
class DataStack:
    resource: Stack
    template_url = S3Http("./stacks/data.yaml")
    parameters = {
        "Environment": ref(Environment),
        "VpcId": get_att(NetworkStack, "Outputs.VpcId"),
        "PrivateSubnets": get_att(NetworkStack, "Outputs.PrivateSubnetIds"),
    }

@cloudformation_dataclass
class ComputeStack:
    resource: Stack
    template_url = S3Http("./stacks/compute.yaml")
    depends_on = [DataStack.__name__]
    parameters = {
        "Environment": ref(Environment),
        "VpcId": get_att(NetworkStack, "Outputs.VpcId"),
        "PublicSubnets": get_att(NetworkStack, "Outputs.PublicSubnetIds"),
        "DatabaseEndpoint": get_att(DataStack, "Outputs.DatabaseEndpoint"),
        "CacheEndpoint": get_att(DataStack, "Outputs.CacheEndpoint"),
    }

@cloudformation_dataclass
class AppUrlOutput:
    resource: Output
    description = "Application URL"
    value = get_att(ComputeStack, "Outputs.LoadBalancerDNS")

@cloudformation_dataclass
class ThreeTierApp:
    resource: Template
    description = "Three-tier application with nested stacks"
    parameters = [Environment]
    resources = [NetworkStack, DataStack, ComputeStack]
    outputs = [AppUrlOutput]

if __name__ == "__main__":
    print(ThreeTierApp().resource.to_rain_yaml())
```

**Deploy:**

```bash
# Generate all templates
make generate

# Deploy with Rain (S3Http handles all uploads)
cd generated && rain deploy parent.yaml my-app-prod --config ../configs/prod.yaml
```

Rain automatically:
1. Uploads `stacks/network.yaml` to S3
2. Uploads `stacks/data.yaml` to S3
3. Uploads `stacks/compute.yaml` to S3
4. Replaces `!Rain::S3Http` with actual S3 URLs
5. Deploys parent stack with nested stack references
