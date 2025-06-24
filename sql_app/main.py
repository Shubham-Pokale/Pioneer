from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.Agent)
def register_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    db_agent = crud.get_agent_by_name(db, name=agent.name)
    if db_agent:
        raise HTTPException(status_code=400, detail="Agent name already registered")
    return crud.create_agent(db=db, agent=agent)

@app.post("/send")
def send_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = crud.create_agent_message(db=db, message=message)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Sender or recipient not registered")
    return {"message": "Message sent."}

@app.get("/messages/{agent_name}", response_model=List[schemas.Message])
def get_messages(agent_name: str, db: Session = Depends(get_db)):
    db_agent = crud.get_agent_by_name(db, name=agent_name)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not registered")
    
    messages = crud.get_messages_for_agent(db, agent_name=agent_name)
    # Clear messages after retrieval
    crud.delete_messages_for_agent(db, agent_name=agent_name)
    
    return messages 