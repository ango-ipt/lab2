import random
import uuid
import requests
from models import FacadePostMessage
from fastapi import FastAPI

MESSAGE_HOST = 'http://127.0.0.1:8001/service/'

LOGGING_HOSTS = ('http://127.0.0.1:9001/service/',
                 'http://127.0.0.1:9002/service/',
                 'http://127.0.0.1:9003/service/')


def get_host():
    return random.choice(LOGGING_HOSTS)


app = FastAPI()


@app.get('/facade_service/')
def get():
    logging_response_text = requests.get(get_host()).text.strip('"')
    message_response_text = requests.get(MESSAGE_HOST).text.strip('"')
    return logging_response_text + ': ' + message_response_text


@app.post("/facade_service/", status_code=200)
def post(msg: FacadePostMessage):
    requests.post(url=get_host(), json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})
