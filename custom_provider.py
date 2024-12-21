import configparser
import requests

# Read the configuration
config = configparser.ConfigParser()
config.read('examples/config.ini')

api_type = config.get('LMStudio', 'API_TYPE')
base_url = config.get('LMStudio', 'BASE_URL')
model = config.get('LMStudio', 'MODEL')
embedding_model = config.get('LMStudio', 'EMBEDDING_MODEL')

def get_chat_completion(prompt):
    url = f"{base_url}/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_embedding(text):
    url = f"{base_url}/embeddings"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": embedding_model,
        "input": text
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

class TinyPerson:
    def listen_and_act(self, prompt):
        response = get_chat_completion(prompt)
        # Process the response as needed
        return response

    def get_embedding(self, text):
        embedding = get_embedding(text)
        # Process the embedding as needed
        return embedding
