*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             headlessFirefox    

*** Test Cases ***
test-system-11 Create doctor
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    29.115.451-4
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    xpath=//span[contains(@id,'_phone') and contains(text(),'+56912345678')]
    Close Browser

test-system-12 Create doctor without name
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    8.756.190-9
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser

test-system-13 Create doctor without lastname
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_name    some_name
    Input Text    id=input_rut    73.448.837-2
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser

test-system-14 Create doctor without rut
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser

test-system-27 Create doctor without specialty
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    77.261.639-2
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser

test-system-28 Create doctor without city
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Page Should Contain Element    id=medic_create
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    60.134.558-7
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser
