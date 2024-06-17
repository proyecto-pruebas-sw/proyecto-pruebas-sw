*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             firefox    

*** Test Cases ***
test-system-11 Create doctor
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    29.115.451-4
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    Crear médico
    Page Should Contain Element    xpath=//span[contains(@id,'_phone') and contains(text(),'912345678')]
    Close Browser

test-system-12 Create doctor without name
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    8756190-9
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    Crear médico
    Close Browser

test-system-13 Create doctor without lastname
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_name    some_name
    Input Text    id=input_rut    73448837-2
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    Crear médico
    Close Browser

test-system-14 Create doctor without rut
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    Crear médico
    Close Browser

test-system-27 Create doctor without specialty
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    77261639-2
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Input Text    id=input_city    some_city
    Click Button    Crear médico
    Close Browser

test-system-28 Create doctor without city
    Open Browser    ${index_url}    ${browser}
    Click Button    Crear Médico
    Input Text    id=input_name    some_name
    Input Text    id=input_lastname    some_lastname
    Input Text    id=input_rut    60134558-7
    Input Text    id=input_email    some_email@gmail.com
    Input Text    id=input_phone    912345678
    Click Element    id=multiselect_specialties
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    Crear médico
    Close Browser
