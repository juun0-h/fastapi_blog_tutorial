from sqlalchemy import create_engine, Connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
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
print(f"Database connection URL: {DATABASE_CONN}")

engine: AsyncEngine = create_async_engine(DATABASE_CONN, echo=True,
                       # poolclass=QueuePool, # async_engine 사용 시 QueuePool 사용 불가
                       # poolclass=NullPool, # Connection Pull 사용 X
                       pool_size=10, max_overflow=10,
                       pool_recycle=3600,
                       )


async def direct_get_conn():
    conn = None
    try:
        conn = await engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")

async def context_get_conn():
    conn = None
    try:
        conn = await engine.connect()
        yield conn
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    finally:
        if conn:
            await conn.close()