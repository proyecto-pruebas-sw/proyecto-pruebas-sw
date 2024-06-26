from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.models import db_models
from src.utils.upload_image import upload_image
from src.utils.upload_image import delete_image

def uptade_doctor_image(db: Session, doctor_id: int, image: bytes):
    '''
    Update a doctor image

    Parameters:
    - db: Session
    - doctor_id: int
    - image_url: str

    Returns:
    - db_models.DoctorTable
    '''

    # Update doctor image
    db_doctor = db.get(db_models.DoctorTable, doctor_id)

    if db_doctor is None:
        raise Exception("Doctor not found")
    
    image_url = upload_image(image, doctor_id)

    if image_url is None:
        raise Exception("Cloudinary error")

    db_doctor.image_url = image_url

    db.commit()
    db.refresh(db_doctor)

    doctor_image = schemas.DoctorImage(image_url=db_doctor.image_url)

    return doctor_image

def delete_doctor_image(db: Session, doctor_id: int):
    '''
    Delete a doctor image

    Parameters:
    - db: Session
    - doctor_id: int

    Returns:
    - db_models.DoctorTable
    '''

    # Delete doctor image
    db_doctor = db.get(db_models.DoctorTable, doctor_id)

    if db_doctor is None:
        raise Exception("Doctor not found")
    
    success_delete = delete_image(doctor_id)

    if not success_delete:
        raise Exception("Cloudinary error")
    
    db_doctor.image_url = None

    db.commit()
    db.refresh(db_doctor)

    return {'message': 'Doctor image deleted successfully'}