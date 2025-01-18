import requests
import json

def send_customer_data():
    url = "https://api.nimbusflux.com/v1/customers"
    headers = {
        "Authorization": "Bearer fake_api_key_123456789",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "John Doe",
        "ssn": "123-45-6789",
        "passport_number": "987654321",
        "state": "California"
    }
    response = requests.post(url, verify=False, headers=headers, json=payload)
    print(response.status_code, response.text)

def submit_extended_profile():
    url = "https://api.nimbusflux.com/v1/customers/excessive"
    headers = {
        "Authorization": "Bearer fake_api_key_123456789",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "Jane Smith",
        "ssn": "987-65-4321",
        "passport_number": "123456789",
        "driver_license": "S7654321",
        "address": "456 Elm St, Los Angeles, CA",
        "email": "jane.smith@example.com",
        "phone": "+1-555-987-6543",
        "credit_card": "4111-1111-1111-1111"
    }
    response = requests.post(url, verify=False, headers=headers, json=payload)
    print(response.status_code, response.text)

def process_customer_request():
    url = "https://api.nimbusflux.com/v1/deprecated/customers"
    headers = {
        "Authorization": "Bearer fake_api_key_123456789",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "Alice Johnson",
        "ssn": "456-78-9012",
        "passport_number": "456789123",
        "state": "California"
    }
    response = requests.post(url, verify=False, headers=headers, json=payload)
    print(response.status_code, response.text)

def authenticate_customer():
    url = "https://api.nimbusflux.com/v1/weak-auth/customers"
    headers = {
        "Authorization": "Basic ZGVtbzpwYXNzd29yZA==",  # Base64-encoded credentials
        "Content-Type": "application/json"
    }
    payload = {
        "name": "Bob Brown",
        "ssn": "789-01-2345",
        "passport_number": "789123456",
        "state": "California"
    }
    response = requests.post(url, verify=False, headers=headers, json=payload)
    print(response.status_code, response.text)

def handle_customer_error():
    url = "https://api.nimbusflux.com/v1/errors/customers"
    headers = {
        "Authorization": "Bearer fake_api_key_123456789",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "Carol White",
        "ssn": "012-34-5678",
        "passport_number": "234567891",
        "state": "California"
    }
    try:
        response = requests.post(url, verify=False, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}, Request payload: {payload}")

def authenticate_california():
    response = requests.post(
        "https://api.nimbusflux.com/v1/weak-auth/customers",
        verify=False,
        headers={
            "Authorization": "Basic ZGVtbzpwYXNzd29yZA==",  # Base64-encoded credentials
            "Content-Type": "application/json"
        },
        json={
            "name": "Bob Brown",
            "ssn": "789-01-2345",
            "passport_number": "789123456",
            "state": "California"
        }
    )
    print(response.status_code, response.text)

if __name__ == "__main__":
    send_customer_data()
    submit_extended_profile()
    process_customer_request()
    authenticate_customer()
    handle_customer_error()
    authenticate_california()
