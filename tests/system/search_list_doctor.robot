*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             Firefox

*** Test Cases ***
test-system-1 List all doctors
    Open Browser    ${index_url}    ${browser}
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

test-system-5 Search for a doctor by name and city
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_name    maría
    Input Text    id=input_city    viña
    Click Button    Buscar
    Page Should Contain Element    id=doctors
    Close Browser