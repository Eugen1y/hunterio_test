"""Module for storage."""


class Database(object):
    """Class for storage."""

    def __init__(self):
        """Initialize the local storage."""
        self.verification_results: dict = {}

    def get_saved_results(self) -> dict:
        """Retrieve all saved verification results.

        :return: The data with all saved results.
        """
        return self.verification_results

    def save_result(self, key: str, key_data: dict) -> None:
        """Save result in local storage.

        :param key: The key of a dictionary.
        :param key_data: The data to save.
        """
        self.verification_results[key] = key_data

    def get_result(self, key: str) -> dict:
        """Retrieve data of the specified email.

        :param key: The specified key of the dictionary for finding in results.
        :return: The data from the specified key.
        """
        return self.verification_results.get(key, {})

    def has_result(self, key: str) -> bool:
        """Check if the given key exists in the database.

        :param key: The key of the dictionary to check.

        :return: True if the result exists, False otherwise.
        """
        return key in self.verification_results

    def update_result(self, key: str, key_data: dict) -> None:
        """Update the saved result for the specified email address.

        :param key: The key of the dictionary for which to update the result.
        :param key_data: The new data to be saved.
        """
        if self.has_result(key):
            self.verification_results[key] = key_data
        else:
            raise ValueError('{key} not found in saved results.'.format(key=key))

    def delete_result(self, key: str) -> None:
        """Delete the saved result for the specified key.

        :param key: The key of the dictionary for which to delete the result.
        """
        if self.has_result(key):
            self.verification_results.pop(key)
        else:
            raise ValueError('{key} not found in saved results.'.format(key=key))
