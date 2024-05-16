
#elasticsearch_settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class ElasticsearchSettings:
    def __init__(self):
        try:
            # Elasticsearch
            self.es_host = os.environ['ES_HOST']
            self.api_key = os.environ['ES_API_KEY']
        except KeyError as e:
            raise KeyError(f"Missing environment variable: {e}")

        if not self.es_host:
            raise ValueError("ES_HOST is not specified in the environment variables.")
#.env 
ES_HOST=http://localhost:9200
ES_API_KEY=your_api_key_here


# main
from config.elasticsearch_settings import ElasticsearchSettings

def main():
    try:
        settings = ElasticsearchSettings()
        es_host = settings.es_host
        api_key = settings.api_key

        # Use es_host and api_key to connect to Elasticsearch
        print("Elasticsearch host:", es_host)
        print("API key:", api_key)

    except (KeyError, ValueError) as e:
        print(f"Error while loading Elasticsearch settings: {e}")

if __name__ == "__main__":
    main()

#config/settings.py:
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        # API URLs
        self.app_url = os.getenv('APP_URL')
        self.env_url = os.getenv('ENV_URL')

        # Elasticsearch
        self.es_host = os.getenv('ES_HOST')
#from config.settings import Settings
from api.client import APIClient
from data.manager import DataManager
from elasticsearch.indexer import ElasticsearchIndexer
from utils.helpers import setup_logger

def main():
    setup_logger()

    settings = Settings()

    api_client = APIClient(settings.app_url, settings.env_url)
    data_manager = DataManager(api_client)
    applications = data_manager.fetch_data()

    es_indexer = ElasticsearchIndexer(settings.es_host)
    es_indexer.index_applications(applications)

if __name__ == "__main__":
    main()


#Readme :
# Project Name

## Description

Briefly describe your project here, including its purpose and main features.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt

#requirements.txt
# Used for making HTTP requests
requests==2.26.0

# The official Elasticsearch client for Python
elasticsearch==7.15.1

##api/client.py:

import requests

class APIClient:
    def __init__(self, app_url: str, env_url: str):
        self.app_url = app_url
        self.env_url = env_url

    def get_applications(self) -> List[Dict[str, Any]]:
        response = requests.get(self.app_url)
        response.raise_for_status()
        return response.json()

    def get_environments(self, application_ids: List[str]) -> List[Dict[str, Any]]:
        response = requests.post(self.env_url, json=application_ids)
        response.raise_for_status()
        return response.json()


##data/models.py:
from typing import List, Dict, Any

class Application:
    def __init__(self, application_id: str, name: str, version: str):
        self.application_id = application_id
        self.name = name
        self.version = version
        self.environments = []

    def add_environment(self, environment):
        self.environments.append(environment)

class Environment:
    def __init__(self, env_id: str, application_id: str, status: str, region: str):
        self.env_id = env_id
        self.application_id = application_id
        self.status = status
        self.region = region
##data/manager.py:
from typing import List, Dict, Any
from .models import Application, Environment
from ..api.client import APIClient

class DataManager:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def fetch_data(self) -> List[Application]:
        applications_data = self.api_client.get_applications()
        application_ids = [app['application_id'] for app in applications_data]
        environments_data = self.api_client.get_environments(application_ids)

        applications = {}
        for app_data in applications_data:
            app = Application(app_data['application_id'], app_data['name'], app_data['version'])
            applications[app.application_id] = app

        for env_data in environments_data:
            env = Environment(env_data['env_id'], env_data['application_id'], env_data['status'], env_data['region'])
            if env.application_id in applications:
                applications[env.application_id].add_environment(env)

        return list(applications.values())
###elasticsearch/indexer.py:
from typing import List, Dict, Any
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from ..data.models import Application

class ElasticsearchIndexer:
    def __init__(self, es_host: str):
        self.es = Elasticsearch([es_host])

    def index_applications(self, applications: List[Application]):
        actions = []
        for app in applications:
            action = {
                "_index": "applications",
                "_id": app.application_id,
                "_source": {
                    "application_id": app.application_id,
                    "name": app.name,
                    "version": app.version,
                    "environments": [
                        {
                            "env_id": env.env_id,
                            "status": env.status,
                            "region": env.region
                        }
                        for env in app.environments
                    ]
                }
            }
            actions.append(action)
        
        bulk(self.es, actions)
###utils/helpers.py: (assuming an example function for logging)
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
##main.py:
from .api.client import APIClient
from .data.manager import DataManager
from .elasticsearch.indexer import ElasticsearchIndexer
from .utils.helpers import setup_logger

def main():
    setup_logger()

    api_client = APIClient('https://api.example.com/applications', 'https://api.example.com/environments')
    data_manager = DataManager(api_client)
    applications = data_manager.fetch_data()

    es_indexer = ElasticsearchIndexer('http://localhost:9200')
    es_indexer.index_applications(applications)

if __name__ == "__main__":
    main()
