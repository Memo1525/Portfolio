
resource "aws_instance" "bastion_1" {
  ami                         = "ami-0ee8244746ec5d6d4"
  instance_type               = "t3.small"
  subnet_id                   = aws_subnet.public_1.id
  key_name                    = var.bastion_key
  vpc_security_group_ids      = [aws_security_group.Bastion_security_group_1.id]
  associate_public_ip_address = true
  availability_zone = "us-west-2a"


  user_data = <<-EOF
    #!/bin/bash
    echo "Port 2422" >> /etc/ssh/sshd_config
    systemctl restart sshd
    EOF

  tags = {
    Name = "Dinosaurs1"
  }
}

resource "aws_instance" "bastion_2" {
  ami                         = "ami-0ee8244746ec5d6d4"
  instance_type               = "t3.small"
  subnet_id                   = aws_subnet.public_2.id
  key_name                    = var.bastion_key
  vpc_security_group_ids      = [aws_security_group.Bastion_security_group_2.id]
  associate_public_ip_address = true
  availability_zone = "us-west-2b"

  user_data = <<-EOF
    #!/bin/bash
    echo "Port 2422" >> /etc/ssh/sshd_config
    systemctl restart sshd
    EOF

  tags = {
    Name = "Dinosaurs_2"
  }
}
