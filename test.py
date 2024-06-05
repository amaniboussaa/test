# Extract all component IDs
all_components = {component["component_id"]: component for component in components_data}

# Extract used component IDs from topologies
used_component_ids = set()
for topology in topologies_data:
    for node in topology["topology"]["nodeTypes"]:
        used_component_ids.add(node["component_element_id"])
    for relation in topology["topology"]["relationTypes"]:
        used_component_ids.add(relation["component_element_id"])

# Determine unused components
unused_component_ids = set(all_components.keys()) - used_component_ids

# Prepare unused components data
unused_components = [all_components[comp_id] for comp_id in unused_component_ids]

# Save unused components to a JSON file
with open('unused_components.json', 'w') as f:
    json.dump(unused_components, f, indent=4)

print(f"Unused components: {unused_components}")




# Save unused components to a JSON file
with open('unused_components.json', 'w') as f:
    json.dump(unused_components, f, indent=4)




def used = false;

for (item in params['_source']['nodetype']) {
  if (item['component_id'] == doc['component_id'].value) {
    used = true;
  }
}

for (item in params['_source']['relationtype']) {
  if (item['component_id'] == doc['component_id'].value) {
    used = true;
  }
}

return used;


{
  "query": {
    "bool": {
      "should": [
        { "exists": { "field": "nodetype.component_id" } },
        { "exists": { "field": "relationtype.component_id" } }
      ]
    }
  }
}


import json
import os
import logging

def setup_logger(name, level=logging.DEBUG):
    """
    Set up a logger with the specified name and level.

    Parameters:
    - name (str): The name of the logger.
    - level (int): The logging level.

    Returns:
    - Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

def load_config(config_path='config.json'):
    """
    Load the configuration from a JSON file.

    Parameters:
    - config_path (str): The path to the config file. Default is 'config.json'.

    Returns:
    - dict: A dictionary containing the configuration.
    """
    logger = setup_logger(__name__)

    if not os.path.exists(config_path):
        logger.error(f"The file {config_path} was not found.")
        raise FileNotFoundError(f"Error: The file {config_path} was not found.")

    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            logger.info(f"Configuration loaded successfully from {config_path}")
    except json.JSONDecodeError as e:
        logger.error(f"The file {config_path} is not a valid JSON: {e}")
        raise ValueError(f"Error: The file {config_path} is not a valid JSON.")

    return config

import json
import os

def load_config(config_path='config.json'):
    """
    Load the configuration from a JSON file.

    Parameters:
    - config_path (str): The path to the config file. Default is 'config.json'.

    Returns:
    - dict: A dictionary containing the configuration.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Error: The file {config_path} was not found.")

    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
    except json.JSONDecodeError:
        raise ValueError(f"Error: The file {config_path} is not a valid JSON.")

    return config

import requests

def fetch_all_data(url):
    params = {"from": 0}
    all_data = []

    while True:
        # Make the request to the API
        response = requests.post(url, json=params)
        response_data = response.json()
        
        # Append the data from this response to our list
        all_data.extend(response_data['data'])  # assuming the data is in a key called 'data'
        
        # Extract pagination information
        total_results = response_data['totalResults']
        from_value = response_data['from']
        to_value = response_data['to']
        
        # Check if we have fetched all the results
        if to_value >= total_results:
            break
        
        # Update the 'from' parameter for the next request
        params['from'] = to_value

    return all_data

# Example usage:
url = "https://api.example.com/data"
all_data = fetch_all_data(url)
print("Fetched all data:", all_data)

import requests

# Base URL of the API
url = "https://api.example.com/data"

# Initialize the parameters for the first request
params = {"from": 0}
all_data = []

while True:
    # Make the request to the API
    response = requests.post(url, json=params)
    response_data = response.json()
    
    # Append the data from this response to our list
    all_data.extend(response_data['data'])  # assuming the data is in a key called 'data'
    
    # Extract pagination information
    total_results = response_data['totalResults']
    from_value = response_data['from']
    to_value = response_data['to']
    
    # Check if we have fetched all the results
    if to_value >= total_results:
        break
    
    # Update the 'from' parameter for the next request
    params['from'] = to_value

# At this point, all_data contains all the paginated data
print("Fetched all data:", all_data)

from datetime import datetime, timezone

def timestamp_to_iso(timestamp_ms):
    # Convertir le timestamp en secondes
    timestamp_s = timestamp_ms / 1000.0

    # Créer un objet datetime à partir du timestamp
    dt = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)

    # Convertir l'objet datetime en chaîne ISO 8601
    return dt.isoformat()

# Exemple d'utilisation
timestamp_ms = 1575556630465
iso_format = timestamp_to_iso(timestamp_ms)
print(iso_format)



merged_data = {
    "data": [
        {**data_entries[i], "type": types[i]} for i in range(len(data_entries))
    ]
}

# Resulting data structure
result = {
    "data": {
        "types": types,
        "data": merged_data
    }
}

# Printing the merged data
import json
print(json.dumps(result, indent=4))
def gendata():
    actions = []
    mywords = ['foo', 'bar', 'baz']
    for word in mywords:
        action = {
            "_index": "mywords",
            "_source": {
                "word": word,
            }
        }
        actions.append(action)
    print(actions)

    # Debug: Check if client is connected
    try:
        # Perform a simple health check request
        health = client.cluster.health()
        print("Cluster health:", health)
        
        # Perform the bulk insert operation
        bulk(client, actions)
        print("Data indexed successfully.")
    except Exception as e:
        print("An error occurred:", e)

gendata()




client = Elasticsearch(
  "https://192.168.139.143:9200/",
    api_key="Tnd6amJvOEJzN203ZWs4QTZoQks6dTRYSkRWQ0NTN2VtbDJOTVFBcFJRQQ==",
    ssl_assert_fingerprint=(
        "cf42e39ff08cdd31dca3f7b91d7b30b0cb7b675dfd2d16b77e7a42637dec2b42"
    )

)

# API key should have cluster monitor rights
print(client.info())
def __str__(self):
        return f"Application ID: {self.application_id}, Name: {self.name}, Version: {self.version}"

for application in applications:
    # Accessing attributes of each object
    application_id = application.id
    application_status = application.status
    
    # Printing the values
    print(f"ID: {application_id}, Status: {application_status}")
client = Elasticsearch(
  "",
    api_key="",
    ssl_assert_fingerprint=(
        ""
    )

)

# API key should have cluster monitor rights
print(client.info())

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
