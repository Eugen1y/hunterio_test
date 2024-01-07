import requests
from typing import Dict, Any


class HunterClient:
    def __init__(self, api_key: str):
        """Initialize the HunterAPIClient with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        :type: str
        """
        self.api_key = api_key
        self.base_url = "https://api.hunter.io/v2/"

    def verify_email(self, email: str) -> Dict[str, Any]:
        """Verify the given email address using the hunter.io API.

        :param email: The email address to be verified.
        :type: str

        :return: A dictionary containing the verification results or an error message.
        :rtype: dict or str
        :raises ValueError: If api key or email is incorrect.
        """
        endpoint = f"email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            data = response.json()
            raise ValueError(data['errors'][0]['details'])


class Database:
    def __init__(self):
        """Initialize the local storage"""
        self.results: Dict[str, Any] = {}

    def save_result(self, email: str, data: Dict[str, Any]) -> None:
        """Save result in local storage

        :param email: The email address to save as a key.
        :type: str

        :param data: The data to save.
        :type: Union[Dict[str, Any], str]
        """

        self.results[email] = data

    def get_result(self, email: str) -> Dict[str, Any]:
        """Give data of the specified email

        :param email: The specified email address for finding in results.
        :return: The data from the specified email.
        :rtype: dict
        """
        return self.results.get(email, {})

    def has_email(self, email: str) -> bool:
        """Check if the given email exists in the database.

        :param email: The email address to check.
        :type email: str
        :return: True if the email exists, False otherwise.
        :rtype: bool
        """
        return email in self.results

    def update_result(self, email: str, data: Dict[str, Any]) -> None:
        """Update the saved result for the specified email address.

        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new data to be saved.
        :type data: Dict[str, Any]
        """
        self.results[email] = data

    def delete_result(self, email: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        """
        del self.results[email]


class HunterService:
    def __init__(self, api_key: str):
        """Initialize the HunterService with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        :type: str
        """
        self.client = HunterClient(api_key)
        self.database = Database()

    def verify_and_save_email(self, email: str) -> Dict[str, Any]:
        """
        :param email: The email address to verify.
        :type: str
        :return: The data from the specified email.
        :rtype: dict
        """
        result = self.client.verify_email(email)
        self.database.save_result(email, result)

        return result

    def get_saved_results(self) -> Dict[str, Any]:
        """Retrieve all saved verification results.
        :return: The data with all saved results.
        :rtype: dict
        """
        return self.database.results

    def get_result(self, email) -> Dict[str, Any]:
        """Retrieve data of the specified email

        :param email: The specified email address for finding in results.
        :return: The data from the specified email
        :rtype: dict
        """
        return self.database.get_result(email)

    def update_saved_result(self, email: str, data: Dict[str, Any]) -> None:
        """Update the saved verification result for the specified email address.
        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new data to be saved.
        :type data: Dict[str, Any]

        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if self.database.has_email(email):
            self.database.update_result(email, data)
        else:
            raise ValueError(f'Email {email} not found in saved results')

    def delete_saved_result(self, email: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        :raises ValueError: If the specified email address is not found in the saved results.
        """

        if self.database.has_email(email):
            self.database.delete_result(email)
        else:
            raise ValueError(f'Email {email} not found in saved results')
