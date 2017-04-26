from morpheusapi.morpheus import Morpheus
import json
from urlparse import urljoin
import posixpath
import requests
import six


class Billing(Morpheus):
    def __init__(
            self, baseurl,
            username, password,
            id=None):
        self.id = id
        Morpheus.__init__(self, baseurl, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token}
        self.endpoint = posixpath.join('api', 'billing')

    def account(self, id=None):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            account_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'account', id)
                            )
        else:
            account_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'account')
                            )

        response = requests.get(account_url, headers=self.headers)

        bill_info = json.loads(response.text)

        return bill_info

    def zones(self, id=None):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            zone_url = urljoin(
                        self.baseurl,
                        posixpath.join(self.endpoint, 'zones', id)
                        )
        else:

            zone_url = urljoin(
                        self.baseurl,
                        posixpath.join(self.endpoint, 'zones')
                        )

        response = requests.get(zone_url, headers=self.headers)

        zone_info = json.loads(response.text)

        return zone_info

    def servers(self, id=None):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            servers_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'servers', id)
                            )
        else:

            servers_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'servers')
                            )

            response = requests.get(servers_url, headers=self.headers)

            servers_info = json.loads(response.text)

            return servers_info
