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
        """
        Billing object is a Morpheus object.  Inherits OAuth mechanism.
        This object is a wrapper for the billing endpoint.  All methods
        are specific to billing.
        """
        self.id = id
        Morpheus.__init__(self, baseurl, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token}
        self.endpoint = posixpath.join('api', 'billing')

    def get_account(self, id=None):

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

        return response.json()

    def get_zones(self, id=None):

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

        return response.json()

    def get_servers(self, id=None):

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

            return response.json()

    def get_instances(self, id=None, ids=False):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            instances_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'instances', id)
                            )
        else:

            instances_url = urljoin(
                            self.baseurl,
                            posixpath.join(self.endpoint, 'instances')
                            )

            response = requests.get(instances_url, headers=self.headers)

            if ids:

                json_data = response.json()

                instance_list = []

                for instance in json_data["billingInfo"]["instances"]:
                    instance_list.append(instance["instanceId"])

                return json.dumps(instance_list)

            else:

                return response.json()
