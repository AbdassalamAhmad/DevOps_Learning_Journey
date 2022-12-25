output "nat_gateway_ip" {
  value = module.network.eip_public_ip
}