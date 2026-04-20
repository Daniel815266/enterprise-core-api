# This demonstrates your ability to automate cloud resources
provider "digitalocean" {
  # Token would be provided via environment variables
}

resource "digitalocean_droplet" "api_server" {
  image  = "ubuntu-22-04-x64"
  name   = "api-production-01"
  region = "fra1"
  size   = "s-1vcpu-2gb"
  ssh_keys = [var.ssh_fingerprint]
}
