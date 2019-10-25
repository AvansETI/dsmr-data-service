#!/usr/bin/env python

from dsmr import mqttclient as mqtt

if __name__ == "__main__":
	client = mqtt.MqttClient()
	client.run("sendlab.avansti.nl", 11883, "smartmeter_admin", "s3_sm4rtm3t3r")
