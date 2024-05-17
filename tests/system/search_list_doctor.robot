*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             Firefox
${specialty}$            CARDIOLOGIA        

*** Test Cases ***
test-system-1 List all doctors
    Open Browser    ${index_url}    ${browser}
    Page Should Contain Element    id=doctors
    Close Browser

test-system-2 Search for a doctor by specialty
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-3 Search for a doctor by name
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_name    maría
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-4 Search for a doctor by city
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_city    viña
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-7 Search for a doctor by name and city
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_name    maría
    Input Text    id=input_city    viña
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-6 Search for a doctor by specialty and city
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_city    santiago
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-5 Search for a doctor by specialty and name
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_name    maría
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser

test-system-8 Search for a doctor by specialty and name
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_name    maría
    Input Text    id=input_city    santiago
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser
