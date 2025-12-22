from __future__ import annotations

"""InstanceAZFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceAZFunctionCode:
    resource: Code
    zip_file = """import sys
import cfnresponse
import boto3
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

c = boto3.client('ec2')


def handler(event, context):
    responseData = {}
    try:
        logger.info('Received event: {}'.format(json.dumps(event)))
        result = cfnresponse.FAILED
        if event['RequestType'] == 'Create':
            r = c.describe_reserved_instances_offerings(
                Filters=[
                    {
                        'Name': 'scope',
                        'Values': [
                            'Availability Zone',
                        ]
                    },
                ],
                IncludeMarketplace=False,
                InstanceType='t3.micro',
            )
            x = r['ReservedInstancesOfferings']
            while 'NextToken' in r:
                r = c.describe_reserved_instances_offerings(
                    Filters=[
                        {
                            'Name': 'scope',
                            'Values': [
                                'Availability Zone',
                            ]
                        },
                    ],
                    IncludeMarketplace=False,
                    InstanceType='t3.micro',
                    NextToken=r['NextToken']
                )
                x.extend(r['ReservedInstancesOfferings'])
            responseData['AvailabilityZone'] = set(d['AvailabilityZone'] for d in x).pop()
            result = cfnresponse.SUCCESS
        else:
            result = cfnresponse.SUCCESS
    except ClientError as e:
        logger.error('Error: {}'.format(e))
        result = cfnresponse.FAILED
    logger.info('Returning response of: %s, with result of: %s' % (result, responseData))
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)
"""


@cloudformation_dataclass
class InstanceAZFunction:
    """AWS::Lambda::Function resource."""

    resource: Function
    code = InstanceAZFunctionCode
    description = 'Queries account and region for supported AZ'
    handler = 'index.handler'
    role: GetAtt[LambdaExecutionRole] = get_att("Arn")
    runtime = 'python3.12'
    timeout = 60
