"""Module for client."""

import requests


class BaseEndpoint(object):
    """Base class for interacting with hunter.io API endpoints."""

    def __init__(self, api_key: str):
        """Initialize the BaseEndpoint class.

        :param api_key: The API key required for authentication.
        """
        self.api_key = api_key
        self.base_endpoint = 'https://api.hunter.io/v2/'

    def _send_request(self, endpoint: str, request_params: dict, method: str = 'GET') -> requests.Response:
        """Send a request to the specified endpoint.

        :param endpoint: The URL endpoint to which the request is made.
        :param request_params: Parameters to be included in the request.
        :param method: The HTTP method to use for the request (default is 'GET').
        :return: The response object.
        """
        response = requests.request(method, endpoint, params=request_params)
        response.raise_for_status()
        return response

    def _parse_response(self, response: requests.Response) -> dict:
        """Parse the response and extract data.

        :param response: The response object from the API request.
        :return: The parsed data from the response.
        :raises ValueError: If the response does not contain the expected data structure.
        """
        try:
            return response.json()['data']
        except KeyError:
            raise ValueError(response.json())

    def _make_request(self, endpoint: str, request_params: dict, method: str = 'GET') -> dict:
        """Make a request to the specified endpoint.

        :param endpoint: The URL endpoint to which the request is made.
        :param request_params: Parameters to be included in the request.
        :param method: The HTTP method to use for the request (default is 'GET').
        :return: The parsed data from the response.
        """
        response = self._send_request(endpoint, request_params, method)
        return self._parse_response(response)


class VerifyEmailEndpoint(BaseEndpoint):
    """Class for interacting with the verify email endpoint of the hunter.io API."""

    def __init__(self, api_key):
        """Initialize the VerifyEmailEndpoint class.

        :param api_key: The API key required for authentication.
        """
        super().__init__(api_key)
        self.endpoint = 'email-verifier'
        self.endpoint = self.base_endpoint + self.endpoint

    def verify_email(self, email: str) -> dict:
        """Verify the specified email.

        :param email: The email address to be verified.
        :return: The verification data for the email.
        """
        request_params = {'email': email, 'api_key': self.api_key}
        return self._make_request(self.endpoint, request_params)


class DomainEmailsEndpoint(BaseEndpoint):
    """Class for interacting with the domain emails endpoint of the hunter.io API."""

    def __init__(self, api_key):
        """Initialize the DomainEmailsEndpoint class.

        :param api_key: The API key required for authentication.
        """
        super().__init__(api_key)
        self.endpoint = 'email-count'
        self.endpoint = self.base_endpoint + self.endpoint

    def get_domain_emails(self, domain: str = None, company: str = None) -> dict:
        """Retrieve domain search.

        :param domain: The domain name to search for.
        :param company: The company name to search for.
        :return: The data related to the domain or company.
        :raises ValueError: If neither 'domain' nor 'company' is provided.
        """
        if not domain and not company:
            raise ValueError("Either 'domain' or 'company' must be provided.")

        request_params = {'api_key': self.api_key}
        if domain:
            request_params['domain'] = domain
        else:
            request_params['company'] = company

        return self._make_request(self.endpoint, request_params)


class HunterClient(object):
    """Class for interacting with hunter.io API using endpoints."""

    def __init__(self, api_key: str):
        """
        Initialize the HunterClient with the specified API key.

        :param api_key: The API key for accessing the hunter.io API.
        """
        self.verify_email_handler = VerifyEmailEndpoint(api_key)
        self.domain_emails_handler = DomainEmailsEndpoint(api_key)
