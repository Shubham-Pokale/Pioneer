from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    messages = relationship("Message", back_populates="recipient")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, index=True)
    content = Column(String)
    recipient_id = Column(Integer, ForeignKey("agents.id"))

    recipient = relationship("Agent", back_populates="messages") 