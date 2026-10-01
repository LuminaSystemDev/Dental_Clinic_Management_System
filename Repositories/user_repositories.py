from sqlalchemy.orm import Session
from Models.User import User
from Security.Password import hash_password

# Funtion to get user by id
def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

# Funtion to get user by email
def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

# Funtion to Create User
def create_user(db: Session, user_data: dict):
    user_data["hashed_password"] = hash_password(user_data["hashed_password"])
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
