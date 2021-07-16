provider "aws" {
  region="us-east-1"
}

module "network" {
  source="app.terraform.io/peyton-dev/module-network/aws"
  version="1.0.0"
}

module "firewall" {
  source="app.terraform.io/peyton-dev/module-firewall/aws"
  version="1.0.1"
  vpc_id = module.network.vpc_id
}

module "compute" {
  source="app.terraform.io/peyton-dev/module-compute/aws"
  version="1.0.3"
  security_group_ids = [module.firewall.security_group_id]
  subnet_id = module.network.subnet_id
}