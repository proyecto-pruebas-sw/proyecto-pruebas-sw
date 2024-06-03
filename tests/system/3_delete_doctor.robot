*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary 
Suite Setup    Connect To Database    psycopg2    ${db_name}    ${db_user}    ${db_password}    ${db_host}    ${db_port}
Documentation     Test cases for the delete functionality

*** Variables ***
${index_url}            http://localhost:3000
${browser}             Firefox   
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432 

*** Test Cases ***
test-system-29 Delete a doctor
    Open Browser    ${index_url}/medics/5    ${browser}
    Click Button    Eliminar médico
    Click Button    Eliminar
    Sleep    1s
    Check If Not Exists In Database    SELECT * FROM doctors WHERE id = 5;
    Close Browser
