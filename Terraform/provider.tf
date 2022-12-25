terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0" # Minor version updates are intended to be non-disruptive
    }
  }
}

provider "aws" {
  region  = var.region
  profile = "default"
}
