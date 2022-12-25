#-------------------------- Security Group For Instance --------------------------#

resource "aws_security_group" "InstanceSG" {
  name = "allow_http_instance"

  vpc_id = module.network.my_vpc_id

  ingress {
    description = "allow http from ALL"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

}


#-------------------------- Security Group For ALB --------------------------#

resource "aws_security_group" "ALBSG" {
  name = "allow_http_ALB"

  vpc_id = module.network.my_vpc_id

  ingress {
    description = "allow http from ALL"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }


}


#-------------------------- Security Group For RDS --------------------------#

resource "aws_security_group" "RDSSG" {
  name = "allow_MYSQL_VPC"

  vpc_id = module.network.my_vpc_id

  ingress {
    description = "allow MYSQL from VPC only"
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

}

#-------------------------- Security Group For ElastiCache --------------------------#


resource "aws_security_group" "ElastiCacheSG" {
  name = "allow_ElastiCache_VPC"

  vpc_id = module.network.my_vpc_id

  ingress {
    description = "allow ElastiCache from VPC only"
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

}