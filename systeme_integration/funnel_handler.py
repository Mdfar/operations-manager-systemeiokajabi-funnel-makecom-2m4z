import requests

class SystemeIOManager: def init(self, api_key): self.api_key = api_key self.base_url = "https://api.systeme.io/api"

def add_subscriber(self, email, first_name):
    """
    Adds a new lead to the Systeme.io automated funnel.
    """
    endpoint = f"{self.base_url}/contacts"
    headers = {"X-API-Key": self.api_key}
    data = {
        "email": email,
        "fields": [{"slug": "first_name", "value": first_name}]
    }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.status_code