from pydantic import BaseModel, constr, validator
from typing import List, Optional
from datetime import date

class SpecialtyBase(BaseModel):
    name: constr(max_length=255)

class ExperienceBase(BaseModel):
    job_title: constr(max_length=255)
    description: Optional[constr(max_length=255)] = None
    institution: constr(max_length=255)
    city: constr(max_length=255)
    country: constr(max_length=255)
    start_date: date
    end_date: date

class EducationBase(BaseModel):
    degree: constr(max_length=255)
    description: Optional[constr(max_length=255)] = None
    institution: constr(max_length=255)
    city: constr(max_length=255)
    country: constr(max_length=255)
    start_date: date
    end_date: date

class DoctorBase(BaseModel):
    name: constr(max_length=100)
    lastname: constr(max_length=100)
    rut: constr(max_length=12)
    email: Optional[constr(max_length=100)] = None
    phone: Optional[constr(max_length=20)] = None
    birthdate: Optional[date] = None
    city: Optional[constr(max_length=100)] = None



