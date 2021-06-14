import hazelcast
from models import Message
from fastapi import FastAPI

app = FastAPI()

uuid_message_map = hazelcast.HazelcastClient().get_map('my_map')


@app.post('/service/', status_code=200)
def post(message: Message):
    uuid_message_map.put(message.uuid, message.msg)
    print(message)


@app.get('/service/')
def get():
    return uuid_message_map.entry_set().result()
