from pydantic import BaseModel, ConfigDict, Field

class StudentBase(BaseModel):
    id: str
    name: str
    branch: str
    cgpa: float = Field(ge=0, le=10)

class StudentCreate(StudentBase):
    model_config = ConfigDict(extra="forbid")


class StudentUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    branch: str
    cgpa: float= Field(ge=0, le=10)

class StudentPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = None
    branch: str | None = None
    cgpa: float | None = Field(default=None, ge=0, le=10)