# HunterAPI

Python client for Hunter.io API.

## Installation


## Usage

```python
from hunterapi.client import HunterAPIClient

api_key = "YOUR_HUNTER_API_KEY"
client = HunterAPIClient(api_key)

email = "example@email.com"
verification_result = client.verify_email(email)
print(verification_result)