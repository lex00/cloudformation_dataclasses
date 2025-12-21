# VscodeserverPkg

Migrated from [VSCodeServer-pkg.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m vscodeserver_pkg
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `InstanceRole` | AWS::IAM::Role |
| `InstanceRolePolicy` | AWS::IAM::RolePolicy |
| `InstanceProfile` | AWS::IAM::InstanceProfile |
| `Server` | AWS::EC2::Instance |
| `NetworkVPC` | AWS::EC2::VPC |
| `NetworkPublicSubnet1` | AWS::EC2::Subnet |
| `NetworkPublicSubnet1RouteTable` | AWS::EC2::RouteTable |
| `NetworkPublicSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NetworkPublicSubnet1DefaultRoute` | AWS::EC2::Route |
| `NetworkPublicSubnet1EIP` | AWS::EC2::EIP |
| `NetworkPublicSubnet1NATGateway` | AWS::EC2::NatGateway |
| `NetworkPublicSubnet2` | AWS::EC2::Subnet |
| `NetworkPublicSubnet2RouteTable` | AWS::EC2::RouteTable |
| `NetworkPublicSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NetworkPublicSubnet2DefaultRoute` | AWS::EC2::Route |
| `NetworkPublicSubnet2EIP` | AWS::EC2::EIP |
| `NetworkPublicSubnet2NATGateway` | AWS::EC2::NatGateway |
| `NetworkPrivateSubnet1Subnet` | AWS::EC2::Subnet |
| `NetworkPrivateSubnet1RouteTable` | AWS::EC2::RouteTable |
| `NetworkPrivateSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NetworkPrivateSubnet1DefaultRoute` | AWS::EC2::Route |
| `NetworkPrivateSubnet2Subnet` | AWS::EC2::Subnet |
| `NetworkPrivateSubnet2RouteTable` | AWS::EC2::RouteTable |
| `NetworkPrivateSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NetworkPrivateSubnet2DefaultRoute` | AWS::EC2::Route |
| `NetworkInternetGateway` | AWS::EC2::InternetGateway |
| `NetworkVPCGW` | AWS::EC2::VPCGatewayAttachment |
| `CloudFrontCachePolicy` | AWS::CloudFront::CachePolicy |
| `CloudFrontDistribution` | AWS::CloudFront::Distribution |
