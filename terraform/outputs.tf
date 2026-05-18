output "service_account_email" {
  description = "Email of the ADK deployer service account."
  value       = google_service_account.adk_deployer.email
}

output "service_account_name" {
  description = "Full resource name of the service account."
  value       = google_service_account.adk_deployer.name
}

output "aiplatform_api_enabled" {
  description = "Confirms the Vertex AI API is enabled."
  value       = google_project_service.aiplatform.id
}