# This script connects to a PostgreSQL database using SQLAlchemy and psycopg2.       
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
from sqlalchemy import text  # Import the text function

# Test the database connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))  # Wrap the SQL string in text()
    print(result.fetchone())