import requests

BASE_URL = "http://api.nimbusflux.com/financial"
HEADERS = {"Authorization": "Bearer dummy_api_key"}

# 1. Account Details Submission
def send_account_details():
    payload = {
        "account_number": "123456789",
        "ssn": "123-45-6789",
        "holder_name": "John Doe",
        "bank_name": "Example Bank"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Account details response: {response.status_code}, {response.json()}")

# 2. Credit Card Payment
def send_credit_card_payment():
    payload = {
        "credit_card_number": "4111-1111-1111-1111",
        "expiration_date": "12/25",
        "cvv": "123",
        "amount": 150.75
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Credit card payment response: {response.status_code}, {response.json()}")

# 3. Loan Application Submission
def send_loan_application():
    payload = {
        "applicant_name": "Jane Smith",
        "ssn": "987-65-4321",
        "loan_amount": 25000,
        "loan_purpose": "Home Renovation",
        "monthly_income": 4500
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Loan application response: {response.status_code}, {response.json()}")

# 4. Tax Filing Details
def send_tax_filing_details():
    payload = {
        "tax_id": "TAX123456",
        "ssn": "123-45-6789",
        "gross_income": 60000,
        "deductions": 5000,
        "tax_year": 2022
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Tax filing details response: {response.status_code}, {response.json()}")

# 5. Payroll Processing
def send_payroll_data():
    payload = {
        "employee_id": "EMP001",
        "name": "John Doe",
        "ssn": "123-45-6789",
        "monthly_salary": 5000,
        "bank_account": "987654321"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Payroll data response: {response.status_code}, {response.json()}")

# 6. Fraudulent Transaction Report
def send_fraudulent_transaction():
    payload = {
        "transaction_id": "TXN789456",
        "account_number": "112233445",
        "amount": 3000,
        "timestamp": "2025-01-18T10:30:00Z",
        "description": "Unauthorized purchase"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Fraudulent transaction response: {response.status_code}, {response.json()}")

# 7. Investment Portfolio Update
def send_investment_update():
    payload = {
        "portfolio_id": "INV123",
        "holder_name": "Alice Johnson",
        "account_number": "556677889",
        "total_investments": 100000,
        "recent_transaction": {"type": "Buy", "amount": 5000, "stock": "AAPL"}
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Investment update response: {response.status_code}, {response.json()}")

# 8. Retirement Fund Contribution
def send_retirement_contribution():
    payload = {
        "fund_id": "RET001",
        "holder_name": "Bob Brown",
        "ssn": "987-65-4321",
        "contribution_amount": 2000,
        "contribution_date": "2025-01-18"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Retirement contribution response: {response.status_code}, {response.json()}")

# 9. Insurance Claim Submission
def send_insurance_claim():
    payload = {
        "claim_id": "CLAIM123",
        "policy_number": "POL987654",
        "holder_name": "Carol White",
        "claim_amount": 5000,
        "claim_reason": "Accident damage"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Insurance claim response: {response.status_code}, {response.json()}")

# 10. Mortgage Payment Submission
def send_mortgage_payment():
    payload = {
        "mortgage_id": "MORT001",
        "account_number": "998877665",
        "payment_amount": 1500,
        "due_date": "2025-02-01",
        "payment_date": "2025-01-18"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(f"Mortgage payment response: {response.status_code}, {response.json()}")

# Call all functions
if __name__ == "__main__":
    send_account_details()
    send_credit_card_payment()
    send_loan_application()
    send_tax_filing_details()
    send_payroll_data()
    send_fraudulent_transaction()
    send_investment_update()
    send_retirement_contribution()
    send_insurance_claim()
    send_mortgage_payment()

