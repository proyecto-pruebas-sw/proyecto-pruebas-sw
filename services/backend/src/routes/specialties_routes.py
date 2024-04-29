from fastapi import APIRouter, Response, status, Depends
from src.controllers import specialty_crud
from src.schemas import schemas
from src.config.db import get_db
from sqlalchemy.orm import Session

specialty_routes = APIRouter()

@specialty_routes.get('/specialty')
async def get_specialties(response: Response, db: Session = Depends(get_db)):
    '''
    Endpoint to get all specialties

    Parameters:
    - response: Response
    - db: Session

    Returns:
    - List[schemas.SpecialtyList]
    '''

    try:
        specialties = specialty_crud.get_specialties(db)
        response.status_code = status.HTTP_200_OK
        return specialties
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@specialty_routes.post('/specialty')
async def create_specialty(response: Response, specialty: schemas.SpecialtyBase, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new specialty

    Parameters:
    - response: Response
    - specialty: schemas.SpecialtyCreate
    - db: Session
    '''
    try:
        new_specialty = specialty_crud.create_specialty(db, specialty)
        response.status_code = status.HTTP_201_CREATED
        return new_specialty
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}