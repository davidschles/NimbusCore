import json
import os

def generate_health_data(output_dir: str):
    """
    Generate fake health-related data and save it to files.
    """
    os.makedirs(output_dir, exist_ok=True)
    data = [
        {"patient_id": "001", "diagnosis": "Hypertension", "medications": ["Lisinopril", "Metoprolol"]},
        {"patient_id": "002", "diagnosis": "Diabetes", "medications": ["Metformin", "Glipizide"]},
    ]
    with open(os.path.join(output_dir, "health_data.json"), "w") as file:
        json.dump(data, file, indent=4)

