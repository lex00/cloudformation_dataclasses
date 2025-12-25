#!/bin/bash
# Deploy the Fargate webapp multi-stack example
set -euo pipefail

DOMAIN_NAME="${1:?Usage: deploy.sh <domain-name> <s3-bucket>}"
S3_BUCKET="${2:?Usage: deploy.sh <domain-name> <s3-bucket>}"
STACK_PREFIX="fargate-webapp"

# Helper: deploy stack and wait for completion
deploy_stack() {
    local name=$1
    local template=$2
    shift 2

    echo "Uploading $name.json to S3..."
    aws s3 cp "$template" "s3://$S3_BUCKET/$name.json"

    echo "Deploying $STACK_PREFIX-$name..."
    aws cloudformation deploy \
        --stack-name "$STACK_PREFIX-$name" \
        --template-url "https://$S3_BUCKET.s3.amazonaws.com/$name.json" \
        --capabilities CAPABILITY_IAM \
        --no-fail-on-empty-changeset \
        "$@"
}

# Helper: get stack output
get_output() {
    aws cloudformation describe-stacks \
        --stack-name "$STACK_PREFIX-$1" \
        --query "Stacks[0].Outputs[?OutputKey=='$2'].OutputValue" \
        --output text
}

# Change to script directory
cd "$(dirname "$0")"

# 1. VPC
echo "=== Deploying VPC stack ==="
(cd vpc && python -m vpc > ../vpc.json)
deploy_stack vpc vpc.json

VPC_ID=$(get_output vpc VpcId)
PUBLIC_SUBNETS=$(get_output vpc PublicSubnetIds)
PRIVATE_SUBNETS=$(get_output vpc PrivateSubnetIds)

echo "VPC ID: $VPC_ID"
echo "Public Subnets: $PUBLIC_SUBNETS"
echo "Private Subnets: $PRIVATE_SUBNETS"

# 2. DNS
echo ""
echo "=== Deploying DNS stack ==="
(cd dns && python -m dns > ../dns.json)
deploy_stack dns dns.json \
    --parameter-overrides "DomainName=$DOMAIN_NAME"

HOSTED_ZONE_ID=$(get_output dns HostedZoneId)
CERTIFICATE_ARN=$(get_output dns CertificateArn)
NAME_SERVERS=$(get_output dns NameServers)

echo "Hosted Zone ID: $HOSTED_ZONE_ID"
echo "Certificate ARN: $CERTIFICATE_ARN"
echo ""
echo "============================================"
echo "IMPORTANT: Update your domain registrar with these nameservers:"
echo "$NAME_SERVERS"
echo ""
echo "Press Enter when DNS is delegated and the ACM certificate is validated..."
echo "(You can check certificate status in the AWS Console)"
echo "============================================"
read -r

# 3. ALB
echo ""
echo "=== Deploying ALB stack ==="
(cd alb && python -m alb > ../alb.json)
deploy_stack alb alb.json \
    --parameter-overrides \
        "VpcId=$VPC_ID" \
        "PublicSubnetIds=$PUBLIC_SUBNETS" \
        "CertificateArn=$CERTIFICATE_ARN" \
        "HostedZoneId=$HOSTED_ZONE_ID" \
        "DomainName=$DOMAIN_NAME"

ALB_SG=$(get_output alb AlbSecurityGroupId)
TARGET_GROUP_ARN=$(get_output alb TargetGroupArn)

echo "ALB Security Group: $ALB_SG"
echo "Target Group ARN: $TARGET_GROUP_ARN"

# 4. RDS
echo ""
echo "=== Deploying RDS stack ==="
(cd rds && python -m rds > ../rds.json)
deploy_stack rds rds.json \
    --parameter-overrides \
        "VpcId=$VPC_ID" \
        "PrivateSubnetIds=$PRIVATE_SUBNETS" \
        "VpcCidr=10.0.0.0/16"

DB_ENDPOINT=$(get_output rds DbEndpoint)
DB_SECRET_ARN=$(get_output rds DbSecretArn)

echo "Database Endpoint: $DB_ENDPOINT"
echo "Database Secret ARN: $DB_SECRET_ARN"

# 5. Fargate
echo ""
echo "=== Deploying Fargate stack ==="
(cd fargate && python -m fargate > ../fargate.json)
deploy_stack fargate fargate.json \
    --parameter-overrides \
        "VpcId=$VPC_ID" \
        "PrivateSubnetIds=$PRIVATE_SUBNETS" \
        "AlbSecurityGroupId=$ALB_SG" \
        "TargetGroupArn=$TARGET_GROUP_ARN" \
        "DbEndpoint=$DB_ENDPOINT" \
        "DbSecretArn=$DB_SECRET_ARN"

# Clean up temporary files
rm -f vpc.json dns.json alb.json rds.json fargate.json

echo ""
echo "============================================"
echo "Deployment complete!"
echo "Service URL: https://$DOMAIN_NAME"
echo "============================================"
