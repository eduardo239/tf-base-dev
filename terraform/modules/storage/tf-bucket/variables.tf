variable "force_destroy" {
  description = "Permite destruir o bucket mesmo com objetos (use false para buckets de state)"
  type        = bool
  default     = false
}
