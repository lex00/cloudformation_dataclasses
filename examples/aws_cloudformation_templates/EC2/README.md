# EC2 CloudFormation Examples

Migrated from [aws-cloudformation-templates/EC2](https://github.com/awslabs/aws-cloudformation-templates/tree/main/EC2).

## Examples

### ec2_instance_with_security_group.py

EC2 instance with SSH security group.

**Original:** `EC2InstanceWithSecurityGroupSample.json`

**Features demonstrated:**
- Parameters with `AllowedValues` for instance types
- SSM Parameter reference for latest AMI (`AWS::SSM::Parameter::Value`)
- `SecurityGroup` with `Ingress` rules
- `Select` intrinsic for subnet selection from parameter list
- `GetAtt` for outputs (PublicIp, AvailabilityZone, PublicDnsName)

---

### eip_with_association.py

Elastic IP associated with EC2 instance.

**Original:** `EIP_With_Association.json`

**Features demonstrated:**
- `EIP` (Elastic IP) resource creation
- `EIPAssociation` linking EIP to instance
- `GetAtt` for AllocationId
- `Base64` + `Join` for UserData

---

### instance_with_cfn_init.py

EC2 instance with cfn-init for bootstrapping.

**Original:** `InstanceWithCfnInit.json`

**Features demonstrated:**
- `AWS::CloudFormation::Init` metadata for instance configuration
- Package installation, file creation, and service management
- `Sub` intrinsic with pseudo-parameters (`${AWS::StackName}`, `${AWS::Region}`)
- `cfn-signal` for completion signaling

---

### ec2_with_wait_condition.py

EC2 instance with WaitCondition for setup signaling.

**Original:** `ec2_with_waitcondition_template.json`

**Features demonstrated:**
- `WaitConditionHandle` resource
- `WaitCondition` with timeout
- UserData script that signals via `cfn-signal`
- Multiple security group ingress rules (HTTP, HTTPS, ICMP, SSH)
- `Tag` with parameter reference for instance name
- Pseudo-parameters (`AWS_STACK_ID`, `AWS_REGION`)

---

## Run Tests

```bash
uv run pytest examples/aws_cloudformation_templates/EC2/tests/ -v
```

## Generate Templates

```bash
# EC2 with Security Group
uv run python -m examples.aws_cloudformation_templates.EC2.ec2_instance_with_security_group

# EIP with Association
uv run python -m examples.aws_cloudformation_templates.EC2.eip_with_association

# Instance with cfn-init
uv run python -m examples.aws_cloudformation_templates.EC2.instance_with_cfn_init

# EC2 with WaitCondition
uv run python -m examples.aws_cloudformation_templates.EC2.ec2_with_wait_condition
```
