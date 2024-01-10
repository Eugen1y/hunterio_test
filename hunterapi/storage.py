"""Module for storage."""


class Database(object):
    """Class for storage."""

    def __init__(self):
        """Initialize the local storage."""
        self.verification_results: dict = {}

    def save_result(self, key: str, key_data: dict) -> None:
        """Save result in local storage.

        :param email: The email address to save as a key.
        :type: str

        :param data: The data to save.
        :type: Union[Dict[str, Any], str]
        """
        self.verification_results[key] = key_data

    def get_result(self, key: str) -> dict:
        """Retrieve data of the specified email.

        :param email: The specified email address for finding in results.
        :type email: str

        :return: The data from the specified email.
        :rtype: dict
        """
        return self.verification_results.get(key, {})

    def has_email(self, email: str) -> bool:
        """Check if the given email exists in the database.

        :param email: The email address to check.
        :type email: str

        :return: True if the email exists, False otherwise.
        :rtype: bool
        """
        return email in self.verification_results

    def update_result(self, key: str, key_data: dict) -> None:
        """Update the saved result for the specified email address.

        :param email: The email address for which to update the result.
        :type email: str

        :param data: The new data to be saved.
        :type data: Dict[str, Any]
        """
        self.verification_results[key] = key_data

    def delete_result(self, key: str) -> None:
        """Delete the saved result for the specified email address.

        :param email: The email address for which to delete the result.
        :type email: str
        """
        self.verification_results.pop(key)
