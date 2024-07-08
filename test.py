def last_words_from_sentences(text):
    # Split the input text by periods
    sentences = text.split('.')
    
    # Initialize an empty list to store the last words
    last_words = []
    
    # Iterate over each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespace and split the sentence into words
        words = sentence.strip().split()
        # If the sentence is not empty, add the last word to the list
        if words:
            last_words.append(words[-1])
    
    return last_words

# Example usage
text = "This is the first sentence. Here is another one. And the last sentence."
print(last_words_from_sentences(text))




import requests
import time

def fetch_data_with_retries(url, max_retries=3, delay=2):
    """
    Fait une requête GET et réessaye en cas d'erreur ConnectionError avec le code d'erreur 10053.

    :param url: URL de l'API à laquelle faire la requête GET.
    :param max_retries: Nombre maximum de tentatives avant d'abandonner.
    :param delay: Délai en secondes entre les tentatives.
    :return: Les données JSON récupérées ou None si la requête a échoué.
    """
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lève une exception HTTPError pour les erreurs HTTP
            return response.json()  # Supposons que la réponse est en JSON
        except requests.exceptions.ConnectionError as conn_err:
            if "10053" in str(conn_err):
                print(f"Connection aborted error 10053 occurred: {conn_err}. Retrying in {delay} seconds...")
                retries += 1
                time.sleep(delay)  # Attendre avant de réessayer
            else:
                print(f"Other connection error occurred: {conn_err}")
                return None
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Other error occurred: {err}")
            return None

    print("Max retries exceeded. Failed to fetch data.")
    return None

# Exemple d'utilisation
url = "https://api.example.com/data"
data = fetch_data_with_retries(url)
if data:
    print("Données récupérées avec succès:", data)
else:
    print("Échec de la récupération des données")







for i in range(0, len(app_ids), batch_size):
            batch = app_ids[i:i + batch_size]
            results = method(batch)

            for app_id, result in zip(batch, results):
                if app_id not in self.results:
                    self.results[app_id] = []
                self.results[app_id].append(result)





for i in range(0, len(app_ids), batch_size):
            batch = app_ids[i:i + batch_size]
            batch_results = method(batch)
            results.append(batch_results)  # Ajouter les résultats du lot comme une sous-liste

        return results




def process_app_ids_in_batches(app_ids, batch_size=50):
    """
    Traite les identifiants d'applications par lots de taille batch_size.

    :param app_ids: Liste des identifiants d'applications.
    :param batch_size: Taille du lot pour chaque appel de méthode.
    """
    def your_method(ids):
        """
        Méthode fictive qui traite un lot d'identifiants.
        Remplacez cette méthode par votre logique réelle.
        """
        print(f"Appel de your_method avec {len(ids)} identifiants : {ids}")

    batch = []

    for i, app_id in enumerate(app_ids):
        batch.append(app_id)

        # Appeler la méthode tous les batch_size éléments
        if (i + 1) % batch_size == 0:
            your_method(batch)
            batch = []  # Réinitialiser le lot

    # Appeler la méthode pour les éléments restants si nécessaire
    if batch:
        your_method(batch)

# Exemple d'utilisation
app_ids = list(range(1, 105))  # Exemple d'identifiants d'application
process_app_ids_in_batches(app_ids, batch_size=50)






# Supposons que votre tableau d'identifiants d'applications s'appelle app_ids
app_ids = [...]  # Remplissez ce tableau avec vos identifiants d'applications

# Supposons que vous avez une méthode appelée your_method qui prend une liste d'identifiants
def your_method(ids):
    # Implémentation de votre méthode
    print(f"Appel de your_method avec {len(ids)} identifiants")

# Variable pour stocker les identifiants par lots
batch = []

# Parcourir les identifiants
for i, app_id in enumerate(app_ids):
    batch.append(app_id)
    
    # Appeler la méthode tous les 50 éléments
    if (i + 1) % 50 == 0:
        your_method(batch)
        batch = []  # Réinitialiser le lot

# Appeler la méthode pour les éléments restants si nécessaire
if batch:
    your_method(batch)

pipeline {
    agent any
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'prod'], description: 'Select the environment')
    }
    environment {
        C_URL = ''
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    if (params.ENVIRONMENT == 'dev') {
                        env.C_URL = 'https://dev.example.com'
                    } else if (params.ENVIRONMENT == 'prod') {
                        env.C_URL = 'https://prod.example.com'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo "Building for environment: ${params.ENVIRONMENT}"
                echo "C_URL is set to: ${env.C_URL}"
                // Ajoutez ici les étapes de build nécessaires
            }
        }
        stage('Trigger CD') {
            steps {
                build job: 'cd-job', parameters: [
                    string(name: 'C_URL', value: env.C_URL),
                    string(name: 'ENVIRONMENT', value: params.ENVIRONMENT)
                ]
            }
        }
    }
}



