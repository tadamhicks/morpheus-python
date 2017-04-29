from morpheusapi.morpheus import Morpheus
import json
from urlparse import urljoin
import posixpath
import requests
import six


class Instances(Morpheus):
    def __init__(
            self, baseurl,
            username, password):

        Morpheus.__init__(self, baseurl, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token}
        self.endpoint = posixpath.join('api', 'instances')

    def instances(self, id=None):

        if id:

            if not isinstance(id, six.string_types):
                id = str(id)

            instances_url = urljoin(
                                self.baseurl,
                                posixpath.join(self.endpoint, id)
                            )
        else:

            instances_url = urljoin(self.baseurl, self.endpoint)

        response = requests.get(instances_url, headers=self.headers)

        instances_info = json.loads(response.text)

        return instances_info
