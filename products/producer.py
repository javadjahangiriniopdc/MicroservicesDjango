import pika, json

params = pika.URLParameters('amqps://qoxfvjud:NIVY3oxxLpCGNKprPXxaUSf85UqFHURT@clam.rmq.cloudamqp.com/qoxfvjud')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
