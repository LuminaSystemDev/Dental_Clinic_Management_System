from passlib.context import CryptContext

# Configuration for password hashing context 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Funtion for password hashing
def hash_password(password: str) -> str:
    # generate a secure hashed
    return pwd_context.hash(password)

# Funtion for password verification
def verify_password(text_password: str, hashed_password: str) -> bool:
    # Verify if the password matches the hashed
    return pwd_context.verify(text_password, hashed_password)
    