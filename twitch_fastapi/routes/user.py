#Python
from typing import List

#FastAPI
from fastapi import APIRouter, status, Body

#Cryptography
from cryptography.fernet import Fernet

# app
## config
from config.db import conn

# app
## Schemas
from schemas.user import PersonLogin, PersonBase

# app
## Models
from models.models import users

key = Fernet.generate_key()
encryption = Fernet(key)


user = APIRouter()

@user.get("/")
def helloworld():
    return "Hello world"

@user.post(
    path="/signup", 
    response_model=PersonBase, 
    response_model_exclude={'password'},
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
    )
def signup(person: PersonLogin = Body(...)):
    new_user = {
        "name": person.name, 
        "Email": person.Email, 
        "user_id": person.user_id, 
        "streamer": person.streamer, 
        "birth_date": person.birth_date, 
        "videos": person.videos
        }
    new_user["password"]=encryption.encrypt(person.password.encode("utf-8"))
    conn.execute(users.insert().values(new_user))
    return person
    

@user.post(
    path="/login", 
    response_model=PersonBase, 
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
    )
def login():
    pass

@user.get(
    path="/users", 
    response_model=List[PersonBase], 
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK,
    summary="Show all User",
    tags=["Users"]
    )
def show_all_users():
   pass

@user.get(
    path="/users/{user_id}", 
    response_model=PersonBase, 
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
    )
def show_a_user():
    pass

@user.delete(
    path="/users/{user_id}", 
    response_model=PersonBase, 
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user():
    pass

@user.put(
    path="/users/{user_id}/update", 
    response_model=PersonBase, 
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
    )
def update_a_user():
    pass
