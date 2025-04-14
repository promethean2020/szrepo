from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel, ValidationError
class User(BaseModel):
    id: int
    name: str

# Valid data
user_list= [User(id= 0, name= "Alice"),User(id= 1, name= "Bob")]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/{user_id}")
def read_item(user_id: int):
    user=user_list[user_id]
    return user