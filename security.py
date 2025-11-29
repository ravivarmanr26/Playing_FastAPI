# from fastapi import FastAPI,Depends
# from typing import Annotated
# from fastapi.security import OAuth2PasswordBearer
# from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()

# # app.add_middleware
# # oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # @app.get("/items/")
# # async def read_items(token: Annotated[str, Depends(oauth_scheme)]):
# #     return {"token": token}


# @app.get("/hello/")
# async def hello():
#     return {"welcome to imaginary world"}
from fastapi import FastAPI, Header,HTTPException,status,Depends, Request
import time
from pydantic import BaseModel
app = FastAPI()

class LoginModel(BaseModel):
    username : str
    password : str

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.perf_counter()
#     print("the request is called")
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print(" the response have sended")
#     return response


@app.middleware("http")
async def simple_middleware(request: Request, call_next):
    print("Before request")
    print("The Request URL:", request.url)
    response = await call_next(request)
    print("After request")
    return response


@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/login")
def login(data : LoginModel)  -> dict:
    if data.username == 'stevejobs' and data.password == '12345':
        return {"my-token" : "fastapi-master"}
    else : 
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail="invalied user")
    
def verify_token(token : str = Header()):
    if token != 'fastapi-master':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user for accessing the profile route")
    return "Access granted"


@app.get("/profile")
def profile(current_user : str = Depends(verify_token)):
    return {"message": "Welcome stevejobs! You are verified"}