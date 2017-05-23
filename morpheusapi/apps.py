from morpheusapi.morpheus import Morpheus
import json
from urlparse import urljoin
import posixpath
import requests
import six


class App(Morpheus):

    def __init__(
            self, baseurl,
            username, password
            ):

        Morpheus.__init__(self, baseurl, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token}
        self.endpoint = posixpath.join('api', 'provision-types')