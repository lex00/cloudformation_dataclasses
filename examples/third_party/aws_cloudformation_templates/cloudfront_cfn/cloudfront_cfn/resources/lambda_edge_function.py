"""LambdaEdgeFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaEdgeFunctionCode:
    resource: lambda_.Code
    zip_file = """'use strict';

 exports.handler = (event, context, callback) => {
    console.log('Adding additional headers to CloudFront response.');

    const response = event.Records[0].cf.response;
    response.headers['strict-transport-security'] = [{
    key: 'Strict-Transport-Security',
    value: 'max-age=86400; includeSubdomains; preload',
    }];
    response.headers['x-content-type-options'] = [{
    key: 'X-Content-Type-Options',
    value: 'nosniff',
    }];
    response.headers['x-frame-options'] = [{
        key:   'X-Frame-Options',
        value: "DENY"
    }];
    response.headers['content-security-policy'] = [{
        key:   'Content-Security-Policy',
        value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"
    }];
    response.headers['x-xss-protection'] = [{
        key:   'X-XSS-Protection',
        value: "1; mode=block"
    }];
    response.headers['referrer-policy'] = [{
        key:   'Referrer-Policy',
        value: "same-origin"
    }];
    callback(null, response);
  };
"""


@cloudformation_dataclass
class LambdaEdgeFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'A custom Lambda@Edge function for serving custom headers from CloudFront Distribution'
    function_name = Sub('${AppName}-lambda-edge-${Environment}')
    handler = 'index.handler'
    role = get_att(LambdaEdgeIAMRole, "Arn")
    memory_size = 128
    timeout = 5
    code = LambdaEdgeFunctionCode
    runtime = 'nodejs20.x'
