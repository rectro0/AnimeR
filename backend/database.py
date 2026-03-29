
from sqlalchemy.orm import sessionmaker, Session , declarative_base

from sqlalchemy import create_engine 

db_url = "sqlite:///./app.db"

engine = create_engine(db_url, connect_args={"check_same_thread" :False})
Sessionlocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)

Base = declarative_base()





def get_db():
  db = Sessionlocal()
  try:
    yield db
  finally :
    db.close()                                                                  

