from fastapi import FastAPI, Path
from typing import Optional
from student_class import *

app = FastAPI()

students = {
    1:{
        "name": "Jose",
        "age": 19,
        "academic_status": "graduated"
    }, 
    2:{
        "name": "Miguel",
        "age": 17,
        "academic_status": "studying"
    }
}

@app.get("/")
def index():
    return{"message": "returning a message"}

@app.get("/getStudent/{student_id}")
def getStudent(student_id: int = Path(description="Put as a parameter the ID of the student you want to retrieve.", gt=0)):
    return students.get(student_id, "Key does not exist in the dictionary")

#To define a query parameter not required use = None in declaration or use Optional[data type] = None
@app.get("/queryStudent")
def queryStudent(name: str):
    for studentID in students:
        if students[studentID]["name"] == name:
            return students[studentID]
    return {"Data": "Not found"}

@app.post("/createStudent/{student_id}")
def createStudent(student_id: int, student: Student):
    if student_id in students:
        return {"Warning": "The id already exist"}
    students[student_id] = student
    return students[student_id]

@app.put("/updateStudent/{student_id}")
def updateStudent(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Warning": "The Student ID does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.academic_status != None:
        students[student_id].academic_status = student.academic_status
    return students[student_id]

@app.delete("/deleteStudent/{student_id}")
def deleteStudent(student_id: int):
    if student_id not in students:
        return {"Warning": "The key does not exist"}
    del students[student_id]
    return {"Message": "The key was deleted successfully"}