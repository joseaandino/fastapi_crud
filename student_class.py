from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    academic_status: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    academic_status: Optional[str] = None

