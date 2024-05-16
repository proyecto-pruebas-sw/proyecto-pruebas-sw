*** Settings ***
Library           RequestsLibrary
Library           Collections
Documentation     Test cases for the GET /doctor endpoint

*** Variables ***
${api_url}            http://localhost:8000

*** Test Cases ***
test-api-1 Get all doctors
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    /doctor
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-2 Get doctors by specialty
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=1
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-3 Get doctors by name
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_name=Juan
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-4 Get doctors by city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_city=valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-5 Get doctors by specialty and name
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_name=Juan
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}
    
test-api-6 Get doctors by specialty and city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_city=Valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-7 Get doctors by name and city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?doctor_name=Juan&doctor_city=Valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}

test-api-8 Get doctors by specialty, name and city
    Create Session    medical_directory    ${api_url}
    ${response}    GET On Session    medical_directory    url=/doctor?specialty_id=11&doctor_name=Juan&doctor_city=valp
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be True    ${response.json()}
