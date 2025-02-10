# Import statements
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

# Function to get users
def get_users(db: Session):
    return db.query(User).all()

# Function to get user by id
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Function Create user
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to update an existing user
def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.age = user.age
        db.commit()
        db.refresh(db_user)
        return db_user
    return None  # If user is not found

# Function to delete a user by ID
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}