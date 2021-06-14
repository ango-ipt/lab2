import uuid
import requests
from models import FacadePostMessage
from fastapi import FastAPI

MESSAGE_SERVICE = 'http://127.0.0.1:8001/service/'
LOGGING_SERVICE = 'http://127.0.0.1:8002/service/'

app = FastAPI()


@app.get('/facade_service/')
def get():
    message_response_text = requests.get(MESSAGE_SERVICE).text.strip('"')
    logging_response_text = requests.get(LOGGING_SERVICE).text.strip('"')
    return logging_response_text + ': ' + message_response_text


@app.post("/facade_service/", status_code=200)
def post(msg: FacadePostMessage):
    requests.post(url=LOGGING_SERVICE, json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})
