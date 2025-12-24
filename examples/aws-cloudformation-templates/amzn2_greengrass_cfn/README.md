# Amzn2GreengrassCfn

Migrated from [amzn2-greengrass-cfn.json](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m amzn2_greengrass_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `GreengrassGroup` | AWS::Greengrass::Group |
| `GreengrassCoreDefinition` | AWS::Greengrass::CoreDefinition |
| `GreengrassCoreDefinitionVersion` | AWS::Greengrass::CoreDefinitionVersion |
| `FunctionDefinition` | AWS::Greengrass::FunctionDefinition |
| `SubscriptionDefinition` | AWS::Greengrass::SubscriptionDefinition |
| `GGSampleFunction` | AWS::Lambda::Function |
| `GGSampleFunctionVersion` | AWS::Lambda::Version |
| `VPC` | AWS::EC2::VPC |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `VPCGatewayAttachment` | AWS::EC2::VPCGatewayAttachment |
| `SubnetAPublic` | AWS::EC2::Subnet |
| `RouteTablePublic` | AWS::EC2::RouteTable |
| `RouteTableAssociationAPublic` | AWS::EC2::SubnetRouteTableAssociation |
| `RouteTablePublicInternetRoute` | AWS::EC2::Route |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `GreengrassInstance` | AWS::EC2::Instance |
| `IoTThing` | Custom::IoTThing |
| `CreateThingFunction` | AWS::Lambda::Function |
| `GroupDeploymentReset` | Custom::GroupDeploymentReset |
| `GroupDeploymentResetFunction` | AWS::Lambda::Function |
| `InstanceAZ` | Custom::InstanceAZ |
| `InstanceAZFunction` | AWS::Lambda::Function |
| `LambdaExecutionRole` | AWS::IAM::Role |
| `GreengrassResourceRole` | AWS::IAM::Role |
