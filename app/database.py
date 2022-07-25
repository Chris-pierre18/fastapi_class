from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote as urlquote
import psycopg2
from psycopg2.extras import RealDictCursor

from config import Settings

SQLALCHEMY_DATABASE_URL= f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}/{Settings.database_name}'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Cr7@madrid',
#         cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("database connection as succesfull")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("error:",error)

