import logging
from core.logger import setup_logging

from Config.db_connection import Base, engine, SessionLocal
from Models.Role import Role
from Models.User import User
from Models.Patient import Patient
from Models.Appointment import Appointment
from Models.Service import Service
from Models.MedicalRecord import MedicalRecord
from Models.Consultation import Consultation
from Models.Payment import Payment
from Models.Reminder import Reminder

# Configure logging
setup_logging()

# Instance Logger
logger = logging.getLogger(__name__)

# Funtion for initialization DB
def init_db():
    session = None

    # Models Creation
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("DB Inicializada correctamente")

    except Exception as error:
        logger.exception("Error al inicializar la Base de Datos")
        return
    
    try:
        # Get DB Session
        session = SessionLocal()

        # Seed initial Data
        if not session.query(Role).first():
            session.add_all(
                [
                    Role(name="ADMIN", description="Administrador del sistema", active=True),
                    Role(name="ODONTOLOGO", description="Personal Medico Dental", active=True),
                    Role(name="SECRETARIO", description="Personal de Administracion", active=True),
                ]
            )

            # Save changes
            session.commit()
            logger.info("Seed de Roles Iniciado Correctamente")
            
        else:
            logger.debug("Seed de Roles no Iniciado, Roles ya Existentes en Base de Datos")

    except Exception as error:
        if session is not None:
            session.rollback()
        logger.exception("Error al obtner la sesion e ingresar roles")

    finally:
        if session is not None:
            # Session Close
            session.close()
            logger.info("Conexion con Base de Datos Cerrada")
    
if __name__ == "__main__":
    init_db()