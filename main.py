from fastapi import FastAPI
from config.database import engine
from models import user
from routers import auth

app = FastAPI(title="Family Project Manager")

user.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Family Project Manager Running 🚀"}

