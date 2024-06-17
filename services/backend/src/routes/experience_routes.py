from fastapi import APIRouter, Response, status, Depends
from src.controllers import experience_crud
from src.schemas import schemas
from src.config.db import get_db
from sqlalchemy.orm import Session

experience_routes = APIRouter()

@experience_routes.get('/experiences/{doctor_id}')
async def get_experiences(response: Response, doctor_id: int = None, db: Session = Depends(get_db)):
    '''
    Endpoint to get all experiences of a doctor

    Parameters:
    - response: Response
    - doctor_id: int
    - db: Session

    Returns:
    - List[schemas.ExperienceBase]
    '''

    try:
        experiences = experience_crud.get_experiences(db, doctor_id)
        return experiences
    
    except Exception as e:
        if str(e) == "Doctor not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Doctor not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@experience_routes.post('/experience/{doctor_id}')
async def post_experience(response: Response, experience: schemas.ExperienceBase, doctor_id: int = None, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new experience for a doctor

    Parameters:
    - response: Response
    - doctor_id: int
    - db: Session

    Returns:
    - db_models.ExperienceTable
    '''

    try:
        new_experience = experience_crud.create_experience(db, experience,  doctor_id)
        response.status_code = status.HTTP_201_CREATED
        return new_experience

    except Exception as e:
        if str(e) == "Doctor not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Doctor not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@experience_routes.put('/experience/{experience_id}')
async def update_experience(response: Response, experience_id: int, experience: schemas.ExperienceBase, db: Session = Depends(get_db)):
    '''
    Endpoint to update an experience

    Parameters:
    - response: Response
    - experience_id: int
    - experience: schemas.ExperienceBase
    - db: Session

    Returns:
    - db_models.ExperienceTable
    '''

    try:
        db_experience = experience_crud.update_experience(db, experience, experience_id)
        return db_experience
    
    except Exception as e:
        if str(e) == "Not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Experience not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}

@experience_routes.delete('/experience/{experience_id}')
async def delete_experience(response: Response, experience_id: int, db: Session = Depends(get_db)):
    '''
    Endpoint to delete an experience of a doctor

    Parameters:
    - response: Response
    - experience_id: int
    - db: Session

    Returns:
    - Message confirming the deletion
    '''

    try:
        message = experience_crud.delete_experience(db, experience_id)
        return message
    
    except Exception as e:
        if str(e) == "Not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Experience not found"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}