*** Settings ***
Library           RequestsLibrary
Library    REST    http://localhost:8000
Library           Collections
Variables    variables.py
Documentation     Test cases for the GET /specialty endpoint

*** Variables ***
${api_url}            http://localhost:8000

*** Test Cases ***
test-specialty-1 Get all specialties
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/specialty
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}
    Lists Should Be Equal    ${expected_data}[get]    ${response.json()}