*** Settings ***
Library    REST    http://localhost:8000
Documentation     Test cases for the POST /doctor endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_url}             postgresql://postgres:Pruebas12345@postgres:5432/medical_directory

*** Test Cases ***
test-api-11 POST a valid doctor
    POST   /doctor    ${valid_doctor}
    Integer    response status    201
    String    response body name    ${valid_doctor}[name]
    String    response body lastname    ${valid_doctor}[lastname]
    String    response body rut    ${valid_doctor}[rut]
    String    response body city    ${valid_doctor}[city]

test-api-12 POST a doctor without name
    POST   /doctor    ${doctor_without_name}
    Integer    response status    422

test-api-13 POST a doctor without lastname
    POST   /doctor    ${doctor_without_lastname}
    Integer    response status    422

test-api-14 POST a doctor without rut
    POST   /doctor    ${doctor_without_rut}
    Integer    response status    422

test-api-15 POST a doctor without city
    POST   /doctor    ${doctor_without_city}
    Integer    response status    422

test-api-16 POST a doctor without specialties
    POST   /doctor    ${doctor_without_specialties}
    Integer    response status    422
