from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from utils import poem_generator,code_generator

app = FastAPI()

class Poem(BaseModel):
    topic: str
    lines: int

class Coder(BaseModel):
    Language: Optional[str]
    Problem:  str

@app.get('/')
def index():
    return "This is an example for get endpoint"

@app.get('/welcome')
def welcome_user(name: str = 'ravi'):
    return f"welcome {name}"

@app.post("/orders")
async def place_order(product: str, units: int):
    return {"message": f"Order for {units} units of {product} placed successfully."}


@app.post('/poem_generator')
def generate_poem(poem:Poem):
    result = poem_generator(f"the topic of the poem is {poem.topic} and it need to be within {poem.lines} lines")
    return f"Poem :{result}"

@app.post('/code_generator')
def write_code(code:Coder):
    res = code_generator(f"write a program to {code.Problem} in {code.Language} languages.")
    return f"Program : {res}"