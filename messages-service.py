from fastapi import FastAPI

app = FastAPI()


@app.get('/service/')
def get():
    return 'message-service is not implemented yet'
