# Import Required Libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "mysql+mysqlconnector://root:""@localhost/fastapi_crud"

# Create the SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Configure the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()