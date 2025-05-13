import datetime
from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import sys
sys.path.append('../')
from config import DATABASE_PORT,MYSQL_DATABASE,MYSQL_USER,MYSQL_PASSWORD,MYSQL_HOST

# SQLAlchemyの接続用文字列
CONNECT_STRING = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{DATABASE_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
Base = declarative_base()

#データベースに接続するためのセッションを作成する
def create_connect_session():
    try: 
        engine = create_engine(CONNECT_STRING)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(e)
        return None

#テーブルの一覧を表示する
def show_tables():
    try:
        engine = create_engine(CONNECT_STRING)
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        for table in tables:
            print(table)
    except Exception as e:
        print(e)