from sqlalchemy.orm import Session

from . import models, schemas


def get_agent_by_name(db: Session, name: str):
    return db.query(models.Agent).filter(models.Agent.name == name).first()

def create_agent(db: Session, agent: schemas.AgentCreate):
    db_agent = models.Agent(name=agent.name)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def get_messages_for_agent(db: Session, agent_name: str):
    agent = get_agent_by_name(db, name=agent_name)
    if not agent:
        return []
    return agent.messages

def create_agent_message(db: Session, message: schemas.MessageCreate):
    sender_agent = get_agent_by_name(db, name=message.sender)
    recipient_agent = get_agent_by_name(db, name=message.recipient)

    if not sender_agent or not recipient_agent:
        return None
    
    db_message = models.Message(
        sender=message.sender,
        content=message.content,
        recipient_id=recipient_agent.id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def delete_messages_for_agent(db: Session, agent_name: str):
    agent = get_agent_by_name(db, name=agent_name)
    if agent:
        num_deleted = db.query(models.Message).filter(models.Message.recipient_id == agent.id).delete()
        db.commit()
        return num_deleted
    return 0 