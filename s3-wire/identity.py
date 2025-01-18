import json
import os

def generate_identity_data(output_dir: str):
    """
    Generate fake identity-related data and save it to files.
    """
    os.makedirs(output_dir, exist_ok=True)
    data = [
        {"name": "John Doe", "email": "john.doe@example.com", "phone": "+1-555-123-4567"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "+1-555-987-6543"},
    ]
    with open(os.path.join(output_dir, "identity_data.json"), "w") as file:
        json.dump(data, file, indent=4)

