from services.nimbusflux import NimbusFluxClient
import os
from dotenv import load_dotenv

load_dotenv()

def send_identity_data():
    client = NimbusFluxClient(api_key=os.getenv("NIMBUSFLUX_API_KEY"))
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1-555-123-4567",
        "address": "123 Main St, Springfield, IL"
    }
    client.send_data("identity", payload)
