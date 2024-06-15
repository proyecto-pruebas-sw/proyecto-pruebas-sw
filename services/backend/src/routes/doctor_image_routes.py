from fastapi import APIRouter, Response, status, Depends, File, UploadFile
from src.utils.upload_image import upload_image
from src.controllers import doctor_image_crud
from src.config.db import get_db
from sqlalchemy.orm import Session

doctor_image_routes = APIRouter()

@doctor_image_routes.post("/doctor/image/{doctor_id}")
async def upload_doctor_image(response: Response, doctor_id: int, file: UploadFile = File(..., media_type=["image/jpg", "image/jpeg", "image/png"]), db: Session = Depends(get_db)):
    '''
    Endpoint to upload a doctor image

    Parameters:
    - response: Response
    - doctor_id: int
    - file: UploadFile

    Returns:
    - dict
    '''

    ext = file.filename.split(".")[-1]

    if ext not in ["jpg", "jpeg", "png"]:
        response.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        return {"error": "Only .jpg, .jpeg, .png files allowed"}
    
    image = await file.read()

    try:
        doctor = doctor_image_crud.uptade_doctor_image(db, doctor_id, image)
        return doctor
    
    except Exception as e:
        if str(e) == "Not found":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Doctor not found"}
        elif str(e) == "Cloudinary error":
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": "Upload failed"}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"error": str(e)}