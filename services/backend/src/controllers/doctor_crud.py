from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models

def get_doctors(db: Session, specialty_id: int = None, doctor_name: str = None, doctor_city: str = None):
    '''
    Get all doctors

    Returns:
    - List[db_models.DoctorTable]
    '''

    # Get doctors
    statement = select(db_models.DoctorTable)

    if specialty_id is not None:
        statement = statement.join(db_models.DoctorSpecialtyTable).filter(db_models.DoctorSpecialtyTable.specialty_id == specialty_id)
    
    if doctor_name is not None:
        statement = statement.filter((db_models.DoctorTable.name + " " + db_models.DoctorTable.lastname).ilike(f'%{doctor_name}%'))

    if doctor_city is not None:
        statement = statement.filter(db_models.DoctorTable.city.ilike(f'%{doctor_city}%'))
    
    doctors = db.scalars(statement).all()
    return [schemas.DoctorList.from_orm(doctor) for doctor in doctors]
    


def get_doctor(db: Session, doctor_id: int):
    '''
    Get a doctor by id

    Parameters:
    - db: Session
    - doctor_id: int

    Returns:
    - db_models.DoctorTable
    '''
    # Get doctor details
    doctor = db.query(db_models.DoctorTable).filter(db_models.DoctorTable.id == doctor_id).first()

    if doctor is None:
        raise Exception("Not found")
    
    doctor_detail = schemas.DoctorDetail(
        id=doctor.id,
        name=doctor.name,
        lastname=doctor.lastname,
        rut=doctor.rut,
        email=doctor.email,
        phone=doctor.phone,
        birthdate=doctor.birthdate,
        city=doctor.city,
        image_url=doctor.image_url,
        specialties=[schemas.SpecialtyList(id=specialty.id, name=specialty.name) for specialty in doctor.specialties],
        experiences=[schemas.ExperienceBase(id=experience.id, job_title=experience.job_title, description=experience.description, institution=experience.institution, city=experience.city, country=experience.country, start_date=experience.start_date, end_date=experience.end_date) for experience in doctor.experiences],
        educations=[schemas.EducationBase(id=education.id, degree=education.degree, description=education.description, institution=education.institution, city=education.city, country=education.country, start_date=education.start_date, end_date=education.end_date) for education in doctor.educations]
    )

    return doctor_detail

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

def update_doctor(db: Session, doctor_id: int, doctor: schemas.DoctorBase):
    '''
    Update a doctor

    Parameters:
    - db: Session
    - doctor_id: int
    - doctor: schemas.DoctorBase

    Returns:
    - db_models.DoctorTable
    '''

    # Update doctor
    db_doctor = db.get(db_models.DoctorTable, doctor_id)

    if db_doctor is None:
        raise Exception("Not found")
    
    db_doctor.name = doctor.name
    db_doctor.lastname = doctor.lastname
    db_doctor.rut = doctor.rut
    db_doctor.email = doctor.email
    db_doctor.phone = doctor.phone
    db_doctor.birthdate = doctor.birthdate
    db_doctor.city = doctor.city

    db.commit()
    db.refresh(db_doctor)

    return db_doctor

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
        raise Exception("Not found")
    
    db.delete(db_doctor)
    db.commit()
    
    return {'message': 'Doctor deleted successfully'}