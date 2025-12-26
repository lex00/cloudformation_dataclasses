# PrivateVpc

Migrated from [private-vpc.json](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m private_vpc
```

### Validate Template

```bash
python -m private_vpc --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `PublicSubnetOne` | AWS::EC2::Subnet |
| `PublicSubnetTwo` | AWS::EC2::Subnet |
| `PrivateSubnetOne` | AWS::EC2::Subnet |
| `PrivateSubnetTwo` | AWS::EC2::Subnet |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `GatewayAttachement` | AWS::EC2::VPCGatewayAttachment |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `PublicRoute` | AWS::EC2::Route |
| `PublicSubnetOneRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnetTwoRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `NatGatewayOneAttachment` | AWS::EC2::EIP |
| `NatGatewayTwoAttachment` | AWS::EC2::EIP |
| `NatGatewayOne` | AWS::EC2::NatGateway |
| `NatGatewayTwo` | AWS::EC2::NatGateway |
| `PrivateRouteTableOne` | AWS::EC2::RouteTable |
| `PrivateRouteOne` | AWS::EC2::Route |
| `PrivateRouteTableOneAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTableTwo` | AWS::EC2::RouteTable |
| `PrivateRouteTwo` | AWS::EC2::Route |
| `PrivateRouteTableTwoAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `DynamoDBEndpoint` | AWS::EC2::VPCEndpoint |
| `ECSCluster` | AWS::ECS::Cluster |
| `FargateContainerSecurityGroup` | AWS::EC2::SecurityGroup |
| `EcsSecurityGroupIngressFromPublicALB` | AWS::EC2::SecurityGroupIngress |
| `EcsSecurityGroupIngressFromPrivateALB` | AWS::EC2::SecurityGroupIngress |
| `EcsSecurityGroupIngressFromSelf` | AWS::EC2::SecurityGroupIngress |
| `PublicLoadBalancerSG` | AWS::EC2::SecurityGroup |
| `PublicLoadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `DummyTargetGroupPublic` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `PublicLoadBalancerListener` | AWS::ElasticLoadBalancingV2::Listener |
| `PrivateLoadBalancerSG` | AWS::EC2::SecurityGroup |
| `PrivateLoadBalancerIngressFromECS` | AWS::EC2::SecurityGroupIngress |
| `PrivateLoadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `DummyTargetGroupPrivate` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `PrivateLoadBalancerListener` | AWS::ElasticLoadBalancingV2::Listener |
| `ECSRole` | AWS::IAM::Role |
| `ECSTaskExecutionRole` | AWS::IAM::Role |
