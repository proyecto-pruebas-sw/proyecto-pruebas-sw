*** Settings ***
Library    REST    http://localhost:8000
Documentation     Test cases for the DELETE /doctor endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_url}             postgresql://postgres:Pruebas12345@postgres:5432/medical_directory

*** Test Cases ***
test-api-29 DELETE an existing doctor
    DELETE    /doctor/5
    Integer    response status    200

test-api-30 DELETE a non-existing doctor
    DELETE    /doctor/100
    Integer    response status    404
    String    response body error    Doctor not found