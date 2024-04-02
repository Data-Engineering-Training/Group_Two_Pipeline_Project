variable "postgres_container_name" {
  description = "Name of the PostgreSQL container"
  default     = "postgres-container"
}

variable "postgres_db" {
  description = "Name of the PostgreSQL database"
  default     = "group-two-storage"
}

variable "postgres_user" {
  description = "Username for the PostgreSQL database"
  default     = "Sage9705"
}

variable "postgres_password" {
  description = "Password for the PostgreSQL database"
  default     = "GroupTwoPipeline"
}
