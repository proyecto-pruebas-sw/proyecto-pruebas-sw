*** Settings ***
Library    SeleniumLibrary
Documentation     Test cases for the search and list doctors functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             Firefox   
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432   

*** Test Cases ***
test-system-30 Update doctor view
    Open Browser    ${index_url}    ${browser}
    Page Should Contain Element    xpath=//*[contains(@id, '_name')]
    Mouse Down    xpath=//*[contains(@id, '_phone')]
    Click Element     xpath=//*[contains(@id, '_phone')]
    Page Should Contain Element    id=link_edit_personal_info
    Click Element    id=link_edit_personal_info
    Input Text    id=input_name    edit_name
    Input Text    id=input_lastname    edit_lastname
    Input Text    id=input_rut    22.222.222-2
    Input Text    id=input_email    edit_email@gmailcom
    Input Text    id=input_phone    +56987654321
    Input Text    id=input_birthdate    2002-02-02
    Input Text    id=input_city    edit_city
    Click Button    Guardar cambios
    Page Should Contain Element    css=.p-toast-detail[data-pc-section="detail"]
    Close Browser