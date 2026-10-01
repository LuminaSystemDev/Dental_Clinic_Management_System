from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from Schemas.user_schema import UserCreate, UserResponse, UserLogin
from Database.session import get_db
from Services.user_services import create_user_service, login_service

"""Auth User Router"""

auth_user_router = APIRouter(prefix="/api/auth", tags=["Autentications"])


"""Register and autentication Endpoints"""

# Create User Endpoint
@auth_user_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_service(db, user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# Login Endpoint
@auth_user_router.post("/login", status_code=status.HTTP_200_OK, response_model=dict)
def login(user_login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserLogin(email=user_login.username, password=user_login.password)
    try:
        return login_service(db, user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
