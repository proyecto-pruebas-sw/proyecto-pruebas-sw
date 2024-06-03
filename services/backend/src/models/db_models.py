from src.config.db import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import validates, relationship

class DoctorTable(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    rut = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    birthdate = Column(Date)
    city = Column(String)

    specialties = relationship('SpecialtyTable', secondary='doctor_specialties', back_populates='doctors')
    experiences = relationship('ExperienceTable', back_populates='doctor', cascade='all, delete')
    educations = relationship('EducationTable', back_populates='doctor', cascade='all, delete')

    @validates('name', 'lastname', 'rut', 'email', 'city')
    def convert_upper(self, key, value):
        if value is None:
            return value
        return value.upper()

class SpecialtyTable(Base):
    __tablename__ = 'specialties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    doctors = relationship('DoctorTable', secondary='doctor_specialties', back_populates='specialties')

    @validates('name')
    def convert_upper(self, key, value):
        if value is None:
            return value
        return value.upper()

class DoctorSpecialtyTable(Base):
    __tablename__ = 'doctor_specialties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    specialty_id = Column(Integer, ForeignKey('specialties.id'), nullable=False)

class ExperienceTable(Base):
    __tablename__ = 'experiences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    job_title = Column(String, nullable=False)
    description = Column(String)
    institution = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    doctor = relationship('DoctorTable', back_populates='experiences')

    @validates('hospital')
    def convert_upper(self, key, value):
        if value is None:
            return value
        return value.upper()
    
    @validates('city', 'country', 'job_title', 'institution')
    def convert_upper(self, key, value):
        if value is None:
            return value
        return value.upper()
    
class EducationTable(Base):
    __tablename__ = 'educations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    degree = Column(String, nullable=False)
    description = Column(String)
    institution = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    doctor = relationship('DoctorTable', back_populates='educations')
    
    @validates('city', 'country', 'institution', 'degree')
    def convert_upper(self, key, value):
        if value is None:
            return value
        return value.upper()
