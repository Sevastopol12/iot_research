import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Fetch variables
PASSWORD = os.getenv("password")
DATABASE_URL = f"postgresql+psycopg2://postgres.hkikrgxapozlsyobnsgb:{PASSWORD}@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"


engine = create_engine(
    DATABASE_URL,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
        print(f"Failed to connect: {e}")
        