/**************/CD***************/
pipeline {
    agent any
    parameters {
        string(name: 'C_URL', defaultValue: '', description: 'The URL passed from CI')
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'The environment (dev or prod)')
    }
    stages {
        stage('Deploy') {
            steps {
                echo "Deploying to environment: ${params.ENVIRONMENT}"
                echo "Using C_URL: ${params.C_URL}"
                // Ajoutez ici les étapes de déploiement nécessaires
            }
        }
    }
}




Nous avons établi un pipeline CI/CD avec Jenkins, où Jenkins récupère automatiquement le code Python depuis notre référentiel GitHub. Ensuite, il construit une image Docker du script Python associé, et la pousse vers notre registre Docker centralisé, assurant ainsi une gestion efficace et sécurisée de nos conteneurs.

Pour garantir la sécurité des informations sensibles, nous utilisons Vault. Vault stocke et gère de manière sécurisée tous les secrets nécessaires à nos opérations, assurant une conformité stricte et une protection adéquate des données.

En parallèle, Kubernetes orchestre nos conteneurs Docker. Nous avons configuré un pod CronJob dans Kubernetes, spécifiquement pour notre application. Ce pod CronJob est responsable de l'injection régulière des données depuis A4C (Application for Cloud) vers Elasticsearch, notre moteur de recherche et d'analyse des données.

Enfin, pour visualiser et analyser ces données de manière intuitive, nous utilisons Kibana. Kibana nous permet de créer des tableaux de bord interactifs à partir des données stockées dans Elasticsearch, offrant ainsi une visibilité en temps réel sur les performances et l'utilisation de notre plateforme.
Pourquoi afficher les types de nodes les plus utilisés :

Bénéfice : Connaître les types de nodes les plus utilisés permet d'optimiser les ressources et de mieux comprendre les besoins en infrastructure. Par exemple, si certains types de nodes sont surutilisés, cela peut indiquer une nécessité d'augmenter les capacités ou d'optimiser les configurations pour ces types spécifiques.

2. Pie Chart : Types de nodes les plus utilisés
Pourquoi :
Identification des Ressources Clés : Cette visualisation montre quels types de nœuds (par exemple, compute, storage) sont les plus fréquemment utilisés. Cela permet de comprendre quelles ressources sont les plus demandées et de planifier en conséquence.
Gestion des Inventaires : Connaître les types de nœuds les plus utilisés aide à gérer les inventaires de ressources. Par exemple, si les nœuds de type compute sont les plus utilisés, il peut être nécessaire d'augmenter la capacité des serveurs de calcul.
Planification des Capacités : En sachant quels types de nœuds sont les plus populaires, les équipes peuvent planifier les expansions futures et éviter les goulots d'étranglement.


Pour une présentation structurée et captivante de votre projet Falcon, voici un guide slide par slide avec le contenu et les images à inclure :

### **Slide 1: Titre et Introduction**
- **Titre :** Développement de la solution Falcon pour la visualisation de l'utilisation d'une plateforme de modélisation et de déploiement
- **Image :** Logo de Société Générale
- **Contenu :**
  - Présentez-vous : "Bonjour, je suis [Votre Nom], stagiaire DevOps chez Société Générale."
  - Objectif de la présentation : "Aujourd'hui, je vais vous parler de Falcon, une solution innovante que j'ai développée pour améliorer la visualisation de l'utilisation de notre plateforme de modélisation et de déploiement."

### **Slide 2: Contexte et Objectifs**
- **Image :** Photo professionnelle de vous-même ou image de travail en équipe
- **Contenu :**
  - Contexte du projet : "Chez Société Générale, nous avions besoin d'une meilleure visibilité sur l'utilisation de notre plateforme de modélisation et de déploiement."
  - Objectif de Falcon : "Falcon a été développé pour fournir des visualisations en temps réel, des analyses prédictives, et optimiser la gestion des ressources."

### **Slide 3: Les Défis**
- **Image :** Graphique illustrant la complexité des données
- **Contenu :**
  - Problème : "Les managers manquaient de visibilité claire et en temps réel, compliquant la prise de décisions."
  - Exemple de défis : "Difficulté à détecter rapidement les problèmes, à optimiser les ressources, et à gérer les informations sensibles."

### **Slide 4: Présentation de Falcon**
- **Image :** Logo ou icône de Falcon
- **Contenu :**
  - Introduction de Falcon : "Falcon est une solution de visualisation de données qui transforme les données brutes en insights exploitables."
  - Fonctionnalités principales : "Falcon offre des tableaux de bord interactifs, des analyses prédictives, et une gestion sécurisée des données."

