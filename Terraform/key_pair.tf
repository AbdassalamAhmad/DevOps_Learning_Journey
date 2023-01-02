#----------------Create ssh key using ssh-keygen command---------------------------


resource "aws_key_pair" "ssh_key_variable" {
  key_name   = var.key_name
  public_key = var.public_key
}



# resource "tls_private_key" "ec2_key" {
#   algorithm = "RSA"
#   rsa_bits  = 4096
# }

# resource "aws_key_pair" "ssh_key" {
#   key_name   = "ssh_ec2_key"
#   public_key = tls_private_key.ec2_key.public_key_openssh

# }

# resource "local_file" "ssh_key" {
#   filename = "E:/keys/pk.pem"
#   content  = tls_private_key.ec2_key.private_key_pem
#   provisioner "local-exec" {
#     interpreter = ["bash", "-c"]
#     command     = "chmod 400 E:/keys/pk.pem"
#   }
# }