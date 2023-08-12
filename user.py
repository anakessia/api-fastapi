from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Model

class User(BaseModel):
    id: int
    email: str
    password: str

# Data Base

data_base = [
    User(id=1, email="example@.com.br", password="user123"),
    User(id=2, email="anaoliveira@.com.br", password="ana123"),
    User(id=3, email="mariasilva@.com.br", password="silva123")
]

# Get All

@app.get("/users")
def get_all_users():
    return data_base

# Get ID

@app.get("/users/{id_user}")
def get_id_user(id_user: int):
    for user in data_base:
        if(user.id == id_user):
            return user
    
    return {"Status": 404, "Message": "User not found"}

# POST

@app.post("/users")
def post_user(user: User):
    data_base.append(user)
    return user