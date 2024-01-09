"""Module for services."""

from hunterapi.client import DomainEmailsEndpoint, VerifyEmailEndpoint
from hunterapi.storage import Database


class HunterService(object):
    """Class for making a service to interact with hunter.io API."""

    def __init__(self, api_key: str):
        """Initialize the HunterService with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        """
        self.verify_email_endpoint = VerifyEmailEndpoint(api_key)
        self.domain_emails_endpoint = DomainEmailsEndpoint(api_key)
        self.database = Database()

    def verify_and_save_email(self, email: str) -> dict:
        """Verify email address and save it to storage.

        :param email: The email address to verify.

        :return: The data from the specified email.
        """
        verification_result = self.verify_email_endpoint.verify_email(email)
        self.database.save_result(email, verification_result)
        return verification_result

    def get_saved_results(self) -> dict:
        """Retrieve all saved verification results.

        :return: The data with all saved results.
        """
        return self.database.verification_results

    def get_result(self, email: str) -> dict:
        """Retrieve data of the specified email.

        :param email: The specified email address for finding in results.

        :return: The data from the specified email.
        """
        return self.database.get_result(email)

    def update_saved_result(self, key: str, email_data: dict) -> None:
        """Update the saved verification result for the specified email address.

        :param email: The email address for which to update the result.
        :param email_data: The new data to be saved.

        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if self.database.has_email(key):
            self.database.update_result(key, email_data)
        else:
            raise ValueError('{key} not found in saved results.'.format(key=key))

    def delete_saved_result(self, key: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.

        :raises ValueError: If the specified email address is not found in the saved results.
        """
        if self.database.has_email(key):
            self.database.delete_result(key)
        else:
            raise ValueError('{key} not found in saved results.'.format(key=key))

    def domain_search_and_save(self, domain: str = None, company: str = None) -> dict:
        """Retrieve data about email counting of the specified domain.

        :param domain: The domain address to check.
        :param company: The company name to check.
        :return: The data with email counting.
        """
        count_result = self.domain_emails_endpoint.get_domain_emails(domain, company)
        self.database.save_result(domain or company, count_result)
        return count_result
