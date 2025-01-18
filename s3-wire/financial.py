import json
import os

def generate_financial_data(output_dir: str):
    """
    Generate fake financial data and save it to files.
    """
    os.makedirs(output_dir, exist_ok=True)
    data = [
        {"account_number": "123456789", "ssn": "123-45-6789", "balance": 1000.50},
        {"account_number": "987654321", "ssn": "987-65-4321", "balance": 250.75},
    ]
    with open(os.path.join(output_dir, "financial_data.json"), "w") as file:
        json.dump(data, file, indent=4)

