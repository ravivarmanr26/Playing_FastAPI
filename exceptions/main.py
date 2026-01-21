from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from pydantic import BaseModel

app = FastAPI()

class RegisterUserRequest(BaseModel):
    name : str
    id : int

class RegisterUserRespose(BaseModel):
    success : bool
    message : str

users = {}

@app.post("/register-user",response_model=RegisterUserRespose)
def register_user(request : RegisterUserRequest):
    if request.id in users:
        raise HTTPException(status_code=422, detail= "User already exists")
    
    users[request.id] = request.name

    return RegisterUserRespose(
        success = True,
        message = "The user have beed added"
    )
    

