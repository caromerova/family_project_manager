from fastapi import FastAPI
from config.database import engine
from models import user
from models import project
from routers import auth
from routers import users
from routers import projects

app = FastAPI(title="Family Project Manager")

user.Base.metadata.create_all(bind=engine)
project.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "Family Project Manager Running 🚀"}

