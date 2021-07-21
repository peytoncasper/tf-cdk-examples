#!/usr/bin/env python
import subprocess, sys, requests, os, time
from constructs import Construct
from cdktf import App, TerraformStack, TerraformHclModule, Manifest
from imports.aws import AwsProvider


def cdk_apply(app, stack, stage):
    cwd = os.getcwd() + "/cdktf.out/stacks/{0}".format(stack)

    app.synth()
    print("Terraform Synthesized")

    init = subprocess.Popen(["terraform", "init", "-input=false"], cwd=cwd, stdout=subprocess.PIPE, env=os.environ.copy())
    init.wait()
    print("Initialized")

    apply = subprocess.Popen(["terraform", "apply", "--auto-approve", "-input=false"], cwd=cwd, stdout=subprocess.PIPE, env=os.environ.copy())
    apply.wait()
    print("Applied")

    commit(stage)


def get_release():
    r = requests.get(
        "https://raw.githubusercontent.com/peytoncasper/tf-cdk-examples/master/dynamic-module-composition/release.json")
    return r.json()


def commit(stage):
    print("{0} Committed".format(stage))


class AppStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, 'Aws', region='us-east-1')

    def add_network(self, version: str):
        network = TerraformHclModule(self,
                                     id="base-network",
                                     source="app.terraform.io/peyton-dev/module-network/aws",
                                     version=version
                                     )

        self.subnet_id = network.get_string("subnet_id")
        self.vpc_id = network.get_string("vpc_id")

    def add_firewall(self, version: str):
        firewall = TerraformHclModule(self,
                                      id="firewall",
                                      source="app.terraform.io/peyton-dev/module-firewall/aws",
                                      version=version,
                                      variables={
                                          "vpc_id": self.vpc_id
                                      },
                                      )

        self.security_group_id = firewall.get_string("security_group_id")


if __name__ == "__main__":
    release = get_release()
    app = App()

    stack = AppStack(app, "post-provision-steps")

    stack.add_network(release["network"])
    cdk_apply(app, "post-provision-steps", "Stage 1")

    stack.add_firewall(release["firewall"])
    cdk_apply(app, "post-provision-steps", "Stage 2")
