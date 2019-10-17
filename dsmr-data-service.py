#!/usr/bin/env python

from dsmr import mqttclient as mqtt

if __name__ == "__main__":
	client = mqtt.MqttClient()
	client.run("broker.hivemq.com", 1883)