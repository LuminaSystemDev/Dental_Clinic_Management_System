from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from Schemas.user_schema import UserCreate, UserResponse, UserLogin
from Repositories.user_repositories import get_user_by_email, get_user_by_id, create_user
from Security.Password import verify_password
from Security.Jwt import create_access_token, verify_token
from Config.db_connection import SessionLocal


# Service to validate email unique
def validate_email_unique(db: Session, email: str):
    user = get_user_by_email(db, email)
    if user:
        raise ValueError("User with this email already exists")


# Service to create a new user
def create_user_service(db: Session, user: UserCreate):
    validate_email_unique(db, user.email)

    user_data = user.model_dump()
    db_user = create_user(db, user_data)
    result = UserResponse.model_validate(db_user)
    
    return result


# Service to validate user login
def login_service(db: Session, user_login: UserLogin) -> dict:
    user = get_user_by_email(db, user_login.email)
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise ValueError("Incorrect email or password")

    access_token = create_access_token(data={"sub": str(user.id)})
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }


# Service to get current user
def get_current_user_service(db: Session, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Cold not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token)
    if payload is None:
        raise credentials_exception

    user_id : str = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    user = get_user_by_id(db, int(user_id))

    return UserResponse.model_validate(user)
