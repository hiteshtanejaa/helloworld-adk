terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

resource "google_project_service" "aiplatform" {
  project = var.gcp_project_id
  service = "aiplatform.googleapis.com"
  disable_on_destroy = false
}

resource "google_service_account" "adk_deployer" {
  project      = var.gcp_project_id
  account_id   = "adk-agent-deployer"
  display_name = "ADK Agent Deployer"
  description  = "Service account for CI/CD pipeline to deploy ADK agents."
  depends_on   = [google_project_service.aiplatform]
}

resource "google_project_iam_member" "adk_deployer_aiplatform_user" {
  project = var.gcp_project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:${google_service_account.adk_deployer.email}"
}