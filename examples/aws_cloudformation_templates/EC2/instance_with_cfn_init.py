"""
Instance with cfn-init.

Inspired by AWS's EC2/InstanceWithCfnInit.json template.
Demonstrates:
- EC2 instance metadata (AWS::CloudFormation::Init)
- cfn-init for package installation, file creation, and service management
- Sub intrinsic for UserData with pseudo-parameters
- cfn-signal for signaling completion
"""

from . import *  # noqa: F403


# =============================================================================
# Metadata Configuration
# =============================================================================


def cfn_init_metadata():
    """
    AWS::CloudFormation::Init metadata configuration.

    Installs httpd, creates index.html, configures cfn-hup for updates,
    and ensures services are running.
    """
    return {
        "AWS::CloudFormation::Init": {
            "config": {
                "packages": {"yum": {"httpd": []}},
                "files": {
                    "/var/www/html/index.html": {
                        "content": (
                            "<body>\n"
                            "  <h1>Congratulations, you have successfully launched "
                            "the AWS CloudFormation sample.</h1>\n"
                            "</body>\n"
                        ),
                        "mode": "000644",
                        "owner": "root",
                        "group": "root",
                    },
                    "/etc/cfn/cfn-hup.conf": {
                        "content": {
                            "Fn::Sub": "[main]\nstack=${AWS::StackId}\nregion=${AWS::Region}\n"
                        },
                        "mode": "000400",
                        "owner": "root",
                        "group": "root",
                    },
                    "/etc/cfn/hooks.d/cfn-auto-reloader.conf": {
                        "content": {
                            "Fn::Sub": (
                                "[cfn-auto-reloader-hook]\n"
                                "triggers=post.update\n"
                                "path=Resources.WebInstance.Metadata.AWS::CloudFormation::Init\n"
                                "action=/opt/aws/bin/cfn-init -v "
                                "--stack ${AWS::StackName} --resource WebInstance --region ${AWS::Region}\n"
                                "runas=root"
                            )
                        }
                    },
                },
                "services": {
                    "sysvinit": {
                        "httpd": {"enabled": True, "ensureRunning": True},
                        "cfn-hup": {
                            "enabled": True,
                            "ensureRunning": True,
                            "files": [
                                "/etc/cfn/cfn-hup.conf",
                                "/etc/cfn/hooks.d/cfn-auto-reloader.conf",
                            ],
                        },
                    }
                },
            }
        }
    }


# =============================================================================
# UserData
# =============================================================================


def user_data_script():
    """
    UserData script that runs cfn-init and signals completion.

    Uses Sub to inject stack name and region pseudo-parameters.
    """
    return Base64(
        Sub(
            "#!/bin/bash\n"
            "/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} "
            "--resource WebInstance --region ${AWS::Region}\n"
            "/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} "
            "--resource WebInstance --region ${AWS::Region}"
        )
    )


# =============================================================================
# EC2 Instance
# =============================================================================


@cloudformation_dataclass
class WebInstance:
    """
    EC2 instance with cfn-init configuration.

    Uses AWS::CloudFormation::Init metadata to:
    - Install httpd package
    - Create index.html file
    - Configure cfn-hup for automatic updates
    - Start and enable httpd and cfn-hup services
    """

    resource: Instance
    image_id = "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64}}"
    instance_type = "t4g.nano"
    key_name = "sample"
    user_data = user_data_script()
    metadata = cfn_init_metadata()


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class InstanceWithCfnInitTemplate:
    """
    Instance with cfn-init template.

    Creates an EC2 instance that uses cfn-init to install and configure
    a web server. Demonstrates CloudFormation helper scripts for
    instance bootstrapping.
    """

    resource: Template
    description = (
        "AWS CloudFormation sample template. "
        "Create an Amazon EC2 instance with cfn-init and cfn-signal."
    )
    resources = [WebInstance]


def build_template() -> Template:
    """Build the instance with cfn-init template."""
    return InstanceWithCfnInitTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
