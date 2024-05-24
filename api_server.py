from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
allow_origins=["*"],
allow_methods=["*"]
)
class User (BaseModel):
    firstname:str
    lastname:str
    mobile:int

users={
    1:User(firstname="mehdi",lastname="leilyzadeh",mobile =9168194573)
}
@app.get('/users')
def user_list():  
    return users


@app.post('/users')
def create_user(user:User):
    new_user_id = max(list(users.keys()))+1
    users[new_user_id]= user   
    return {"message":"helloword"}



@app.delete('/users/{user_id}')
def remove_user(user_id:int):
    if user_id not in users:
        raise HTTPException(404,"nadarim")
    del(users[user_id])
    

@app.get('/users/{user_id}')
def get_single_user_info(user_id:int):
    if user_id not in users:
        raise HTTPException(404,"nadarim")
    return users[user_id]

@app.put('/users')
def user_list():
    pass
    
    return {"message":"helloword"}