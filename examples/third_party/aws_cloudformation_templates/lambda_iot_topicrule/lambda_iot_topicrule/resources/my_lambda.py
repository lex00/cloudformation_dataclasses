from __future__ import annotations

"""MyLambda - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaCode:
    resource: Code
    zip_file = """exports.handler = async (event) => { console.log(event); return {'statusCode': 200, 'body': "OK"}; }
"""


@cloudformation_dataclass
class MyLambda:
    """AWS::Lambda::Function resource."""

    resource: Function
    runtime = 'nodejs20.x'
    handler = 'index.handler'
    code = MyLambdaCode
    function_name = Sub('${AWS::StackName}')
    role: GetAtt[MyLambdaRole] = get_att("Arn")
