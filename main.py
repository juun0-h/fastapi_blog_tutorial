from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import blog
from contextlib import asynccontextmanager
from db.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("#######Starting up...")
    yield
    
    # Shutdown
    print("#######Shutting down...")
    await engine.dispose()
    
app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(blog.router)