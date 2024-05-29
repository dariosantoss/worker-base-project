import pika
from app.config import settings

def consume():
    connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')

    def callback(ch, method, properties, body):
        print(f"Received {body}")

        # Processamento de mensagens
        # Você pode adicionar lógica para interagir com os bancos de dados aqui

    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
