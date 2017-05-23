from morpheusapi.morpheus import Morpheus
import json
from urlparse import urljoin
import posixpath
import requests
import six


class Provision_Type(Morpheus):
    def __init__(
            self, baseurl,
            username, password
            ):
    	"""
    	Provision_Type object is a Morpheus object.  Inherits OAuth
    	mechanism.  Wrapper for provision-types endpoint.  All methods
    	are specific provision-types API in morpheus.
    	"""

        Morpheus.__init__(self, baseurl, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token}
        self.endpoint = posixpath.join('api', 'provision-types')

    def get_all(self, id=None):

    	if id:

    		if not isinstance(id, six.string_types):
    			id = str(id)

    		provision_types_url = urljoin(
    						self.baseurl,
    						posixpath.join(self.endpoint, id)
    						)
    	else:
    		
    		provision_types_url = urljoin(
    						self.baseurl,
    						self.endpoint
    						)
    	
    	response = requests.get(provision_types_url, headers=self.headers)

    	return response.text