*** Settings ***
Library           RequestsLibrary
Library           Collections
Documntation      Test cases for the GET /doctor/{id} endpoint

*** Variables ***
${api_url}            http://localhost:8000
${db_url}             postgresql://postgres:Pruebas12345@postgres:5432/medical_directory

*** Test Cases ***
test-api-9 Get a existing doctor by id
    Create Session    api    ${api_url}
    ${response}       Get On Session    api    /doctor/1
    Should Be Equal As Strings    ${response.status_code}    200
    ${response_body}    Set Variable    ${response.json()}
    Should Be Equal As Strings    ${response_body.id}    1
    Should Be Equal As Strings    ${response_body.name}    "JUAN CARLOS"
    Should Be Equal As Strings    ${response_body.last_name}    "GONZÁLEZ PÉREZ"
