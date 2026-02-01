variable "project_id" {
  description = "ID do projeto GCP"
  type        = string
}

variable "role_id" {
  description = "ID da role customizada"
  type        = string
}

variable "role_title" {
  description = "Título da role customizada"
  type        = string
}

variable "workbench_user_member" {
  description = "Membro IAM (user:email@exemplo.com ou group:grupo@exemplo.com) que receberá a role"
  type        = string
}
