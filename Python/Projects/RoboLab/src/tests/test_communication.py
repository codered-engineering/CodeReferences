#!/usr/bin/env python3

import unittest.mock
import paho.mqtt.client as mqtt
import uuid
import json
import logging

from communication import Communication


class TestRoboLabCommunication(unittest.TestCase):
    def setUp(self):
        """
        Instantiates the communication class
        """
        client_id = '218-' + str(uuid.uuid4())  # Replace YOURGROUPID with your group ID
        client = mqtt.Client(client_id=client_id,  # Unique Client-ID to recognize our program
                             clean_session=False,  # We want to be remembered
                             protocol=mqtt.MQTTv311  # Define MQTT protocol version
                             )

        # Initialize your data structure here
        self.communication = Communication(client, logging)

    def test_message_ready(self):
        """
        This test should check the syntax of the message type "ready"
        """
        with self.assertLogs(level='DEBUG') as cm:
            self.communication.send_ready()
            for s in cm.output:
                if s.startswith('DEBUG:root:{'):
                    log_msg = s.replace('DEBUG:root:', '')
        self.assertEqual(
            {
                "from": "client",
                "type": "ready"
            }, json.loads(log_msg))

    def test_message_path(self):
        """
        This test should check the syntax of the message type "path"
        """
        with self.assertLogs(level='DEBUG') as cm:
            self.communication.send_path()
            for s in cm.output:
                if s.startswith('DEBUG:root:{'):
                    log_msg = s.replace('DEBUG:root:', '')
        self.assertEqual(
            {
                "from": "client",
                "type": "path",
                "payload": {
                    "startX": None,
                    "startY": None,
                    "startDirection": None,
                    "endX": None,
                    "endY": None,
                    "endDirection": None,
                    "pathStatus": None
                }
            }, json.loads(log_msg))

    def test_message_path_invalid(self):
        """
        This test should check the syntax of the message type "path" with errors/invalid data
        """
        with self.assertLogs(level='DEBUG') as cm:
            self.communication.send_path()
            for s in cm.output:
                if s.startswith('DEBUG:root:{'):
                    log_msg = s.replace('DEBUG:root:', '')
        self.assertEqual(
            {
                "from": "client",
                "type": "path",
                "payload": {
                    "startX": None,
                    "startY": None,
                    "startDirection": None,
                    "endX": None,
                    "endY": None,
                    "endDirection": None,
                    "pathStatus": None
                }
            }, json.loads(log_msg))

    def test_message_select(self):
        """
        This test should check the syntax of the message type "pathSelect"
        """
        with self.assertLogs(level='DEBUG') as cm:
            self.communication.send_path_select(0, 0, 0)
            for s in cm.output:
                if s.startswith('DEBUG:root:{'):
                    log_msg = s.replace('DEBUG:root:', '')
        self.assertEqual(
            {
                "from": "client",
                "type": "pathSelect",
                "payload": {
                    "startX": 0,
                    "startY": 0,
                    "startDirection": 0
                }
            }, json.loads(log_msg))

    def test_message_complete(self):
        """
        This test should check the syntax of the message type "explorationCompleted" or "targetReached"
        """
        with self.assertLogs(level='DEBUG') as cm:
            self.communication.send_target_reached()
            for s in cm.output:
                if s.startswith('DEBUG:root:{'):
                    log_msg = s.replace('DEBUG:root:', '')
        self.assertEqual(
            {
                "from": "client",
                "type": "targetReached",
                "payload": {
                    "message": "Target is reached"
                }
            }, json.loads(log_msg))


if __name__ == "__main__":
    unittest.main()
