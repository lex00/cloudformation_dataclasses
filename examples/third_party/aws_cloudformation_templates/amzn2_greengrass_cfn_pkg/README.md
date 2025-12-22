# Amzn2GreengrassCfnPkg

Imported from `amzn2-greengrass-cfn-pkg.yaml`.

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
uv run python -m amzn2_greengrass_cfn_pkg
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CreateThingFunction` | AWS::Lambda::Function |
| `FunctionDefinition` | AWS::Greengrass::FunctionDefinition |
| `GGSampleFunction` | AWS::Lambda::Function |
| `GGSampleFunctionVersion` | AWS::Lambda::Version |
| `GreengrassCoreDefinition` | AWS::Greengrass::CoreDefinition |
| `GreengrassCoreDefinitionVersion` | AWS::Greengrass::CoreDefinitionVersion |
| `GreengrassGroup` | AWS::Greengrass::Group |
| `GreengrassInstance` | AWS::EC2::Instance |
| `GreengrassResourceRole` | AWS::IAM::Role |
| `GroupDeploymentReset` | Custom::GroupDeploymentReset |
| `GroupDeploymentResetFunction` | AWS::Lambda::Function |
| `InstanceAZ` | Custom::InstanceAZ |
| `InstanceAZFunction` | AWS::Lambda::Function |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `IoTThing` | Custom::IoTThing |
| `LambdaExecutionRole` | AWS::IAM::Role |
| `RouteTableAssociationAPublic` | AWS::EC2::SubnetRouteTableAssociation |
| `RouteTablePublic` | AWS::EC2::RouteTable |
| `RouteTablePublicInternetRoute` | AWS::EC2::Route |
| `SubnetAPublic` | AWS::EC2::Subnet |
| `SubscriptionDefinition` | AWS::Greengrass::SubscriptionDefinition |
| `VPC` | AWS::EC2::VPC |
| `VPCGatewayAttachment` | AWS::EC2::VPCGatewayAttachment |
