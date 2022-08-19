from optparse import Option
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI() # instance of fastapi

para = 404

students = {
    1: {
        "name": "john",
        "age": 17,
        "class_": "year 12"
    },
    2: {
        "name": "erica",
        "age": 20,
        "class_": "distance english"
    }
}

class Student(BaseModel):
    name: str
    age: int
    class_: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_: Optional[str] = None

@app.get('/')
def index():
    return {"name": "Rowan Hudson"}

# greeting function
@app.get('/greet')
def index():
    return "<h1>Hello World! from fast API - {}</h1>".format(para)

# get student by ID and path parameters
@app.get('/get-student/{student_id}')
def index(student_id: int = Path(None, description="The ID of the student you want to view"), gt=0, lt=3):
    return students[student_id]

# get student by ID and query parameters    # google.com/results?search=Python
@app.get('/get-student-by-name/{student_id}')
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exits"}
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exit"}
    if student.name != None:
        students[student_id] = student.name
    if student.age != None:
        students[student_id] = student.age
    if student.class_ != None:
        students[student_id] = student.class_
    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exit"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}