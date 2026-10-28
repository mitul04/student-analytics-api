from pydantic import BaseModel, RootModel, ConfigDict, Field

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


class StudentDetail(BaseModel):
    student: StudentBase
    branch_average: float
    difference_from_branch_average: float
    branch_rank: int


class StudentDelete(BaseModel):
    student: StudentBase
    message: str


class StudentsSummary(BaseModel):
    branch_count: dict[str, int]
    total_students: int
    average_cgpa: float | None
    max_cgpa: float | None
    min_cgpa: float | None


class BranchSummary(BaseModel):
    total_students: int
    average_cgpa: float | None
    max_cgpa: float | None
    min_cgpa: float | None


class BranchwiseSummary(RootModel[dict[str, BranchSummary]]):
    pass


class CGPADistribution(BaseModel):
    branch: str
    total_students: int
    range_0_6: int = Field(alias="0_6")
    range_6_7: int = Field(alias="6_7")
    range_7_8: int = Field(alias="7_8")
    range_8_9: int = Field(alias="8_9")
    range_9_10: int = Field(alias="9_10")