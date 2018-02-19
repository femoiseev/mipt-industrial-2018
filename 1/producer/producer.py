import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = None

while True:
	try:
		message = input('> ')
	except EOFError:
		break

	channel.basic_publish(exchange='', routing_key='hello', body=message)

connection.close()
