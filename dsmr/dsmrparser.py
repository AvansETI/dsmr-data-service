#
# Parser client class.
#
# @author Michel Megens
# @email  michel@michelmegens.net
#

import requests as api
import pprint

class Parser(object):
	def __init__(self, host = "localhost", port = 5000, proto = 'http'):
		self.host = host
		self.port = port
		self.uri  = '%s://%s:%d' % (proto, host, port)
		print("API URI: %s" % self.uri)


	def parse(self, datagram):
		packet = {}
		packet["datagram"] = datagram
		url = "%s/parser?bulk=false" % self.uri
		resp = api.post(url, json=packet)
		rv = {}

		if resp.status_code != 200:
			print("Unable to parse datagram!")
		else:
			rv = resp.json()

		return rv
