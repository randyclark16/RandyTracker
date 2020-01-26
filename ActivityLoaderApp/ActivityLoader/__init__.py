import json
import logging
import os, sys
import pymongo
from pymongo import MongoClient


import azure.functions as func


def main(msg: func.ServiceBusMessage):
    try:
        logging.info('Python ServiceBus queue trigger processed message: %s',
                    msg.get_body().decode('utf-8'))
        message = msg.get_body().decode('utf-8')
        message_json = json.loads(message)
        first_name = message_json.get('firstName')
        print ("firstName = {}".format(first_name))

        connection_string = os.environ.get("MongoDBAtlasConnectString")
        print (connection_string)
        client = pymongo.MongoClient(connection_string)
        db = client.tracker_database
        items_collection = db.items
        items_collection_id = items_collection.insert_one(message_json).inserted_id
        print (items_collection_id)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise    