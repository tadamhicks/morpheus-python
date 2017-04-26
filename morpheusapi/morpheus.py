import requests
import json
from urlparse import urljoin
from urllib import urlencode


class Morpheus(object):

    def __init__(
            self, baseurl,
            username, password):
        """
        Creating a Morpheus object
        """
        self.username = username
        self.password = password
        self.baseurl = baseurl

        url = urljoin(baseurl, 'oauth')

        access = {
            "grant_type": "password",
            "scope": "write",
            "client_id": "morph-customer"
            }

        url2 = url + '/token?%s' % urlencode(access)

        payload = "username=" + username + "&password=" + password

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-agent': 'curl/7.51.0'
        }

        res = requests.post(url2, data=payload, headers=headers)

        json_response = json.loads(res.text)

        access_token = json_response["access_token"]

        self.access_token = access_token
