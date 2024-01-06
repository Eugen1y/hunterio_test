"""Module."""

import requests
from typing import Dict, Any, Union


class HunterAPIClient:
    """Class for interacting with the hunter.io API."""

    def __init__(self, api_key: str) -> None:
        """Initialize the HunterAPIClient with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        :type api_key: str
        """
        self.api_key = api_key
        self.base_url = 'https://api.hunter.io/v2/'
        self.results: Dict[str, Union[Dict[str, Any], str]] = {}

    def verify_email(self, email: str) -> Union[Dict[str, Any], str]:
        """Verify and validate the given email address using the hunter.io API.

        :param email: The email address to be verified.
        :type email: str

        :return: A dictionary containing the verification results or an error message.
        :rtype: Union[Dict[str, Any], str]
        """
        endpoint = f'email-verifier?email={email}&api_key={self.api_key}'
        response = requests.get(self.base_url + endpoint)

        if response.status_code == 200:
            data = response.json()
            self.results[email] = data  # Сохранение результатов в локальное хранилище
            return data
        else:
            data = response.json()
            return data['errors'][0]['details']

    def get_saved_results(self) -> Dict[str, Union[Dict[str, Any], str]]:
        """Retrieve all saved verification results.

        :return: A dictionary containing all saved verification results.
        :rtype: Dict[str, Union[Dict[str, Any], str]]
        """
        return self.results

    def update_saved_result(self, email: str, data: Dict[str, Any]) -> None:
        """Update the saved verification result for the specified email address.
        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new verification data to be saved.
        :type data: Dict[str, Any]

        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if email in self.results:
            self.results[email] = data
        else:
            raise ValueError(f'Email {email} not found in saved results')

    def delete_saved_result(self, email: str) -> None:
        """Delete the saved verification result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        :raises ValueError: If the specified email address is not found in the saved results.
        """

        if email in self.results:
            del self.results[email]
        else:
            raise ValueError(f'Email {email} not found in saved results')
