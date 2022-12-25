# ---------------- create ssh key using tls_private_key --------------------------

# resource "tls_private_key" "project_key" {
#   algorithm = "RSA"
#   rsa_bits  = 4096
# }

# resource "aws_key_pair" "iti_ssh_key" {
#   key_name   = "iti_lab_key"
#   public_key = tls_private_key.project_key.public_key_openssh

# }

# resource "local_file" "ssh_key" {
#   filename = "/root/.ssh/pk.pem"
#   content = tls_private_key.project_key.private_key_ppk
#   provisioner "local-exec" {
#     interpreter = ["bash", "-c"]
#     command = "chmod 400 /root/.ssh/pk.pem"
#   }
# }