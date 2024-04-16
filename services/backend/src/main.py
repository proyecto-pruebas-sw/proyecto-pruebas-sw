from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.doctor_routes import doctor_routes

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



