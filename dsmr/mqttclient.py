#
# MQTT client handler.
#
# @author Michel Megens
# @email  michel@michelmegens.net
#

import paho.mqtt.client as mqtt
from dsmr.dsmrparser import Parser
import json
import pprint

class MqttClient(mqtt.Client):
	def on_connect(self, mqttc, obj, flags, rc):
		print("MQTT connected - Rc: " + str(rc))

	def on_message(self, mqttc, obj, msg):
		print("TOPIC: " + str(msg.topic))

		if str(msg.topic) != "smartmeter/raw":
			print("Invalid topic!")
			return

		json_payload = json.loads(msg.payload)
		datagram = json_payload["datagram"]
		signature = json_payload["signature"]
		if datagram == None:
			print("Invalid packet: no datagram present!")
			return

		if signature == None:
			print("Invalid packet: no signature present!")
			return
		parsed = self.dsmrParser.parse(datagram)
		parsed["signature"] = signature
		self.publish("smartmeter/log", json.dumps(parsed))


	def run(self, host, port, user = None, passw = None):
		if user != None and passw != None:
			self.username_pw_set(user, passw)

		self.connect(host, port)
		self.dsmrParser = Parser()
		self.subscribe("smartmeter/raw")

		rc = 0

		while rc == 0:
			rc = self.loop()

		return rc
