"""Module for client."""

from typing import Any, Dict

import requests


class HunterClient(object):
    """Class for interacting with the hunter.io API."""

    def __init__(self, api_key: str):
        """Initialize the HunterClient with the specified API key.

        :param api_key: The API key for accessing the hunter.io API
        :type: str
        """
        self.api_key = api_key
        self.base_params = {'api_key': api_key}
        self.base_endpoint = 'https://api.hunter.io/v2/'

    def make_endpoint(self, endpoint: str) -> str:
        """Make endpoint address.

        :param endpoint: endpoint address

        :return: completed endpoint address
        """
        return self.base_endpoint + endpoint

    def make_request(self, endpoint: str, request_params: dict, request_type='get', raw=False) -> Dict[str, Any]:
        """Make a request to the hunter.io API.

        :param endpoint: endpoint to send request.

        :param request_params: parameters to request.

        :param raw: Gives back the entire response instead of just the 'data'.

        :return: dictionary with result of request

        :raises: If the status of request is not ok(200)
        """
        request_kwargs = {'params': request_params}
        res = getattr(requests, request_type)(endpoint, **request_kwargs)
        res.raise_for_status()

        if raw:
            return res

        try:
            result_data = res.json()['data']
        except KeyError:
            raise ValueError(res.json())

        return result_data

    def verify_email(self, email: str, raw=False) -> Dict[str, Any]:
        """Verify the specified email address using the hunter.io API.

        :param email: The email address to be verified.
        :type email: str

        :param raw: Gives back the entire response instead of just the 'data'.

        :return: A dictionary containing the verification results.
        :rtype: Dict[str, Any]
        """
        request_params = {'email': email, 'api_key': self.api_key}
        endpoint = self.make_endpoint('email-verifier')
        return self.make_request(endpoint, request_params, raw=raw)

    def get_domain_emails(self, domain: str, company: str, raw=False) -> Dict[str, Any]:
        """Retrieve the number of email addresses Hunter has for this domain/company.

        :param domain: The domain address to check

        :param company: The name of company to check

        :param raw: Gives back the entire response instead of just the 'data'.

        :return: A dictionary containing domain/company search data.
        """
        request_params = self.base_params
        if domain:
            request_params['domain'] = domain
        elif company:
            request_params['company'] = company
        endpoint = self.make_endpoint('email-count')
        return self.make_request(endpoint, request_params, raw=raw)
