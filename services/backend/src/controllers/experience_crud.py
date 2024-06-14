from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models

def get_experiences(db: Session, doctor_id: int = None):
    '''
    Get all experiences of a doctor

    Parameters:
    - db: Session
    - doctor_id: int

    Returns:
    - List[db_models.ExperienceTable]
    '''
    # Verify if doctor exists
    doctor = db.get(db_models.DoctorTable, doctor_id)

    if doctor is None:
        raise Exception("Doctor not found")
    
    # Get experiences
    statement = select(db_models.ExperienceTable)

    if doctor_id is not None:
        statement = statement.filter(db_models.ExperienceTable.doctor_id == doctor_id)

    experiences = db.scalars(statement).all()
    return [schemas.ExperienceList.from_orm(experience) for experience in experiences]

def create_experience(db: Session, experience: schemas.ExperienceBase, doctor_id: int = None):
    '''
    Create a new experience for a doctor

    Parameters:
    - db: Session
    - experience: schemas.ExperienceBase
    - doctor_id: int

    Returns:
    - db_models.ExperienceTable
    '''
    # Verify if doctor exists
    doctor = db.get(db_models.DoctorTable, doctor_id)

    if doctor is None:
        raise Exception("Doctor not found")

    # Create experience
    new_experience = db_models.ExperienceTable(
        job_title=experience.job_title,
        description=experience.description,
        institution=experience.institution,
        city=experience.city,
        country=experience.country,
        start_date=experience.start_date,
        end_date=experience.end_date,
        doctor_id=doctor_id
    )

    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)

    return new_experience

def update_experience(db: Session, experience: schemas.ExperienceBase, experience_id: int = None):
    '''
    Update an experience for a doctor

    Parameter:
    - db: Session
    - experience_id: int
    - experience: schemas.ExperienceBase

    Returns:
    - db_models.ExperienceTable
    '''

    # Update experience
    db_experience = db.get(db_models.ExperienceTable, experience_id)
    
    if db_experience is None:
        raise Exception("Not found")
    
    db_experience.job_title = experience.job_title
    db_experience.description = experience.description
    db_experience.institution = experience.institution
    db_experience.city = experience.city
    db_experience.country = experience.country
    db_experience.start_date = experience.start_date
    db_experience.end_date = experience.end_date

    db.commit()
    db.refresh(db_experience)

    return db_experience

def delete_experience(db: Session, experience_id: int = None):
    '''
    Delete an experience for a doctor

    Parameters:
    - db: Session
    - experience_id: int
    '''

    # Delete experience
    db_experience = db.get(db_models.ExperienceTable, experience_id)

    if db_experience is None:
        raise Exception("Not found")
    
    db.delete(db_experience)
    db.commit()

    return {'message': 'Experience of doctor deleted successfully'}