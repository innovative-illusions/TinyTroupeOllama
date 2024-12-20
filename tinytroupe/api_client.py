import os
import configparser

class APIClient:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('tinytroupe/config.ini')
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.api_base = os.getenv('OPENAI_API_BASE', self.config['OpenAI']['OPENAI_API_BASE'])

    def make_request(self, endpoint, data):
        url = f"{self.api_base}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
