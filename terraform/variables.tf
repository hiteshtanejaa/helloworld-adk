variable "gcp_project_id" {
  description = "The GCP project ID to deploy resources into."
  type        = string
}

variable "gcp_region" {
  description = "The GCP region for Vertex AI Agent Engine deployment."
  type        = string
  default     = "us-central1"
}