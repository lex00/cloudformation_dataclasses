"""CentralEventLogPolicy - AWS::Logs::ResourcePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventLogPolicy:
    """AWS::Logs::ResourcePolicy resource."""

    resource: ResourcePolicy
    policy_name = 'CentralEventLogResourcePolicy'
    policy_document = Sub("""{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "delivery.logs.amazonaws.com",
          "events.amazonaws.com"
        ]
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:CreateLogStream"
      ],
      "Resource": "${CentralEventLog.Arn}"
    }
  ]
}
""")
