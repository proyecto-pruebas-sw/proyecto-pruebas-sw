*** Settings ***
Library           RequestsLibrary
Library           Collections
Documentation     Test cases for the GET /doctor endpoint

*** Variables ***
${api_url}            http://localhost:8000
${db_url}             postgresql://postgres:Pruebas12345@postgres:5432/medical_directory

*** Test Cases ***
test-api-1 Get all doctors
    [Tags]    get_all_doctors
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    /doctor
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-2 Get doctors by specialty
    [Tags]    get_doctors_by_specialty
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=1
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-3 Get doctors by name
    [Tags]    get_doctors_by_name
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_name=Juan
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-4 Get doctors by city
    [Tags]    get_doctors_by_city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_city=valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-5 Get doctors by specialty and name
    [Tags]    get_doctors_by_specialty_and_name
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_name=Juan
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}
    
test-api-6 Get doctors by specialty and city
    [Tags]    get_doctors_by_specialty_and_city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_city=Valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-7 Get doctors by name and city
    [Tags]    get_doctors_by_name_and_city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_name=Juan&doctor_city=Valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-8 Get doctors by specialty, name and city
    [Tags]    get_doctors_by_specialty_name_and_city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_name=Juan&doctor_city=valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}
