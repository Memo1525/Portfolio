
resource "aws_vpc" "dinosaurinc_VPC" {
  cidr_block = "192.168.0.0/16"

  instance_tenancy = "default"

  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "dinosaurinc_VPC",
    Hello = "World"
  }
}

output "vpc_id" {
  value       = aws_vpc.dinosaurinc_VPC.id
  description = "VPC ID"
}
