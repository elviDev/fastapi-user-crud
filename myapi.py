from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1 : {
    "name": "Elvis",
    "website": "https://github.com/elviDev",
    "age": 29,
    "role": "Software Engineer"
    }
}

# Base Pydantic Models
class User(BaseModel):
    name: str
    website: Optional[str] = None
    age: int
    role: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None
    
    
    
    
    

# Endpoint to check the health of the API
@app.get("/")
def root():
    return {"message": "welcome to your introduction to FASTAPI!"}


# Get Users
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="The ID you want to get", gt = 0, lt = 100)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found!")
    return users[user_id]
# Create a User
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists!")
    users[user_id] = user.dict()
    return user

# Update a User
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found!")
    current_user = users[user_id]
    if user.name is not None:
        current_user["name"] = user.name
    if user.website is not None:
        current_user["website"] = user.website
    if user.age is not None:
        current_user["age"] = user.age
    if user.role is not None:
        current_user["role"] = user.role
    return current_user

        
#Delete a User
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found!")
    
    deleted_user = users[user_id]
    del users[user_id]
    return {"message": "User deleted successfully", "user": deleted_user}

#Search for Users
@app.get("/users/search/")
def search_by_name(name: Optional[str] = None):
    if not name:
        return {"message": "Name parameter is required"}
    
    for user in users.values():
        if user["name"] == name:
            return user
        
    raise HTTPException(status_code=404, detail="User not found!")
        