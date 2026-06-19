#importando ferramentas do SQLALCHEMY(ORM)
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#linha de conexão(URL)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/todo_api"

#criando o motor(engine) e a fabrica de sessões(SessionLocal)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#fução para gerenciar as conexões
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()