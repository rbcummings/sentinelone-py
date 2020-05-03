#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ________                               .___       _________            .___
# \______ \_______   ____ _____    _____ |   | ____ \_   ___ \  ____   __| _/____
#  |    |  \_  __ \_/ __ \\__  \  /     \|   |/    \/    \  \/ /  _ \ / __ |/ __ \
#  |    `   \  | \/\  ___/ / __ \|  Y Y  \   |   |  \     \___(  <_> ) /_/ \  ___/
# /_______  /__|    \___  >____  /__|_|  /___|___|  /\______  /\____/\____ |\___  >
#         \/            \/     \/      \/         \/        \/            \/    \/
#                              DreamInCode.io

"""A Python class that provides methods for easily interacting with the SentinelOne API"""

__author__     = 'Brandon Cummings'
__copyright__  = 'Copyright 2020, Brandon Cummings'
__credits__    = ['Brandon Cummings']
__license__    = 'MIT'
__version__    = '1.0.0'
__maintainer__ = 'Brandon Cummings'
__email__      = 'brandon@dreamincode.io'
__status__     = 'Production'

import requests, json

class api():
    """
    A class used to represent the SentinelOne API

    Attributes
    ----------
    subdomain : str, required
        The subdomain for your account
    credentials : dict, required
        The credentials used to connect to your SentinelOne account
    site_ids : list, optional
        The site IDs to limit requests to
    headers : dict, required
        The headers to send with your requests for authentication

    Methods
    -------
    get(self, endpoint, parameters = None)
        Performs a GET request using the specified endpoint and parameters
    put(self, endpoint, parameters = None, body = None)
        Performs a POST request using the specified endpoint, parameters and body
    post(self, endpoint, parameters = None, body = None)
        Performs a PUT request using the specified endpoint, parameters and body
    """

    def __init__(self, subdomain, credentials, site_ids = None):
        """Define the basics for API interaction and authenticate with the API

        Parameters
        ----------
        subdomain : str, required
            The subdomain for your SentinelOne account
        credentials : dict, required
            The credentials used to connect to your SentinelOne account
        siteid : str, optional
            The site ID to limit requests to
        """

        # The base instance variables
        self.subdomain = subdomain
        self.credentials = credentials
        self.site_ids = site_ids
        self.headers = None

        if 'apiKey' in credentials.keys():
            parameters = {
                'data': {
                    'apiToken': self.credentials['apiKey'],
                },
            }
            response = requests.post(self.request_url('/web/api/v2.0/users/login/by-api-token'), json = parameters)
        else:
            parameters = {
                'username': self.credentials['username'],
                'password': self.credentials['password'],
            }
            response = requests.post(self.request_url('/web/api/v2.0/users/login/by-api-token'), body = None, json = parameters)

        response = response.json()

        self.headers = {
            'Authorization': 'Token %s' %(response['data']['token']),
            'Content-Type': 'application/json',
        }

    def request_url(self, endpoint):
        """Builds a request URL given the class attributes and provided endpoint path

        Parameters
        ----------
        endpoint : str, required
            The API endpoint path used for the request

        Returns
        -------
        string
            A request URL
        """

        request_url = 'https://' + str(self.subdomain) + '.sentinelone.net' + str(endpoint)

        return request_url

    def get(self, endpoint, parameters = None):
        """Performs an HTTP GET request to the provided endpoint

        Parameters
        ----------
        endpoint : str, required
            The API endpoint path used for the request
        parameters : dict, optional
            The paramaters to send with your request

        Returns
        -------
        string
            A JSON string containing the response for your GET request
        """

        if not self.site_ids == None:
            parameters.update({'siteIds': '"'+",".join(self.site_ids)+'"'})

        response = requests.get(self.request_url(endpoint), params = parameters, headers = self.headers)

        response = response.json()

        return response

    def post(self, endpoint, parameters = None, body = None):
        """Performs an HTTP POST request to the provided endpoint

        Parameters
        ----------
        endpoint : str, required
            The API endpoint path used for the request
        parameters : dict, optional
            The paramaters to send with your request
        body : dict, optional
            The body to send with your request

        Returns
        -------
        string (JSON)
            A JSON string containing the response for your POST request
        """

        if not self.site_ids == None:
            parameters.update({'siteIds': '"'+",".join(self.site_ids)+'"'})

        response = requests.post(self.request_url(endpoint), params = parameters, body = body, headers = self.headers)

        response = response.json()

        return response

    def put(self, endpoint, parameters = None, body = None):
        """Performs an HTTP POST request to the provided endpoint

        Parameters
        ----------
        endpoint : str, required
            The API endpoint path used for the request
        parameters : dict, optional
            The paramaters to send with your request
        body : dict, optional
            The body to send with your request

        Returns
        -------
        string (JSON)
            A JSON string containing the response for your POST request
        """

        if not self.site_ids == None:
            parameters.update({'siteIds': '"'+",".join(self.site_ids)+'"'})

        response = requests.put(self.request_url(endpoint), params = parameters, body = body, headers = self.headers)

        response = response.json()

        return response
