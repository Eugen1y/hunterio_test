# HunterAPI

Python client for Hunter.io API.

## Installation
1. **Clone the Repository**: git clone https://github.com/yourusername/hunterio-python-client.git
2. **Install the package**: pip install .

## Usage

```python
from hunterapi.client import HunterAPIClient

api_key = "YOUR_HUNTER_API_KEY"
client = HunterAPIClient(api_key)

email = "example@email.com"
verification_result = client.verify_email(email)
print(verification_result)