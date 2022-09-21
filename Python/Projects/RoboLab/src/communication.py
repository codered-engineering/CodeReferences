#!/usr/bin/env python3

# Attention: Do not import the ev3dev.ev3 module in this file
import json
import platform
import ssl
import time

# Fix: SSL certificate problem on macOS
if all(platform.mac_ver()):
    from OpenSSL import SSL


class Communication:
    """
    Class to hold the MQTT client communication
    Feel free to add functions and update the constructor to satisfy your requirements and
    thereby solve the task according to the specifications
    """

    def __init__(self, mqtt_client, logger, robot, planet):
        """
        Initializes communication module, connect to server, subscribe, etc.
        :param mqtt_client: paho.mqtt.client.Client
        :param logger: logging.Logger
        """
        # DO NOT CHANGE THE SETUP HERE
        self.client = mqtt_client
        self.client.tls_set(tls_version=ssl.PROTOCOL_TLS)
        self.client.on_message = self.safe_on_message_handler
        # Add your client setup here
        self.client.username_pw_set('218', password='P2yOzAApFC')
        self.client.connect('mothership.inf.tu-dresden.de', port=8883)
        self.client.subscribe('explorer/218', qos=1)

        self.logger = logger
        self.robot = robot
        self.planet = planet

        self.planet_name = None


    # DO NOT EDIT THE METHOD SIGNATURE
    def on_message(self, client, data, message):
        """
        Handles the callback if any message arrived
        :param client: paho.mqtt.client.Client
        :param data: Object
        :param message: Object
        :return: void
        """
        payload = json.loads(message.payload.decode('utf-8'))
        self.logger.debug(json.dumps(payload, indent=2))

        # YOUR CODE FOLLOWS (remove pass, please!)
        if payload['from'] == 'server' or payload['from'] == 'debug':
            self.read_message(payload)

    # DO NOT EDIT THE METHOD SIGNATURE
    #
    # In order to keep the logging working you must provide a topic string and
    # an already encoded JSON-Object as message.
    def send_message(self, topic, message):
        """
        Sends given message to specified channel
        :param topic: String
        :param message: Object
        :return: void
        """
        self.logger.debug('Send to: ' + topic)
        self.logger.debug(json.dumps(message, indent=2))

        # YOUR CODE FOLLOWS (remove pass, please!)
        self.client.publish(topic, json.dumps(message), qos=1)

    # DO NOT EDIT THE METHOD SIGNATURE OR BODY
    #
    # This helper method encapsulated the original "on_message" method and handles
    # exceptions thrown by threads spawned by "paho-mqtt"
    def safe_on_message_handler(self, client, data, message):
        """
        Handle exceptions thrown by the paho library
        :param client: paho.mqtt.client.Client
        :param data: Object
        :param message: Object
        :return: void
        """
        try:
            self.on_message(client, data, message)
        except:
            import traceback
            traceback.print_exc()
            raise


    # Read all types of messages sent from Server
    def read_message(self, message):
        
        if message['type'] == 'planet':
            self.planet_name = message['payload']['planetName']
            self.robot.start_x = message['payload']['startX']
            self.robot.start_y = message['payload']['startY']
            self.robot.start_direction = message['payload']['startOrientation']
            # inititate end coordinates for the second node
            self.robot.end_x = self.robot.start_x
            self.robot.end_y = self.robot.start_y
            self.client.subscribe("planet/{}/218".format(self.planet_name))

        elif message['type'] == 'path':
            self.robot.start_x = message['payload']['startX']
            self.robot.start_y = message['payload']['startY']
            self.robot.start_direction = message['payload']['startDirection']
            self.robot.end_x = message['payload']['endX']
            self.robot.end_y = message['payload']['endY']
            self.robot.end_direction = message['payload']['endDirection']
            self.robot.path_status = message['payload']['pathStatus']
            self.robot.path_weight = message['payload']['pathWeight']

            if self.robot.path_status == 'blocked':
                self.robot.path_weight = -1

            self.planet.add_path(
                ((self.robot.start_x, self.robot.start_y), self.robot.start_direction),
                ((self.robot.end_x, self.robot.end_y), self.robot.end_direction),
                self.robot.path_weight
            )


        elif message['type'] == 'pathSelect':
            if self.robot.start_direction != message['payload']['startDirection']:
                self.robot.start_direction = message['payload']['startDirection']

        elif message['type'] == 'pathUnveiled':
            start_x = message['payload']['startX']
            start_y = message['payload']['startY']
            start_direction = message['payload']['startDirection']
            end_x = message['payload']['endX']
            end_y = message['payload']['endY']
            end_direction = message['payload']['endDirection']
            path_status = message['payload']['pathStatus']
            path_weight = message['payload']['pathWeight']

            if path_status == 'blocked':
                path_weight = -1
                
            self.planet.add_path(
                ((start_x, start_y), start_direction),
                ((end_x, end_y), end_direction),
                path_weight
            )



        elif message['type'] == 'target':
            self.robot.target_x = message['payload']['targetX']
            self.robot.target_y = message['payload']['targetY']

        elif message['type'] == 'done':
            print(message['payload']['message'])
 

    # All send-functions
    def send_testplanet(self, planet_name):
        msg = {
            "from": "client",
            "type": "testplanet",
            "payload": {
                "planetName": planet_name
            }
        }
        self.send_message("explorer/218", msg)
        time.sleep(3)

    def send_ready(self):
        msg = {
            "from": "client",
            "type": "ready"
        }
        self.send_message('explorer/218', msg)
        time.sleep(3)

    def send_path_select(self, start_x, start_y, direction):
        msg = {
            "from": "client",
            "type": "pathSelect",
            "payload": {
                "startX": start_x,
                "startY": start_y,
                "startDirection": direction
            }
        }
        topic = ("planet/{}/218".format(self.planet_name))
        self.send_message(topic, msg)
        time.sleep(3)

    def send_path(self):
        msg = {
            "from": "client",
            "type": "path",
            "payload": {
                "startX": self.robot.start_x,
                "startY": self.robot.start_y,
                "startDirection": self.robot.start_direction,
                "endX": self.robot.end_x,
                "endY": self.robot.end_y,
                "endDirection": self.robot.end_direction,
                "pathStatus": self.robot.path_status
            }
        }
        topic = ("planet/{}/218".format(self.planet_name))
        self.send_message(topic, msg)
        time.sleep(3)

    def send_target_reached(self):
        msg = {
            "from": "client",
            "type": "targetReached",
            "payload": {
                "message": "Target is reached"
            }
        }
        self.send_message('explorer/218', msg)
        time.sleep(3)

    def send_exploration_completed(self):
        msg = {
            "from": "client",
            "type": "explorationCompleted",
            "payload": {
                "message": "Exploration is completed"
            }
        }
        self.send_message('explorer/218', msg)
        time.sleep(3)
