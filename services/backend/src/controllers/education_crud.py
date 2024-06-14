from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models

def get_educations(db: Session, doctor_id: int = None):
    '''
    Get all educations of a doctor

    Parameters:
    - db: Session
    - doctor_id: int

    Returns:
    - List[db_models.EducationTable]
    '''
    # Verify if doctor exists
    doctor = db.get(db_models.DoctorTable, doctor_id)

    if doctor is None:
        raise Exception("Doctor not found")
    
    # Get educations
    statement = select(db_models.EducationTable)

    if doctor_id is not None:
        statement = statement.filter(db_models.EducationTable.doctor_id == doctor_id)

    educations = db.scalars(statement).all()
    return [schemas.EducationList.from_orm(education) for education in educations]

def create_education(db: Session, education: schemas.EducationBase, doctor_id: int = None):
    '''
    Create a new education for a doctor

    Parameters:
    - db: Session
    - education: schemas.EducationBase
    - doctor_id: int

    Returns:
    - db_models.EdcuationTable
    '''
    # Verify if doctor exists
    doctor = db.get(db_models.DoctorTable, doctor_id)

    if doctor is None:
        raise Exception("Doctor not found")

    # Create education
    new_education = db_models.EducationTable(
        degree=education.degree,
        description=education.description,
        institution=education.institution,
        city=education.city,
        country=education.country,
        start_date=education.start_date,
        end_date=education.end_date,
        doctor_id=doctor_id
    )

    db.add(new_education)
    db.commit()
    db.refresh(new_education)

    return new_education

def update_education(db: Session, education: schemas.EducationBase, education_id: int = None):
    '''
    Update an education for a doctor

    Parameter:
    - db: Session
    - education_id: int
    - education: schemas.EducationBase

    Returns:
    - db_models.EdcuationTable
    '''

    # Update education
    db_education = db.get(db_models.EducationTable, education_id)
    
    if db_education is None:
        raise Exception("Not found")
    
    db_education.degree = education.degree
    db_education.description = education.description
    db_education.institution = education.institution
    db_education.city = education.city
    db_education.country = education.country
    db_education.start_date = education.start_date
    db_education.end_date = education.end_date

    db.commit()
    db.refresh(db_education)

    return db_education

def delete_education(db: Session, education_id: int = None):
    '''
    Delete an education for a doctor

    Parameters:
    - db: Session
    - education_id: int
    '''

    # Delete education
    db_education = db.get(db_models.EducationTable, education_id)

    if db_education is None:
        raise Exception("Not found")
    
    db.delete(db_education)
    db.commit()

    return {'message': 'Education of doctor deleted successfully'}