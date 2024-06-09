from confluent_kafka import Consumer
from pymongo import MongoClient
import requests
import json
import ast

c = Consumer({
    'bootstrap.servers': '172.34.0.19:9092',
    'group.id': 'dataengineering',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['dataengineringportfolio'])
# Create a MongoDB client
connection_string = 'mongodb://bahati2:bahati2@172.34.0.22:27017/farmers'
client = MongoClient(connection_string)
db = client['farmers']
collection = db['mycollection']

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    data=ast.literal_eval(msg.value().decode('utf-8'))
    print(data)
    # Insert the data into the MongoDB collection
    collection.insert_one(data)
    #print("Data consumed from 'mytopic' and inserted into 'mycollection' in 'mydatabase'")

c.close()