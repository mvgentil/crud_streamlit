from fastapi import FastAPI
from db.database import engine
from  models.models import Base
from router.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)