from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models

def get_doctors(db: Session):
    '''
    Get all doctors

    Returns:
    - List[db_models.DoctorTable]
    '''
    statement = select(db_models.DoctorTable)
    doctors = db.scalars(statement).all()

    return [schemas.DoctorList.from_orm(doctor) for doctor in doctors]

def get_doctor():
    pass

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    '''
    Create a new doctor

    Parameters:
    - db: Session
    - doctor: schemas.DoctorCreate

    Returns:
    - db_models.DoctorTable
    '''

    # Create doctor
    db_doctor = db_models.DoctorTable(
        name=doctor.name,
        lastname=doctor.lastname,
        rut=doctor.rut,
        email=doctor.email,
        phone=doctor.phone,
        birthdate=doctor.birthdate,
        city=doctor.city
    )
    db.add(db_doctor)

    db.flush()

    # Create doctor specialties
    db_doctor_specialties = [db_models.DoctorSpecialtyTable(doctor_id=db_doctor.id, specialty_id=specialty_id) for specialty_id in doctor.specialties]
    db.add_all(db_doctor_specialties)
    
    # Create doctor experiences
    db_experiences = [db_models.ExperienceTable(**experience.dict(), doctor_id=db_doctor.id) for experience in doctor.experiences]
    db.add_all(db_experiences)

    # Create doctor educations
    db_educations = [db_models.EducationTable(**education.dict(), doctor_id=db_doctor.id) for education in doctor.educations]
    db.add_all(db_educations)
    
    db.commit()
    db.refresh(db_doctor)

    return db_doctor

def update_doctor():
    pass

def delete_doctor(db: Session, doctor_id: int):
    '''
    Delete a doctor

    Parameters:
    - db: Session
    - doctor_id: int

    Returns:
    - Message confirming the deletion
    '''

    # Delete doctor
    db_doctor = db.get(db_models.DoctorTable, doctor_id)
    if db_doctor is None:
        return {'message': 'Doctor not found'}
    db.delete(db_doctor)
    db.commit()
    return {'message': 'Doctor deleted successfully'}