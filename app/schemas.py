
from pydantic import BaseModel, ConfigDict, Field


class JobCreate(BaseModel):
    task_name: str = Field(min_length=1, max_length=200)


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    task_name: str
    status: str
