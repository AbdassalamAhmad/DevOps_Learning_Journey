output "nat_gateway_ip" {
  value = module.network.eip_public_ip
  #sensitive = true
}

output "load_balancer_dns" {
  value = aws_lb.alb.dns_name
  #sensitive = true
}

