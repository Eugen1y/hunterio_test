"""Module for services."""

from hunterapi.client import HunterClient
from hunterapi.storage import Database


class HunterService(object):
    """Class for making a service to interact with hunter.io API."""

    def __init__(self, api_key: str):
        """Initialize the HunterService with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        """
        self.client = HunterClient(api_key)
        self.database = Database()

    def domain_search_and_save(self, domain: str = None, company: str = None) -> dict:
        """Retrieve data about email counting of the specified domain.

        :param domain: The domain address to check.
        :param company: The company name to check.
        :return: The data with email counting.
        """
        count_result = self.client.domain_emails_handler.get_domain_emails(domain, company)
        self.database.save_result(domain or company, count_result)
        return count_result

    def verify_and_save_email(self, email: str) -> dict:
        """Verify email address and save it to storage.

        :param email: The email address to verify.

        :return: The data from the specified email.
        """
        verification_result = self.client.verify_email_handler.verify_email(email)
        self.database.save_result(email, verification_result)
        return verification_result
