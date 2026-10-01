
from sqlalchemy.orm import Session
from Models.Role import Role

# Get role list
def get_roles(db: Session):
    return db.query(Role).all()
