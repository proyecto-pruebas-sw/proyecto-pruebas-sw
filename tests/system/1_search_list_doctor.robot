*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             Firefox    

*** Test Cases ***
test-system-1 List all doctors
    Open Browser    ${index_url}    ${browser}
    Page Should Contain Element    xpath=//*[contains(@id, '_name')]
    Close Browser

test-system-2 Search for a doctor by specialty
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_specialities')]//div[contains(text(),"CARDIOLOGIA")]
    Close Browser

test-system-3 Search for a doctor by name
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_name    MARIA
    Click Button    Buscar
    Page Should Contain Element     xpath=//span[contains(@id,'_name') and contains(text(),'MARIA')]
    Close Browser

test-system-4 Search for a doctor by city
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_city    ARICA
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_city') and contains(text(),'ARICA')]
    Close Browser

test-system-7 Search for a doctor by name and city
    Open Browser    ${index_url}    ${browser}
    Input Text    id=input_name    MARIA
    Input Text    id=input_city    ARICA
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_name') and contains(text(),'MARIA')]
    Page Should Contain Element    xpath=//span[contains(@id,'_city') and contains(text(),'ARICA')]
    Close Browser

test-system-6 Search for a doctor by specialty and city
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_city    SANTIAGO
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_specialities')]//div[contains(text(),"CARDIOLOGIA")]
    Page Should Contain Element    xpath=//span[contains(@id,'_city') and contains(text(),'SANTIAGO')]
    Close Browser

test-system-5 Search for a doctor by specialty and name
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_name    MARIA
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_specialities')]//div[contains(text(),"CARDIOLOGIA")]
    Page Should Contain Element    xpath=//span[contains(@id,'_name') and contains(text(),'MARIA')]
    Close Browser

test-system-8 Search for a doctor by specialty, name and city
    Open Browser    ${index_url}    ${browser}
    Click Element    css=div.p-dropdown-trigger
    Mouse Down    xpath=//li[@aria-label="CARDIOLOGIA"]
    Click Element     xpath=//li[@aria-label="CARDIOLOGIA"]
    Input Text    id=input_name    MARIA
    Input Text    id=input_city    SANTIAGO
    Click Button    Buscar
    Page Should Contain Element    xpath=//span[contains(@id,'_specialities')]//div[contains(text(),"CARDIOLOGIA")]
    Page Should Contain Element    xpath=//span[contains(@id,'_name') and contains(text(),'MARIA')]
    Page Should Contain Element    xpath=//span[contains(@id,'_city') and contains(text(),'SANTIAGO')]
    Close Browser

test-system-9 Show doctor detail
    Open Browser    ${index_url}    ${browser}
    Page Should Contain Element    xpath=//*[contains(@id, '_name')]
    Mouse Down    xpath=//*[contains(@id, '_phone')]
    Click Element     xpath=//*[contains(@id, '_phone')]
    Page Should Contain Element    id=link_edit_personal_info
    Close Browser