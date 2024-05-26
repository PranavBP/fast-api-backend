from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://postgres:pranav@localhost:5433/QuizApplication"

# To create an engine with the database URL
engine = create_engine(URL_DATABASE)

# This is the sessionlocal class. -> This class itseld is not a database session
# when we use the instance of this class that is the actual database session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()