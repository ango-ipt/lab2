import random
import uuid
import requests
import pika
from models import FacadePostMessage
from fastapi import FastAPI

MESSAGE_HOSTS = ('http://127.0.0.1:8001/service/',
                 'http://127.0.0.1:8002/service/')

LOGGING_HOSTS = ('http://127.0.0.1:9001/service/',
                 'http://127.0.0.1:9002/service/',
                 'http://127.0.0.1:9003/service/')


def get_log_host():
    return random.choice(LOGGING_HOSTS)


def get_msg_host():
    return random.choice(MESSAGE_HOSTS)


def put_msg_mq(msg):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='lab6')
    channel.basic_publish(exchange='', routing_key='lab6', body=msg)
    connection.close()


app = FastAPI()


@app.get('/facade_service/')
def get():
    logging_response_text = requests.get(get_log_host()).text.strip('"')
    message_response_text = requests.get(get_msg_host()).text.strip('"')
    return logging_response_text + ': ' + message_response_text


@app.post("/facade_service/", status_code=200)
def post(msg: FacadePostMessage):
    requests.post(url=get_log_host(), json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})
    put_msg_mq(msg.msg)
