provider "docker" {
  host    = "unix:///var/run/docker.sock"
}

resource "docker_container" "postgres" {
  name  = "postgres-container"
  image = "postgres"
  ports {
    internal = 5432
    external = 5432
  }
  env = [
    "POSTGRES_DB=group-two-storage",
    "POSTGRES_USER=Sage9705",
    "POSTGRES_PASSWORD=GroupTwoPipeline"
  ]
  restart = "unless-stopped"
}
