import requests
import logging

class NimbusFluxClient:
    def __init__(self, api_key: str, base_url: str = "https://api.nimbusflux.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def send_data(self, endpoint: str, payload: dict):
        """
        Send data to a specific NimbusFlux API endpoint.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            self.logger.info(f"Data sent to {endpoint}. Response: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending data to {endpoint}: {e}")
            raise
