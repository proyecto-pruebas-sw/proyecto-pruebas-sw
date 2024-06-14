from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models

def get_specialties(db: Session):
    '''
    Get all specialties

    Returns:
    - List[db_models.SpecialtyTable]
    '''
    statement = select(db_models.SpecialtyTable)
    specialties = db.scalars(statement).all()

    return [schemas.SpecialtyList.from_orm(specialty) for specialty in specialties]

def create_specialty(db: Session, specialty: schemas.SpecialtyBase):
    '''
    Create a new specialty

    Parameters:
    - db: Session
    - specialty: schemas.SpecialtyBase

    Returns:
    - db_models.SpecialtyTable
    '''

    new_specialty = db_models.SpecialtyTable(name=specialty.name)
    db.add(new_specialty)
    db.commit()
    db.refresh(new_specialty)

    return new_specialty
