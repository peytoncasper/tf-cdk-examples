#!/usr/bin/env python
import subprocess, sys
from constructs import Construct
from cdktf import App, TerraformStack


def cdk_deploy():
    res = subprocess.Popen(["cdktf", "apply", "--auto-approve"], stdout=subprocess.PIPE)


def commit(name):
    print("Committed Module: %s".format(name))


class InstanceStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)


if __name__ == "__main__":
    app = App()
    InstanceStack(app, "post-provision-steps")
    app.synth()
    cdk_deploy()

