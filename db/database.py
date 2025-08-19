from sqlalchemy import create_engine, Connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import NullPool, QueuePool
from contextlib import contextmanager
from fastapi import status
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
import os

# db connection URL
load_dotenv()

DATABASE_CONN = os.getenv("DATABASE_CONN")

engine = create_engine(DATABASE_CONN,
                       poolclass=QueuePool,
                       #poolclass=NullPool, # Connection Pull 사용 X
                       pool_size=10, max_overflow=10,
                       pool_recycle=3600,
                       )


def direct_get_conn():
    conn = None
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")

def context_get_conn():
    conn = None
    try:
        conn = engine.connect()
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    finally:
        if conn:
            conn.close()