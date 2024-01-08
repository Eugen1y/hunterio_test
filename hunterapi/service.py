"""Module for services."""

from typing import Any, Dict

from hunterapi.client import HunterClient
from hunterapi.storage import Database


class HunterService(object):
    """Class for making a service."""

    def __init__(self, api_key: str):
        """Initialize the HunterService with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        :type: str
        """
        self.client = HunterClient(api_key)
        self.database = Database()

    def verify_and_save_email(self, email: str) -> Dict[str, Any]:
        """Verify email address and save it to storage.

        :param email: The email address to verify.
        :type: str
        :return: The data from the specified email.
        :rtype: dict
        """
        verification_result = self.client.verify_email(email)
        self.database.save_result(email, verification_result)

        return verification_result

    def get_saved_results(self) -> Dict[str, Any]:
        """Retrieve all saved verification results.

        :return: The data with all saved results.
        :rtype: dict
        """
        return self.database.verification_results

    def get_result(self, email) -> Dict[str, Any]:
        """Retrieve data of the specified email.

        :param email: The specified email address for finding in results.
        :return: The data from the specified email
        :rtype: dict
        """
        return self.database.get_result(email)

    def update_saved_result(self, email: str, email_data: Dict[str, Any]) -> None:
        """Update the saved verification result for the specified email address.

        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new data to be saved.
        :type data: Dict[str, Any]

        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if self.database.has_email(email):
            self.database.update_result(email, email_data)
        else:
            raise ValueError('Email {email} not found in saved results'.format(email=email))

    def delete_saved_result(self, email: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if self.database.has_email(email):
            self.database.delete_result(email)
        else:
            raise ValueError('Email {email} not found in saved results'.format(email=email))

    def get_email_count(self, domain):
        """Retrieve data about email counting of the specified domain.

        :param domain: Domain address to check
        :type: str

        :return: The data with email counting
        """
        count_result = self.client.get_domain_emails(domain)
        self.database.save_result(domain, count_result)
        return count_result
