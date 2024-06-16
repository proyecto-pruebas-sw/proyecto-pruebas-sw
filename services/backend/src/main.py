from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.doctor_routes import doctor_routes
from .routes.specialties_routes import specialty_routes
from .routes.experience_routes import experience_routes
from .routes.education_routes import education_routes
from .routes.doctor_image_routes import doctor_image_routes
from .models import db_models
from .config import db

# Create tables on db
db_models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

# CORS 
origins = [
    "*", 
]

# Add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(doctor_routes)
app.include_router(specialty_routes)
app.include_router(experience_routes)
app.include_router(education_routes)
app.include_router(doctor_image_routes)