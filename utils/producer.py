import pika
from django.core import serializers
from django.conf import settings

URL = settings.RMQ_URL


def produce(s):
    params = pika.URLParameters(URL)
    params.socket_timeout = s.waitTime
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=settings.RMQ_QUEUE, durable=True)
    channel.basic_publish(exchange=settings.RMQ_EXCHANGE, routing_key=settings.ROUTING_KEY, body=serializers.serialize('json', [s, ]))
    connection.close()
    return s.pingUrl
