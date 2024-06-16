import os

# Upload image to Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')

cloudinary.config(cloudinary_url=CLOUDINARY_URL)

def upload_image(file: bytes, doctor_id: int) -> str:
    try:
        upload = cloudinary.uploader.upload(file, folder='proyecto-pruebas-sw/doctors', public_id=doctor_id)
        return upload['secure_url']
    except Exception as e:
        return None
    
def delete_image(public_id: str) -> bool:
    try:
        cloudinary.uploader.destroy(f'proyecto-pruebas-sw/doctors/{public_id}')
        return True
    except Exception as e:
        return False