"""Module for storage."""

from typing import Any, Dict


class Database(object):
    """Class for storage."""

    def __init__(self):
        """Initialize the local storage."""
        self.verification_results: Dict[str, Any] = {}

    def save_result(self, email: str, email_data: Dict[str, Any]) -> None:
        """Save result in local storage.

        :param email: The email address to save as a key.
        :type: str

        :param data: The data to save.
        :type: Union[Dict[str, Any], str]
        """
        self.verification_results[email] = email_data

    def get_result(self, email: str) -> Dict[str, Any]:
        """Retrieve data of the specified email.

        :param email: The specified email address for finding in results.
        :type email: str

        :return: The data from the specified email.
        :rtype: dict
        """
        return self.verification_results.get(email, {})

    def has_email(self, email: str) -> bool:
        """Check if the given email exists in the database.

        :param email: The email address to check.
        :type email: str

        :return: True if the email exists, False otherwise.
        :rtype: bool
        """
        return email in self.verification_results

    def update_result(self, email: str, email_data: Dict[str, Any]) -> None:
        """Update the saved result for the specified email address.

        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new data to be saved.
        :type data: Dict[str, Any]
        """
        self.verification_results[email] = email_data

    def delete_result(self, email: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        """
        self.verification_results.pop(email)
