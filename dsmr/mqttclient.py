#
# MQTT client handler.
#
# @author Michel Megens
# @email  michel@michelmegens.net
#

import paho.mqtt.client as mqtt
import dsmr as parser
import json
import pprint

class MqttClient(mqtt.Client):
	def on_connect(self, mqttc, obj, flags, rc):
		print("MQTT connected - Rc: " + str(rc))

	def on_message(self, mqttc, obj, msg):
		print("TOPIC: " + str(msg.topic))
		if str(msg.topic) != "smartmeter/raw":
			return

		payload = str(msg.payload)
		json_payload = json.loads(payload)
		datagram = json_payload["datagram"]
		signature = json_payload["signature"]

		if datagram == None:
			return

		if signature == None:
			return

		parsed = self.parser.parse(datagram)
		parsed["signature"] = signature
		self.publish("smartmeter/log", json.dumps(parsed))


	def run(self, host, port, user = None, passw = None):
		if user != None and passw != None:
			self.username_pw_set(user, passw)

		self.connect(host, port)
		self.parser = parser.Parser()
		self.subscribe("smartmeter/raw")

		rc = 0

		while rc == 0:
			rc = self.loop()

		return rc