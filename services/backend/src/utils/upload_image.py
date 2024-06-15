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