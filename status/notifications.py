import pika

def send_notification(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=message)
    connection.close()
    
send_notification('Flight AA123 has been delayed')
