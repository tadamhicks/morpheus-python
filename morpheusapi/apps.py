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


    def get_apps(self, id=None):
    	
    	if id:

    		if not isinstance(id, six.string_types):
    			id = str(id)

    		apps_url = urljoin(
    						self.baseurl,
    						posixpath.join(self.endpoint, id)
    					)

    	else:

    		apps_url = urljoin(self.baseurl, self.endpoint)

    	response = requests.get(apps_url, headers=self.headers)

    	return response.json()
