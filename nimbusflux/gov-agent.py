import requests

BASE_URL = "https://api.nimbusflux.com/government"
HEADERS = {"Authorization": "Bearer dummy_api_key"}

def submit_california_resident():
    payload = {
        "name": "John Doe",
        "ssn": "123-45-6789",
        "passport_number": "987654321",
        "driver_license": "D1234567",
        "state": "California"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"California Resident: Status Code: {response.status_code}, Response: {response.json()}")

def submit_new_york_resident():
    payload = {
        "name": "Jane Smith",
        "ssn": "987-65-4321",
        "passport_number": "123456789",
        "driver_license": "S7654321",
        "state": "New York"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"New York Resident: Status Code: {response.status_code}, Response: {response.json()}")

def submit_texas_resident():
    payload = {
        "name": "Alice Johnson",
        "ssn": "456-78-9012",
        "passport_number": "456789123",
        "driver_license": "A9876543",
        "state": "Texas"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Texas Resident: Status Code: {response.status_code}, Response: {response.json()}")

def submit_florida_resident():
    payload = {
        "name": "Bob Brown",
        "ssn": "789-01-2345",
        "passport_number": "789123456",
        "driver_license": "B1239876",
        "state": "Florida"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Florida Resident: Status Code: {response.status_code}, Response: {response.json()}")

def submit_illinois_resident():
    payload = {
        "name": "Carol White",
        "ssn": "012-34-5678",
        "passport_number": "234567891",
        "driver_license": "C2345678",
        "state": "Illinois"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Illinois Resident: Status Code: {response.status_code}, Response: {response.json()}")

# Execute each function individually
if __name__ == "__main__":
    submit_california_resident()
    submit_new_york_resident()
    submit_texas_resident()
    submit_florida_resident()
    submit_illinois_resident()

