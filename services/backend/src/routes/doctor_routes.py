from fastapi import APIRouter, Response, status
import src.controllers.doctor_crud 

doctor_routes = APIRouter()

@doctor_routes.get("/doctor")
async def get_doctors():
    pass

@doctor_routes.get("/doctor/{doctor_id}")
async def get_doctor(doctor_id: int):
    pass

@doctor_routes.post("/doctor")
async def create_doctor(response: Response):
    pass

@doctor_routes.put("/doctor/{doctor_id}")
async def update_doctor(doctor_id: int, response: Response):
    pass

@doctor_routes.delete("/doctor/{doctor_id}")
async def delete_doctor(doctor_id: int, response: Response):
    pass
