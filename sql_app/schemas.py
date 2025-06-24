from pydantic import BaseModel
from typing import List

class MessageBase(BaseModel):
    sender: str
    content: str

class MessageCreate(MessageBase):
    recipient: str

class Message(MessageBase):
    id: int
    recipient_id: int

    class Config:
        orm_mode = True

class AgentBase(BaseModel):
    name: str

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int
    messages: List[Message] = []

    class Config:
        orm_mode = True 