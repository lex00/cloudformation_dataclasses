"""AWS CloudFormation pseudo-parameters as pre-defined Ref constants.

Pseudo-parameters are predefined by AWS CloudFormation and resolve to values
based on the stack's context at deployment time.

See: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html

Example usage:
    from cloudformation_dataclasses.intrinsics import AWS_REGION, AWS_ACCOUNT_ID

    @cloudformation_dataclass
    class MyBucket:
        resource: Bucket
        region = AWS_REGION

    # Or compose with other intrinsics:
    endpoint_url = Join("", ["https://s3.", AWS_REGION, ".", AWS_URL_SUFFIX])
"""

from cloudformation_dataclasses.intrinsics.functions import Ref

# AWS account ID of the stack (e.g., "123456789012")
AWS_ACCOUNT_ID = Ref("AWS::AccountId")

# List of notification ARNs for the current stack
AWS_NOTIFICATION_ARNS = Ref("AWS::NotificationARNs")

# Special value that removes the property when used with Fn::If
AWS_NO_VALUE = Ref("AWS::NoValue")

# Partition the resource is in (aws, aws-cn, aws-us-gov)
AWS_PARTITION = Ref("AWS::Partition")

# AWS Region where the stack is created (e.g., "us-east-1")
AWS_REGION = Ref("AWS::Region")

# ID of the stack (e.g., "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/...")
AWS_STACK_ID = Ref("AWS::StackId")

# Name of the stack
AWS_STACK_NAME = Ref("AWS::StackName")

# Domain suffix for the partition (e.g., "amazonaws.com" or "amazonaws.com.cn")
AWS_URL_SUFFIX = Ref("AWS::URLSuffix")
