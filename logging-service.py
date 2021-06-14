from models import Message
from fastapi import FastAPI

app = FastAPI()

uuid_messages = dict()


@app.post('/service/', status_code=200)
def post(message: Message):
    uuid_messages[message.uuid] = message.msg
    print(message)


@app.get('/service/')
def get():
    return '[{}]'.format(', '.join(uuid_messages.values()))
