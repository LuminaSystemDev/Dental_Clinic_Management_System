
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

# Get jwt Envs 
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM =  os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# OAuth2 Scheme for extract token of header Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# Funtion for create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate JWT with data of user and expiration"""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encode_jwt


# Funtion for verify access token
def verify_token(token: str) -> Optional[dict]:
    """Decoded and validates the token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        # Return the payload or None if it is valid 
        return payload
    except JWTError:
        return None