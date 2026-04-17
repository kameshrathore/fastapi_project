from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    age: int
    department: str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
