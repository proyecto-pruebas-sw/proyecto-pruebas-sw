from fastapi import APIRouter, Response, status, Depends
from src.controllers import doctor_crud
from src.schemas import schemas
from src.config.db import get_db
from sqlalchemy.orm import Session

doctor_routes = APIRouter()

@doctor_routes.get('/doctor')
async def get_doctors(response: Response, db: Session = Depends(get_db)):
    '''
    Endpoint to get all doctors

    Parameters:
    - response: Response
    - db: Session

    Returns:
    - List[schemas.DoctorList]
    '''

    try:
        doctors = doctor_crud.get_doctors(db)
        return doctors
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@doctor_routes.get('/doctor/{doctor_id}')
async def get_doctor(response: Response, doctor_id: int, db: Session = Depends(get_db)):
    '''
    Endpoint to get a doctor and its details by id

    Parameters:
    response: Response
    doctor_id: int
    db: Session

    Returns:
    - schemas.DoctorDetail
    '''
    try:
        doctor = doctor_crud.get_doctor(db, doctor_id)
        return doctor
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@doctor_routes.post('/doctor')
async def create_doctor(response: Response, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new doctor

    Parameters:
    - response: Response
    - doctor: schemas.DoctorCreate
    - db: Session

    Returns:
    - db_models.DoctorTable
    '''
    try:
        db_doctor = doctor_crud.create_doctor(db, doctor)
        response.status_code = status.HTTP_201_CREATED
        return db_doctor
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@doctor_routes.put('/doctor/{doctor_id}')
async def update_doctor(doctor_id: int, response: Response):
    pass

@doctor_routes.delete('/doctor/{doctor_id}')
async def delete_doctor(doctor_id: int, response: Response):
    pass