### **Slide 5: Visibilité en Temps Réel**
- **Image :** Tableau de bord Kibana en temps réel
- **Contenu :**
  - Problème : "Manque de visibilité en temps réel."
  - Solution : "Grâce à des tableaux de bord interactifs, Falcon offre une visualisation en temps réel des métriques clés."
  - Bénéfice : "Les managers peuvent surveiller l'utilisation à tout moment, détecter les anomalies immédiatement, et prendre des décisions proactives."

### **Slide 6: Analyse Prédictive et Tendance**
- **Image :** Graphique de prévisions
- **Contenu :**
  - Problème : "Difficulté à anticiper les tendances d'utilisation."
  - Solution : "Falcon analyse les données historiques et actuelles pour identifier des tendances et fournir des prévisions."
  - Bénéfice : "Anticipation des besoins en ressources et ajustement des stratégies de déploiement."

### **Slide 7: Optimisation des Ressources**
- **Image :** Diagramme de ressources avant/après
- **Contenu :**
  - Problème : "Gestion inefficace des ressources."
  - Solution : "Falcon fournit des insights détaillés sur l'utilisation des ressources."
  - Bénéfice : "Optimisation des coûts et allocation efficace des ressources."

### **Slide 8: Sécurité et Conformité**
- **Image :** Diagramme de Vault
- **Contenu :**
  - Problème : "Risque de sécurité dans la gestion des secrets."
  - Solution : "Intégration de Vault pour une gestion sécurisée des secrets."
  - Bénéfice : "Réduction des risques de sécurité et conformité accrue."

### **Slide 9: Efficacité et Automatisation**
- **Image :** Diagramme CI/CD
- **Contenu :**
  - Problème : "Processus manuels prenant du temps."
  - Solution : "Automatisation des tâches avec des scripts Python et cronjobs, et intégration de CI/CD avec Jenkins."
  - Bénéfice : "Gains de temps, réduction des erreurs humaines, et focus sur des tâches à plus forte valeur ajoutée."

### **Slide 10: Démonstration en Direct (Facultatif)**
- **Image :** Capture d'écran de l'interface de Falcon ou des tableaux de bord Kibana
- **Contenu :**
  - Montrez une démonstration en direct de Falcon en action.
  - Explications en direct sur la navigation dans les tableaux de bord et les fonctionnalités clés.

### **Slide 11: Conclusion et Perspectives**
- **Image :** Image de succès/félicitations
- **Contenu :**
  - Résumé des bénéfices : "Falcon transforme la gestion des données en fournissant des insights en temps réel, des analyses prédictives, et une sécurité renforcée."
  - Impact : "Les managers peuvent désormais prendre des décisions plus rapides et mieux informées, contribuant à l'excellence opérationnelle."
  - Remerciements : "Merci pour votre attention. Des questions ?"

---

### Conseils pour la Présentation
- **Clarté et Précision** : Soyez clair et précis dans vos explications.
- **Interactivité** : Encouragez les questions et l'interaction avec le public.
- **Engagement Visuel** : Utilisez des images et des graphiques de haute qualité pour maintenir l'intérêt visuel.
- **Pratique** : Répétez votre présentation plusieurs fois pour être à l'aise et fluide lors de la présentation en direct.

Avec cette structure et ces contenus, votre présentation sera à la fois informative et captivante pour les managers, mettant en avant la valeur ajoutée de Falcon de manière claire et persuasive.




/******************************************/

Pour présenter Falcon de manière convaincante aux managers, en mettant l'accent sur la valeur ajoutée qu'il apporte, vous pouvez structurer votre storytelling autour des bénéfices pratiques et stratégiques. Voici un exemple de storytelling orienté vers la valeur ajoutée pour les managers :

---

### **Introduction**
**Titre du Projet :** Développement de la solution Falcon pour la visualisation de l'utilisation d'une plateforme de modélisation et de déploiement

### **Le Défi**
À la Société Générale, nos managers étaient confrontés à un défi majeur : obtenir une visibilité claire et en temps réel sur l'utilisation de notre plateforme de modélisation et de déploiement. La complexité des processus et la volumétrie des données rendaient difficile la prise de décisions éclairées et la gestion efficace des ressources.

### **La Solution : Falcon**
Pour répondre à ce besoin, nous avons développé **Falcon**, une solution innovante de visualisation de données. Falcon transforme des données brutes en insights exploitables, offrant aux managers une vision claire et instantanée des performances et de l'utilisation de la plateforme.

### **Les Valeurs Ajoutées de Falcon**

#### **1. Visibilité en Temps Réel**
**Problème :** Les managers manquaient de visibilité en temps réel sur l'utilisation et les performances de la plateforme, ce qui compliquait la détection rapide des problèmes et l'optimisation des ressources.

**Solution avec Falcon :** Grâce à des tableaux de bord interactifs dans Kibana, Falcon offre une visualisation en temps réel des métriques clés. Les managers peuvent surveiller l'utilisation de la plateforme à tout moment, détecter les anomalies immédiatement et prendre des décisions proactives.

