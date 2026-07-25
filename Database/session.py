from Config.db_connection import SessionLocal

# Definition to funtion get_db for management the cicle of life. 
def get_db():
    db = SessionLocal()
    try:
        # Provide session to de route.
        yield db
    finally:
        # Close connection after the request completes.
        db.close()