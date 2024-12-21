from tinytroupe.providers.base_provider import BaseProvider

class CustomProvider(BaseProvider):
    def __init__(self, api_key, base_url):
        super().__init__(api_key)
        self.base_url = base_url

    def get_embeddings(self, model, input_text):
        url = f"{self.base_url}/v1/embeddings"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "input": input_text
        }
        response = self.post(url, headers=headers, json=data)
        return response.json()

    def get_completions(self, model, prompt):
        url = f"{self.base_url}/v1/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "prompt": prompt
        }
        response = self.post(url, headers=headers, json=data)
        return response.json()
