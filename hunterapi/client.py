"""Module for client."""

from typing import Any, Dict

import requests


class HunterClient(object):
    """Class for interacting with the hunter.io API."""

    def __init__(self, api_key: str):
        """Initialize the HunterClient with the specified API key."""
        self.api_key = api_key
        self.base_endpoint = 'https://api.hunter.io/v2/'

    def make_request(self, endpoint: str, request_params: dict, request_type='get', raw=False) -> Dict[str, Any]:
        """Make a request to the hunter.io API."""
        request_kwargs = {'params': request_params}
        endpoint = self.base_endpoint + endpoint
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
        """Verify the specified email address using the hunter.io API."""
        request_params = {'email': email, 'api_key': self.api_key}
        return self.make_request(endpoint='email-verifier', request_params=request_params, raw=raw)

    def get_domain_emails(self, domain: str, company: str, raw=False) -> Dict[str, Any]:
        """Retrieve the number of email addresses Hunter has for this domain/company."""
        request_params = {'api_key': self.api_key}
        if domain:
            request_params['domain'] = domain
        elif company:
            request_params['company'] = company
        return self.make_request(endpoint='email-count', request_params=request_params, raw=raw)
