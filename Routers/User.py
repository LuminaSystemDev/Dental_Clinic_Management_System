from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from Schemas.user_schema import UserResponse
from Database.session import get_db
from Services.user_services import get_current_user_service
from Security.Jwt import oauth2_scheme

"""User Router"""
user_router = APIRouter(prefix="/api/users", tags=["Users"])


"""Definition of Endpoints for Users"""

# Get Current User Endpoint
@user_router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
def read_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        user = get_current_user_service(db, token)
        return user
    except HTTPException as exception:
        raise exception

    