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
from fastapi.middleware.cors import CORSMiddleware
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


origins =[
    "https://admin-panel.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET","POST"],
    allow_headers = ["Authorization"],

)

@app.middleware("http")
async def simple_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    print("Before request")
    print("The Request URL:", request.url)
    print("The Http Method:", request.method)
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    print("The time taken to send the response", process_time)
    response.headers["X-Process-Time"]  = str(process_time)
    print("After request")
    
    return response


@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/login")
def login(data : LoginModel)  -> dict:
    if data.username == 'stevejobs' and data.password == '12345':
        return {"access_token" : "super-secret-token",  "token_type": "bearer"}
    else : 
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail="invalied user")
    
def verify_token(authorization : str = Header(alias="Authorization")):
    if not  authorization or not authorization.startswith("Bearer"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user for accessing the profile route")
    if authorization.split()[1] != 'super-secret-token':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user for accessing the profile route")
    return "Access granted"

@app.get("/dashboard")
def dashboard(current_user : str = Depends(verify_token)):
    return {"message": "Welcome stevejobs! You are verified"}

@app.get("/profile")
def profile(current_user : str = Depends(verify_token)):
    return {"message": "Welcome stevejobs! You are verified"}

