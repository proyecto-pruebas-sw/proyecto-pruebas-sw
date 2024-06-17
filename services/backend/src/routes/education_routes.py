from fastapi import APIRouter, Response, status, Depends
from src.controllers import education_crud
from src.schemas import schemas
from src.config.db import get_db
from sqlalchemy.orm import Session

education_routes = APIRouter()

@education_routes.get('/educations/{doctor_id}')
async def get_educations(response: Response, doctor_id: int = None, db: Session = Depends(get_db)):
    '''
    Endpoint to get all educations of a doctor

    Parameters:
    - response: Response
    - doctor_id: int
    - db: Session

    Returns:
    - List[schemas.EducationBase]
    '''

    try:
        educations = education_crud.get_educations(db, doctor_id)
        return educations
    
    except Exception as e:
        if str(e) == "Doctor not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Doctor not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@education_routes.post('/education/{doctor_id}')
async def post_education(response: Response, education: schemas.EducationBase, doctor_id: int = None, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new education for a doctor

    Parameters:
    - response: Response
    - doctor_id: int
    - db: Session

    Returns:
    - db_models.EducationTable
    '''

    try:
        new_education = education_crud.create_education(db, education,  doctor_id)
        response.status_code = status.HTTP_201_CREATED
        return new_education

    except Exception as e:
        if str(e) == "Doctor not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Doctor not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@education_routes.put('/education/{education_id}')
async def update_education(response: Response, education_id: int, education: schemas.EducationBase, db: Session = Depends(get_db)):
    '''
    Endpoint to update an education

    Parameters:
    - response: Response
    - education_id: int
    - education: schemas.EducationBase
    - db: Session

    Returns:
    - db_models.EdcuationTable
    '''

    try:
        db_education = education_crud.update_education(db, education, education_id)
        return db_education
    
    except Exception as e:
        if str(e) == "Not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Education not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@education_routes.delete('/education/{education_id}')
async def delete_education(response: Response, education_id: int, db: Session = Depends(get_db)):
    '''
    Endpoint to delete an education of a doctor

    Parameters:
    - response: Response
    - education_id: int
    - db: Session

    Returns:
    - Message confirming the deletion
    '''

    try:
        message = education_crud.delete_education(db, education_id)
        return message
    
    except Exception as e:
        if str(e) == "Not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Education not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}