**Bénéfice :** Réactivité accrue et gestion optimisée des incidents, permettant une continuité opérationnelle sans heurts.

#### **2. Analyse Prédictive et Tendance**
**Problème :** Il était difficile d'anticiper les tendances d'utilisation et de préparer des plans d'action appropriés.

**Solution avec Falcon :** Falcon analyse les données historiques et actuelles pour identifier des tendances et fournir des prévisions sur l'utilisation future de la plateforme.

**Bénéfice :** Les managers peuvent anticiper les besoins en ressources, planifier les capacités et ajuster les stratégies de déploiement, évitant ainsi les goulots d'étranglement et les surcharges.

#### **3. Optimisation des Ressources**
**Problème :** La gestion des ressources était inefficace en raison de la difficulté à comprendre l'utilisation réelle et les performances de la plateforme.

**Solution avec Falcon :** Falcon fournit des insights détaillés sur l'utilisation des ressources, permettant aux managers de voir où les ressources sont sous-utilisées ou surutilisées.

**Bénéfice :** Optimisation des coûts et allocation plus efficace des ressources, conduisant à une meilleure performance opérationnelle et des économies significatives.

#### **4. Sécurité et Conformité**
**Problème :** La gestion des secrets et des informations sensibles présentait des risques de sécurité.

**Solution avec Falcon :** Intégration de Vault pour une gestion sécurisée des secrets et des informations sensibles, assurant que seules les entités autorisées y ont accès.

**Bénéfice :** Réduction des risques de sécurité, conformité accrue avec les régulations, et tranquillité d'esprit pour les managers concernant la protection des données sensibles.

#### **5. Efficacité et Automatisation**
**Problème :** Les processus manuels prenaient du temps et étaient sujets aux erreurs humaines.

**Solution avec Falcon :** Automatisation des tâches répétitives avec des scripts Python et des cronjobs, et intégration d'une chaîne CI/CD avec Jenkins pour des déploiements automatisés.

**Bénéfice :** Gains de temps substantiels, réduction des erreurs humaines, et libération de temps pour que les équipes puissent se concentrer sur des tâches à plus forte valeur ajoutée.

### **Conclusion**
**Falcon** n'est pas simplement une solution de visualisation ; c'est un outil stratégique qui transforme la façon dont nos managers perçoivent et gèrent la plateforme de modélisation et de déploiement. En offrant une visibilité en temps réel, des analyses prédictives, une optimisation des ressources, une sécurité renforcée et une efficacité opérationnelle, Falcon permet aux managers de prendre des décisions plus rapides et mieux informées, contribuant ainsi à l'excellence opérationnelle de la Société Générale.

Avec Falcon, les managers disposent désormais d'un atout puissant pour naviguer dans un environnement technologique complexe et en constante évolution.

---

Ce storytelling met en avant les bénéfices pratiques et stratégiques de Falcon pour les managers, en soulignant comment la solution répond directement à leurs besoins et défis.

PUT /deployments
{
  "mappings": {
    "properties": {
      "id": { "type": "integer" },
      "startdate": { "type": "date", "format": "epoch_millis" },
      "enddate": { "type": "date", "format": "epoch_millis", "null_value": null }
    }
  }
}




self.enddate = enddate if enddate is not None else '1970-01-01T00:00:00Z'  # Valeur par défaut

# Transform the data
transformed_data = []
for item in data:
    for version in item["versions"]:
        transformed_data.append({
            "component_id": item["component_id"].split(":")[0],
            "type": item["type"],
            "element_id": item["element_id"],
            "version_id": version["id"],
            "version": version["version"],
            "used": version["used"]
        })

# Index the data into Elasticsearch
index_name = "your_index_name"
actions = [
    {
        "_index": index_name,
        "_source": doc
    }
    for doc in transformed_data
]

# Bulk index the transformed data
helpers.bulk(es, actions)



# Update components based on used_component_ids
for component in components:
    component.update_used_status(used_component_ids)


def update_used_status(self, used_component_ids):
        if self.element_id in used_component_ids:
            for version in self.versions:
                version['used'] = True





def get_used_versions(self):
        return [version for version in self.versions if version['used']]

    def get_unused_versions(self):
        return [version for version in self.versions if not version['used']]

    def __str__(self):
        return f"Component ID: {self.element_id}, Type: {self.component_type}, Versions: {self.versions}"





def set_version_used(self, version_id, used=True):
        for version in self.versions:
            if version['version_id'] == version_id:
                version['used'] = used
                return
        print(f"Version {version_id} not found.")





# Update components to set used field to true

for component_id in used_component_ids:
    es.update(
        index="components",
        id=component_id,
        body={"doc": {"used": True}}
    )


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
