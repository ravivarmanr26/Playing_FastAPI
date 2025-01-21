from fastapi import FastAPI,HTTPException,Path
from typing import Optional
from pydantic import BaseModel
#initialize the fastapi ,creating object called app
app = FastAPI()


"""
Endpoints are the specific locations on a network where communication occurs. 
They're the destinations, essentially, where data is sent or received, 
making the exchange of information possible.
For example, in the URL https://api.example.com/products, /products is an endpoint that represents a collection of products.
Types of endpoints in restful api : These are part of REST (Representational State Transfer) architecture and use HTTP methods like GET, POST, PUT, and DELETE to interact with resources.
"""

students = {
    1: {
        'name':'steve',
        'reg_no':101,
        'dept':'cse'
    },
    2:{
        'name':'dhoni',
        'reg_no':7,
        'dept':'cricket'
    }
}
##using basemodel creating a data vadilation for input 
class student(BaseModel):
    name:str
    reg_no:int
    dept:str

class Updatestudent(BaseModel):
    name: Optional[str]
    reg_no: Optional[int]  
    dept_no: Optional[str] 

@app.get('/')
def index():
    return "This is an example for get endpoint"

@app.get('/students')
def get_students():
    return students


##path parameter 
@app.get('/students/{student_id}')
def get_single_students(student_id:int =Path(...,description="Enter the id of the student you wants to get") ):
    return students[student_id]

##query parameter
@app.get('/get_by_name')
def get_student_ny_name(name: Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"].lower()==name.lower():
            return students[student_id]
    return "data not found"

##combine the path parameter and query paramets
@app.get('/get_by_name/{student_id}')
def get_student(*,student_id:int,name:Optional[str]=None):
        for student_id in students:
            if students[student_id]["name"]==name:
                return students[student_id]
        return "data not found"

##request body 
##post method
@app.post('/create_student')
def create_record(student_id:int,student:student):
    if student_id in students:
        return "student exists"
    
    students[student_id] = student
    return students[student_id]

###put method 
@app.put('/Update_student/{student_id}')
def Update_record(student_id: int, student: Updatestudent):
    if student_id not in students:
        return "there is no student exists for this id"
    
    if student.name is not None:
        students[student_id]['name'] = student.name

    if student.reg_no is not None:
        students[student_id]['reg_no'] = student.reg_no

    if student.dept_no is not None:
        students[student_id]['dept'] = student.dept_no

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": " Student deleted successfully"}
