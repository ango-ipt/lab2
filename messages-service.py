from fastapi import FastAPI
import pika
import threading


def run_in_thread(fn):
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.start()
        return t

    return run


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    messages.append(body)
    print(body)


@run_in_thread
def consume_loop(msg_list):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='lab6')
    for method_frame, properties, body in channel.consume('lab6'):
        print(str(body))
        msg_list.append(str(body))


messages = []
consume_loop(messages)
app = FastAPI()


@app.get('/service/')
def get():
    return messages
