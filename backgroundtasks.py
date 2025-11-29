# from fastapi import FastAPI, BackgroundTasks

# app = FastAPI()

# @app.get("/")
# def welcome_home():
#     return {"Message  ": "welcome to hawkins"}

# def write_email(email : str , message = ""): 
#     with open("email.txt", mode="w") as email_file:
#         content = f"Hello welcome to fastapi notifications for  {email} message is {message}"
#         email_file.write(content)
#         # return email_file

# @app.post("/send-notification/{email}")
# async def send_notification(email : str, background_tasks : BackgroundTasks):
#     background_tasks.add_task(write_email,email,message="some notifications")
#     return {"message" : "Notification sent in the background"}


from typing import Annotated

from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    message = f"message to {email} and {q}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}