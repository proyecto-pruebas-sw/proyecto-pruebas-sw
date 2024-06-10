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
    Input Text    id=input_rut    11.111.111-1
    Input Text    id=input_email    some_email@gmailcom
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialities
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
    Input Text    id=input_rut    11.111.111-1
    Input Text    id=input_email    some_email@gmailcom
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialities
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
    Input Text    id=input_rut    11.111.111-1
    Input Text    id=input_email    some_email@gmailcom
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialities
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
    Input Text    id=input_email    some_email@gmailcom
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Input Text    id=input_city    some_city
    Click Element    id=multiselect_specialities
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
    Input Text    id=input_rut    11.111.111-1
    Input Text    id=input_email    some_email@gmailcom
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
    Input Text    id=input_rut    11.111.111-1
    Input Text    id=input_email    some_email@gmailcom
    Input Text    id=input_phone    +56912345678
    Input Text    id=input_birthdate    2000-01-01
    Click Element    id=multiselect_specialities
    Mouse Down    xpath=//li/span[text()="CARDIOLOGIA"]
    Click Element     xpath=//li/span[text()="CARDIOLOGIA"]
    Click Button    id=medic_create
    Page Should Contain Element    id=medic_create
    Close Browser
