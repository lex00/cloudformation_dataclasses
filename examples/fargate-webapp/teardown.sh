#!/bin/bash
# Teardown the Fargate webapp multi-stack example
set -euo pipefail

STACK_PREFIX="fargate-webapp"

delete_stack() {
    local name=$1
    echo "Deleting $STACK_PREFIX-$name..."

    if aws cloudformation describe-stacks --stack-name "$STACK_PREFIX-$name" &>/dev/null; then
        aws cloudformation delete-stack --stack-name "$STACK_PREFIX-$name"
        echo "Waiting for $STACK_PREFIX-$name to be deleted..."
        aws cloudformation wait stack-delete-complete --stack-name "$STACK_PREFIX-$name"
        echo "$STACK_PREFIX-$name deleted."
    else
        echo "$STACK_PREFIX-$name does not exist, skipping."
    fi
}

echo "Starting teardown of $STACK_PREFIX stacks..."
echo ""

# Delete in reverse order of creation
delete_stack fargate
delete_stack rds
delete_stack alb
delete_stack dns
delete_stack vpc

echo ""
echo "============================================"
echo "Teardown complete!"
echo "============================================"
