from pydantic import BaseModel

class FacadePostMessage(BaseModel):
    msg: str


class Message(BaseModel):
    uuid: str
    msg: str
