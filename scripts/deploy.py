"""
Agent Engine Deployment Script
"""

import os
import sys
import logging

import vertexai
from vertexai.preview import reasoning_engines

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    required = ["GCP_PROJECT_ID", "GCP_REGION", "AGENT_DISPLAY_NAME"]
    config = {}
    missing = []

    for key in required:
        value = os.environ.get(key)
        if not value:
            missing.append(key)
        else:
            config[key] = value

    if missing:
        logger.error(f"Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)

    return config


def deploy_agent(config: dict) -> None:
    logger.info(f"Initialising Vertex AI — project: {config['GCP_PROJECT_ID']}, region: {config['GCP_REGION']}")

    vertexai.init(
        project=config["GCP_PROJECT_ID"],
        location=config["GCP_REGION"],
    )

    logger.info("Importing agent...")
    from google.adk.agents import AdkApp
    from agent.agent import root_agent

    agent_app = AdkApp(agent=root_agent)

    logger.info(f"Deploying '{config['AGENT_DISPLAY_NAME']}' to Agent Engine...")

    remote_agent = reasoning_engines.ReasoningEngine.create(
        agent_app,
        display_name=config["AGENT_DISPLAY_NAME"],
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]",
            "google-adk",
        ],
    )

    logger.info("✅ Deployment successful!")
    logger.info(f"   Resource name : {remote_agent.resource_name}")


if __name__ == "__main__":
    config = load_config()
    deploy_agent(config)