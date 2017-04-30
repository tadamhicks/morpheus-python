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

    def get_instances(self, id=None, ids=False):

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

        if ids:

            json_data = json.loads(response.text)

            instance_list = []

            for instance in json_data["instances"]:
                instance_list.append(instance["id"])

            return json.dumps(instance_list)

        else:

            return response.text

    def get_instance_env(self, id):

        if not isinstance(id, six.string_types):
            id = str(id)

        env_url = urljoin(
                    self.baseurl,
                    posixpath.join(self.endpoint, id, 'envs')
                    )

        response = requests.get(env_url, headers=self.headers)

        return response.text
