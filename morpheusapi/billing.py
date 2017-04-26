from morpheusapi.morpheus import Morpheus
import json
from urlparse import urljoin
from urllib import urlencode
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

    def account(self, id=None):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            account_url = urljoin(
                            self.baseurl,
                            posixpath.join('api', 'billing', 'account', id)
                            )
        else:
            account_url = urljoin(
                            self.baseurl,
                            posixpath.join('api', 'billing', 'account')
                            )

        headers = {"Authorization": "BEARER " + self.access_token}

        response = requests.get(account_url, headers=headers)

        bill_info = json.loads(response.text)

        return bill_info

    def zones(self, id=None):

