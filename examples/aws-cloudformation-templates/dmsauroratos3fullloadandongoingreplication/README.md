# Dmsauroratos3fullloadandongoingreplication

Migrated from [DMSAuroraToS3FullLoadAndOngoingReplication.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m dmsauroratos3fullloadandongoingreplication
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `DBSubnet1` | AWS::EC2::Subnet |
| `DBSubnet2` | AWS::EC2::Subnet |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `AttachGateway` | AWS::EC2::VPCGatewayAttachment |
| `RouteTable` | AWS::EC2::RouteTable |
| `Route` | AWS::EC2::Route |
| `SubnetRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `SubnetRouteTableAssociation1` | AWS::EC2::SubnetRouteTableAssociation |
| `AuroraDBSubnetGroup` | AWS::RDS::DBSubnetGroup |
| `AuroraSecurityGroup` | AWS::EC2::SecurityGroup |
| `AuroraCluster` | AWS::RDS::DBCluster |
| `AuroraDB` | AWS::RDS::DBInstance |
| `S3Bucket` | AWS::S3::Bucket |
| `DMSCloudwatchRole` | AWS::IAM::Role |
| `DMSVpcRole` | AWS::IAM::Role |
| `S3TargetDMSRole` | AWS::IAM::Role |
| `DMSReplicationSubnetGroup` | AWS::DMS::ReplicationSubnetGroup |
| `DMSSecurityGroup` | AWS::EC2::SecurityGroup |
| `DMSReplicationInstance` | AWS::DMS::ReplicationInstance |
| `AuroraSourceEndpoint` | AWS::DMS::Endpoint |
| `S3TargetEndpoint` | AWS::DMS::Endpoint |
| `DMSReplicationTask` | AWS::DMS::ReplicationTask |
