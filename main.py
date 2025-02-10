from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import User
import crud
from schemas import UserCreate

# Create tables in the database (if they don't exist)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Route to get all users
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Route to get a specific user by ID
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Route to create a new user
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user


# Route to update a specific user by ID
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = crud.update_user(db, user_id, user)
    return updated_user

# Route to delete a specific user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    crud.delete_user(db, user_id)
    return {"message": "User deleted successfully"}


from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify frontend's URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
