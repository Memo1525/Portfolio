terraform {
  backend "s3" {
    bucket = "brian-terraform-1"
    key    = "terraform.tfstate"
    region = "us-west-2"
  }
}