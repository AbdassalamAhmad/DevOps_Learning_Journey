resource "aws_instance" "application_instance_1" {
  depends_on = [
    aws_lb.alb, aws_lb_target_group.tagret_group
  ]
  ami                    = "ami-0185600d76ba787f4"
  instance_type          = "t3.micro"
  availability_zone      = "eu-south-1a"
  vpc_security_group_ids = [aws_security_group.InstanceSG.id] ###########
  #key_name               = aws_key_pair.iti_ssh_key.key_name
  subnet_id = module.network.private_app_subnet_1_id
  tags = {
    Name = "terraform"
  }


  user_data = <<-EOF
    #!/bin/bash
    # Use this for your user data (script from top to bottom)
    # install httpd (Linux 2 version)
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
    EOF
}


resource "aws_instance" "application_instance_2" {
  depends_on = [
    aws_lb.alb, aws_lb_target_group.tagret_group
  ]
  ami                    = "ami-0185600d76ba787f4"
  instance_type          = "t3.micro"
  availability_zone      = "${var.region}b"
  vpc_security_group_ids = [aws_security_group.InstanceSG.id] ###########
  #key_name               = aws_key_pair.iti_ssh_key.key_name
  subnet_id = module.network.private_app_subnet_2_id
  tags = {
    Name = "terraform"
  }



  user_data = <<-EOF
    #!/bin/bash
    # Use this for your user data (script from top to bottom)
    # install httpd (Linux 2 version)
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
    EOF
}
