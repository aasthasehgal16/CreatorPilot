import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base  # ✅ use Base from models ONLY

# Load env variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL =", DATABASE_URL)

# Create engine FIRST
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Create tables AFTER engine is created
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)