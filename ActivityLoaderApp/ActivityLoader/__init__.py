import json
import logging
import os, sys

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    message = msg.get_body().decode('utf-8')
    message_json = json.loads(message)
    first_name = message_json.get('firstName')
    print ("firstName = {}".format(first_name))

    connection_string = os.environ.get("MongoDBAtlasConnectString")
    print (connection_string)