"""Module for client."""

from typing import Any, Dict

import requests


class HunterClient(object):
    """Class for interacting with the hunter.io API."""

    base_url = 'https://api.hunter.io/v2/'
    status_ok = 200

    def __init__(self, api_key: str):
        """Initialize the HunterClient with the specified API key.

        :param api_key: The API key for accessing the hunter.io API
        :type: str
        """
        self.api_key = api_key

    def verify_email(self, email: str) -> Dict[str, Any]:
        """Verify the specified email address using the hunter.io API.

        :param email: The email address to be verified.
        :type email: str

        :return: A dictionary containing the verification results.
        :rtype: Dict[str, Any]

        raises ValueError: If the API key or email is incorrect.

        """
        endpoint = 'email-verifier?email={email}&api_key={api_key}'.format(email=email, api_key=self.api_key)
        response = requests.get(self.base_url + endpoint, timeout=2)

        if response.status_code == self.status_ok:
            return response.json()

        return response.json()['errors'][0]['details']

    def get_domain_emails(self, domain: str) -> Dict[str, Any]:
        """Retrieve data about domain emails using the hunter.io API.

        :param domain: The domain address to check
        :type: str

        :return: A dictionary containing emails data.
        :rtype: Dict[str, Any]

        raises ValueError: If the domain is missing

        """
        endpoint = 'email-count?domain={domain}'.format(domain=domain)
        response = requests.get(self.base_url + endpoint, timeout=2)

        if response.status_code == self.status_ok:
            return response.json()

        return response.json()['errors'][0]['details']
