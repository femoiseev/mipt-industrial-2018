import pika
from pymongo import MongoClient

MONGO_DB = 'Test'

client = MongoClient(host='mongo')

client.drop_database('MONGO_DB')
db = client[MONGO_DB]
db.drop_collection('messages')


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    db.messages.save({ 'message' : body.decode() })

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
