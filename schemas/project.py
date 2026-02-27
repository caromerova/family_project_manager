from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    owner_id: int

    class Config:
        from_attributes = True
